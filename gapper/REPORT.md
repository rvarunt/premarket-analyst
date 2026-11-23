# Premarket Report: November 23, 2026

*Single-brain pass: Claude only. Second brain not wired in yet.*

> Rules pick the watchlist. The AI judges the quality of the setups. This is not financial advice.

**Data warning: read this first.** The packet says "Scan run 2026-11-23 07:19 EST (premarket)." Same problem as last week: most gaps aren't this morning's gaps. For most names `price` sits on or within a cent of `prior_close` (NVDA 125.65 vs 125.65, AMD 424.3 vs 424.3, IREN 11.82 vs 11.82, INTC 51.37 vs 51.37, NOK 6.88 vs 6.88, SNDK 79.245 vs 79.25). So `gap_pct` is really Friday's close vs Thursday's close. The index proxies line up with that: SPY's `prev_close` of 715.84 is exactly what Friday's report showed as SPY's last. Read the numbers below as Friday's session. The packet has no futures numbers for this morning, only headlines.

Yahoo rate-limited the scan again: 111 requests failed even after retries. Intraday data is `unavailable` for all 20 gappers, so VWAP, HOD, LOD, premarket high and premarket volume are null across the board. Per-ticker Yahoo news failed, so catalysts are Alpaca headlines plus RSS matches only. VIX, 10Y, 3M, WTI and the dollar are null. Index levels are ETF proxies (SPY, DIA, QQQ, IWM). `next_earnings_date` is null for all 20. `today_open` is null for all 20.

The SEC market cap fallback mismatched at least three names this morning, so don't trust those caps. SONN came back as "SOUTHERN CO" with a $57.5B cap. TPEI and TAWN both came back as "BANK OF MONTREAL /CAN/" using the exact same share count (708,905,679), giving TPEI $69.2B and TAWN $4.83B. Market cap is null for 7 more (MACI, MRAL, IREZ, IPFXU, APLZ, MRAX, NBIZ).

## Summary

- **The tape in one line:** Friday was a crash day for tech. SPY -3.51%, QQQ -5.48%, IWM -2.83%, DIA -1.94%, with NVDA -13.93% and AMD -13.31%. MarketWatch says the S&P made a "swift fall into a correction." This morning the headlines lean bounce: "US Stock Futures Bounce After AI-Driven Correction: Markets Wrap" (Bloomberg) and "Nvidia stock bounces as Trump administration pushes for rehiring of Jensen Huang" (MarketWatch). The packet has no futures numbers to size that bounce.
- **The catch we're watching:** whether the bounce holds or the AI unwind keeps going. Asia didn't bounce: "Asian stock markets tumble as AI bubble fears mount" (Al Jazeera). The bull case is in the feed too: Morgan Stanley's top strategist calls it a "fat pitch," and MarketWatch notes slides this steep and fast "trigger a rebound 91% of the time over the last decade."
- **Two-brain verdict:** Single-brain run, no second opinion.

## Pre-Market Gappers

All 20 gappers in the packet. Gap % is `price` vs `prev_close` (mostly Friday's move, see the warning above). Market cap in parentheses. The headline is the first one the packet lists for each ticker.

- **SONN** +3949.21% ($57.51B, mismatched to Southern Co): no headline in the packet (`catalyst_found: false`)
- **SNDK** -89.5% ($11.28B): "Morgan Stanley Adjusts Price Target on Sandisk to $218 From $218.75"
- **MACI** +62.2% (cap null): "Melar Acquisition Corp. I Completes Business Combination with Everli Global Inc."
- **MRAL** -36.56% (cap null): no headline in the packet (`catalyst_found: false`)
- **IREZ** +36.36% (cap null): no headline in the packet (`catalyst_found: false`)
- **IPFXU** -36.18% (cap null): no headline in the packet (`catalyst_found: false`)
- **APLZ** +35.77% (cap null): no headline in the packet (`catalyst_found: false`)
- **TPEI** +34.06% ($69.22B, mismatched to Bank of Montreal): "Deutsche Bank bullish on EU utilities as earnings forecasts lag sector upcycle - Investing.com"
- **MRAX** -34.0% (cap null): no headline in the packet (`catalyst_found: false`)
- **TAWN** -33.95% ($4.83B, mismatched to Bank of Montreal): "Deutsche Bank bullish on EU utilities as earnings forecasts lag sector upcycle - Investing.com"
- **NBIZ** +32.12% (cap null): no headline in the packet (`catalyst_found: false`)
- **IREN** -17.92% ($4.22B): "Blue Owl Managed Funds Lead $2.4 Billion AI Factory Financing for IREN"
- **WULF** -15.14% ($4.93B): "Lansing Town Board Votes to Ban AI Data Centers Amid TeraWulf Project Proposal"
- **NVDA** -13.93% ($3.03T): "Trump Administration Pushes for Reinstatement of Jensen Huang as NVIDIA CEO"
- **AMD** -13.31% ($695.89B): "Law Firms Announce Securities Investigations into Advanced Micro Devices, Inc."
- **NOK** -8.27% ($39.51B): "VodafoneThree Partners with Nokia and NVIDIA for UK AI-RAN Trials"
- **INTC** -7.77% ($273.03B): "Glows.ai Joins Intel's Innovation Pass Program at SC26"
- **SOFI** -7.58% ($16.22B): "SoFi Releases National Survey on Homebuyer Challenges and Sentiment"
- **AAL** -6.25% ($7.89B): "American Airlines Retires International First-Class Cabin"
- **IBIT** -5.9% ($47.34B): no headline in the packet (`catalyst_found: false`)

## Day Trading Watchlist

The bar is Trend Join Long: gap > 3%, price > $3, market cap > $1B, premarket RVOL > 1.5, and price already breaking above yesterday's high.

No names cleared the day-trading bar today. Every gapper is `day_eligible: false`. Every real, cap-qualified name in the packet (SNDK, IREN, WULF, NVDA, AMD, NOK, INTC, SOFI, AAL, IBIT) is gapping down. The only up-movers with a cap over $1B are SONN and TPEI, and both caps come from a wrong SEC match. With premarket high and HOD null for everyone, there are no live levels to build a plan off even if something had qualified.

## Swing Watchlist

The bar is: gap >= 8%, price > $3, open above yesterday's high, open above the 200-day SMA, market cap >= $800M, and a real catalyst (earnings on the gap day, or news with no earnings).

No names made the swing list today. The rules engine flagged one, TPEI (`swing_eligible: true`), and it's pulled. Its only headline is "Deutsche Bank bullish on EU utilities as earnings forecasts lag sector upcycle - Investing.com," a generic RSS match that doesn't mention TPEI. TAWN got the exact same headline, which tells you it's a false match. So there's no catalyst, and no catalyst means no trade. On top of that, its $69.22B cap is a mismatch to Bank of Montreal and its 20-day average volume is 0. Details in Skips and Traps.

## Market Trends of the Day

Friday was the AI unwind going vertical. QQQ fell 5.48% against DIA's 1.94%, so tech did most of the damage. Every big AI name in the gapper list got hit on huge volume: NVDA -13.93% (RVOL 63.54), AMD -13.31% (RVOL 59.77), INTC -7.77% (RVOL 42.67), IREN -17.92% (RVOL 44.72), WULF -15.14% (RVOL 19.74). Bitcoin went with it: IBIT -5.9%, no headline in the packet.

The weekend news on Nvidia is the swing factor. MarketWatch says "Shares in Nvidia rose on Monday after a weekend of more developments, including the Trump administration pushing for the reinstatement of Jensen Huang to lead the company." AMD has bad news stacking up: "Law Firms Announce Securities Investigations into Advanced Micro Devices, Inc." on top of the Hunterbrook China-ties report and an insider sale.

Memory got hit hardest. SNDK's headlines are all bad: "SanDisk Shares Decline Amid Weak NAND Flash Price Outlook," "SanDisk Shares Decline Following Commerce Department Regulatory Update," and "SanDisk Shares Decline Following Kioxia Pricing Warning." One Barchart link reads "micron-sk-hynix-and-sandisk-shares-plummet."

Data center builders have a local-politics problem too: "Lansing Town Board Votes to Ban AI Data Centers Amid TeraWulf Project Proposal."

It's global and it hasn't stopped. "Asian stock markets tumble as AI bubble fears mount" (Al Jazeera), and Breakingviews has "Asia AI rout puts governments in a bind." US futures are the exception this morning, per Bloomberg.

Two other things in the feed. CrowdStrike "will acquire Zscaler in an all-stock transaction that values the company at approximately $43.9 billion" (MarketWatch). Neither name is in the gapper list, so the packet has no price on either. And "Gold climbs more than 2% as dollar rally pauses" (Reuters), though the packet has no gold or DXY row to confirm it.

The bull case is getting louder. Morgan Stanley's strategist points to "trough Nasdaq valuations, implied earnings declines and a capitulation in both sentiment and positioning." MarketWatch cites a 91% rebound rate after slides this steep. The bear case is Ackman: "The U.S. may enter a recession if the Fed raises rates," because "financial conditions have already considerably tightened."

One headline to ignore: "Nasdaq 100 Forecast: NDX falls ahead of Nvidia's earnings & Anthropic's debut this week" (StoneX). Last week's reports in this repo already covered Nvidia's post-earnings slide and Anthropic's debut, so this headline looks out of date.

## Technical Signals for Today

ETF proxy levels from the scan vs each one's `prev_close` (this is Friday's session, not this morning's futures):

- SPY 690.68 (prev 715.84), -3.51%
- DIA 481.23 (prev 490.75), -1.94%
- QQQ 609.75 (prev 645.1), -5.48%
- IWM 256.72 (prev 264.21), -2.83%

Thursday was everything down about 2%. Friday was worse, and it was a tech-led break. MarketWatch calls the S&P's drop a "swift fall into a correction." VIX, 10Y, 3M, WTI and DXY are all null, so there's no volatility, rate, oil or dollar read.

Cap-qualified names vs prior-day high and the 200-day SMA (no VWAP or HOD today, intraday data was unavailable):

- NVDA 125.65: under its prior-day high of 143.72 and well under the 200-day SMA of 203.34. RVOL 63.54.
- AMD 424.3: under its prior-day high of 474.68, and just under the 200-day SMA of 429.77. RVOL 59.77.
- INTC 51.37: under its prior-day high of 56.47, well under the 200-day SMA of 87.55. RVOL 42.67.
- IREN 11.82: under its prior-day high of 14.05, under a third of the 200-day SMA of 41.73. RVOL 44.72.
- WULF 9.84: under its prior-day high of 11.26 and the 200-day SMA of 17.94. RVOL 19.74.
- NOK 6.88: under its prior-day high of 7.31 and the 200-day SMA of 10.4. RVOL 21.76.
- SOFI 12.495: under its prior-day high of 13.59 and the 200-day SMA of 17.14. RVOL 30.0.
- AAL 11.92: under its prior-day high of 12.83 and the 200-day SMA of 13.44. RVOL 30.85.
- IBIT 33.01: under its prior-day high of 35.12 and the 200-day SMA of 40.87. RVOL 31.47.
- SNDK 79.245: the numbers don't agree with each other. See Skips and Traps.

Every real cap-qualified name is below its prior-day high and below its 200-day. Nothing in the packet is leading.

On volume: daily bars are Alpaca IEX, a subset of the tape, and the volume figures look like a full Friday session against a 20-day average. Don't read those RVOL multiples literally.

## Economic Data, Rates and the Fed

From `econ_calendar` (USD, high impact only):

- **Today (Monday, November 23):** nothing high-impact listed.
- **Tomorrow (Tuesday, November 24):** nothing high-impact listed.

The calendar's `note` field is empty, so the packet doesn't flag a fetch problem. It just lists zero events. The calendar came from a cached weekly feed the scan marked "fresh." No 10Y or 3M reading, so there's no rates read. The only Fed angle in the packet is Ackman's warning that the US "may enter a recession if the Fed raises rates." The packet doesn't say whether a hike is actually on the table. With an empty calendar, today trades on AI headlines and positioning, not macro data.

## Coming Up

- **Tomorrow's events:** no high-impact USD releases in the calendar.
- **Earnings:** "Best Buy Reports Earnings Tomorrow. Here's What Investors Should Be Watching." (The Motley Fool). `next_earnings_date` is null for all 20 gappers, and the packet has no market-wide earnings calendar.

## Skips and Traps

- **TPEI** +34.06%: the rules engine's only swing flag, pulled. The one headline is an unrelated RSS match about EU utilities, and TAWN got the identical headline, so no catalyst found. The $69.22B cap comes from a wrong SEC match to "BANK OF MONTREAL /CAN/." 20-day average volume is 0. Also, `prior_day_high`, `prior_close` and `sma_200` are all exactly 44.99, which means there's almost no price history. Skip.
- **TAWN** -33.95%: same bad SEC match (same 708,905,679 shares as TPEI), same unrelated headline, 20-day average volume 0. Skip.
- **SONN** +3949.21%: the packet says "SOUTHERN CO" with a $57.51B cap. That's a wrong SEC match. No daily bars, no catalyst, and a move from 1.26 to 51.02 that the packet can't explain. Skip.
- **SNDK** -89.5%: the numbers don't fit together. `prev_close` is 754.98, `price` and `prior_close` are about 79.25, and the 200-day SMA is 1283.0. The packet doesn't say why. It could be a corporate action or bad data, but that isn't in the packet either. The headlines are all bad news ("Weak NAND Flash Price Outlook," "Commerce Department Regulatory Update," "Kioxia Pricing Warning"). Gap-down, way under any trend line. Skip.
- **MACI** +62.2%: "Melar Acquisition Corp. I Completes Business Combination with Everli Global Inc." The link says the combined company begins trading on Nasdaq Monday, November 23 under EVRL. A de-SPAC on day one, cap null, 20-day average volume 282. Price of 13.3 is also under the prior-day high of 15.9. Skip.
- **IREZ** +36.36%, **APLZ** +35.77%, **NBIZ** +32.12%: `catalyst_found: false`, cap null. No catalyst found, so no trade. Average volumes are 10,454, 497 and 11,530.
- **MRAL** -36.56%, **IPFXU** -36.18%, **MRAX** -34.0%: `catalyst_found: false`, cap null, gap-downs. IPFXU's 20-day average volume is 16 and MRAX's is 20. Skip.
- **NVDA** -13.93%: the Huang reinstatement push is the most important headline in the packet this morning, and MarketWatch says the stock is bouncing on it. But the packet has Friday's close, not today's premarket price, so it can't show the bounce. Price is under the prior-day high and way under the 200-day. It's a gap-down name in the data, not a list name. Watch it as the tell for the whole tape.
- **AMD** -13.31%: "Law Firms Announce Securities Investigations," the Hunterbrook China-ties report, and "AMD Insider Executes Significant Share Sale." Bad news stacking up, and it just lost the 200-day. Skip.
- **IREN** -17.92% and **WULF** -15.14%: AI data center names in free fall. WULF has a town board voting to ban its proposed data center. IREN's Blue Owl financing headline is real, but the packet doesn't date it and it didn't stop the slide. Both far under their 200-day SMAs. Skip.
- **INTC**, **NOK**, **SOFI**, **AAL**, **IBIT**: all gapping down 5.9% to 8.27% with the tape. Headlines are either routine (surveys, partnerships, executive changes) or none at all (IBIT). Nothing here explains the move besides the broad selloff. Skip.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
