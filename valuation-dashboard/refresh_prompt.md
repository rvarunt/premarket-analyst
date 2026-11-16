# Daily refresh — scheduled task prompt (TradingView route)

This is the prompt for a Claude scheduled task that refreshes the dashboard every weekday from
TradingView, using your signed-in TradingView account in the Claude desktop app's browser pane.
It needs the Claude desktop app open on your computer at run time.

Prefer not to use TradingView? Use `build_data.py` instead (free Yahoo data, see SETUP.md).

**To use it:** replace the two placeholders, then ask Claude: "create a scheduled task, weekdays
7:50 New York time, with this prompt".

| Placeholder | Replace with |
|---|---|
| `{{DASHBOARD_URL}}` | Your dashboard's claude.ai/artifact/… link (Claude gives it to you when it publishes the dashboard) |
| `{{TRADINGVIEW_USERNAME}}` | The TradingView username you sign in with (only used to check you are signed in) |

---

Refresh the user's "Daily Valuation Dashboard" artifact ({{DASHBOARD_URL}}, a Data-type dashboard) with today's TradingView numbers. Only update its two data files (datasets "companies" and "markets"); do not change the page, the assumptions dataset, or anything else. Do not delete anything except the two superseded data assets named in step 5.

1. Read datasets/companies and datasets/markets with ArtifactData (url above) to get each one's current source.url ("/_blob/<id>") and version. Read the current companies file with Artifact read (url above, path = the blob id) — its "rows" list is the company list to refresh: keep every row's id, symbol, ticker, name, bucket and order exactly as they are (some symbols appear twice under different buckets; fetch each symbol once and reuse it).
2. Open https://www.tradingview.com/ in the built-in browser pane (mcp__remote-devices__Claude_Browser__*; load the built-in-browser skill first). The user is normally signed in (account {{TRADINGVIEW_USERNAME}}). If not signed in, stop and report that.
3. In the page, with javascript_tool, GET https://scanner.tradingview.com/symbol?symbol=<SYM>&fields=<FIELDS> (credentials:'include') for each distinct symbol.
   Company FIELDS: close,currency,market_cap_basic,price_earnings_ttm,earnings_per_share_diluted_ttm,price_earnings_growth_ttm,price_book_ratio,price_sales_current,enterprise_value_ebitda_ttm,ebitda_ttm,dividends_yield_current,dps_common_stock_prim_issue_fy,beta_5_year,free_cash_flow_ttm,net_debt_fq,book_value_per_share_fq,return_on_equity_fq,total_revenue_yoy_growth_ttm,earnings_per_share_forecast_next_fy,total_revenue,Perf.1M,Perf.YTD,change
   Market symbols (fields close,change,Perf.1M,Perf.YTD): TVC:US10Y, TVC:DE10Y, NASDAQ:QQQ, NASDAQ:SMH, AMEX:XLF, TVC:SX5E, EURONEXT:AEX, and FX (close only): FX:EURUSD, FX_IDC:GBPUSD, FX_IDC:CHFUSD, FX_IDC:KRWUSD, FX_IDC:HKDUSD, FX_IDC:CNYUSD, FX_IDC:JPYUSD, FX_IDC:INRUSD.
   Also check NASDAQ:ANT (Anthropic). If it now has a non-null close and market_cap_basic, append a row for it with id "NASDAQ:ANT|Platforms & neocloud", ticker "ANT", name "Anthropic", bucket "Platforms & neocloud", and mention it in the summary. Otherwise leave it out.
4. Build companies.json = {"rows":[...], "meta":[{"label":"Source","value":"TradingView market data (scanner fields), pulled <UTC ISO minute>"},{"label":"Units","value":"price in local currency (AstraZeneca converted from pence to GBP); EPS, DPS, book value, FCF, EBITDA, net debt, revenue and market cap in USD as TradingView reports them; fx_usd = USD per 1 unit of local currency"}]}. Each row has exactly these keys: id, symbol, ticker, name, region, currency, bucket, price, fx_usd, mcap_usd, shares, eps_ttm, eps_next_fy, dps, bvps, fcf_ttm, ebitda_ttm, net_debt, revenue_ttm, roe_pct, beta_5y, rev_growth_pct, pe, peg, pb, ps, ev_ebitda, div_yield_pct, perf_1m_pct, perf_ytd_pct.
   Rules: region = "US" for USD, "Europe" for EUR/GBP/GBX/CHF, else "Asia". If currency is GBX: price = close/100, currency "GBP", fx_usd = GBP/USD. Otherwise price = close and fx_usd = 1 for USD or the matching FX close. mcap_usd = market_cap_basic; shares = round(mcap_usd/(close_in_local_units*fx_per_local_unit)) (for GBX use close × GBPUSD/100). pe = price_earnings_ttm, or mcap/shares/eps when that is null and eps > 0. ps = price_sales_current, or mcap_usd/total_revenue when null and revenue > 0. Map the rest from the matching fields; null when missing.
   Build markets.json = {"rows":[...], "meta":[{"label":"Source","value":"TradingView market data, pulled <same timestamp>"}]} with rows {symbol, name, kind, currency, value, change_pct, perf_1m_pct, perf_ytd_pct}: US10Y "US 10Y yield" rate; DE10Y "German 10Y yield" rate; QQQ "QQQ (Nasdaq-100)", SMH "SMH (Semis)", XLF "XLF (Financials)", SX5E "Euro Stoxx 50", AEX "AEX" as benchmark (currency null); and one fx row per FX symbol with name "<CCY>/USD", kind "fx", currency the 3-letter code, value = close, other fields null.
   If a symbol fails, keep yesterday's row for it from the current file and say so in the summary.
5. Upload both files as assets (Artifact publish with url, asset:true, file_path; one call per file). Then update datasets/companies and datasets/markets with ArtifactData "update" (if_version from step 1) setting source.url to the new "/_blob/<id>", updated = {at: <now UTC ISO>, by: "Claude (daily refresh from TradingView)"}, edit = {via:"claude", at:<now>}. Then delete each previous asset (Artifact delete with path = old blob id) only once its dataset points to the new one.
6. Send the user one short paragraph with SendUserMessage: how many companies look cheap and rich today (the page's rule: fair value = median of the models for the company's group; Cheap if upside > 15%, Rich if < −15%, companies with only one model excluded) — if you can't reproduce that reliably, just say the dashboard is refreshed and name any symbols that failed. This is a research aid, not advice.
