# Premarket Report: November 26, 2026

*Single-brain pass: Claude only. Second brain not wired in yet.*

> Rules pick the watchlist. The AI judges the quality of the setups. This is not financial advice.

**Read this first: no cash session today.** It's Thanksgiving. The packet's own headlines say it: "Is the stock market open for Thanksgiving? The answer might surprise you." (MarketWatch), whose summary says "the major exchanges are closed, but trading of equity futures is open for part of the day." There's also "Is the stock market closed? Thanksgiving, Black Friday trading hours" (Detroit Free Press). No regular session means no 10:00am to 3:30pm trade window, so nothing below is a trade for today. Treat this as a read on Wednesday's close heading into Friday.

**Data warning.** The packet says "Scan run 2026-11-26 07:07 EST (premarket)." Same pattern as the last several days: these aren't this morning's gaps. For the cap-qualified names, `price` equals `prior_close` (MU 600.4 vs 600.4, SNDK 73.56 vs 73.56, AMBA 35.68 vs 35.66, PHAR 10.05 vs 10.11). So `gap_pct` is really Wednesday's close vs Tuesday's close. The index proxies agree: SPY's `prev_close` of 718.91 is the SPY last from yesterday's report. The packet has no futures numbers, only headlines.

Yahoo rate-limited the scan again: 61 requests failed even after retries. Intraday data is `unavailable` for all 15 gappers, so VWAP, HOD, LOD, premarket high and premarket volume are null across the board. `today_open` and `next_earnings_date` are null for all 15. VIX, 10Y, 3M, WTI and the dollar are null. Index levels are ETF proxies (SPY, DIA, QQQ, IWM). Market cap is null for MUU, NVDL, NVD, RKT and NU. `rvol` is null for the seven rows sourced from Alpaca's movers list (WLDSW, EUDA, FCUV, RIBBU, PW, PHAR, AMBA).

## Summary

- **The tape in one line:** Wednesday was a wobble, not a flush. QQQ -0.66%, SPY -0.3%, DIA +0.3%, IWM +0.61%. MarketWatch: "A rebound off lows for the S&P 500 on Wednesday calms bourses after AI wash out," and "Futures point to Black Friday gains for Wall Street."
- **The catch we're watching:** Markets are closed today. The real question is whether Wednesday's late tech bounce ("Oracle, CoreWeave and other tech stocks bounce back after selloff") holds into Friday, or whether "this stock-market selloff is probably going to get worse before it gets better" (MarketWatch).
- **Two-brain verdict:** Single-brain run, no second opinion.

## Pre-Market Gappers

All 15 gappers in the packet. Gap % is `price` vs `prev_close` (Wednesday's move for the big names, see the warning above). Market cap in parentheses. The headline is the first one the packet lists for each ticker.

- **WLDSW** +134.68% ($277.4M, SEC-derived): no headline in the packet (`catalyst_found: false`)
- **EUDA** -53.67% ($7.9M): "EUDA Health Subsidiary Melana International Wins Golden Bull Award 2026 Singapore"
- **FCUV** +53.12% ($5.5M): "Focus Universal Inc. (FCUV) Experiences Significant Stock Price Movement"
- **RIBBU** +52.5% ($475.9M, SEC-derived): no headline in the packet (`catalyst_found: false`)
- **PW** -32.97% ($1.3M): "Power REIT Reports Third Quarter 2026 Financial Results"
- **PHAR** -23.98% ($7.05B, SEC-derived): "Form 8.5 (EPT/RI) Disclosure Regarding Pharos Energy Plc"
- **AMBA** -19.77% ($1.57B): "Analyst Downgrades and Price Target Adjustments for Ambarella"
- **MUU** -8.95% (cap null): no headline in the packet (`catalyst_found: false`)
- **NVDL** -8.01% (cap null): no headline in the packet (`catalyst_found: false`)
- **NVD** +7.94% (cap null): no headline in the packet (`catalyst_found: false`)
- **RKT** +7.34% (cap null): "New York Regulators Fine Rocket Mortgage and Mr. Cooper $6.75 Million for Cybersecurity Violations"
- **STLA** +5.94% ($10.59B): "Stellantis Scales Back French Plant Operations"
- **SNDK** -5.58% ($10.47B): "Tradr ETFs Announces Launch of Triple Threat Series Including Memory ETF Featuring SanDisk"
- **MU** -4.71% ($679.31B): "Tradr ETFs Announces Upcoming Launch of Leveraged ETF Featuring Micron Technology, Inc."
- **NU** +4.21% (cap null): "Nubank Receives Official Recognition as a Bank in Brazil"

## Day Trading Watchlist

The bar is Trend Join Long: gap > 3%, price > $3, market cap > $1B, premarket RVOL > 1.5, and price already breaking above yesterday's high.

No names cleared the day-trading bar today. Every gapper is `day_eligible: false`. And there's no session to trade anyway. STLA came closest: gap +5.94%, price 3.655, $10.59B cap, RVOL 34.7, but it sits just under its prior-day high of 3.69. RKT (+7.34%) and NU (+4.21%) are also under their prior-day highs (15.28 vs 15.39, 12.365 vs 12.53) and have null market caps.

## Swing Watchlist

The bar is: gap >= 8%, price > $3, open above yesterday's high, open above the 200-day SMA, market cap >= $800M, and a real catalyst (earnings on the gap day, or news with no earnings).

No names made the swing list today. Every gapper is `swing_eligible: false`. The only up-gappers over 8% are WLDSW, FCUV and RIBBU, and all three are sub-$800M caps with junk volume. See Skips and Traps.

## Market Trends of the Day

Tuesday was the AI selloff. Wednesday was the dip-buy that didn't quite finish. QQQ still lost 0.66% and SPY 0.3%, but DIA (+0.3%) and IWM (+0.61%) were green, the same tech-down, everything-else-up rotation as Tuesday, just much milder. MarketWatch's read: "Oracle, CoreWeave and other technology stocks bounced back from early losses on Wednesday, after what appeared to be a major selloff eased ahead of the market's close."

Memory is where the selling stuck. MU -4.71% (RVOL 58.24) with "BNP Paribas Downgrades Micron Technology to Neutral" in its headlines, and SNDK -5.58% (RVOL 142.86) with "SanDisk Shares Decline Amid Weak NAND Flash Price Outlook." AMBA -19.77% after earnings, with BofA cutting its target to $30 from $70 and Morgan Stanley to $70 from $96 (both per the packet's links).

Overseas and overnight, the mood is better. "Global stocks rally as investors shrug off U.S. tariffs and AI jitters" (CNBC) and "Futures point to Black Friday gains for Wall Street as global markets welcome U.S. resilience" (MarketWatch).

The strategist split is wide. Deutsche Bank says "The tech rout should bottom soon, with a 25% rally for the S&P 500 to follow," targeting 9,000 by end of 2027 as focus "shifts from capital expenditure to monetization." On the other side, MarketWatch's "Why this stock-market selloff is probably going to get worse before it gets better" argues "Monday's rally helped to paper over deeper issues." The FT chimes in with "It's an earnings bubble, not a valuation bubble."

## Technical Signals for Today

ETF proxy levels from the scan vs each one's `prev_close` (this is Wednesday's session, not this morning's futures):

- SPY 716.74 (prev 718.91), -0.3%
- DIA 501.29 (prev 499.78), +0.3%
- QQQ 633.92 (prev 638.12), -0.66%
- IWM 268.84 (prev 267.2), +0.61%

Tech lagged again, but the gap between QQQ and the rest narrowed a lot from Tuesday. VIX, 10Y, 3M, WTI and DXY are all null, so there's no volatility, rate, oil or dollar read.

Cap-qualified names vs prior-day high and the 200-day SMA (no VWAP or HOD, intraday data was unavailable):

- MU 600.4: under its prior-day high of 604.78 and the 200-day SMA of 776.38.
- SNDK 73.56: just under its prior-day high of 73.77. The 200-day SMA of 1275.57 still doesn't fit the price. Bad data, ignore it.
- STLA 3.655: just under its prior-day high of 3.69, well under the 200-day SMA of 6.08.
- AMBA 35.68: under its prior-day high of 36.54, about half the 200-day SMA of 66.69.
- PHAR 10.05: under its prior-day high of 10.89 and the 200-day SMA of 13.34.

Not one cap-qualified name is above its 200-day SMA.

On volume: daily bars are Alpaca IEX, a subset of the tape, and the RVOL figures look like a full Wednesday session against a 20-day average. Don't read those multiples literally.

## Economic Data, Rates and the Fed

From `econ_calendar` (USD, high impact only):

- **Today (Thursday, November 26):** nothing high-impact listed.
- **Tomorrow (Friday, November 27):** nothing high-impact listed.

The calendar's `note` field is empty, so no fetch problem flagged. With no 10Y or 3M reading there's no rates read, and the packet has no Fed headlines today. Yesterday's Core PCE and Prelim GDP prints aren't in this packet, so there's nothing to report on what they showed.

## Coming Up

- **Tomorrow's events:** nothing high-impact on the USD calendar. Friday is Black Friday. The packet's Detroit Free Press headline mentions "Black Friday trading hours" but doesn't give them, so check the session hours before you plan anything.
- **Earnings:** `next_earnings_date` is null for all 15 gappers, and the packet has no market-wide earnings calendar. MU has a headline "Micron Technology Schedules Fiscal First Quarter 2027 Earnings Call" with no date in the title (the link points to December).

## Skips and Traps

- **Everything, today:** no cash session. Nothing trades until Friday.
- **STLA** +5.94%: the closest thing to a day setup, but under its prior-day high (3.655 vs 3.69) and way under its 200-day (6.08). The lead headline is bad news, "Stellantis Scales Back French Plant Operations," with "Stellantis Files Lawsuit Against Unifor Over Brampton Plant Access" right behind it. The only bullish item is "Stellantis Plans Increased Fiat 500 Production at Mirafiori for 2027," whose link mentions a JPMorgan report lifting autos. Up on a mixed-to-bad headline set. Treat as a trap.
- **RKT** +7.34%: null market cap, and the catalyst match is broken. Three of its five headlines are about Reckitt ("Reckitt Enters 10-Year Renewable Power Purchase Agreement" and others), a different company. The Rocket ones are a $6.75M regulatory fine and a Las Vegas Grand Prix sponsorship. Neither explains the move. Skip.
- **NU** +4.21%: null market cap, under its prior-day high (12.365 vs 12.53). The headlines are older news (bank license, Q3 results) plus "Nubank Halts Some Crypto Transactions." Skip.
- **AMBA** -19.77%: earnings gap-down with two big target cuts. Not a long setup for either list.
- **PHAR** -23.98%: real bad news, "Pharming Temporarily Pauses RUCONEST® Manufacturing Following Media Fill Failure," with the link adding it notified the FDA of a likely supply interruption. Also, the $7.05B SEC-derived cap sits next to a 20-day average volume of 182, which doesn't hang together. And the lead headline is about Pharos Energy, a different company. Skip.
- **MU** and **SNDK**: gap-downs on memory weakness, both under their prior-day highs. The lead headlines are leveraged-ETF launches, not catalysts. Skip.
- **WLDSW** +134.68% and **RIBBU** +52.5%: warrant- and unit-style tickers (W and U suffixes, and RIBBU's name is Ribbon Acquisition Corp.), no catalyst, 20-day average volume of 0 and 20. `prev_close` doesn't match `prior_close` for either (41.0 vs 23.7, 62.0 vs 39.0), so the gap math itself is shaky. Skip.
- **FCUV** +53.12%: $5.5M cap. The lead headline just says the stock moved, and the next one is "Focus Universal Inc. Announces Exercise of Warrants for Approximately $3.7 Million in Gross Proceeds." More shares. Skip.
- **EUDA** -53.67% and **PW** -32.97%: $7.9M and $1.3M caps, both with reverse splits in their headlines ("1-for-20" and "One-for-Ten"). Skip.
- **MUU**, **NVDL**, **NVD**: ticker-only rows, no name, no cap, no catalyst. The scanner's note says names like this are often ETFs, warrants or foreign issuers SEC doesn't cover. Skip.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
