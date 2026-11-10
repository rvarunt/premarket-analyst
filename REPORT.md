# Premarket Report: 2026-11-10

*Single-brain pass: Claude only. Second brain not wired in yet.*

> Rules pick the watchlist. The AI judges the quality of the setups. This is not financial advice.

**Data warning:** the scan ran at 06:21 ET and Yahoo was rate-limited or blocked. 115 requests failed even after retries. VIX, 10Y, 3M, oil and dollar are null in the packet. Intraday levels (premarket high, VWAP, HOD, LOD) are null for every gapper, and premarket RVOL is null for the first 10 names. Nothing below is filled in. Where the packet is blank, this report says so.

## Summary

- **The tape in one line:** The packet shows S&P 500 +2.36%, Dow +2.17%, Nasdaq +3.42%, Russell 2000 +3.25%. VIX is null, so there's no read on fear. Headlines point to a tech and AI rebound ("Asian Stocks to Rally on US Tech Surge, Oil Slump: Markets Wrap - Bloomberg.com").
- **The catch we're watching:** CPI at 8:30 AM ET (headline forecast 0.3% m/m, core forecast 0.2%). A hot print plus "Fed's Waller puts half-point rate hike into the mix for December" is the thing that could flip a tech-led bounce.
- **Two-brain verdict:** Single-brain run, no second opinion.

## Pre-Market Gappers

All 20 gappers from the packet. Gap % and price are from the packet. Market cap in parentheses where available.

- **HYB** +205.9% (price 25.0845, prior close 8.2, market cap null) : "The New America High Income Fund To Pay A Special Dividend Of $0.0475 Per Share On Common Stock"
- **WCT** +92.2% ($207M) : "Wellchange Holdings Company Limited Announces 1-for-10 Reverse Stock Split"
- **SMX** +89.7% ($16.8M) : "SMX Announces Reverse Stock Split"
- **TANH** +65.7% ($120M) : "Tantech Holdings LTD Announces Yefang Zhang Resigns As Chairman; Yao L Xu Appointed Chairman Effective Oct 1"
- **CKX** +58.2% ($33.7M) : "CKX Lands Announces $1 Billion Investment Led by Brad Jacobs"
- **TLS** +48.8% ($527M) : "Telos Corporation Reports Third Quarter 2026 Financial Results and Raises Full-Year Outlook"
- **PCTTU** +46.6% ($898M) : "8 Stocks Halted In Tuesday's Session"
- **GFR** +38.0% ($969M) : "Strathcona Resources to Acquire Greenfire Resources in C$2.7-C$2.9 Billion Deal"
- **RGTIW** +32.4% ($1.12B) : no catalyst headline found
- **UVIX** -27.2% ($3.86B) : "UVIX Jumps 13% As VIX Nears 'Fear Zone' Of 30, Volatility ETFs Surge"
- **VISN** -25.0% ($839M) : "Vistance Networks Q3 2026 Earnings Call Transcript"
- **IBRX** -17.6% ($7.56B) : "ImmunityBio Q3 Adj. EPS $(0.09) Misses $(0.08) Estimate, Sales $48.841M Miss $59.250M Estimate"
- **AMD** +13.7% ($834B) : "Jim Cramer Calls AMD a Winner After 13% Surge, But Warns US Data Center Roadmap Is 'Suspect'"
- **ONDS** +11.8% ($3.40B) : "Ondas Inc. Issues Third-Quarter Revenue Guidance"
- **WULF** +8.8% ($6.20B) : "TeraWulf Analysts Stay Bullish After Google Backstops $19 Billion Anthropic Lease"
- **AAL** +7.5% ($9.37B) : "Why Is American Airlines Stock Surging on Monday?"
- **NOK** +7.0% ($47.0B) : "Nokia Deploys AI Agents to Enhance Telecom Network Engineering"
- **INTC** +5.4% ($315.6B) : "Evercore ISI Adjusts Intel Price Target to $131 From $133"
- **NVDA** -4.3% ($4.31T) : "Wells Fargo Maintains Overweight on NVIDIA, Lowers Price Target to $300"
- **CIFR** +4.1% ($3.11B) : "Morgan Stanley Maintains Overweight on Cipher Digital, Lowers Price Target to $27.5"

## Day Trading Watchlist

The bar is Trend Join Long: gap > 3%, price > $3, market cap > $1B, premarket RVOL > 1.5, and price already breaking above yesterday's high.

No names cleared the day-trading bar today. Every gapper has `day_eligible: false`. Worth noting: for AMD, NOK, INTC, NVDA, WULF, AAL, ONDS and CIFR the price sits just under prior-day high (AMD 508.675 vs 515.1, INTC 59.37 vs 60.02, NOK 8.185 vs 8.28). No premarket high, VWAP, HOD or LOD data came through, so there are no levels to build a trigger from.

## Swing Watchlist

The bar is: gap >= 8%, price > $3, open above yesterday's high, open above the 200-day SMA, market cap >= $800M, and a real catalyst. Remember the real open hasn't printed yet, so the current gap price stands in for it.

No names cleared the swing bar today. Every gapper has `swing_eligible: false`.

## Market Trends of the Day

AI and chips are the story, in both directions. AMD is +13.7% and the Cramer headline calls it a 13% surge. INTC is +5.4% and NOK +7.0%, while NVDA is -4.3% with Wells Fargo lowering its target to $300. AI-power and compute names TeraWulf (+8.8%) and Cipher Digital (+4.1%) are up despite target cuts. Headlines frame the backdrop as a post-midterm AI selloff ("AI Stocks Got Hammered After Midterms, but This Analyst Says the Panic Is Overblown") and a Morgan Stanley view that "Market Correction Nearing End". Also in the news: "Anthropic reportedly retracts IPO terms sent to banks by mistake, exposing jitters over AI investments" and a short-seller claim about Nvidia chips reaching China.

Airlines are bid (AAL +7.5%, "CORRECTION: Airline companies are trading higher") alongside "Crude Oil Falls Over 3%". Volatility products are getting crushed: UVIX -27.2% after a big run.

## Technical Signals for Today

Packet index changes: S&P 500 +2.36%, Dow +2.17%, Nasdaq +3.42%, Russell 2000 +3.25%. Index levels are null. VIX, 10Y, 3M, WTI and DXY are all null because the Yahoo batch failed, so there are no breadth, volatility or rate signals to report. The UVIX headline says "VIX Nears 'Fear Zone' Of 30", but that is a headline, not a packet VIX reading. Intraday levels for every gapper are null.

Where the packet has daily context: AMD (508.675) is above its 200-day SMA of 417.2. NVDA (178.64), INTC (59.37), WULF (12.37), CIFR (6.805), NOK (8.185), ONDS (5.96) are all below their 200-day SMAs.

## Economic Data, Rates and the Fed

Today (the packet filters to USD high-impact only):
- 8:30 AM ET, Core CPI m/m: forecast 0.2%, previous 0.3%.
- 8:30 AM ET, CPI m/m: forecast 0.3%, previous 0.6%.

The Fed angle: the MarketWatch headline reads "Fed's Waller puts half-point rate hike into the mix for December". No other rate figures are in the packet. A CPI above forecast fits that hawkish framing and is the main risk to the tech bounce.

## Coming Up

- **Tomorrow's events:** none in the packet (no USD high-impact releases for 2026-11-11).
- **Earnings:** `next_earnings_date` is null for every gapper, and the packet has no market-wide earnings calendar. Recent-results headlines in the news feed (not upcoming dates): Palantir, Trade Desk, Hims & Hers, CoreWeave, On Holding, Telos, ImmunityBio, Vistance Networks.

## Skips and Traps

- **HYB** +205.9%: the only headlines are about a $0.0475 special dividend and ex-dividend date. That can't explain a 3x move, and a $25 price against a $8.23 prior close and 200-day SMA looks like bad data or a thin-print artifact. Market cap is null. Skip.
- **WCT** +92.2% and **SMX** +89.7%: reverse-split headlines. A reverse split mechanically resets price, it isn't a real gap. SMX is a $16.8M cap. Skip.
- **TANH** +65.7%: the catalyst is a chairman resignation and appointment, plus generic "stocks moving premarket" headlines about other companies. $120M cap. No real story. Skip.
- **CKX** +58.2%: a "$1 Billion Investment Led by Brad Jacobs" is the headline, but this is a $33.7M cap that was halted on a circuit breaker and already up 73% intraday earlier. Too small and too wild. Skip.
- **TLS** +48.8%: strong headline (Q3 results, raised full-year outlook, Needham target to $9), but market cap is $527M, below both bars, and price 7.17 is under prior-day high 7.19. Not eligible. Watch only.
- **PCTTU** +46.6%: the only headline is "8 Stocks Halted In Tuesday's Session". That's not a catalyst. Price 4.47 is far below prior-day high 9.81 and the 200-day SMA of 15.78. Skip.
- **GFR** +38.0%: an M&A headline (Strathcona buying Greenfire), but that links to the target name, not clearly to GFR, and market cap is $969M with no RVOL. Not eligible. Skip.
- **RGTIW** +32.4%: `catalyst_found: false`. No catalyst, skip. It's also a warrant.
- **UVIX** -27.2%, **VISN** -25.0%, **IBRX** -17.6%, **NVDA** -4.3%: gapping down, no long setups here. IBRX is a clear earnings miss ("Sales $48.841M Miss $59.250M Estimate").
- **AMD** +13.7%: the best-looking name by trend, above its 200-day SMA, but it fails the rules because price 508.675 sits below prior-day high 515.1. The only headline is commentary on a surge that already happened, and Cramer warns the data-center roadmap is "Suspect". Chasing is a trap. Watch only.
- **WULF, CIFR, INTC, NOK, ONDS, AAL**: all below their 200-day SMAs and under prior-day highs. WULF and CIFR have target cuts in the headlines.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
