# Premarket Report: November 25, 2026

*Single-brain pass: Claude only. Second brain not wired in yet.*

> Rules pick the watchlist. The AI judges the quality of the setups. This is not financial advice.

**Data warning: read this first.** The packet says "Scan run 2026-11-25 07:17 EST (premarket)." Same issue as the last several days: these aren't this morning's gaps. For every cap-qualified name `price` equals `prior_close` (NVDA 155.48 vs 155.48, HPE 40.22 vs 40.22, AMD 413.11 vs 413.11, INTC 54.9 vs 54.9, IREN 12.94 vs 12.94). So `gap_pct` is really Tuesday's close vs Monday's close. The index proxies agree: SPY's `prev_close` of 722.56 is the SPY last from yesterday's report. Read every number below as Tuesday's session. The packet has no futures numbers for this morning, only headlines.

Yahoo rate-limited the scan again: 108 requests failed even after retries. Intraday data is `unavailable` for all 20 gappers, so VWAP, HOD, LOD, premarket high and premarket volume are null across the board. `rvol` is null for the 9 micro-cap/unknown names. Per-ticker catalyst headlines carry no published date or source. VIX, 10Y, 3M, WTI and the dollar are null. Index levels are ETF proxies (SPY, DIA, QQQ, IWM). `next_earnings_date` and `today_open` are null for all 20. Market cap is null for ADIU, AXTX, MXLL and AXTU (no SEC CIK).

## Summary

- **The tape in one line:** Tuesday gave back a chunk of Monday's Huang rally, and it was all tech. QQQ -2.01%, SPY -0.51%, while DIA +0.82% and IWM +0.55%. NVDA -5.88%, AMD -8.81%, INTC -7.95%, HPE -16.35%. Overnight, "Asia's markets dive as return of Nvidia's Huang fails to quell AI doubts" (Al Jazeera).
- **The catch we're watching:** Core PCE m/m and Prelim GDP q/q both drop at 8:30 AM ET today. That's the macro test, landing on a tape that's already rotating out of AI.
- **Two-brain verdict:** Single-brain run, no second opinion.

## Pre-Market Gappers

All 20 gappers in the packet. Gap % is `price` vs `prev_close` (Tuesday's move for the big names, see the warning above). Market cap in parentheses. The headline is the first one the packet lists for each ticker.

- **JAGX** +109.24% ($2.19B, SEC-derived, suspect): "Jaguar Health Announces 1-for-25 Reverse Stock Split"
- **EUDA** -44.0% ($17.0M): "EUDA Health Subsidiary Melana International Wins Golden Bull Award 2026 Singapore"
- **NAMSW** +41.43% ($1.61B, the parent's cap on a warrant ticker): no headline in the packet (`catalyst_found: false`)
- **SMXT** +40.82% ($19.6M): "SolarMax Technology Reports Third Quarter 2026 Financial Results"
- **EMBC** +40.64% ($457.8M): "Embecta Reports Fiscal Fourth Quarter and Full Year 2026 Financial Results"
- **ADIU** -34.86% (cap null): no headline in the packet (`catalyst_found: false`)
- **AXTX** -34.29% (cap null): no headline in the packet (`catalyst_found: false`)
- **MXLL** -34.04% (cap null): no headline in the packet (`catalyst_found: false`)
- **AXTU** -33.92% (cap null): no headline in the packet (`catalyst_found: false`)
- **HPE** -16.35% ($53.39B): "Hewlett Packard Enterprise Reports Record Quarterly Revenue and Increases Share Repurchase Authorization"
- **INSM** +14.14% ($37.33B): "Ademi LLP Investigates Proposed Acquisition of Insmed"
- **IREN** -11.61% ($4.62B): "Blue Owl Managed Funds Lead $2.4 Billion AI Factory Financing for IREN"
- **SNDK** -10.92% ($11.09B): "SanDisk Chief Accounting Officer Discloses Stock Sale in SEC Filing"
- **CIFR** -10.66% ($2.52B): "Cipher Digital Faces Regulatory Headwinds Following Potential Overseas Data-Center Penalties"
- **AMD** -8.81% ($677.54B): "BNP Paribas Adjusts Price Target for AMD"
- **BMNR** -8.47% ($8.26B): "Bitmine Immersion Technologies Continues Ethereum Accumulation Strategy"
- **WULF** -8.12% ($5.02B): "B. Riley Adjusts TeraWulf Price Target to $22"
- **INTC** -7.95% ($291.79B): "BNP Paribas Adjusts Price Target on Intel to $60 From $70"
- **NVDA** -5.88% ($3.75T): "NVIDIA Reinstates Jensen Huang as President and CEO"
- **VALE** -4.49% ($30.52B): "Vale's 'Novas Pontes' Infrastructure Project Reaches 86% Completion"

## Day Trading Watchlist

The bar is Trend Join Long: gap > 3%, price > $3, market cap > $1B, premarket RVOL > 1.5, and price already breaking above yesterday's high.

No names cleared the day-trading bar today. Every gapper is `day_eligible: false`. Only three cap-qualified names gapped up (JAGX, NAMSW, INSM), and all three sit under their prior-day high: JAGX 12.8 vs 13.3, INSM 170.175 vs 170.59. NAMSW's 13.45 is above its 8.82 prior high, but its RVOL is null and its 20-day average volume is 0. Everything else gapped down. With premarket high and HOD null across the board, there are no live levels to build a plan off anyway.

## Swing Watchlist

The bar is: gap >= 8%, price > $3, open above yesterday's high, open above the 200-day SMA, market cap >= $800M, and a real catalyst (earnings on the gap day, or news with no earnings).

No names made the swing list today. Every gapper is `swing_eligible: false`. INSM is the closest near-miss (above its 200-day SMA of 122.65, a hair under its prior-day high), and it's a buyout, covered in Skips and Traps.

## Market Trends of the Day

Monday was the Huang relief rally. Tuesday was the hangover, and it was a clean rotation: tech sold, everything else held. QQQ -2.01% against DIA +0.82% and IWM +0.55%.

The AI complex took the hit on heavy volume. NVDA -5.88% (RVOL 33.55), AMD -8.81% (RVOL 36.4), INTC -7.95% (RVOL 26.18), IREN -11.61% (RVOL 25.78), SNDK -10.92% (RVOL 134.8), CIFR -10.66% (RVOL 17.27), WULF -8.12% (RVOL 18.21). Crypto went with it: BMNR -8.47% (RVOL 39.08).

The tell is that good AI earnings aren't getting paid. HPE posted "Record Quarterly Revenue" and fell 16.35%. The packet's link for that headline reads "hpe-just-posted-its-strongest-growth-ever-but-its-stock-is-sinking," and Barclays cut its target to $51 from $77 (per the link). Dell is the same story after the close: "Dell earnings beat on AI strength, company authorizes $25 billion buyback" (CNBC), but also "Dell stock tanks after blowout earnings. Wall Street Just Isn't Impressed." (Yahoo Finance) and "Dell Delivered Strong Earnings but at the Wrong Time for the Stock" (Barron's). MarketWatch has the opposite, "Dell's stock rises as the AI boom helps sales more than double," from earlier in the evening. DELL isn't in the gapper list, so the packet has no price on it to settle which one's right.

Overseas, the AI doubt carried: "Asia's markets dive as return of Nvidia's Huang fails to quell AI doubts" (Al Jazeera).

Not everyone's bearish. JPMorgan says "The S&P 500 is headed to 8,200, and downturns like this one are actually part of the reason," arguing AI should be judged on adoption, not capex. And Michael Darda argues "The Fed slowing the economy is a good thing," saying markets should applaud a hawkish Fed.

Outside tech, the one big up move is a deal: "Sanofi to Acquire Insmed for $41 Billion" put INSM +14.14%.

## Technical Signals for Today

ETF proxy levels from the scan vs each one's `prev_close` (this is Tuesday's session, not this morning's futures):

- SPY 718.91 (prev 722.56), -0.51%
- DIA 499.78 (prev 495.71), +0.82%
- QQQ 638.12 (prev 651.18), -2.01%
- IWM 267.2 (prev 265.75), +0.55%

Narrow selloff, not a broad one. Tech down, Dow and small caps up. VIX, 10Y, 3M, WTI and DXY are all null, so there's no volatility, rate, oil or dollar read.

Cap-qualified names vs prior-day high and the 200-day SMA (no VWAP or HOD today, intraday data was unavailable):

- NVDA 155.48: under its prior-day high of 159.88, well under the 200-day SMA of 203.07.
- AMD 413.11: under its prior-day high of 428.64 and back under the 200-day SMA of 431.98. Yesterday it was the only AI name above its 200-day. Not anymore.
- INTC 54.9: under its prior-day high of 57.52, way under the 200-day SMA of 87.62.
- HPE 40.22: under its prior-day high of 42.22 and the 200-day SMA of 42.92.
- IREN 12.94: under its prior-day high of 14.16, about a third of the 200-day SMA of 41.42.
- CIFR 5.53: under its prior-day high of 6.16 and the 200-day SMA of 16.88.
- WULF 10.01: under its prior-day high of 10.66 and the 200-day SMA of 17.89.
- BMNR 13.18: under its prior-day high of 14.11 and the 200-day SMA of 20.21.
- VALE 9.37: under its prior-day high of 9.75 and the 200-day SMA of 14.81.
- INSM 170.175: just under its prior-day high of 170.59, well above the 200-day SMA of 122.65. The only cap-qualified name above its 200-day.
- SNDK 77.905: under its prior-day high of 83.82. The 200-day SMA of 1277.92 still doesn't fit the price. See Skips and Traps.

On volume: daily bars are Alpaca IEX, a subset of the tape, and the RVOL figures look like a full Tuesday session against a 20-day average. Don't read those multiples literally.

## Economic Data, Rates and the Fed

From `econ_calendar` (USD, high impact only):

- **Today (Wednesday, November 25):**
  - 8:30 AM ET, Core PCE Price Index m/m: forecast 0.3%, previous 0.3%.
  - 8:30 AM ET, Prelim GDP q/q: forecast 3.5%, previous 3.4%.
- **Tomorrow (Thursday, November 26):** nothing high-impact listed.

The scan ran at 7:17 AM ET, before the 8:30 release, so the packet has no actuals. Check the prints before the open. The calendar's `note` field is empty, so no fetch problem flagged. With no 10Y or 3M reading there's no rates read. The only Fed color in the packet is Darda's piece, which frames the Fed as hawkish and slowing demand on purpose. The packet doesn't say what the Fed itself is planning.

## Coming Up

- **Tomorrow's events:** nothing high-impact on the USD calendar.
- **Earnings:** Dell's results are already out (see Market Trends). `next_earnings_date` is null for all 20 gappers, and the packet has no market-wide earnings calendar.

## Skips and Traps

- **INSM** +14.14%: real catalyst, wrong kind of trade. "Sanofi to Acquire Insmed for $41 Billion" is in the headlines, and the lead headline is a shareholder-rights firm investigating the deal. A cash buyout pins the stock near the deal price, so there's no trend left to ride. Also just under its prior-day high (170.175 vs 170.59). Skip.
- **HPE** -16.35%: down on a good-news headline ("Record Quarterly Revenue"), with Barclays and UBS both cutting targets (links read "to-51-from-77" and "to-52-from-66"). A gap down, so not a long setup for either list. Watch it as the AI-sentiment tell.
- **JAGX** +109.24%: the numbers don't hang together. The lead headline is "Jaguar Health Announces 1-for-25 Reverse Stock Split," the 200-day SMA is 1.99 against a 12.8 price, and the 20-day average volume is 6,955. The $2.19B SEC-derived cap likely mixes pre- and post-split figures. The packet doesn't confirm either way. There's also "Jaguar Health Files S-3 Registration Statement" (a shelf). Under its prior-day high of 13.3. Skip.
- **NAMSW** +41.43%: a warrant ticker carrying the parent NewAmsterdam Pharma's $1.61B cap. No catalyst, 20-day average volume 0, and `prev_close` (9.51) doesn't match `prior_close` (8.82). Skip.
- **EMBC** +40.64%: $457.8M cap, under the $800M swing floor and the $1B day floor. Earnings plus "Embecta and Pfizer Announce Strategic Collaboration for Metabolic Health Management" is a real story, but it's too small for either list and sits under its prior-day high (8.08 vs 8.22). Skip.
- **SMXT** +40.82% and **EUDA** -44.0%: micro-caps ($19.6M and $17.0M) with reverse splits and, for SMXT, a "Nasdaq Notice Regarding Delayed Form 10-Q Filing" in the headlines. 20-day average volume of 135 and 481. Skip both.
- **ADIU**, **AXTX**, **MXLL**, **AXTU**: all about -34%, no name, no cap, no catalyst in the packet. Ticker-only rows. Skip.
- **SNDK** -10.92%: a 200-day SMA of 1277.92 against a 77.905 price still doesn't fit, and the headlines are an insider sale, "Weak NAND Flash Price Outlook" and a "Commerce Department Regulatory Update." Skip.
- **NVDA**, **AMD**, **INTC**, **IREN**, **CIFR**, **WULF**, **BMNR**, **VALE**: all gap-downs on Tuesday's AI and crypto selling, all under their prior-day highs and 200-day SMAs. The headlines are mostly target cuts (BNP on AMD to $650 from $960 and on INTC to $60 from $70, Fubon on INTC to $66 from $105, B. Riley on WULF to $22), older news, or overhangs (AMD's securities investigations, WULF's Lansing data-center ban, CIFR's regulatory headwinds, "Vale Rules Out Extra Dividend for 2026"). Nothing long here.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
