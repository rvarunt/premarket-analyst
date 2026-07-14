# Premarket Report: July 14, 2026

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** Green across the board into the close: S&P proxy (SPY) +0.38%, Dow proxy (DIA) +0.06%, Nasdaq proxy (QQQ) +1.10%, Russell proxy (IWM) +0.35%. Nasdaq led.
- **The catch we're watching:** Today's CPI print and Fed Chairman Warsh's testimony already happened (both were on today's calendar and both show up in the news feed: "Warsh Says No Tolerance For Inflation"). Tomorrow brings PPI data and a second day of Warsh testimony, plus IBM just had its "worst day ever" (-25.21%) and is dragging software stocks with it, worth watching for follow-through.
- **Two-brain verdict:** Single-brain run, no GPT pass to compare against yet.

## Pre-Market Gappers

- **NXTC** +201.83% — "Nextcure Transforms Into Avere as Investors Back Oral Psoriasis Therapy"
- **VEEE** +54.91% — "10 Consumer Discretionary Stocks Moving In Tuesday's Intraday Session"
- **IBX** -50.38% — no catalyst headline in the feed
- **CRMT** +41.72% — "10 Consumer Discretionary Stocks Moving In Tuesday's Intraday Session"
- **LESL** -41.07% — "10 Consumer Discretionary Stocks Moving In Tuesday's Intraday Session"
- **FXHO** +33.72% — "12 Information Technology Stocks Moving In Tuesday's Intraday Session"
- **BMGL** +32.25% — "12 Health Care Stocks Moving In Monday's Pre-Market Session"
- **AXTC** +29.84% — no catalyst headline in the feed
- **WYFL** -29.06% — no catalyst headline in the feed
- **IBM** -25.21% — "BMW's U.S. business is delivering when it matters most"
- **BWET** +21.99% — "Why Did the Commodity Complex Remind Me of the Bangles to Start the Week?"
- **LCID** -16.15% — "Lucid Stock Dives After Report Claims EV Company Is Weighing Strategic Options"
- **BMNR** +11.46% — "Why Is BitMine Stock Gaining Tuesday?"
- **CLSK** +8.44% — "BTIG Reiterates Buy on Cleanspark, Maintains $26 Price Target"
- **WULF** -7.13% — "Why Is TeraWulf Stock Falling on Tuesday?"
- **ETHA** +5.83% — "Bitcoin and ethereum prices today, Monday, July 13, 2026: Strong price openings backtracking this morning"
- **ONDS** +5.38% — "Squeeze Watch: 10 Stocks Bears Love to Hate Most Right Now"
- **JOBY** +5.35% — "Joby Aviation Stock Tests $8 Support Zone: What's Driving the Air Taxi Pullback?"
- **INTC** +4.59% — "10 Information Technology Stocks With Whale Alerts In Today's Session"
- **NVDA** +4.08% — "Bank Earnings Indicate Strong Economy; IBM Drops Dragging Software; Warsh Says No Tolerance For Inflation"

## Day Trading Watchlist

`day_eligible` encodes the Trend Join Long rule: gap > 3%, price > $3, market cap > $1B, premarket RVOL > 1.5, and price already breaking above yesterday's high.

No names cleared the day-trading bar today. Every cap-qualified up gapper (NVDA, INTC, ONDS, JOBY, BMNR, ETHA, CLSK) came in with an RVOL at or near 0 in the packet (0.0 for most, 0.01 for BMNR and ETHA), so none of them clear the RVOL > 1.5 leg of the rule even though several are up and holding above yesterday's high.

## Swing Watchlist

`swing_eligible` encodes: gap >= 8%, price > $3, open > yesterday's high, open > the 200-day SMA, market cap >= $800M, and a real catalyst.

Two names cleared it. Both were checked against the standing red-flag rule (market cap under $2B, or a catalyst headline quoting near-zero revenue against the market cap) and neither triggered it: BWET's market cap is $2.37B and CLSK's is $3.44B, both above the $2B floor, and no catalyst headline for either quotes a revenue figure.

| Ticker | Catalyst | Trend context | Idea | Second-brain check | Conviction |
|---|---|---|---|---|---|
| BWET | "BWET Soars 615% As Freight Rates Triple, Turning Shipping ETFs Into The Hottest Geopolitical Trade" | Open ($264.80) is well above the 200-day SMA ($81.88) and above yesterday's high ($214.90). | News catalyst, no earnings involved: a geopolitical freight-rate spike, not a company-specific story (this is Amplify Commodity Trust, a commodity/shipping trust product, not an operating company). Price ($257.35) is currently sitting just below VWAP ($261.13) with zero premarket volume logged, so there's no live confirmation the move is holding. Watch-and-build-a-plan only, no stop, no target. | n/a, single-brain run | 🟡 |
| CLSK | "CleanSpark Stock Jumps After Inking $6.6 Billion, 20-Year Data Center Lease in Georgia" | Open ($14.66) is above the 200-day SMA ($13.30) and above yesterday's high ($12.75). | News catalyst: a real, dollar-figure data center lease deal, plus BTIG reiterating Buy with a $26 target (about 2x the current price). But the stock already made a high of $15.09 today and faded back to $13.42, an 11%+ pullback off the high by the time of this after-hours snapshot, so the move isn't holding its best levels. Watch-and-build-a-plan only, no stop, no target. | n/a, single-brain run | 🟡 |

## Market Trends of the Day

Broad tape was green today, Nasdaq (QQQ proxy, +1.10%) led the other three. A bank-earnings-beat thread runs through several matched headlines: "Bank Earnings Indicate Strong Economy," "Bank of America Earnings Top Views," and "Goldman Sachs Posts Upbeat Q2 Earnings" all show up across different tickers' catalyst feeds today.

Crypto-adjacent names were unusually active: BMNR, WULF, CLSK, and ETHA all moved on Bitcoin/Ethereum-linked news, against a backdrop of a "Trump Reinstates Strait of Hormuz Blockade" headline that reportedly knocked Bitcoin, Ethereum, XRP, and Dogecoin lower. That same Hormuz headline connects to the other big theme in the feed: a freight and oil trade, with BWET's catalyst citing freight rates tripling and crude gains showing up in more than one other ticker's matched headlines.

The one gap-down that stands out from the crowd is IBM, off -25.21% on a headline literally calling it IBM's "worst day ever," dragging software stocks with it and lifting cybersecurity names like Palo Alto by contrast.

## Technical Signals for Today

- S&P 500 proxy (SPY): 751.94, +0.38% from prior close (749.13).
- Dow proxy (DIA): 524.75, +0.06% from prior close (524.45).
- Nasdaq proxy (QQQ): 719.71, +1.10% from prior close (711.85). Strongest of the four.
- Russell 2000 proxy (IWM): 294.49, +0.35% from prior close (293.46).
- VIX, 10-year yield, 3-month yield, WTI crude, and the dollar index all failed to load this run (data source outage), so there's no vol or rates read to lean on today.
- NVDA closed near its high of day ($212.55 HOD vs. $211.79 last) and well above its 200-day SMA ($191.79), holding its gap rather than fading.
- INTC is up at $107.76, close to its HOD of $109.17, and sitting far above its 200-day SMA ($62.83), a continuation of the move flagged in yesterday's report.
- IBM is trading at $217.07, well below its 200-day SMA ($275.24), so today's drop breaks it further into a downtrend rather than just a one-day air pocket.

## Economic Data, Rates and the Fed

Today already had its main events: CPI m/m (forecast -0.1% vs. previous 0.5%), CPI y/y (forecast 3.8% vs. previous 4.2%), Core CPI m/m (forecast 0.2%, flat with previous), Core CPI y/y (forecast 2.8% vs. previous 2.9%), and Fed Chairman Warsh testifying at 10am ET. The feed shows the market's reaction was choppy: one headline has the Dow falling over 100 points "Following Inflation Data," another has the Nasdaq surging over 100 points on bank earnings the same day, and a third quotes Warsh saying he has "No Tolerance For Inflation."

Tomorrow: Core PPI m/m (forecast 0.3% vs. previous 0.4%) and PPI m/m (forecast 0.0% vs. previous 1.1%, a sharp deceleration if it holds) both at 8:30am ET, plus Warsh testifies again at 10:00am ET, a second day in a row.

## Coming Up

- **Tomorrow's events:** Core PPI m/m, PPI m/m (both 8:30am ET), Fed Chairman Warsh testifies again (10:00am ET).
- **Earnings:** The structured next-earnings-date field is null for all 20 gappers this run, the per-ticker lookup was rate-limited across the board, so this is a data gap, not a finding that nothing's on the calendar. One exception worth flagging from the catalyst text itself: CRMT's own headlines show it already reported Q4 earnings today, July 14 ("Earnings Scheduled For July 14, 2026," plus the actual EPS/sales prints).

## Skips and Traps

- **CRMT (+41.72%):** One headline reports a real miss, "Q4 EPS $(3.56) Misses $(0.66) Estimate, Sales $302.826M Miss $339.989M Estimate," while another says an adjusted EPS number beat. Stock's up over 40% regardless. A GAAP miss dressed up by an adjusted beat is exactly the kind of mixed quarter that shouldn't be chased just because the headline number everyone's looking at is green.
- **NXTC (+201.83%):** A $23.7M market cap name up over 200% with an RVOL of 14.58. Extreme, thin, and speculative even though there's a real story behind it (a company rebrand tied to a drug candidate). Not a name to size into on a gap this size in a stock this small.
- **VEEE (+54.91%):** Continuation of the reverse-merger story already flagged as a trap in the last report; today's headlines are just recaps of the same move ("Here's Why It's Still Trending"). Same caution applies: the underlying deal leaves existing shareholders with a minority stake in the surviving entity.
- **FXHO (+33.72%):** Every matched headline is a generic "stocks moving" wrap piece, nothing specific to this ticker's own news. Thin story.
- **BMGL (+32.25%):** The catalyst is procedural, regaining Nasdaq listing compliance, not a fundamental driver. A 32% pop on housekeeping news like that looks like an overreaction.
- **IBX, AXTC, WYFL:** No catalyst found in the feed for any of the three. No story, no trade, regardless of the size of the gap.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
