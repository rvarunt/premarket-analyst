#!/usr/bin/env python3
"""Premarket data gatherer. Collects raw data into packet.json. No analysis, no opinions.
All judgment (conviction, buckets, narrative) happens later in the AI prompts."""

import json
import os
import random
import re
import time
from datetime import datetime, timedelta, timezone
from html import unescape
from pathlib import Path
from urllib.parse import quote
from zoneinfo import ZoneInfo

import feedparser
import requests
import yfinance as yf

ET = ZoneInfo("America/New_York")

DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
}


def _load_dotenv(path=".env"):
    # Minimal .env loader so ALPACA_API_KEY_ID / ALPACA_API_SECRET_KEY can be
    # dropped in a gitignored .env without adding a python-dotenv dependency.
    # Real environment variables always win over .env values.
    p = Path(path)
    if not p.exists():
        return
    for line in p.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


_load_dotenv()

ALPACA_DATA_BASE_URL = "https://data.alpaca.markets"
ALPACA_KEY_ID = os.environ.get("ALPACA_API_KEY_ID")
ALPACA_SECRET_KEY = os.environ.get("ALPACA_API_SECRET_KEY")
ALPACA_HEADERS = None
if ALPACA_KEY_ID and ALPACA_SECRET_KEY:
    ALPACA_HEADERS = {
        "APCA-API-KEY-ID": ALPACA_KEY_ID,
        "APCA-API-SECRET-KEY": ALPACA_SECRET_KEY,
    }

MARKET_SNAPSHOT_SYMBOLS = {
    "S&P 500": "^GSPC",
    "Dow": "^DJI",
    "Nasdaq": "^IXIC",
    "Russell 2000": "^RUT",
    "VIX": "^VIX",
    "US 10Y": "^TNX",
    "US 3M": "^IRX",
    "WTI Oil": "CL=F",
    "Dollar (DXY)": "DX-Y.NYB",
}

# Alpaca's free tier covers US equities/ETFs, not index or futures symbols, so
# these liquid ETF proxies stand in for the index rows above whenever the
# yfinance leg fails.
PROXY_MAP = {
    "S&P 500": "SPY",
    "Dow": "DIA",
    "Nasdaq": "QQQ",
    "Russell 2000": "IWM",
}

STATIC_UNIVERSE = [
    "NVDA", "AMD", "AVGO", "SMCI", "MRVL", "TSLA", "AAPL", "MSFT", "META",
    "AMZN", "GOOGL", "NFLX", "DELL", "SNOW", "PLTR", "COIN", "MSTR", "SOFI",
    "RIVN", "NIO", "MARA", "RIOT", "BA", "DIS", "JPM", "BAC", "XOM", "CVX",
    "HOOD", "UBER", "CRWD", "PANW", "CELH", "LULU", "NKE", "CAVA", "DKNG",
    "ARM", "INTC", "MU",
]

RSS_FEEDS = {
    "MarketWatch Top": "https://feeds.content.dowjones.io/public/rss/mw_topstories",
    "MarketWatch RealTime": "https://feeds.content.dowjones.io/public/rss/mw_realtimeheadlines",
    "Yahoo Finance": "https://finance.yahoo.com/news/rssindex",
    "Nasdaq Markets": "https://www.nasdaq.com/feed/rssoutbound?category=Markets",
    "Google News Markets": (
        "https://news.google.com/rss/search?q=" + quote("markets OR earnings when:1d")
        + "&hl=en-US&gl=US&ceid=US:en"
    ),
}

SPAM_PATTERNS = [
    re.compile(r"price prediction", re.I),
    re.compile(r"\b20\d{2}-20\d{2}\b"),
]

# Personal-finance advice columns show up in the same RSS feeds as real market
# news (MarketWatch runs both). They're not catalysts for anything, so keep
# them out of market_news entirely rather than let them dilute it.
PERSONAL_FINANCE_PATTERNS = [
    re.compile(r"\bretir\w*\b", re.I),  # retirement, retiree(s), retiring, retired
    re.compile(r"\bsocial security\b", re.I),
    re.compile(r"\b401\(?k\)?\b", re.I),
    re.compile(r"\bfinancial[\s-]literacy\b", re.I),
    re.compile(r"\bcredit[\s-]card\b", re.I),
]

MAX_NEWS_AGE = timedelta(hours=36)

# A headline only counts as a catalyst if it names the ticker on a word
# boundary, or contains a distinctive company-name token (4+ letters, not in
# NAME_STOP). Short/generic words are shared across unrelated companies, so
# matching on them alone would cross-match the wrong one, e.g. "Applied"
# alone would hit both Applied Optoelectronics and Applied Digital.
NAME_STOP = {
    "the", "inc", "incorporated", "corp", "corporation", "co", "company",
    "holdings", "holding", "technologies", "technology", "group", "digital",
    "applied", "advanced", "strategy", "strategies", "motors", "motor",
    "energy", "platforms", "platform", "systems", "system", "international",
    "industries", "industry", "solutions", "solution", "labs", "laboratories",
    "capital", "partners", "partner", "resources", "resource", "global",
    "networks", "network", "software", "sciences", "science", "therapeutics",
    "pharmaceuticals", "pharma", "ventures", "enterprises", "enterprise",
    "limited", "ltd", "plc", "llc", "lp", "class", "common", "brands", "brand",
}

PRIMARY_PUBLISHERS = {
    "bloomberg", "reuters", "cnbc", "marketwatch", "barron's", "barrons",
    "yahoo finance", "wsj", "wall street journal", "dow jones",
    "associated press", "ap", "business wire", "pr newswire", "globenewswire",
    "investor's business daily", "ibd",
}

ECON_CALENDAR_URL = "https://nfs.faireconomy.media/ff_calendar_thisweek.json"
ECON_CACHE_FILE = Path(".econ_calendar_cache.json")
ECON_CACHE_TTL_SECONDS = 4 * 60 * 60

SEC_TICKERS_URL = "https://www.sec.gov/files/company_tickers.json"
SEC_TICKERS_CACHE_FILE = Path(".sec_tickers_cache.json")
SEC_TICKERS_CACHE_TTL_SECONDS = 7 * 24 * 60 * 60
# SEC requires a descriptive User-Agent identifying the requester on every
# request; override with a real contact address via env if you have one.
SEC_USER_AGENT = os.environ.get("SEC_EDGAR_USER_AGENT", "premarket-analyst research contact@example.com")
SEC_HEADERS = {"User-Agent": SEC_USER_AGENT}
SEC_MIN_REQUEST_INTERVAL = 0.11  # stay under SEC's 10 req/sec limit

GAP_MIN_ABS_PCT = 4
GAP_MIN_PRICE = 3
GAP_TOP_N = 12

# Labels of calls that exhausted all retries this run, so main() can write an
# honest note into gaps_to_fill instead of silently shipping a thin packet.
RATE_LIMIT_FAILURES = []


def with_retries(fn, attempts=4, base_delay=2, label=""):
    """Run fn, retrying with exponential backoff plus jitter. Returns None
    (and records the failure) if every attempt fails."""
    last_err = None
    for attempt in range(1, attempts + 1):
        try:
            return fn()
        except Exception as e:
            last_err = e
            if attempt < attempts:
                delay = base_delay * (2 ** (attempt - 1)) + random.uniform(0, 1.5)
                print(f"    retry {attempt}/{attempts - 1} for {label}: {e} (waiting {delay:.1f}s)")
                time.sleep(delay)
    print(f"    giving up on {label}: {last_err}")
    RATE_LIMIT_FAILURES.append(label)
    return None


def polite_delay(low=0.4, high=1.2):
    # A small random gap between per-ticker requests, on top of retry backoff,
    # so the scanner doesn't hammer Yahoo in a tight loop and trip the limiter
    # in the first place.
    time.sleep(random.uniform(low, high))


def new_yf_session():
    # yfinance defaults to a curl_cffi session that impersonates a browser TLS
    # fingerprint. That impersonation breaks under many corporate/agent proxies
    # (connection reset during the TLS handshake). A plain requests.Session
    # avoids the impersonation layer and just does normal HTTPS. Reused across
    # every call in this module so we're not opening a fresh connection per ticker.
    return requests.Session()


def _slice_batch(batch, ticker):
    """Pull one ticker's OHLCV frame out of a yf.download(group_by='ticker')
    result. A single-ticker batch comes back as a flat frame instead of
    ticker-indexed columns, so that case is treated as already being that
    ticker's data. A genuinely missing ticker in a multi-ticker batch (not
    just a single-ticker shape) returns None rather than the whole batch."""
    if batch is None:
        return None
    if getattr(batch.columns, "nlevels", 1) > 1:
        if ticker not in batch.columns.get_level_values(0):
            return None
        sub = batch[ticker]
    else:
        sub = batch
    if sub is None or sub.empty:
        return None
    return sub.dropna(how="all")


def batch_fetch_daily_bars(tickers, session, period="5d", label="daily bars batch"):
    """One yf.download call for many tickers' daily bars, instead of one
    Ticker.history() call per ticker. Returns {ticker: DataFrame or None}."""
    if not tickers:
        return {}

    def fetch():
        df = yf.download(
            tickers=" ".join(tickers),
            period=period,
            interval="1d",
            session=session,
            group_by="ticker",
            threads=False,
            progress=False,
            auto_adjust=True,
        )
        # yf.download swallows per-ticker failures (including rate limits)
        # internally and returns an empty/all-NaN frame instead of raising,
        # so a totally failed batch has to be turned into an exception here
        # for with_retries to actually retry it.
        if df is None or df.empty or df.isna().all().all():
            raise ValueError("batch download returned no usable data (likely rate limited)")
        return df

    raw = with_retries(fetch, label=label)
    return {t: _slice_batch(raw, t) for t in tickers}


# ---------------------------------------------------------------------------
# 0. Alpaca data helpers
#
# Alpaca is the primary data source for anything stock/ETF-shaped (bars,
# screeners, news). yfinance is kept only as a fallback for those, and as the
# primary (only) source for index/futures symbols Alpaca's free tier doesn't
# carry. Free-tier Alpaca serves feed=iex, which is a subset of the full
# consolidated tape (one exchange's prints, not all of them) but is good
# enough for scanning purposes here.
# ---------------------------------------------------------------------------

def alpaca_available():
    return ALPACA_HEADERS is not None


def alpaca_get(path, params=None, label="", attempts=3):
    if not alpaca_available():
        return None

    def fetch():
        resp = requests.get(
            f"{ALPACA_DATA_BASE_URL}{path}",
            headers=ALPACA_HEADERS,
            params=params,
            timeout=20,
        )
        resp.raise_for_status()
        return resp.json()

    return with_retries(fetch, attempts=attempts, label=label or f"alpaca {path}")


def _chunked(seq, size):
    for i in range(0, len(seq), size):
        yield seq[i:i + size]


def alpaca_batch_daily_bars(tickers, start, label="alpaca daily bars"):
    """Batched Alpaca v2 daily bars (feed=iex) for many symbols, paginated and
    chunked. Returns {ticker: [{"t","o","h","l","c","v"}, ...]} ascending by
    date, only for tickers Alpaca actually returned data for."""
    if not tickers or not alpaca_available():
        return {}
    out = {}
    for chunk in _chunked(list(tickers), 100):
        params = {
            "symbols": ",".join(chunk),
            "timeframe": "1Day",
            "start": start,
            "feed": "iex",
            "limit": 10000,
            "adjustment": "raw",
        }
        data = alpaca_get("/v2/stocks/bars", params, label=label)
        if not data:
            continue
        for sym, arr in (data.get("bars") or {}).items():
            out.setdefault(sym, []).extend(arr)
        page_token = data.get("next_page_token")
        guard = 0
        while page_token and guard < 20:
            params["page_token"] = page_token
            data = alpaca_get("/v2/stocks/bars", params, label=f"{label} (page)")
            if not data:
                break
            for sym, arr in (data.get("bars") or {}).items():
                out.setdefault(sym, []).extend(arr)
            page_token = data.get("next_page_token")
            guard += 1
    return out


def get_alpaca_snapshots(symbols, label="alpaca snapshots"):
    if not symbols or not alpaca_available():
        return {}
    out = {}
    for chunk in _chunked(list(symbols), 100):
        data = alpaca_get("/v2/stocks/snapshots", {"symbols": ",".join(chunk), "feed": "iex"}, label=label)
        if isinstance(data, dict):
            for sym, snap in data.items():
                if isinstance(snap, dict):
                    out[sym] = snap
    return out


def get_alpaca_news(ticker, limit=10):
    data = alpaca_get("/v1beta1/news", {"symbols": ticker, "limit": limit},
                       label=f"alpaca news {ticker}", attempts=2)
    if not data:
        return []
    items = []
    for n in data.get("news") or []:
        title = (n.get("headline") or "").strip()
        if not title:
            continue
        items.append({"title": title, "publisher": n.get("source") or "alpaca", "link": n.get("url", "")})
    return items


def _normalize_alpaca_bars(bars):
    out = []
    for b in bars:
        ts = datetime.fromisoformat(b["t"].replace("Z", "+00:00"))
        out.append({
            "date": ts.astimezone(ET).date(),
            "open": b["o"], "high": b["h"], "low": b["l"], "close": b["c"], "volume": b["v"],
        })
    out.sort(key=lambda r: r["date"])
    return out


def _normalize_yf_frame(df):
    if df is None or df.empty:
        return []
    if df.index.tz is not None:
        df = df.tz_localize(None)
    out = []
    for idx, row in df.iterrows():
        d = idx.date() if hasattr(idx, "date") else idx
        out.append({
            "date": d,
            "open": float(row["Open"]), "high": float(row["High"]),
            "low": float(row["Low"]), "close": float(row["Close"]),
            "volume": int(row["Volume"]),
        })
    out.sort(key=lambda r: r["date"])
    return out


def batch_fetch_daily_metrics_bars(tickers, session, lookback_days=380, label="daily bars"):
    """Alpaca daily bars first, yfinance daily bars for whatever tickers
    Alpaca didn't cover. Returns {ticker: {"bars": [...], "source": "alpaca"
    | "yfinance_fallback" | "unavailable"}}."""
    if not tickers:
        return {}
    start = (datetime.now(ET) - timedelta(days=lookback_days)).date().isoformat()
    alpaca_raw = alpaca_batch_daily_bars(tickers, start, label=f"{label} (alpaca)")

    result = {}
    missing = []
    for t in tickers:
        bars = alpaca_raw.get(t)
        if bars and len(bars) >= 2:
            result[t] = {"bars": _normalize_alpaca_bars(bars), "source": "alpaca"}
        else:
            missing.append(t)

    if missing:
        print(f"  {len(missing)} ticker(s) missing/thin from Alpaca daily bars, "
              f"falling back to yfinance: {missing[:10]}{'...' if len(missing) > 10 else ''}")
        yf_period = "1y" if lookback_days > 10 else "5d"
        yf_batch = batch_fetch_daily_bars(missing, session, period=yf_period, label=f"{label} (yfinance fallback)")
        for t in missing:
            normalized = _normalize_yf_frame(yf_batch.get(t))
            result[t] = {"bars": normalized, "source": "yfinance_fallback" if normalized else "unavailable"}

    return result


# ---------------------------------------------------------------------------
# 0b. SEC EDGAR market cap fallback
#
# yfinance is keyless but frequently rate-limited, and Alpaca's free tier has
# no fundamentals data, so market cap (needed for both eligibility flags) can
# end up null from either source. SEC EDGAR's XBRL company-facts API is a
# third, always-keyless option: shares outstanding x current price. It's a
# last resort, not a primary, since it requires a per-ticker CIK lookup and a
# dei filing that not every issuer makes (foreign private issuers file
# different forms; ETFs don't file this concept at all).
# ---------------------------------------------------------------------------

_sec_last_request_at = [0.0]


def _sec_throttle():
    elapsed = time.time() - _sec_last_request_at[0]
    if elapsed < SEC_MIN_REQUEST_INTERVAL:
        time.sleep(SEC_MIN_REQUEST_INTERVAL - elapsed)
    _sec_last_request_at[0] = time.time()


def _load_sec_ticker_map(session):
    """Ticker -> {"cik": zero-padded 10-digit str, "name": str}, built from
    SEC's company_tickers.json and cached locally with a 7-day TTL."""
    cached = None
    if SEC_TICKERS_CACHE_FILE.exists():
        try:
            cached = json.loads(SEC_TICKERS_CACHE_FILE.read_text())
        except Exception:
            cached = None

    if cached and (time.time() - cached.get("fetched_at", 0)) < SEC_TICKERS_CACHE_TTL_SECONDS:
        return cached["data"]

    def fetch():
        _sec_throttle()
        resp = session.get(SEC_TICKERS_URL, headers=SEC_HEADERS, timeout=20)
        resp.raise_for_status()
        return resp.json()

    raw = with_retries(fetch, attempts=2, label="sec company_tickers.json")
    if raw is None:
        if cached:
            print("  SEC ticker map fetch failed, using stale cache")
            return cached["data"]
        return {}

    ticker_map = {}
    for entry in raw.values():
        ticker = (entry.get("ticker") or "").upper()
        if not ticker:
            continue
        ticker_map[ticker] = {
            "cik": str(entry.get("cik_str")).zfill(10),
            "name": entry.get("title") or ticker,
        }

    SEC_TICKERS_CACHE_FILE.write_text(json.dumps({"fetched_at": time.time(), "data": ticker_map}))
    print(f"  SEC ticker map refreshed, {len(ticker_map)} tickers")
    return ticker_map


def get_sec_shares_outstanding(ticker, cik, session):
    """Most recent dei:EntityCommonStockSharesOutstanding value for a CIK. A
    404 here is a routine, permanent miss (issuer doesn't file this concept)
    rather than a transient failure, so it's returned as a clean None instead
    of being retried or recorded as a rate-limit failure."""

    def fetch():
        _sec_throttle()
        url = f"https://data.sec.gov/api/xbrl/companyconcept/CIK{cik}/dei/EntityCommonStockSharesOutstanding.json"
        resp = session.get(url, headers=SEC_HEADERS, timeout=20)
        if resp.status_code == 404:
            return None
        resp.raise_for_status()
        return resp.json()

    data = with_retries(fetch, attempts=2, label=f"sec shares outstanding {ticker}")
    if not data:
        return None
    shares_entries = (data.get("units") or {}).get("shares") or []
    if not shares_entries:
        return None
    latest = max(shares_entries, key=lambda e: e.get("end", ""))
    return latest.get("val")


def backfill_market_cap_via_sec(gappers, session):
    missing = [g for g in gappers if g.get("market_cap") is None]
    if not missing:
        return
    print(f"  backfilling market cap via SEC EDGAR for {len(missing)} gapper(s) still missing it...")
    ticker_map = _load_sec_ticker_map(session)
    for g in missing:
        ticker = g["ticker"]
        entry = ticker_map.get(ticker.upper())
        if not entry:
            g["market_cap_source"] = "sec_unavailable_no_cik"
            continue

        shares = get_sec_shares_outstanding(ticker, entry["cik"], session)
        if shares is None:
            g["market_cap_source"] = "sec_unavailable_no_concept"
            continue

        price = g.get("price")
        if price is None:
            g["market_cap_source"] = "sec_unavailable_no_price"
            continue

        g["market_cap"] = int(shares * price)
        g["market_cap_source"] = "sec_edgar"
        if not g.get("name") or g.get("name") == ticker:
            g["name"] = entry["name"]
        print(f"    {ticker}: market cap ${g['market_cap']:,} via SEC ({shares:,} shares x ${price})")


# ---------------------------------------------------------------------------
# 1. Market snapshot
# ---------------------------------------------------------------------------

def get_market_snapshot(session):
    print("Fetching market snapshot (yfinance for indices/futures)...")
    snapshot = {}
    try:
        symbols = list(MARKET_SNAPSHOT_SYMBOLS.values())
        batch = batch_fetch_daily_bars(symbols, session, period="5d", label="market snapshot batch")
        for name, symbol in MARKET_SNAPSHOT_SYMBOLS.items():
            hist = batch.get(symbol)
            if hist is None or len(hist) < 2:
                snapshot[name] = {
                    "symbol": symbol, "last": None, "prev_close": None, "change_pct": None,
                    "data_source": "yfinance_failed",
                }
                continue
            last = float(hist["Close"].iloc[-1])
            prev_close = float(hist["Close"].iloc[-2])
            change_pct = round((last - prev_close) / prev_close * 100, 2) if prev_close else None
            snapshot[name] = {
                "symbol": symbol,
                "last": round(last, 2),
                "prev_close": round(prev_close, 2),
                "change_pct": change_pct,
                "data_source": "yfinance",
            }
            print(f"  {name}: {snapshot[name]['last']} ({change_pct}%)")
    except Exception as e:
        # yfinance can throw outright (not just per-symbol misses) if the whole
        # batch call blows up; degrade to an empty snapshot rather than crash
        # the whole scan, and let the Alpaca ETF-proxy pass below fill what it can.
        print(f"  yfinance market snapshot failed entirely: {e}")
        for name, symbol in MARKET_SNAPSHOT_SYMBOLS.items():
            snapshot.setdefault(name, {
                "symbol": symbol, "last": None, "prev_close": None, "change_pct": None,
                "data_source": "yfinance_failed",
            })

    proxy_symbols = list(PROXY_MAP.values())
    alpaca_proxies = {}
    try:
        alpaca_proxies = get_alpaca_snapshots(proxy_symbols, label="market snapshot ETF proxies")
    except Exception as e:
        print(f"  Alpaca ETF proxy snapshot failed: {e}")

    for name, proxy_symbol in PROXY_MAP.items():
        entry = snapshot.get(name)
        if entry and entry.get("last") is not None:
            continue
        proxy = alpaca_proxies.get(proxy_symbol)
        daily = (proxy or {}).get("dailyBar")
        prev = (proxy or {}).get("prevDailyBar")
        if not daily or not prev or prev.get("c") in (None, 0):
            snapshot[name] = entry or {
                "symbol": MARKET_SNAPSHOT_SYMBOLS[name], "last": None, "prev_close": None,
                "change_pct": None, "data_source": "unavailable",
            }
            continue
        last = float(daily["c"])
        prev_close = float(prev["c"])
        change_pct = round((last - prev_close) / prev_close * 100, 2) if prev_close else None
        snapshot[name] = {
            "symbol": MARKET_SNAPSHOT_SYMBOLS[name],
            "last": round(last, 2),
            "prev_close": round(prev_close, 2),
            "change_pct": change_pct,
            "data_source": "alpaca_etf_proxy",
            "is_proxy": True,
            "proxy_symbol": proxy_symbol,
        }
        print(f"  {name} (proxy {proxy_symbol}): {snapshot[name]['last']} ({change_pct}%)")

    return snapshot


# ---------------------------------------------------------------------------
# 2 & 3. Live movers / static universe fallback, and gap filter
# ---------------------------------------------------------------------------

def get_alpaca_movers(top=50):
    """Combine Alpaca's gainers+losers screener with most-actives into one
    candidate list. Neither endpoint returns company name or market cap
    (free tier has no fundamentals), so those are backfilled later, only for
    names that survive the gap filter."""
    result = {}

    movers_data = alpaca_get("/v1beta1/screener/stocks/movers", {"top": top}, label="alpaca movers")
    if movers_data:
        for bucket in ("gainers", "losers"):
            for q in movers_data.get(bucket) or []:
                symbol = q.get("symbol")
                if not symbol:
                    continue
                price = q.get("price")
                change = q.get("change")
                prev_close = round(price - change, 2) if price is not None and change is not None else None
                result[symbol] = {
                    "ticker": symbol,
                    "name": symbol,
                    "price": price,
                    "prev_close": prev_close,
                    "gap_pct": q.get("percent_change"),
                    "market_cap": None,
                    "market_cap_source": None,
                    "volume": None,
                    "candidate_data_source": "alpaca_movers",
                }

    actives_data = alpaca_get("/v1beta1/screener/stocks/most-actives", {"top": top, "by": "volume"},
                               label="alpaca most-actives")
    if actives_data:
        actives = actives_data.get("most_actives") or []
        symbols = [q.get("symbol") for q in actives if q.get("symbol")]
        snaps = get_alpaca_snapshots(symbols, label="most-actives snapshots") if symbols else {}
        for q in actives:
            symbol = q.get("symbol")
            if not symbol:
                continue
            if symbol in result:
                if result[symbol].get("volume") is None:
                    result[symbol]["volume"] = q.get("volume")
                continue
            snap = snaps.get(symbol) or {}
            daily = snap.get("dailyBar") or {}
            prev = snap.get("prevDailyBar") or {}
            price = daily.get("c")
            prev_close = prev.get("c")
            gap_pct = round((price - prev_close) / prev_close * 100, 2) if price and prev_close else None
            result[symbol] = {
                "ticker": symbol,
                "name": symbol,
                "price": price,
                "prev_close": prev_close,
                "gap_pct": gap_pct,
                "market_cap": None,
                "market_cap_source": None,
                "volume": q.get("volume"),
                "candidate_data_source": "alpaca_most_actives",
            }

    return list(result.values())


def get_static_universe_movers(session):
    print(f"Falling back to static universe ({len(STATIC_UNIVERSE)} tickers)...")
    batch = batch_fetch_daily_metrics_bars(
        STATIC_UNIVERSE, session, lookback_days=10, label="static universe daily bars"
    )

    movers = []
    for ticker in STATIC_UNIVERSE:
        bars = (batch.get(ticker) or {}).get("bars") or []
        if len(bars) < 2:
            print(f"    skipping {ticker}, no daily bars from alpaca or yfinance")
            continue
        price = bars[-1]["close"]
        prev_close = bars[-2]["close"]
        volume = bars[-1]["volume"]
        price_source = batch[ticker]["source"]

        def fetch_info(ticker=ticker):
            t = yf.Ticker(ticker, session=session)
            return t.info or {}

        # Name and market cap aren't in the daily bars, so this stays a
        # per-ticker yfinance call regardless of where the price came from
        # (Alpaca's free tier has no fundamentals). The delay after it keeps
        # the loop from firing 40 requests back to back.
        info = with_retries(fetch_info, attempts=2, label=f"static info {ticker}") or {}
        polite_delay()

        gap_pct = round((price - prev_close) / prev_close * 100, 2) if prev_close else None
        movers.append({
            "ticker": ticker,
            "name": info.get("shortName") or info.get("longName") or ticker,
            "price": round(price, 2),
            "prev_close": round(prev_close, 2),
            "gap_pct": gap_pct,
            "market_cap": info.get("marketCap"),
            "market_cap_source": "yfinance" if info.get("marketCap") is not None else None,
            "volume": info.get("regularMarketVolume") or int(volume),
            "candidate_data_source": price_source,
        })
        print(f"  {ticker}: gap {gap_pct}%")
    return movers


def backfill_name_and_market_cap(gappers, session):
    # Alpaca's free screener/snapshot endpoints carry no company name or
    # market cap, so pull those from yfinance .info -- but only for the
    # handful of names that survive the gap filter, not the whole screener.
    # Anything yfinance can't fill here still gets a shot via SEC EDGAR next.
    print(f"  backfilling name/market cap for {len(gappers)} gapper(s) via yfinance...")
    for g in gappers:
        ticker = g["ticker"]

        def fetch_info(ticker=ticker):
            t = yf.Ticker(ticker, session=session)
            return t.info or {}

        info = with_retries(fetch_info, attempts=2, label=f"market cap backfill {ticker}") or {}
        polite_delay()
        if info.get("shortName") or info.get("longName"):
            g["name"] = info.get("shortName") or info.get("longName")
        market_cap = info.get("marketCap")
        if market_cap is not None:
            g["market_cap"] = market_cap
            g["market_cap_source"] = "yfinance"
        if g.get("volume") is None:
            g["volume"] = info.get("regularMarketVolume")


def gap_filter(movers):
    kept = []
    for m in movers:
        gap = m.get("gap_pct")
        price = m.get("price")
        if gap is None or price is None:
            continue
        if abs(gap) >= GAP_MIN_ABS_PCT and price >= GAP_MIN_PRICE:
            kept.append(m)
    kept.sort(key=lambda m: abs(m["gap_pct"]), reverse=True)
    return kept[:GAP_TOP_N]


def get_gappers(session):
    print("Trying Alpaca screeners (movers, most-actives)...")
    alpaca_movers = get_alpaca_movers()
    print(f"  alpaca screeners: {len(alpaca_movers)} candidate name(s)")

    if len(alpaca_movers) >= 5:
        candidate_source = "alpaca_screener"
        movers = alpaca_movers
    else:
        candidate_source = "static_universe_fallback"
        movers = get_static_universe_movers(session)

    gappers = gap_filter(movers)

    if candidate_source == "alpaca_screener" and gappers:
        backfill_name_and_market_cap(gappers, session)

    # Order of preference for market cap: yfinance (already tried above, or in
    # get_static_universe_movers), then SEC EDGAR for whatever's still missing.
    if gappers:
        backfill_market_cap_via_sec(gappers, session)

    print(f"Gap filter kept {len(gappers)} of {len(movers)} candidates (source: {candidate_source})")
    return gappers, candidate_source


# ---------------------------------------------------------------------------
# 4. Market-wide news
# ---------------------------------------------------------------------------

def strip_html(text):
    if not text:
        return ""
    text = re.sub(r"<[^>]+>", " ", text)
    text = unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def is_spam(title):
    return any(p.search(title) for p in SPAM_PATTERNS)


def is_personal_finance(title):
    return any(p.search(title) for p in PERSONAL_FINANCE_PATTERNS)


def is_too_old(entry, max_age=MAX_NEWS_AGE):
    # feedparser normalizes the published/updated date into a UTC struct_time
    # when it can parse it. No parseable date means we can't verify freshness,
    # so treat it as stale rather than risk a zombie headline slipping through.
    parsed = entry.get("published_parsed") or entry.get("updated_parsed")
    if not parsed:
        return True
    published_at = datetime(*parsed[:6], tzinfo=timezone.utc)
    return (datetime.now(timezone.utc) - published_at) > max_age


def gather_market_news(session):
    print("Gathering market-wide news...")
    items = []
    for name, url in RSS_FEEDS.items():
        try:
            resp = session.get(url, timeout=15, headers=DEFAULT_HEADERS)
            resp.raise_for_status()
            parsed = feedparser.parse(resp.content)
            entries = parsed.entries or []
        except Exception as e:
            print(f"  '{name}' failed, skipping: {e}")
            continue
        count = 0
        for e in entries:
            title = (e.get("title") or "").strip()
            if not title or is_spam(title) or is_personal_finance(title):
                continue
            if is_too_old(e):
                continue
            summary = strip_html(e.get("summary") or e.get("description") or "")
            items.append({
                "source": name,
                "title": title,
                "summary": summary,
                "link": e.get("link", ""),
                "published": e.get("published", "") or e.get("updated", ""),
            })
            count += 1
        print(f"  '{name}': {count} usable headlines")
    return items


# ---------------------------------------------------------------------------
# 5. Economic calendar
# ---------------------------------------------------------------------------

def _empty_calendar(note):
    return {
        "source": ECON_CALENDAR_URL,
        "filter": "USD country, High impact only",
        "today_date": None,
        "tomorrow_date": None,
        "today": [],
        "tomorrow": [],
        "note": note,
    }


def fetch_econ_calendar(session):
    print("Fetching economic calendar...")
    try:
        return _fetch_econ_calendar_inner(session)
    except Exception as e:
        print(f"  econ calendar failed entirely: {e}")
        return _empty_calendar(f"Failed to build calendar: {e}")


def _fetch_econ_calendar_inner(session):
    cached = None
    if ECON_CACHE_FILE.exists():
        try:
            cached = json.loads(ECON_CACHE_FILE.read_text())
        except Exception:
            cached = None

    cache_fresh = bool(cached) and (time.time() - cached.get("fetched_at", 0)) < ECON_CACHE_TTL_SECONDS
    note = ""
    raw = None

    if cache_fresh:
        raw = cached["data"]
        print("  using cached weekly feed (fresh)")
    else:
        try:
            resp = session.get(ECON_CALENDAR_URL, timeout=15, headers=DEFAULT_HEADERS)
            resp.raise_for_status()
            raw = resp.json()
            ECON_CACHE_FILE.write_text(json.dumps({"fetched_at": time.time(), "data": raw}))
            print(f"  live fetch ok, {len(raw)} events this week")
        except Exception as e:
            print(f"  live fetch failed ({e}), trying cache")
            if cached and cached.get("data"):
                raw = cached["data"]
                note = "Live fetch failed, using last cached weekly feed."
            else:
                return _empty_calendar(f"Live fetch failed and no cache available: {e}")

    now_et = datetime.now(ET)
    today_date = now_et.date()
    tomorrow_date = today_date + timedelta(days=1)

    today_events, tomorrow_events = [], []
    for ev in raw:
        if ev.get("country") != "USD" or ev.get("impact") != "High":
            continue
        try:
            dt = datetime.fromisoformat(ev["date"]).astimezone(ET)
        except Exception:
            continue
        entry = {
            "time_et": dt.strftime("%-I:%M %p ET"),
            "title": ev.get("title", ""),
            "forecast": ev.get("forecast", ""),
            "previous": ev.get("previous", ""),
        }
        if dt.date() == today_date:
            today_events.append((dt, entry))
        elif dt.date() == tomorrow_date:
            tomorrow_events.append((dt, entry))

    today_events.sort(key=lambda x: x[0])
    tomorrow_events.sort(key=lambda x: x[0])

    return {
        "source": ECON_CALENDAR_URL,
        "filter": "USD country, High impact only",
        "today_date": today_date.isoformat(),
        "tomorrow_date": tomorrow_date.isoformat(),
        "today": [e for _, e in today_events],
        "tomorrow": [e for _, e in tomorrow_events],
        "note": note,
    }


# ---------------------------------------------------------------------------
# 6. Per-gapper enrichment
# ---------------------------------------------------------------------------

def _distinctive_tokens(name):
    tokens = re.split(r"[^A-Za-z0-9]+", name or "")
    keep = []
    for tok in tokens:
        low = tok.lower()
        if len(low) < 4 or low in NAME_STOP or low.isdigit():
            continue
        keep.append(low)
    return keep


def _headline_matches(title, ticker, tokens):
    if re.search(r"\b" + re.escape(ticker) + r"\b", title):
        return True
    low_title = title.lower()
    for tok in tokens:
        if re.search(r"\b" + re.escape(tok) + r"\b", low_title):
            return True
    return False


def _normalize_yf_news_item(item):
    # yfinance has shipped both a flat news schema and a newer schema nested
    # under "content"; support both so a schema change doesn't nuke catalysts.
    content = item.get("content") if isinstance(item.get("content"), dict) else None
    if content:
        return {
            "title": content.get("title", ""),
            "publisher": (content.get("provider") or {}).get("displayName", ""),
            "link": (content.get("canonicalUrl") or {}).get("url", ""),
        }
    return {
        "title": item.get("title", ""),
        "publisher": item.get("publisher", ""),
        "link": item.get("link", ""),
    }


def get_catalyst_headlines(ticker, name, session, market_news):
    tokens = _distinctive_tokens(name)
    matched = []

    def fetch_news():
        t = yf.Ticker(ticker, session=session)
        return t.news or []

    yf_news = with_retries(fetch_news, attempts=2, label=f"news {ticker}") or []
    for raw_item in yf_news:
        norm = _normalize_yf_news_item(raw_item)
        title = (norm.get("title") or "").strip()
        if not title or is_spam(title):
            continue
        if _headline_matches(title, ticker, tokens):
            matched.append({
                "title": title, "publisher": norm.get("publisher", ""), "link": norm.get("link", ""),
                "data_source": "yfinance",
            })

    # Alpaca news is already filtered server-side by symbol, so it doesn't
    # need the name/token matching yfinance and RSS headlines go through.
    alpaca_news = get_alpaca_news(ticker)
    for item in alpaca_news:
        title = item["title"]
        if not title or is_spam(title):
            continue
        matched.append({
            "title": title, "publisher": item.get("publisher") or "alpaca", "link": item.get("link", ""),
            "data_source": "alpaca",
        })

    for item in market_news:
        title = item["title"]
        if _headline_matches(title, ticker, tokens):
            matched.append({
                "title": title, "publisher": item["source"], "link": item["link"],
                "data_source": "rss",
            })

    seen = set()
    deduped = []
    for m in matched:
        key = m["title"].lower().strip()
        if key in seen:
            continue
        seen.add(key)
        deduped.append(m)

    deduped.sort(key=lambda m: 0 if m["publisher"].lower() in PRIMARY_PUBLISHERS else 1)
    return deduped[:5]


def _levels_from_alpaca_bars(bars):
    highs = [b["h"] for b in bars]
    lows = [b["l"] for b in bars]
    closes = [b["c"] for b in bars]
    vols = [b["v"] for b in bars]

    typical = [(h + l + c) / 3 for h, l, c in zip(highs, lows, closes)]
    vwap_den = sum(vols)
    vwap = round(sum(t * v for t, v in zip(typical, vols)) / vwap_den, 2) if vwap_den else None

    market_open = datetime.strptime("09:30", "%H:%M").time()
    premarket_bars = [
        b for b in bars
        if datetime.fromisoformat(b["t"].replace("Z", "+00:00")).astimezone(ET).time() < market_open
    ]
    premarket_high = max((b["h"] for b in premarket_bars), default=None)
    premarket_volume = sum(b["v"] for b in premarket_bars)

    return {
        "vwap": vwap,
        "hod": round(max(highs), 2) if highs else None,
        "lod": round(min(lows), 2) if lows else None,
        "premarket_high": round(premarket_high, 2) if premarket_high is not None else None,
        "premarket_volume": int(premarket_volume),
    }


def _levels_from_yf_bars(bars):
    bars = bars.tz_convert(ET)
    today = datetime.now(ET).date()
    today_bars = bars[bars.index.date == today]
    if today_bars.empty:
        return {"vwap": None, "hod": None, "lod": None, "premarket_high": None, "premarket_volume": None}

    market_open = datetime.strptime("09:30", "%H:%M").time()
    premarket_bars = today_bars[today_bars.index.time < market_open]

    typical = (today_bars["High"] + today_bars["Low"] + today_bars["Close"]) / 3
    vwap_num = (typical * today_bars["Volume"]).sum()
    vwap_den = today_bars["Volume"].sum()
    vwap = round(float(vwap_num / vwap_den), 2) if vwap_den else None

    return {
        "vwap": vwap,
        "hod": round(float(today_bars["High"].max()), 2),
        "lod": round(float(today_bars["Low"].min()), 2),
        "premarket_high": round(float(premarket_bars["High"].max()), 2) if not premarket_bars.empty else None,
        "premarket_volume": int(premarket_bars["Volume"].sum()) if not premarket_bars.empty else 0,
    }


def get_intraday_levels(ticker, session):
    """Today's 5-min bars including extended hours, feed=iex (free-tier IEX
    is a subset of the consolidated tape -- one exchange's prints, not all of
    them -- but good enough for VWAP/HOD/LOD/premarket scanning). Falls back
    to yfinance 5-min bars if Alpaca has nothing for today."""
    now_et = datetime.now(ET)
    today = now_et.date()
    start = datetime.combine(today, datetime.min.time(), tzinfo=ET).astimezone(timezone.utc).isoformat()
    end = now_et.astimezone(timezone.utc).isoformat()

    if alpaca_available():
        params = {
            "symbols": ticker, "timeframe": "5Min", "start": start, "end": end,
            "feed": "iex", "limit": 10000, "adjustment": "raw",
        }
        data = alpaca_get("/v2/stocks/bars", params, label=f"alpaca intraday {ticker}")
        bars = ((data or {}).get("bars") or {}).get(ticker) or []
        if bars:
            levels = _levels_from_alpaca_bars(bars)
            levels["data_source"] = "alpaca"
            return levels

    def fetch_yf():
        t = yf.Ticker(ticker, session=session)
        b = t.history(period="5d", interval="5m", prepost=True)
        if b is None or b.empty:
            raise ValueError("no intraday bars")
        return b

    yf_bars = with_retries(fetch_yf, label=f"yfinance intraday {ticker}")
    if yf_bars is None:
        return {
            "vwap": None, "hod": None, "lod": None, "premarket_high": None, "premarket_volume": None,
            "data_source": "unavailable",
        }

    levels = _levels_from_yf_bars(yf_bars)
    levels["data_source"] = "yfinance_fallback"
    return levels


def get_daily_metrics(ticker, current_price, daily_bars_batch):
    # Bars come from a single batched call made once for all gappers up front
    # (see batch_fetch_daily_metrics_bars in main), not a per-ticker fetch here.
    entry = daily_bars_batch.get(ticker) or {}
    bars = entry.get("bars") or []
    data_source = entry.get("source", "unavailable")

    if not bars:
        return {
            "sma_200": None, "prior_day_high": None, "prior_close": None,
            "today_open": None, "today_open_effective": current_price, "avg_volume_20d": None,
            "data_source": data_source,
        }

    today = datetime.now(ET).date()
    today_open = None
    if bars[-1]["date"] == today:
        today_open = round(float(bars[-1]["open"]), 2)
        bars = bars[:-1]  # drop today's partial bar from prior-day/average calcs

    if not bars:
        return {
            "sma_200": None, "prior_day_high": None, "prior_close": None,
            "today_open": today_open,
            "today_open_effective": today_open if today_open is not None else current_price,
            "avg_volume_20d": None, "data_source": data_source,
        }

    closes_tail = [b["close"] for b in bars[-200:]]
    sma_200 = round(sum(closes_tail) / len(closes_tail), 2) if closes_tail else None
    prior_day_high = round(float(bars[-1]["high"]), 2)
    prior_close = round(float(bars[-1]["close"]), 2)
    vols_tail = [b["volume"] for b in bars[-20:]]
    avg_volume_20d = int(sum(vols_tail) / len(vols_tail)) if vols_tail else None

    # Before the 9:30 ET open there is no real "today's open" yet. Use the
    # current gap price as a stand-in so eligibility checks are still
    # computable premarket; it gets replaced by the real print once trading starts.
    today_open_effective = today_open if today_open is not None else current_price

    return {
        "sma_200": sma_200,
        "prior_day_high": prior_day_high,
        "prior_close": prior_close,
        "today_open": today_open,
        "today_open_effective": today_open_effective,
        "avg_volume_20d": avg_volume_20d,
        "data_source": data_source,
    }


def get_next_earnings_date(ticker, session):
    def fetch():
        t = yf.Ticker(ticker, session=session)
        dates = t.earnings_dates
        if dates is None or dates.empty:
            raise ValueError("no earnings dates")
        return dates

    dates = with_retries(fetch, attempts=2, label=f"earnings {ticker}")
    if dates is None:
        return None
    now_et = datetime.now(ET)
    upcoming = [d for d in dates.index if d.tz_convert(ET) >= now_et] if dates.index.tz else \
        [d for d in dates.index if d >= now_et.replace(tzinfo=None)]
    if not upcoming:
        return None
    return min(upcoming).date().isoformat()


def enrich_gapper(gapper, session, market_news, daily_bars_batch):
    ticker = gapper["ticker"]
    print(f"  enriching {ticker}...")

    daily = get_daily_metrics(ticker, gapper.get("price"), daily_bars_batch)
    intraday = get_intraday_levels(ticker, session)
    polite_delay()
    catalysts = get_catalyst_headlines(ticker, gapper.get("name", ticker), session, market_news)
    polite_delay()
    next_earnings = get_next_earnings_date(ticker, session)

    avg_vol = daily.get("avg_volume_20d")
    premarket_vol = intraday.get("premarket_volume")
    # Alpaca's premarket_volume is a real print; yfinance's is near-zero, so
    # only prefer it over the screener's own volume figure when it actually
    # came from Alpaca.
    if intraday.get("data_source") == "alpaca" and premarket_vol:
        today_volume = premarket_vol
    else:
        today_volume = gapper.get("volume") or premarket_vol
    rvol = round(today_volume / avg_vol, 2) if today_volume and avg_vol else None

    gapper.update({
        "sma_200": daily.get("sma_200"),
        "prior_day_high": daily.get("prior_day_high"),
        "prior_close": daily.get("prior_close"),
        "today_open": daily.get("today_open"),
        "today_open_effective": daily.get("today_open_effective"),
        "avg_volume_20d": avg_vol,
        "rvol": rvol,
        "vwap": intraday.get("vwap"),
        "hod": intraday.get("hod"),
        "lod": intraday.get("lod"),
        "premarket_high": intraday.get("premarket_high"),
        "premarket_volume": intraday.get("premarket_volume"),
        "next_earnings_date": next_earnings,
        "catalyst_headlines": catalysts,
        "catalyst_found": len(catalysts) > 0,
        "daily_bars_data_source": daily.get("data_source"),
        "intraday_data_source": intraday.get("data_source"),
    })
    return gapper


# ---------------------------------------------------------------------------
# 7. Deterministic eligibility flags
# ---------------------------------------------------------------------------

def compute_eligibility(g):
    gap = g.get("gap_pct")
    price = g.get("price")
    market_cap = g.get("market_cap")
    rvol = g.get("rvol")
    prior_day_high = g.get("prior_day_high")
    today_open = g.get("today_open_effective")
    sma_200 = g.get("sma_200")
    catalyst_found = g.get("catalyst_found")

    day_eligible = (
        None not in (gap, price, market_cap, rvol, prior_day_high)
        and gap > 3 and price > 3 and market_cap > 1_000_000_000
        and rvol > 1.5 and price > prior_day_high
    )

    swing_eligible = (
        None not in (gap, price, today_open, prior_day_high, sma_200, market_cap)
        and gap >= 8 and price > 3 and today_open > prior_day_high
        and today_open > sma_200 and market_cap >= 800_000_000
        and bool(catalyst_found)
    )

    return day_eligible, swing_eligible


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

CRITERIA_TEXT = {
    "day_trading": (
        "Trend Join Long. Backtest: 54.6% win rate, profit factor 1.59, 280 trades. "
        "Premarket selection: gap > 3%, price > $3, market cap > $1B, premarket RVOL > 1.5, "
        "price breaking above yesterday's high. Intraday plan: trigger above premarket high "
        "and prior HOD, stop 1% below premarket high or LOD (whichever is lower) as 1R, "
        "scale 1/3 at +1R and 1/3 at +2R, trail the rest on the 21-EMA, flat by 3:51pm ET."
    ),
    "swing": (
        "Backtest: 57.6% win rate / PF 5.34 on news catalysts, 44.7% / PF 2.57 on earnings "
        "catalysts. Premarket selection: gap >= 8%, price > $3, open > yesterday's high, "
        "open > 200-day SMA, market cap >= $800M, a real catalyst (earnings on the gap day, "
        "or news with no earnings). Entry and exit management is not built yet, so swing "
        "picks are starter ideas only, no stops or targets."
    ),
}


def trading_day_note(now_et):
    t = now_et.time()
    if t < datetime.strptime("09:30", "%H:%M").time():
        session_note = "premarket"
    elif t < datetime.strptime("16:00", "%H:%M").time():
        session_note = "regular session"
    else:
        session_note = "after hours"
    return f"Scan run {now_et.strftime('%Y-%m-%d %H:%M %Z')} ({session_note})."


def main():
    RATE_LIMIT_FAILURES.clear()
    now_et = datetime.now(ET)
    session = new_yf_session()

    if not alpaca_available():
        print("WARNING: ALPACA_API_KEY_ID/ALPACA_API_SECRET_KEY not set (env or .env). "
              "Running on yfinance fallbacks only.")

    market_snapshot = get_market_snapshot(session)
    gappers, candidate_source = get_gappers(session)
    market_news = gather_market_news(session)
    econ_calendar = fetch_econ_calendar(session)

    gapper_tickers = [g["ticker"] for g in gappers]
    daily_bars_batch = batch_fetch_daily_metrics_bars(
        gapper_tickers, session, lookback_days=380, label="gapper daily bars"
    )

    print(f"Enriching {len(gappers)} gappers...")
    for g in gappers:
        enrich_gapper(g, session, market_news, daily_bars_batch)
        day_eligible, swing_eligible = compute_eligibility(g)
        g["day_eligible"] = day_eligible
        g["swing_eligible"] = swing_eligible
        polite_delay()

    gaps_to_fill = [
        "Market-wide earnings coverage is partial (only per-gapper next earnings date is pulled, "
        "not a full market earnings calendar).",
        "Intraday levels (VWAP, HOD, LOD, premarket high) come from free 5-min bars (Alpaca IEX, "
        "or yfinance if Alpaca had nothing for today), not a true tick-level feed, so they're an "
        "approximation. IEX is a subset of the consolidated tape.",
        "Before 9:30am ET, today's open is not real yet. The scanner uses the current gap "
        "price as a stand-in for swing eligibility until the actual open prints.",
    ]

    if not alpaca_available():
        gaps_to_fill.append(
            "ALPACA_API_KEY_ID/ALPACA_API_SECRET_KEY were not set, so this run used yfinance "
            "for everything Alpaca would normally cover (movers/most-actives screeners, daily "
            "bars, intraday bars, news). RVOL in particular is weaker without Alpaca, since "
            "yfinance reports near-zero premarket volume."
        )

    if RATE_LIMIT_FAILURES:
        preview = ", ".join(RATE_LIMIT_FAILURES[:8])
        more = f" and {len(RATE_LIMIT_FAILURES) - 8} more" if len(RATE_LIMIT_FAILURES) > 8 else ""
        gaps_to_fill.append(
            f"{len(RATE_LIMIT_FAILURES)} request(s) failed even after retries this scan "
            f"({preview}{more}). Fields tied to those calls are null or missing rather than guessed at."
        )

    sec_misses = [g["ticker"] for g in gappers if g.get("market_cap") is None]
    if sec_misses:
        gaps_to_fill.append(
            f"Market cap unavailable for {len(sec_misses)} gapper(s) even after the SEC EDGAR "
            f"fallback ({', '.join(sec_misses)}): likely a missing CIK, or an issuer/instrument "
            "that doesn't file the dei:EntityCommonStockSharesOutstanding concept (foreign private "
            "issuers, ETFs, some SPACs/warrants). Their eligibility flags are false rather than guessed."
        )

    data_sources = {
        "market_snapshot": "yfinance for index/futures rows; Alpaca ETF proxies (SPY/DIA/QQQ/IWM) "
                            "fill in S&P 500/Dow/Nasdaq/Russell 2000 whenever the yfinance leg fails.",
        "top_movers_universe": candidate_source,
        "daily_bars": "alpaca (v2 bars, feed=iex), yfinance fallback per-ticker when Alpaca has no data",
        "intraday_levels": "alpaca (v2 5-min bars incl. extended hours, feed=iex), yfinance fallback",
        "market_news": "rss",
        "per_ticker_news": "yfinance + alpaca (v1beta1/news), merged and deduped; RSS market_news "
                            "matches added on top",
        "company_name": "yfinance primary, SEC EDGAR company_tickers.json name as a byproduct of the "
                         "market cap fallback",
        "market_cap": "yfinance primary; SEC EDGAR fallback (dei:EntityCommonStockSharesOutstanding "
                       "shares outstanding x Alpaca/yfinance price) when yfinance is unavailable; null "
                       "with a gaps_to_fill note for issuers SEC doesn't cover",
        "alpaca_credentials_present": alpaca_available(),
    }

    packet = {
        "generated_at": now_et.isoformat(),
        "candidate_source": candidate_source,
        "trading_day_note": trading_day_note(now_et),
        "scan_params": {
            "gap_filter_min_abs_pct": GAP_MIN_ABS_PCT,
            "gap_filter_min_price": GAP_MIN_PRICE,
            "gap_filter_top_n": GAP_TOP_N,
        },
        "criteria": CRITERIA_TEXT,
        "data_sources": data_sources,
        "market_snapshot": market_snapshot,
        "econ_calendar": econ_calendar,
        "gappers": gappers,
        "market_news": market_news[:20],
        "gaps_to_fill": gaps_to_fill,
    }

    out_path = Path("packet.json")
    out_path.write_text(json.dumps(packet, indent=2, default=str))
    print(f"Wrote {out_path.resolve()}")


if __name__ == "__main__":
    main()
