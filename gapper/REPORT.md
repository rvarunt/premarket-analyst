# Premarket Report: November 18, 2026

*Single-brain pass: Claude only. Second brain not wired in yet.*

> Rules pick the watchlist. The AI judges the quality of the setups. This is not financial advice.

**Data warning: read this first.** The packet says "Scan run 2026-11-18 06:18 EST (premarket)." But just like yesterday, the gaps mostly aren't this morning's gaps. For most names `price` sits on or within a few cents of `prior_close` (NKE 35.86 vs 35.86, SNAP 5.5 vs 5.5, ONDS 4.395 vs 4.39, SLS 19.15 vs 19.17), so `gap_pct` is Tuesday's close vs Monday's close. The index proxies have the same problem: SPY's `prev_close` of 740.04 is exactly what yesterday's report showed as SPY's last. So the numbers below are Tuesday's session, while the overnight headlines describe a rally after Nvidia's print. The packet has no futures numbers to size that rally.

Yahoo rate-limited the scan again: 69 requests failed even after retries. Intraday data is `unavailable` for all 17 gappers, so VWAP, HOD, LOD, premarket high and premarket volume are null across the board. Per-ticker Yahoo news failed for every name, so catalysts are Alpaca headlines only. VIX, 10Y, 3M, WTI and the dollar are null. Market cap is null for PICS, LUCK and SNAP. `next_earnings_date` is null for all 17. Index levels are ETF proxies (SPY, DIA, QQQ, IWM), not the indices.

## Summary

- **The tape in one line:** the packet's proxies show Tuesday's selloff (SPY -1.03%, DIA -1.64%, IWM -1.48%, QQQ -0.72%), but the overnight headlines flipped: "Stock Futures Rally as Nvidia Earnings Calm AI Trade Fears" (WSJ) and "Nvidia stock up nearly 4% as earnings beat expectations. Neoclouds surge" (CNBC).
- **The catch we're watching:** FOMC Meeting Minutes at 2:00 PM ET, the only high-impact USD event today. Behind that, whether the Nvidia relief holds after MarketWatch's note that "the S&P 500 just broke a crucial support level" (its 200-day moving average).
- **Two-brain verdict:** Single-brain run, no second opinion.

## Pre-Market Gappers

All 17 gappers in the packet. Gap % is `price` vs `prev_close` (mostly Tuesday's move, see the warning above). Market cap in parentheses. Headline is the first one the packet lists for each ticker.

- **SLS** +156.36% ($3.90B) : "SELLAS Life Sciences Commences $150 Million Public Offering of Common Stock"
- **BKHAU** +117.04% ($72.5M) : no headline in the packet (`catalyst_found: false`)
- **VAI** +40.45% ($61.9M) : "Valor Energy Inc. Completes Acquisition of Youngstown Project for AI Data Center Development"
- **GLSI** +35.9% ($274.5M) : "Greenwich LifeSciences Announces Acceptance of Abstracts at SABCS 2026"
- **PSIG** -31.93% ($52.1M) : "PS International Group Ltd. Announces Unaudited Financial Results for the Six Months Ended June 30, 2026"
- **PICS** -29.39% (cap null) : "PicPay Announces Third Quarter 2026 Financial and Operating Results"
- **TCX** +28.65% ($165.3M) : "Tucows Agrees to Sell Ting Fiber Markets to Clearwave"
- **DUOT** -27.41% ($116.2M) : "Duos Technologies Group Reports Q3 2026 Financial Results"
- **CING** +25.87% ($70.6M) : "Cingulate Inc. Reports Third Quarter 2026 Financial Results and Provides Regulatory Update"
- **IBO** +25.66% ($53.3M) : "Impact BioMedical Announces Name and Ticker Symbol Change"
- **LUCK** +25.6% (cap null) : "Lucky Strike Entertainment Receives Take-Private Proposal from CEO"
- **NFE** +23.61% ($61.5M) : "New Fortress Energy Reports Third Quarter 2026 Financial Results"
- **SPAI** +23.08% ($61.8M) : "Safe Pro Group Reports Record Third Quarter 2026 Financial Results"
- **IMA** +21.88% ($48.6M) : "William Blair Maintains Buy Rating on ImageneBio"
- **SNAP** +7.84% (cap null) : "Seller Snap Launches MCP Server for AI Integration"
- **ONDS** -6.89% ($2.51B) : "Needham Adjusts Ondas Price Target to $14 From $19, Maintains Buy Rating"
- **NKE** -6.35% ($30.67B) : "Nike Reaffirms Fiscal 2027 Guidance and Outlines 'Full Stride Ahead' Strategy"

## Day Trading Watchlist

The bar is Trend Join Long: gap > 3%, price > $3, market cap > $1B, premarket RVOL > 1.5, and price already breaking above yesterday's high.

No names cleared the day-trading bar today. Every gapper is `day_eligible: false`. Only one up-mover has a known cap over $1B: SLS (+156.36%, $3.90B, RVOL 315.8), and it's at 19.15, well under its prior-day high of 24.87. ONDS and NKE are cap-qualified but gapping down. With premarket high and HOD null for everyone, there are no live levels to build a plan off even if something had qualified.

## Swing Watchlist

The bar is: gap >= 8%, price > $3, open above yesterday's high, open above the 200-day SMA, market cap >= $800M, and a real catalyst (earnings on the gap day, or news with no earnings).

No names made the swing list today. Every gapper is `swing_eligible: false`. SLS is the closest: gap, price, cap and the 200-day SMA (8.88) all clear, but 19.15 is under yesterday's high of 24.87. Everything else up 8% or more is under $800M or has no cap.

## Market Trends of the Day

The story flipped overnight. Yesterday was the AI unwind into Nvidia's print. This morning the feed is all relief: "Nvidia’s stock rises as blowout numbers help ease CEO transition fears" (MarketWatch, citing a "$130 billion quarterly forecast"), "Nvidia Reports Strong $115.8 Billion Quarterly Revenue In First Earnings Post-Jensen Huang" (Forbes), and "Instant view: Nvidia earnings beat estimates; attention turns to call" (Reuters). MarketWatch has NVDA "up over 3% in premarket trading on Wednesday."

It's spreading to the AI complex: "AMD, Broadcom, CoreWeave stocks rise on Nvidia earnings beat" (Yahoo Finance) and "Neoclouds surge" (CNBC). One note of caution there: on financing neoclouds, interim CEO Colette Kress said Nvidia will take "a very strong look" at the customers it helps. JPMorgan, per MarketWatch, says "there is likely more volatility to come in the near-term."

The Huang overhang isn't gone. "Nvidia Reports Faster Growth, Says Jensen Huang Won’t Return as CEO" (WSJ), and MarketWatch's "Why Nvidia broke with its usual practice in holding back its quarterly SEC report" says Nvidia isn't filing its 10-Q yet, and that this is the first official sign the resignation was about more than personal conduct.

The bigger-picture read is split. Truist says investors should start asking "what could go right" after "tech’s 42% valuation reset" and use the weakness to add exposure. Bespoke, via MarketWatch, says the S&P 500 breaking its 200-day "may not be" the bearish signal it usually is.

None of today's gappers are part of that AI theme except VAI's data-center acquisition headline, and that's a $61.9M name.

## Technical Signals for Today

ETF proxy levels from the scan, vs each one's `prev_close` (this is Tuesday's session, not this morning's futures):

- SPY 732.41 (prev 740.04), -1.03%
- DIA 507.37 (prev 515.83), -1.64%
- IWM 268.96 (prev 273.0), -1.48%
- QQQ 657.06 (prev 661.8), -0.72%

QQQ held up best on Tuesday, which is the reverse of Monday. That's two straight down days on the proxies: SPY went from 754.27 to 740.04 to 732.41 across the last two reports. MarketWatch says the S&P 500 has now broken its 200-day moving average. The packet has no 200-day level for SPY, so you can't check how far under it is. VIX, 10Y, 3M, WTI and DXY are all null, so there's no volatility, rate, oil or dollar read.

Cap-qualified names vs prior-day high and the 200-day SMA (no VWAP or HOD today, intraday data was unavailable):

- SLS 19.15, way under its prior-day high of 24.87, but far above the 200-day SMA of 8.88. RVOL 315.8 on 121.3M shares vs a 20-day average of 384,066. It ran and faded hard Tuesday.
- NKE 35.86, under its prior-day high of 40.68 and the 200-day SMA of 44.54. RVOL 49.24.
- ONDS 4.395, under its prior-day high of 4.7 and about half its 200-day SMA of 8.64. RVOL 29.0.

On volume: daily bars are Alpaca IEX, a subset of the tape, and the volume looks like a full Tuesday session against a 20-day average. Don't read those RVOL multiples literally. RVOL is null for every micro-cap.

## Economic Data, Rates and the Fed

From `econ_calendar` (USD, high impact only):

- **Today, 2:00 PM ET:** FOMC Meeting Minutes. No forecast or previous.
- **Tomorrow:** nothing high-impact.

The minutes are the one scheduled macro risk. They land late, after the 10:00am open of the day-trade window, so expect any rate reaction to hit the afternoon. The packet has no 10Y or 3M reading, so there's no live read on how rates are set up going in.

## Coming Up

- **Tomorrow's events:** No high-impact USD releases in the calendar for Thursday, November 19.
- **Earnings:** `next_earnings_date` is null for all 17 gappers, and the packet has no market-wide earnings calendar. Nvidia's print is now out. The only other company flagged in the feed is "Imperial Brands: What We Think of the Stock After Earnings" (Morningstar), which has already reported. NKE has "NIKE, Inc. Schedules Capital Markets Day" in its feed, but no date in the packet.

## Skips and Traps

- **SLS** +156.36%: $3.90B cap, RVOL 315.8, and a real catalyst: "SELLAS Life Sciences Announces Positive Topline Results from Pivotal Phase 3 REGAL Trial." But the top headline is "SELLAS Life Sciences Commences $150 Million Public Offering of Common Stock." Selling stock into the pop is dilution. Price 19.15 is way under the 24.87 prior-day high, so it already faded off its highs. Also, the cap is SEC shares outstanding times today's price, so it's set by the spike itself. Neither flag is set. Don't chase a biotech that's raising money into the move.
- **LUCK** +25.6%: "Lucky Strike Entertainment Receives Take-Private Proposal from CEO." It's a real story, but the cap is null, so neither flag can fire. A take-private proposal also tends to pin a stock near the offer price, and the packet has no price for the offer. Its feed also has "Reports Fiscal Q1 2027 Results and Suspends Dividend." Skip.
- **BKHAU** +117.04%: `catalyst_found: false`, volume null, 20-day average volume 0, and price 17.45 doesn't line up with a 13.05 prior close or the 8.04 prev close. Broken data on a $72.5M unit. Ignore the number.
- **IBO** +25.66% and **CING** +25.87%: reverse splits in the feed ("1-for-12.62 Reverse Stock Split", "Executes 1-for-12 Reverse Stock Split"). IBO also has a pending merger with Zoar Limited and a 20-day average volume of 127 shares. Sub-$100M caps. Trap territory.
- **VAI** +40.45%: $61.9M cap, 20-day average volume 1,999. The AI data-center angle ("Completes Acquisition of Youngstown Project for AI Data Center Development") is on-theme, but the company just renamed itself ("Senmiao Technology Limited Changes Name to Valor Energy Inc."). Skip.
- **NFE** +23.61%: $61.5M cap, and its feed has "Announces Filing Grace Period" and "Fast LNG Unit Offline Due to Mechanical Issue." Up on a stock in distress. Trap.
- **GLSI** +35.9%, **TCX** +28.65%, **SPAI** +23.08%, **IMA** +21.88%: all under $300M, all with thin 20-day average volume (344 to 7,361 shares). Real headlines, but under both cap bars. Skip.
- **SNAP** +7.84%: cap null, so neither flag can fire. The first headline is about "Seller Snap," a different company. Other items are a West Virginia AG lawsuit and an activist letter ("Irenic Capital Urges Snap Inc. to Implement Cost-Cutting and AI Monetization Strategies"). Price 5.5 is right at the 5.51 prior-day high. Watch only, no setup.
- **PSIG** -31.93%, **PICS** -29.39%, **DUOT** -27.41%: gap-downs. PSIG has a Nasdaq deficiency notice, and PICS's feed has "PicPay Shares Decline Amid Market Reaction to Brazilian Election Results." Neither setup is a short. Skip.
- **NKE** -6.35% and **ONDS** -6.89%: cap-qualified gap-downs, both well under their 200-day SMAs. NKE reaffirmed guidance ("Nike Reaffirms Fiscal 2027 Guidance and Outlines 'Full Stride Ahead' Strategy") and still sold off on a 49x RVOL. ONDS has the same Needham target cut as yesterday. Not long setups. Skip.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
