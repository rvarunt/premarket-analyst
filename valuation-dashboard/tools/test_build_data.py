"""Offline tests for build_data.py (no network): python -m unittest valuation-dashboard/tools/test_build_data.py"""
import datetime as dt
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import build_data as b  # noqa: E402

TODAY = dt.date(2026, 11, 16)
CLOSES = [(dt.date(2025, 12, 31), 100.0), (dt.date(2026, 10, 16), 110.0), (dt.date(2026, 11, 13), 121.0)]
FX = {"USD": 1.0, "EUR": 1.10, "GBP": 1.30, "TWD": 0.031, "KRW": 0.00075}


def fx(c):
    return FX["GBP"] / 100 if c in ("GBp", "GBX") else FX.get(c)


class FakeSource:
    def __init__(self, infos):
        self.infos = infos

    def info(self, s):
        return self.infos.get(s, {})

    def closes(self, s, start):
        return [(TODAY, 4.5)] if s == "^TNX" else CLOSES

    fx = staticmethod(fx)


class CompanyRow(unittest.TestCase):
    def c(self, sym="NASDAQ:AAA", y="AAA", group="Software"):
        return {"id": f"{sym}|{group}", "symbol": sym, "ticker": sym.split(":")[1], "yahoo": y, "name": "A", "bucket": group}

    def test_us_stock(self):
        info = {"currency": "USD", "currentPrice": 50, "trailingPE": 25, "forwardPE": 20, "priceToBook": 5,
                "sharesOutstanding": 1e9, "freeCashflow": 2e9, "ebitda": 3e9, "totalDebt": 1e9, "totalCash": 4e9,
                "totalRevenue": 10e9, "returnOnEquity": 0.2, "revenueGrowth": 0.15, "beta": 1.2, "dividendRate": 1.0,
                "enterpriseToEbitda": 16}
        r = b.company_row(self.c(), info, CLOSES, fx, TODAY)
        self.assertEqual(r["region"], "US")
        self.assertAlmostEqual(r["eps_ttm"], 2.0)
        self.assertAlmostEqual(r["eps_next_fy"], 2.5)
        self.assertAlmostEqual(r["bvps"], 10.0)
        self.assertAlmostEqual(r["mcap_usd"], 50e9)
        self.assertAlmostEqual(r["net_debt"], -3e9)
        self.assertAlmostEqual(r["div_yield_pct"], 2.0)
        self.assertAlmostEqual(r["roe_pct"], 20.0)
        self.assertAlmostEqual(r["ps"], 5.0)            # mcap / revenue when Yahoo gives none
        self.assertAlmostEqual(r["perf_1m_pct"], 10.0)
        self.assertAlmostEqual(r["perf_ytd_pct"], 21.0)

    def test_london_pence_converted(self):
        info = {"currency": "GBp", "financialCurrency": "USD", "currentPrice": 14000, "trailingPE": 28,
                "sharesOutstanding": 1.5e9, "totalRevenue": 60e9}
        r = b.company_row(self.c("LSE:AZN", "AZN.L", "Pharma & biotech"), info, CLOSES, fx, TODAY)
        self.assertEqual(r["currency"], "GBP")
        self.assertEqual(r["region"], "Europe")
        self.assertAlmostEqual(r["price"], 140.0)
        self.assertAlmostEqual(r["fx_usd"], 1.30)
        self.assertAlmostEqual(r["eps_ttm"], 140 / 28 * 1.30, places=4)   # USD
        self.assertAlmostEqual(r["revenue_ttm"], 60e9)                     # reported in USD already
        self.assertAlmostEqual(r["mcap_usd"], 1.5e9 * 140 * 1.30, delta=1e3)

    def test_foreign_reporting_currency(self):
        # Korean listing reporting in KRW: totals convert at KRW rate, per-share from ratios
        info = {"currency": "KRW", "financialCurrency": "KRW", "currentPrice": 200000, "trailingPE": 10,
                "sharesOutstanding": 6.7e9, "ebitda": 100e12, "freeCashflow": None}
        r = b.company_row(self.c("KRX:005930", "005930.KS", "AI chips & semis"), info, CLOSES, fx, TODAY)
        self.assertEqual(r["region"], "Asia")
        self.assertAlmostEqual(r["eps_ttm"], 20000 * 0.00075)
        self.assertAlmostEqual(r["ebitda_ttm"], 100e12 * 0.00075)
        self.assertIsNone(r["fcf_ttm"])

    def test_loss_maker_and_missing(self):
        info = {"currency": "USD", "currentPrice": 10, "trailingEps": -2, "sharesOutstanding": 1e8}
        r = b.company_row(self.c(), info, [], fx, TODAY)
        self.assertAlmostEqual(r["eps_ttm"], -2)
        self.assertIsNone(r["pe"])
        self.assertIsNone(r["perf_1m_pct"])
        empty = b.company_row(self.c(), {}, [], fx, TODAY)
        self.assertIsNone(empty["price"])


class Build(unittest.TestCase):
    def test_build_and_markets(self):
        comps = [{"id": "NASDAQ:AAA|Software", "symbol": "NASDAQ:AAA", "ticker": "AAA", "yahoo": "AAA", "name": "A", "bucket": "Software"},
                 {"id": "EURONEXT:BBB|Banks", "symbol": "EURONEXT:BBB", "ticker": "BBB", "yahoo": "BBB.AS", "name": "B", "bucket": "Banks"}]
        src = FakeSource({"AAA": {"currency": "USD", "currentPrice": 10}, "BBB.AS": {"currency": "EUR", "currentPrice": 20}})
        rows, markets, failed = b.build(comps, src, TODAY, 2.7)
        self.assertEqual([r["id"] for r in rows], [c["id"] for c in comps])
        m = {x["symbol"]: x for x in markets}
        self.assertEqual(m["TVC:US10Y"]["value"], 4.5)
        self.assertEqual(m["TVC:DE10Y"]["value"], 2.7)
        self.assertEqual(m["EURUSD"]["value"], 1.10)
        self.assertEqual(failed, [])

    def test_companies_csv_loads(self):
        comps = b.load_companies(Path(b.HERE / "companies.csv"))
        self.assertGreater(len(comps), 10)
        self.assertEqual(len({c["id"] for c in comps}), len(comps))


if __name__ == "__main__":
    unittest.main()
