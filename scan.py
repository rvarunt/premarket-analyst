#!/usr/bin/env python3
"""Premarket data gatherer. Collects raw data into packet.json. No analysis, no opinions.
All judgment (conviction, buckets, narrative) happens later in the AI prompts."""

import json
import os
import re
import time
from datetime import datetime, timedelta
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

GAP_MIN_ABS_PCT = 4
GAP_MIN_PRICE = 3
GAP_TOP_N = 12


def with_retries(fn, attempts=3, base_delay=3, label=""):
    """Run fn, retrying on any exception. Returns None (and prints) if all attempts fail."""
    last_err = None
    for attempt in range(1, attempts + 1):
        try:
            return fn()
        except Exception as e:
            last_err = e
            if attempt < attempts:
                delay = base_delay * attempt
                print(f"    retry {attempt}/{attempts - 1} for {label}: {e} (waiting {delay}s)")
                time.sleep(delay)
    print(f"    giving up on {label}: {last_err}")
    return None


def new_yf_session():
    # yfinance defaults to a curl_cffi session that impersonates a browser TLS
    # fingerprint. That impersonation breaks under many corporate/agent proxies
    # (connection reset during the TLS handshake). A plain requests.Session
    # avoids the impersonation layer and just does normal HTTPS.
    return requests.Session()


# ---------------------------------------------------------------------------
# 1. Market snapshot
# ---------------------------------------------------------------------------

def get_market_snapshot(session):
    print("Fetching market snapshot...")
    snapshot = {}
    for name, symbol in MARKET_SNAPSHOT_SYMBOLS.items():
        def fetch(symbol=symbol):
            t = yf.Ticker(symbol, session=session)
            hist = t.history(period="5d", interval="1d")
            if hist is None or len(hist) < 2:
                raise ValueError("not enough daily bars")
            last = float(hist["Close"].iloc[-1])
            prev_close = float(hist["Close"].iloc[-2])
            return last, prev_close

        result = with_retries(fetch, label=f"snapshot {name}")
        if result is None:
            snapshot[name] = {"symbol": symbol, "last": None, "prev_close": None, "change_pct": None}
            continue
        last, prev_close = result
        change_pct = round((last - prev_close) / prev_close * 100, 2) if prev_close else None
        snapshot[name] = {
            "symbol": symbol,
            "last": round(last, 2),
            "prev_close": round(prev_close, 2),
            "change_pct": change_pct,
        }
        print(f"  {name}: {snapshot[name]['last']} ({change_pct}%)")
    return snapshot


# ---------------------------------------------------------------------------
# 2 & 3. Live movers / static universe fallback, and gap filter
# ---------------------------------------------------------------------------

def _screen_to_movers(quotes):
    movers = {}
    for q in quotes or []:
        symbol = q.get("symbol")
        if not symbol:
            continue
        movers[symbol] = {
            "ticker": symbol,
            "name": q.get("shortName") or q.get("longName") or symbol,
            "price": q.get("regularMarketPrice"),
            "prev_close": q.get("regularMarketPreviousClose"),
            "gap_pct": q.get("regularMarketChangePercent"),
            "market_cap": q.get("marketCap"),
            "volume": q.get("regularMarketVolume"),
        }
    return movers


def get_live_movers(session):
    print("Trying live screeners (day_gainers, most_actives)...")
    combined = {}
    for query in ("day_gainers", "most_actives"):
        def fetch(query=query):
            return yf.screen(query, count=25, session=session)

        result = with_retries(fetch, label=f"screener {query}")
        if result is None:
            continue
        quotes = result.get("quotes") if isinstance(result, dict) else None
        movers = _screen_to_movers(quotes)
        print(f"  {query}: {len(movers)} names")
        combined.update(movers)
    return list(combined.values())


def get_static_universe_movers(session):
    print(f"Falling back to static universe ({len(STATIC_UNIVERSE)} tickers)...")
    movers = []
    for ticker in STATIC_UNIVERSE:
        def fetch(ticker=ticker):
            t = yf.Ticker(ticker, session=session)
            hist = t.history(period="5d", interval="1d")
            if hist is None or len(hist) < 2:
                raise ValueError("not enough daily bars")
            info = t.info or {}
            return hist, info

        result = with_retries(fetch, label=f"static {ticker}")
        if result is None:
            continue
        hist, info = result
        price = float(hist["Close"].iloc[-1])
        prev_close = float(hist["Close"].iloc[-2])
        gap_pct = round((price - prev_close) / prev_close * 100, 2) if prev_close else None
        movers.append({
            "ticker": ticker,
            "name": info.get("shortName") or info.get("longName") or ticker,
            "price": round(price, 2),
            "prev_close": round(prev_close, 2),
            "gap_pct": gap_pct,
            "market_cap": info.get("marketCap"),
            "volume": info.get("regularMarketVolume") or int(hist["Volume"].iloc[-1]),
        })
        print(f"  {ticker}: gap {gap_pct}%")
    return movers


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
    live_movers = get_live_movers(session)
    if len(live_movers) >= 5:
        candidate_source = "live_screener"
        movers = live_movers
    else:
        candidate_source = "static_universe_fallback"
        movers = get_static_universe_movers(session)
    gappers = gap_filter(movers)
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
            if not title or is_spam(title):
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
            matched.append({"title": title, "publisher": norm.get("publisher", ""), "link": norm.get("link", "")})

    for item in market_news:
        title = item["title"]
        if _headline_matches(title, ticker, tokens):
            matched.append({"title": title, "publisher": item["source"], "link": item["link"]})

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


def get_intraday_levels(ticker, session):
    def fetch():
        t = yf.Ticker(ticker, session=session)
        bars = t.history(period="5d", interval="5m", prepost=True)
        if bars is None or bars.empty:
            raise ValueError("no intraday bars")
        return bars

    bars = with_retries(fetch, label=f"intraday {ticker}")
    if bars is None:
        return {"vwap": None, "hod": None, "lod": None, "premarket_high": None, "premarket_volume": None}

    bars = bars.tz_convert(ET)
    today = datetime.now(ET).date()
    today_bars = bars[bars.index.date == today]
    if today_bars.empty:
        return {"vwap": None, "hod": None, "lod": None, "premarket_high": None, "premarket_volume": None}

    premarket_bars = today_bars[today_bars.index.time < datetime.strptime("09:30", "%H:%M").time()]

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


def get_daily_metrics(ticker, session, current_price):
    def fetch():
        t = yf.Ticker(ticker, session=session)
        hist = t.history(period="1y", interval="1d")
        if hist is None or hist.empty:
            raise ValueError("no daily bars")
        return hist.tz_localize(None) if hist.index.tz is not None else hist

    hist = with_retries(fetch, label=f"daily {ticker}")
    if hist is None:
        return {
            "sma_200": None, "prior_day_high": None, "prior_close": None,
            "today_open": None, "avg_volume_20d": None,
        }

    today = datetime.now(ET).date()
    today_open = None
    if hist.index[-1].date() == today:
        today_open = round(float(hist["Open"].iloc[-1]), 2)
        hist = hist.iloc[:-1]  # drop today's partial bar from prior-day/average calcs

    if hist.empty:
        return {
            "sma_200": None, "prior_day_high": None, "prior_close": None,
            "today_open": today_open, "avg_volume_20d": None,
        }

    sma_200 = round(float(hist["Close"].tail(200).mean()), 2) if len(hist) >= 1 else None
    prior_day_high = round(float(hist["High"].iloc[-1]), 2)
    prior_close = round(float(hist["Close"].iloc[-1]), 2)
    avg_volume_20d = int(hist["Volume"].tail(20).mean())

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


def enrich_gapper(gapper, session, market_news):
    ticker = gapper["ticker"]
    print(f"  enriching {ticker}...")

    daily = get_daily_metrics(ticker, session, gapper.get("price"))
    intraday = get_intraday_levels(ticker, session)
    catalysts = get_catalyst_headlines(ticker, gapper.get("name", ticker), session, market_news)
    next_earnings = get_next_earnings_date(ticker, session)

    avg_vol = daily.get("avg_volume_20d")
    today_volume = gapper.get("volume") or intraday.get("premarket_volume")
    # yfinance reports ~0 true premarket volume. A real premarket RVOL needs a
    # premarket-aware feed (e.g. Alpaca). Full/partial-day volume vs the 20-day
    # average volume is the keyless stand-in used here.
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
    now_et = datetime.now(ET)
    session = new_yf_session()

    market_snapshot = get_market_snapshot(session)
    gappers, candidate_source = get_gappers(session)
    market_news = gather_market_news(session)
    econ_calendar = fetch_econ_calendar(session)

    print(f"Enriching {len(gappers)} gappers...")
    for g in gappers:
        enrich_gapper(g, session, market_news)
        day_eligible, swing_eligible = compute_eligibility(g)
        g["day_eligible"] = day_eligible
        g["swing_eligible"] = swing_eligible

    gaps_to_fill = [
        "Market-wide earnings coverage is partial (only per-gapper next earnings date is pulled, "
        "not a full market earnings calendar).",
        "Intraday levels (VWAP, HOD, LOD, premarket high) come from free 5-min bars, not a "
        "true tick-level feed, so they're an approximation.",
        "RVOL uses full/partial-day volume vs the 20-day average as a keyless stand-in. Real "
        "premarket RVOL needs a premarket-aware feed like Alpaca; yfinance reports near-zero "
        "premarket volume.",
        "Before 9:30am ET, today's open is not real yet. The scanner uses the current gap "
        "price as a stand-in for swing eligibility until the actual open prints.",
    ]

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
