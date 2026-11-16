#!/usr/bin/env python3
"""Build the dashboard's data files from free Yahoo Finance data (via yfinance).

Reads the company list in companies.csv and writes, in the same format the
dashboard page expects:

    data/companies.json   one row per company (price, fundamentals, multiples)
    data/markets.json     10Y yields, FX rates to USD, benchmark indices

No TradingView account or browser is needed. Run it on your own computer:

    pip install -r requirements.txt
    python valuation-dashboard/build_data.py

Then run `node valuation-dashboard/tools/check_models.js` to see the valuations,
or ask Claude to publish the two files to your dashboard.

Units, same as the TradingView version: price is in the stock's own currency
(London pence converted to pounds); everything else (EPS, dividends, book value,
cash flow, EBITDA, debt, revenue, market cap) is in USD. fx_usd is USD per
1 unit of the stock's currency.

Yahoo data has gaps for some markets, and Yahoo limits how fast you can ask.
If a company fails it is written with nulls and listed at the end.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent

EUROPE = {"EUR", "GBP", "GBp", "GBX", "CHF", "DKK", "SEK", "NOK"}

BENCHMARKS = [
    ("NASDAQ:QQQ", "QQQ", "QQQ (Nasdaq-100)"),
    ("NASDAQ:SMH", "SMH", "SMH (Semis)"),
    ("AMEX:XLF", "XLF", "XLF (Financials)"),
    ("TVC:SX5E", "^STOXX50E", "Euro Stoxx 50"),
    ("EURONEXT:AEX", "^AEX", "AEX"),
]


# ---------------------------------------------------------------- helpers

def num(x):
    """Return x as a float, or None if it is missing or not a finite number."""
    try:
        f = float(x)
    except (TypeError, ValueError):
        return None
    return f if f == f and f not in (float("inf"), float("-inf")) else None


def pos(x):
    f = num(x)
    return f if f is not None and f > 0 else None


def rnd(x, sig=6):
    f = num(x)
    return None if f is None else float(f"{f:.{sig}g}")


def region_for(currency: str) -> str:
    if currency == "USD":
        return "US"
    return "Europe" if currency in EUROPE else "Asia"


def perf_pct(closes: list[tuple[dt.date, float]], since: dt.date):
    """Percent change from the last close on/before `since` to the latest close."""
    if not closes:
        return None
    base = None
    for d, c in closes:
        if d <= since:
            base = c
        else:
            break
    if base is None:
        base = closes[0][1]
    last = closes[-1][1]
    return (last / base - 1) * 100 if base else None


def load_companies(path: Path) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f) if (r.get("symbol") or "").strip()]
    out = []
    for r in rows:
        sym, group = r["symbol"].strip(), r["group"].strip()
        out.append({
            "id": f"{sym}|{group}",
            "symbol": sym,
            "ticker": sym.split(":")[-1],
            "yahoo": (r.get("yahoo") or sym.split(":")[-1]).strip(),
            "name": r["name"].strip(),
            "bucket": group,
        })
    return out


# ---------------------------------------------------------------- core (no network)

def company_row(c: dict, info: dict, closes: list, fx_usd, today: dt.date) -> dict:
    """Turn one Yahoo `info` dict into a dashboard row. `fx_usd(ccy)` returns USD per unit."""
    quote_ccy = info.get("currency") or "USD"
    pence = quote_ccy in ("GBp", "GBX")
    price = num(info.get("currentPrice")) or num(info.get("regularMarketPrice")) or (closes[-1][1] if closes else None)
    if price is not None and pence:
        price /= 100.0
    ccy = "GBP" if pence else quote_ccy
    fx_q = fx_usd(ccy)                                   # USD per 1 unit of quote currency
    fin_ccy = info.get("financialCurrency") or ccy
    fx_f = fx_usd(fin_ccy)                               # USD per 1 unit of reporting currency

    def usd_total(key):
        v = num(info.get(key))
        return None if v is None or fx_f is None else v * fx_f

    def usd_per_share(local):
        return None if local is None or fx_q is None else local * fx_q

    pe, fpe, pb = pos(info.get("trailingPE")), pos(info.get("forwardPE")), num(info.get("priceToBook"))
    # Per-share figures derived from Yahoo's ratios are in the quote currency, which
    # sidesteps Yahoo mixing quote and reporting currencies for foreign listings.
    eps_local = price / pe if (price and pe) else num(info.get("trailingEps"))
    epsf_local = price / fpe if (price and fpe) else num(info.get("forwardEps"))
    bvps_local = price / pb if (price and pb) else num(info.get("bookValue"))
    dps_local = num(info.get("dividendRate"))

    shares = pos(info.get("sharesOutstanding")) or pos(info.get("impliedSharesOutstanding"))
    mcap_usd = shares * price * fx_q if (shares and price and fx_q) else None
    debt, cash = usd_total("totalDebt"), usd_total("totalCash")
    net_debt = (debt or 0) - (cash or 0) if (debt is not None or cash is not None) else None
    revenue = usd_total("totalRevenue")

    ps = num(info.get("priceToSalesTrailing12Months"))
    if ps is None and mcap_usd and revenue and revenue > 0:
        ps = mcap_usd / revenue
    if pe is None and eps_local and eps_local > 0 and price:
        pe = price / eps_local

    year_start = dt.date(today.year, 1, 1)
    return {
        "id": c["id"], "symbol": c["symbol"], "ticker": c["ticker"], "name": c["name"],
        "region": region_for(ccy), "currency": ccy, "bucket": c["bucket"],
        "price": rnd(price), "fx_usd": rnd(fx_q), "mcap_usd": rnd(mcap_usd),
        "shares": round(shares) if shares else None,
        "eps_ttm": rnd(usd_per_share(eps_local)), "eps_next_fy": rnd(usd_per_share(epsf_local)),
        "dps": rnd(usd_per_share(dps_local)), "bvps": rnd(usd_per_share(bvps_local)),
        "fcf_ttm": rnd(usd_total("freeCashflow")), "ebitda_ttm": rnd(usd_total("ebitda")),
        "net_debt": rnd(net_debt), "revenue_ttm": rnd(revenue),
        "roe_pct": rnd(num(info.get("returnOnEquity")) * 100 if num(info.get("returnOnEquity")) is not None else None, 4),
        "beta_5y": rnd(info.get("beta"), 4),
        "rev_growth_pct": rnd(num(info.get("revenueGrowth")) * 100 if num(info.get("revenueGrowth")) is not None else None, 4),
        "pe": rnd(pe, 4), "peg": rnd(num(info.get("trailingPegRatio")) or num(info.get("pegRatio")), 3),
        "pb": rnd(pb, 4), "ps": rnd(ps, 4), "ev_ebitda": rnd(info.get("enterpriseToEbitda"), 4),
        "div_yield_pct": rnd(dps_local / price * 100 if (dps_local and price) else 0.0, 3),
        "perf_1m_pct": rnd(perf_pct(closes, today - dt.timedelta(days=30)), 3),
        "perf_ytd_pct": rnd(perf_pct(closes, year_start - dt.timedelta(days=1)), 3),
    }


# ---------------------------------------------------------------- network (yfinance)

class Yahoo:
    def __init__(self, pause: float = 0.6):
        import yfinance as yf  # imported here so the core can be tested without it
        self.yf, self.pause, self._fx = yf, pause, {"USD": 1.0}

    def _retry(self, fn, what):
        for attempt in range(3):
            try:
                return fn()
            except Exception as e:  # noqa: BLE001 - yfinance raises many types
                if attempt == 2:
                    print(f"  ! {what}: {e}", file=sys.stderr)
                    return None
                time.sleep(2 * (attempt + 1))

    def info(self, sym):
        time.sleep(self.pause)
        return self._retry(lambda: self.yf.Ticker(sym).info, f"info {sym}") or {}

    def closes(self, sym, start: dt.date):
        h = self._retry(lambda: self.yf.Ticker(sym).history(start=start.isoformat(), auto_adjust=False), f"history {sym}")
        if h is None or len(h) == 0:
            return []
        return [(idx.date(), float(c)) for idx, c in h["Close"].items() if c == c]

    def fx(self, ccy):
        if not ccy:
            return None
        if ccy in self._fx:
            return self._fx[ccy]
        if ccy in ("GBp", "GBX"):
            g = self.fx("GBP")
            return None if g is None else g / 100
        c = self.closes(f"{ccy}USD=X", dt.date.today() - dt.timedelta(days=10))
        self._fx[ccy] = c[-1][1] if c else None
        if self._fx[ccy] is None:
            print(f"  ! no FX rate for {ccy}", file=sys.stderr)
        return self._fx[ccy]


def build(companies, src, today: dt.date, de10y_pct: float):
    start = min(dt.date(today.year, 1, 1) - dt.timedelta(days=7), today - dt.timedelta(days=40))
    rows, failed, cache = [], [], {}
    for c in companies:
        y = c["yahoo"]
        if y not in cache:
            print(f"  {y}")
            cache[y] = (src.info(y), src.closes(y, start))
        info, closes = cache[y]
        if not info and not closes:
            failed.append(c["symbol"])
        rows.append(company_row(c, info, closes, src.fx, today))

    markets = []
    tnx = src.closes("^TNX", today - dt.timedelta(days=10))
    us10y = tnx[-1][1] if tnx else None
    if us10y is not None and us10y > 20:      # very old yfinance versions return yield x 10
        us10y /= 10
    markets.append({"symbol": "TVC:US10Y", "name": "US 10Y yield", "kind": "rate", "currency": None,
                    "value": rnd(us10y, 5), "change_pct": None, "perf_1m_pct": None, "perf_ytd_pct": None})
    markets.append({"symbol": "TVC:DE10Y", "name": "German 10Y yield", "kind": "rate", "currency": None,
                    "value": de10y_pct, "change_pct": None, "perf_1m_pct": None, "perf_ytd_pct": None})
    for sym, ysym, name in BENCHMARKS:
        cl = src.closes(ysym, start)
        chg = (cl[-1][1] / cl[-2][1] - 1) * 100 if len(cl) >= 2 else None
        markets.append({"symbol": sym, "name": name, "kind": "benchmark", "currency": None,
                        "value": rnd(cl[-1][1] if cl else None), "change_pct": rnd(chg, 4),
                        "perf_1m_pct": rnd(perf_pct(cl, today - dt.timedelta(days=30)), 4),
                        "perf_ytd_pct": rnd(perf_pct(cl, dt.date(today.year, 1, 1) - dt.timedelta(days=1)), 4)})
    fx_codes = sorted({r["currency"] for r in rows if r["currency"] and r["currency"] != "USD"})
    for ccy in fx_codes:
        markets.append({"symbol": f"{ccy}USD", "name": f"{ccy}/USD", "kind": "fx", "currency": ccy,
                        "value": rnd(src.fx(ccy)), "change_pct": None, "perf_1m_pct": None, "perf_ytd_pct": None})
    return rows, markets, failed


def previous_de10y(out_dir: Path):
    try:
        for r in json.loads((out_dir / "markets.json").read_text())["rows"]:
            if r["symbol"] == "TVC:DE10Y" and num(r["value"]) is not None:
                return float(r["value"])
    except Exception:  # noqa: BLE001
        pass
    return None


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--companies", default=str(HERE / "companies.csv"))
    p.add_argument("--out", default=str(HERE / "data"))
    p.add_argument("--de10y", type=float, default=None,
                   help="German 10Y yield in %% (Yahoo has no reliable feed). Default: last value used, else 3.0")
    p.add_argument("--only", nargs="*", help="Only these symbols (TradingView style, e.g. NASDAQ:NVDA)")
    a = p.parse_args(argv)

    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    companies = load_companies(Path(a.companies))
    if a.only:
        companies = [c for c in companies if c["symbol"] in set(a.only)]
    de10y = a.de10y if a.de10y is not None else previous_de10y(out)
    if de10y is None:
        de10y = 3.0
        print("  note: German 10Y not given; using 3.0%. Pass --de10y to set it.", file=sys.stderr)

    print(f"Fetching {len(companies)} companies from Yahoo Finance…")
    rows, markets, failed = build(companies, Yahoo(), dt.date.today(), de10y)
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    (out / "companies.json").write_text(json.dumps({"rows": rows, "meta": [
        {"label": "Source", "value": f"Yahoo Finance via yfinance, pulled {stamp}"},
        {"label": "Units", "value": "price in local currency (London pence converted to GBP); EPS, DPS, book value, FCF, "
                                    "EBITDA, net debt, revenue and market cap in USD; fx_usd = USD per 1 unit of local currency"},
    ]}, indent=0))
    (out / "markets.json").write_text(json.dumps({"rows": markets, "meta": [
        {"label": "Source", "value": f"Yahoo Finance via yfinance, pulled {stamp}; German 10Y entered manually ({de10y}%)"},
    ]}, indent=0))
    print(f"Wrote {out/'companies.json'} ({len(rows)} rows) and {out/'markets.json'}.")
    if failed:
        print("No data for: " + ", ".join(failed), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
