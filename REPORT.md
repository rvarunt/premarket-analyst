# Premarket Report: August 13, 2026

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** Futures proxies are green across the board but small. SPY proxy for the S&P is +0.26%, DIA/Dow is flat at -0.03%, QQQ/Nasdaq is +0.74%, IWM/Russell 2000 is +0.58%. No VIX, no rates, no oil, no dollar data today, all of it failed to pull (see Technical Signals below).
- **The catch we're watching:** Core PPI and headline PPI print at 8:30am ET. Yesterday's CPI reportedly pushed September hike odds to 33% per one of today's catalyst headlines, so PPI adds another data point to that read before the open.
- **Two-brain verdict:** Single-brain run today, no second opinion to compare against.

## Pre-Market Gappers

- **BOXL** +168.6% - "Boxlight Shares Rally Following Capital Raising Deals"
- **NEBX** +68.51% - "Double Or Nothing: Tradr Rolls Out 6 High-Octane ETFs Promising Big Swings"
- **NBIL** +68.28% - "Nebius Q2 Outlook: Will Goldman's $35.5 Billion Revenue Forecast Overpower Jim Cramer's 'Sell' Warning?"
- **NBIG** +68.07% - "Nebius Q2 Outlook: Will Goldman's $35.5 Billion Revenue Forecast Overpower Jim Cramer's 'Sell' Warning?"
- **NBIZ** -67.76% - "Coinbase, Nebius, IREN Stocks Are Getting Hammered, And These ETFs Are Making A Fortune"
- **NBIC** +66.52% - no catalyst headline in the packet
- **QNTU** +53.25% - "Tradr Bets on Quantum Boom With 5 New 2X ETFs on Quantinuum, Ciena"
- **BRUNW** +50.07% - no catalyst headline in the packet
- **XHLD** +49.86% - "TEN Holdings Q2 EPS $(0.70) Up From $(1.95) YoY, Sales $731.000K Down From $1.116M YoY"
- **CRWX** +40.64% - no catalyst headline in the packet
- **WXM** -39.75% - "12 Industrials Stocks Moving In Wednesday's Intraday Session" (only generic mover-list mentions, nothing WXM-specific)
- **SMCZ** -38.64% - "Super Micro Plummets, But This ETF Turned It Into A 40% Payday"
- **SMCI** +18.59% - "Citigroup Maintains Neutral on Super Micro Computer, Raises Price Target to $39"
- **WEN** +14.7% - "Wendy's Traders Smell a Buyout Cooking, Nelson Peltz Preps a Bid"
- **TE** -10.26% - "T1 Energy Files Prospectus For Resale Of 13,615,979 Shares"
- **IREN** +9.89% - "IREN Announces Delivery And Acceptance Of Horizon 1 By Microsoft, First Of Four 50MW Deployments Under $9.7B Five-Year Contract; Achieves NVIDIA Exemplar Cloud Status"
- **NOK** +9.25% - "Why Is Nokia Stock Surging Wednesday?"
- **KEEL** +7.93% - "Keel Infrastructure Q2 Earnings Miss Estimates as Bitcoin Wind-Down Continues"
- **ACHR** -7.23% - "Why Is Archer Aviation Stock Falling on Wednesday?"
- **ORCL** +5.4% - "Oracle Weighs Another Round of Job Cuts This Month as AI Infrastructure Spending Drives Debt: Report"

## Day Trading Watchlist

The "Trend Join Long" rule: gap over 3%, price over $3, market cap over $1B, premarket RVOL over 1.5, and price already breaking above yesterday's high.

No names cleared the day-trading bar today. And it's worth saying why: every single gapper in this packet came back with `intraday_data_source: "unavailable"`, so `premarket_high`, `hod`, `lod`, and `vwap` are null across the board. The rules engine can't confirm the "breaking above yesterday's high" leg of the setup without that data, so nothing gets flagged eligible, no matter how good the catalyst looks. This isn't a "nothing is happening" day, it's a data blackout day. See Skips and Traps below for names that would be worth a second look once intraday data comes back.

## Swing Watchlist

The swing rule: gap of 8% or more, price over $3, open above yesterday's high, open above the 200-day SMA, market cap of $800M or more, and a real catalyst.

No names cleared the swing bar today either, same root cause as the day watchlist: `today_open` is null for every gapper (it's premarket, the real open hasn't printed, and the scanner is using the current gap price as a stand-in per its own note in the packet), and none of the big gappers pair size with an $800M+ market cap and a genuine single-company catalyst at the same time. The closest candidates on catalyst quality alone (IREN, WEN) are both under the 8% gap threshold anyway.

## Market Trends of the Day

AI infrastructure spending is the throughline, but it's not a clean "everything AI is up" morning. Lenovo beat expectations on AI PCs, servers and services. On the flip side, Cisco is getting hit on margin concerns despite the AI capex story. Bank of America put out a blunt note to Nvidia investors, and Oracle's own gap up is riding alongside a headline about it weighing more job cuts to fund AI infrastructure debt, so the AI trade is showing some cracks even where the stocks are green. IREN's gap is the cleanest AI-infra catalyst in the packet: a real signed delivery under a $9.7B five-year Microsoft contract. Outside the US, South Korea's market is described as shifting from bear to bull. And there's a tape-wide tension worth flagging: one of the packet's news items says the rally has energized stocks but left the credit market concerned, which is the kind of divergence that tends to matter more than any single gapper.

## Technical Signals for Today

Index proxies (via Alpaca ETF fallback since the direct index pulls failed): SPY proxy +0.26%, DIA proxy -0.03%, QQQ proxy +0.74%, IWM proxy +0.58%. All small moves, nothing extended.

Everything else needed a straight yfinance pull and every one of those calls failed today: VIX, US 10Y, US 3M, WTI Oil, and the Dollar Index all came back null (`data_source: yfinance_failed`). No breadth data is in the packet either. So there's no vol read, no rates read, no dollar read to hand you this morning. Take that as a flag on its own, not just a gap in the report.

## Economic Data, Rates and the Fed

Today, 8:30am ET: Core PPI m/m, forecast 0.3%, previous 0.2%. Also at 8:30am ET: headline PPI m/m, forecast 0.2%, previous -0.3%. That's it for high-impact USD data today per the calendar filter, nothing else listed.

One of today's catalyst headlines (attached to SMCI) references yesterday's CPI print sending September Fed hike odds to 33%. That's the only Fed-odds figure anywhere in the packet, so take it as one data point from one headline, not a verified consensus number. PPI this morning adds to that read before the bell.

## Coming Up

- **Tomorrow's events:** Nothing listed. The econ calendar's "tomorrow" (August 14) came back empty under the high-impact USD filter.
- **Earnings:** `next_earnings_date` is null for every gapper in this packet, so there's nothing to report here. No confirmed earnings dates for any of today's names.

## Skips and Traps

- **NBIC, BRUNW, CRWX**: `catalyst_found: false` on all three. No catalyst, no story, skip regardless of the gap size (66.52%, 50.07%, and 40.64% respectively).
- **NEBX, NBIL, NBIG, NBIZ, QNTU, SMCZ**: these read like leveraged or inverse single-stock ETFs riding another name's move (Nebius for the NB-tickers, Quantinuum/Ciena for QNTU, Super Micro for SMCZ), not real single-company catalysts. None of them have a market cap (SEC EDGAR has no CIK or no shares-outstanding concept for any of them, consistent with these being funds, not operating companies), and their "catalysts" are ETF-launch or generic sector pieces about the underlying name, not about the ticker itself. Skip the whole group.
- **BOXL**: +168.6% on a $31.5M market cap, driven by a mix of a Q2 sales miss and a capital-raising deal. A capital raise is dilutive by nature, and a 168% pop on a sub-$50M name off that kind of news is exactly the setup this report warns about. Treat as a trap, not a buy, even though it's not on either watchlist.
- **XHLD**: $64M market cap, and the only ticker-specific headline in the packet quotes Q2 sales of $731,000. That's not a typo, sales in the hundreds of thousands against a 49.86% pop. No fundamental case here.
- **WXM**: catalyst_found came back true, but every headline attached to it is a generic "12 Industrials Stocks Moving" roundup, nothing actually about WXM. Treat the catalyst as unconfirmed and skip.
- **KEEL**: +7.93% on a Q2 EPS and sales miss ("Q2 EPS $(0.11) Misses $(0.06) Estimate, Sales $30.430M Miss $32.397M Estimate"). Gapping up on a miss is the bad-news-pop pattern this report flags as a trap, not a buy.
- **NOK**: the only headline is "Why Is Nokia Stock Surging Wednesday?", which doesn't actually answer its own question in what made it into the packet. No confirmed catalyst behind the +9.25%, treat with caution.
- **ORCL**: gapping up +5.4% alongside a headline about weighing more job cuts to fund AI infrastructure debt. Cost cuts can read either way to the market, but debt-funded AI capex plus layoffs is a mixed signal at best, not a clean green light.
- **TE**: gapping down -10.26% alongside a share resale prospectus for 13.6M shares (dilutive) and a mixed Q2 (EPS miss, sales beat). Down on bad news is expected, not a trap, just not a name to fade into strength today.
- **ACHR**: gapping down -7.23% with only a "why is it falling" headline and no specifics in the packet. Nothing actionable either way.
- **WEN and IREN**: these are the two best-looking catalysts in the whole packet (a real buyout rumor with a named source on WEN, a signed $9.7B Microsoft contract on IREN), and neither made a watchlist. That's purely the intraday data blackout described above, not a knock on the catalysts. Worth a manual look once premarket high/HOD/LOD data is actually available today.
- **SMCI**: split analyst picture (Citi Neutral with a price target raise to $39, Goldman Sachs still Sell with a price target raise to $34), no single clear catalyst behind the +18.59% beyond that. Would also have needed intraday confirmation it didn't get today.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
