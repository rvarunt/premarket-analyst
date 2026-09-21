# Premarket Report: September 21, 2026

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** Mixed open on the proxies that came through: S&P 500 (via SPY) -0.13%, Dow (via DIA) -0.48%, Russell 2000 (via IWM) -0.46%, only Nasdaq (via QQQ) +0.62% in the green. VIX, the 10 year, the 3 month, oil, and the dollar all came back null again, yfinance rate limited every one of them even after retries.
- **The catch we're watching:** Twenty gappers came through the Alpaca screener, and four large caps (MARA, KEEL, PURR, BMNR) clear every leg of both watchlist bars except one: their premarket quote is still just under yesterday's high. IBIT and ETHA are even closer misses on the day trading bar alone. Neither watchlist cleared.
- **Two-brain verdict:** Single brain, no second opinion to compare.

## Pre-Market Gappers

- **OIG** +2967.6%: "12 Industrials Stocks Moving In Friday's After-Market Session"
- **IMCC** +143.1%: "Why Lobo Technologies Shares Are Trading Higher By Around 32%; Here Are 20 Stocks Moving Premarket"
- **GEMG** +60.4%: "Trading Halt: Halted at 7:50:00 p.m. ET - Trading Halt: Halt News Pending"
- **TJGC** +53.0%: "TJGC Group Files Prospectus For Offering $100M Mixed Shelf"
- **PCTTU** -50.7%: "8 Stocks Halted In Tuesday's Session"
- **TNMG** +43.9%: "TNL Mediagene To Implement 1-for-8 Share Consolidation Effective September 8"
- **SVRN** +43.2%: "12 Industrials Stocks Moving In Friday's Intraday Session"
- **AUC** +39.5%: "ATIF Holdings Appoints CEO Kamran Khan As Interim CFO, Succeeding Shibin Yu"
- **HUHU** +39.0%: "HUHUTECH International Says Japanese Subsidiary Selected For Unnamed Hiroshima Semiconductor Manufacturer's Tool Hook-Up Program Spanning FY2027 And FY2028; No Minimum Volume Or Value Committed"
- **PRPL** +34.3%: "Purple Innovation Q2 Adj. EPS $(1.52) Beats $(1.67) Estimate, Sales $98.270M Miss $105.687M Estimate"
- **DAIC** -33.0%: "Aethlon Medical, Oklo, CID HoldCo, Xenon Pharmaceuticals and Moderna: Why These 5 Stocks Are on Investors' Radars Today"
- **MSTP** +32.7%: "Trading Halt: Halt status updated at 8:55:00 AM ET: Quotation Resumption: News and Resumption Times"
- **XENE** -30.7%: "Dow Falls Over 200 Points; Xenon Pharmaceuticals Shares Plunge"
- **MARA** +13.7%: "Why Is MARA Stock Surging on Friday?"
- **KEEL** +10.7%: "Southern Company's Subsidiary PowerSecure Agrees To Provide Fully Integrated Backup Resiliency Solution For Keel Infrastructure's Data Center Campus In Moses Lake, Washington"
- **PURR** +9.8%: "PURR Jumps 8% as SEC Approves 'Innovation Exemption' for Tokenized Stock Trading"
- **BMNR** +8.7%: "Why Is BitMine Stock Surging on Friday?"
- **ETHA** +7.8%: "Ethereum's Layer-2 Tokens Rallied Up to 26% in a Day. Why Ethereum Only Managed 7%"
- **IBIT** +6.2%: "JPMorgan Says Bitcoin Could Beat Gold as Analyst Predicts It'll 'Triple' Gold"
- **NFLX** -4.6%: "Why Is Netflix Stock Falling Friday?"

## Day Trading Watchlist

No names cleared the day-trading bar today. That flag encodes gap over 3%, price over $3, market cap over $1B, premarket RVOL over 1.5, and price already breaking above yesterday's high.

Six names clear every leg of that rule except the last one. All six have market cap well over $1B and heavy RVOL (27x to 57x), but the premarket quote is still sitting just under yesterday's high on every one of them:

| Ticker | Price now | Prior day high | Gap to clear |
|---|---|---|---|
| IBIT | $46.01 | $46.12 | -0.2% |
| ETHA | $19.90 | $19.97 | -0.4% |
| MARA | $13.24 | $13.31 | -0.5% |
| BMNR | $25.95 | $26.36 | -1.6% |
| KEEL | $4.00 | $4.08 | -2.0% |
| PURR | $14.075 | $14.46 | -2.7% |

IBIT is the closest, less than a quarter percent under yesterday's high. But this scan ran at 7:18am ET, well before the open, so none of these are real trades yet, they're names to watch for a break the moment the session starts.

One more note: the scanner marks `today_open` as null for every gapper (no real print yet) and uses the premarket quote as a stand-in per the packet's own gaps-to-fill note. Treat the table above as directional, not exact, until the actual open prints.

## Swing Watchlist

No names cleared the swing bar either. That flag encodes gap of 8% or more, price over $3, open above yesterday's high, open above the 200-day SMA, market cap of $800M or more, and a real catalyst behind the move.

MARA, KEEL, PURR, and BMNR all clear the 8% gap floor and the $800M cap floor, and all four are above their 200-day SMA. But they're the same four names sitting just under yesterday's high from the table above, so none of them clear the swing bar either. ETHA and IBIT don't even reach the 8% swing floor (7.8% and 6.2%), so they're day-trading-only near-misses, not swing near-misses.

Plenty of the smaller names clear the 8% gap threshold on paper (IMCC, GEMG, TJGC, TNMG, SVRN, AUC, HUHU, PRPL, MSTP), but every one of them is under the $800M market cap floor, TJGC is the closest at $258M. So the gap size is there, the level and the size aren't.

## Market Trends of the Day

Today's `market_news` feed leans general finance and lifestyle, not a tight macro thread like some prior runs, but a few real market items surface. Futures sentiment into the week: "Dow, S&P 500, Nasdaq futures rise as oil falls, anticipation builds for Trump-Xi summit," and a separate item flags "Trump and Xi dine with AI titans and Meta takes the stage" as the thing to watch this week. That framing doesn't quite match what the packet's own index proxies show as of the scan (S&P, Dow, and Russell proxies all slightly red, only Nasdaq green), so treat the futures-rally headline as a different moment in the morning than this scan's snapshot.

Consumer stress is a visible thread: "Key Christmas retailer files for Chapter 11 bankruptcy" and "Dollar General CEO raises major red flag about consumers" both point the same direction. Goldman strategists are flagging that "corporate earnings are growing much faster than the economy," a bubble-concern framing worth keeping in mind against any single hot gapper. Novo Nordisk is down on its 2030 goals reveal, and Chevron's CEO is out with commentary on oil price and the economy, both worth a glance if energy or healthcare context matters to your other positions.

Crypto is the real story behind today's biggest qualified gappers: MARA, KEEL, PURR, BMNR, ETHA, and IBIT all show up on the gapper list together, and their own catalyst headlines point at a Bitcoin and Ethereum rally (Bitcoin topping $80,000, Ethereum eyeing a $3,000 rebound, JPMorgan calling for Bitcoin to triple gold). That's a coherent group move, not six unrelated coincidences.

## Technical Signals for Today

Partial data again this morning. The four major index proxies came through via Alpaca ETF data: S&P 500 (SPY proxy) -0.13%, Dow (DIA proxy) -0.48%, Nasdaq (QQQ proxy) +0.62%, Russell 2000 (IWM proxy) -0.46%. Mixed, not a clean risk-on or risk-off tape. These are ETF stand-ins, not the actual index prints, so treat them as directional.

VIX, the 10-year yield, the 3-month yield, WTI crude, and the dollar index all came back null, yfinance rate limited them even after retries. No read on volatility or rates levels this morning.

## Economic Data, Rates and the Fed

Nothing on the calendar. The econ calendar (high-impact USD only) shows zero events for today, September 21, and zero for tomorrow, September 22.

## Coming Up

- **Tomorrow's events:** None in the calendar for September 22.
- **Earnings:** No earnings dates available. Every gapper's `next_earnings_date` field came back null this run. The packet's own gaps-to-fill note says 106 requests failed even after retries this scan, and the per-ticker enrichment log shows yfinance returning "Too Many Requests" on every single ticker's intraday, news, and earnings pull.

## Skips and Traps

**OIG is close to a total data blackout.** A +2967.6% gap off a $0.38 prior close, but there's no market cap, no volume, no RVOL, and no intraday data at all, both the daily bars and intraday sources came back "unavailable." The only catalyst headlines on file are stale, dated August 2023 and generic ("12 Industrials Stocks Moving," a Dow/NVIDIA market recap). Nothing in the packet explains today's move. Don't touch this one.

**PRPL and TJGC are up on news that isn't clean good news.** PRPL beat on EPS but missed on sales and cut its FY2026 sales guidance from $465-485M down to $420-440M, guidance cuts are explicitly the kind of headline that should make a gap-up suspicious, not confirm it, even though the packet also shows a genuine EPS beat in the mix. TJGC's most recent headline is a $100M mixed shelf prospectus, a dilutive filing, while the stock is gapping up 53%; there's an older AI/robotics IP licensing headline in the same ticker's history that could be the real story, but the freshest item on file is the shelf filing. Both are worth a second look before trusting the pop, though neither clears the cap floor for either watchlist anyway.

**IMCC, SVRN, AUC, and GEMG have thin or mismatched catalysts.** `catalyst_found` is true for all four, but IMCC's most relevant headline is actually about Lobo Technologies, a different company, and SVRN's includes a headline about iSpecimen, also a different company. AUC's only ticker-specific item is a CEO appointment from earlier this year, not a same-day story. GEMG has no market cap data (SEC EDGAR has no CIK for it) and its two headlines are a stale trading halt notice and an unrelated leveraged-ETF product launch. None of these four have a real, fresh, ticker-specific reason for today's move sitting in the packet.

**TNMG and MSTP look like corporate-action or product artifacts.** TNMG just implemented a 1-for-8 reverse share consolidation effective September 8, which can distort gap and RVOL math for a while after the fact. MSTP has no market cap data at all and its only non-halt headline is about a different, similarly-named leveraged crypto ETF product crashing, consistent with MSTP itself being a fund or derivative product rather than an operating company.

**PCTTU's catalyst is three years stale.** The only headline on file is "8 Stocks Halted In Tuesday's Session" from 2022. Nothing in the packet explains today's -50.7% move.

**HUHU has real, specific catalysts** (semiconductor subsidiary contract wins, a purchase order, a construction milestone) but sits at a $141M market cap, well under both watchlist floors. Worth knowing the name, but the rules aren't built to size it.

**XENE, DAIC, and NFLX are down moves with catalysts that actually match the direction**, not traps, just not gap-up candidates. XENE's headlines ("Xenon Pharmaceuticals Shares Plunge," "Xenon Stock Reaction Is Overblown: Analyst") line up with its -30.7% gap. NFLX's headlines ("Why Is Netflix Stock Falling Friday?", a Wells Fargo target cut) line up with its -4.6% gap. DAIC only shows up in a generic radar-list headline, no clear reason for its -33.0% drop in the packet.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
