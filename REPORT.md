# Premarket Report: 2026-11-05

*Single-brain run. Claude only.*

> Rules pick the watchlist. The AI judges the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** Green on the ETF proxies: SPY +1.64%, DIA +3.1%, QQQ +0.93%, IWM +1.47% (last vs prior close, ETF stand-ins for the indices). VIX, 10Y, 3M, oil and DXY came back null (Yahoo failed). Headline: "Dow scores its best day in 18 months in a broad relief rally after Democrats sweep to power in Congress".
- **The catch we're watching:** Tomorrow's jobs report. Jim Cramer "Warns Friday's Jobs Report Could 'Repeal' Midterm Rally". Consensus is Non-Farm Employment Change 65K, unemployment 4.2%.
- **Two-brain verdict:** Single-brain run, no second opinion.
- **Bottom line:** No name cleared the day-trading bar. One name, RYTM, cleared the swing bar. Data is thin: 111 requests failed after retries, and no intraday levels or RVOL for most names.

## Pre-Market Gappers

20 gappers in the packet. Intraday levels (VWAP, HOD, LOD, premarket high) are unavailable for all of them and no open has printed yet. Showing the first catalyst headline in the packet for each name.

- **DUOG** +54.25% "66% In One Day: How This ETF Turned a Duolingo Rally Into a Monster Trade"
- **CRCT** +48.74% "Cricut Reports Third Quarter 2026 Financial Results and Announces Dividends"
- **HUTG** -45.66% "Rare Earths, Energy And Crypto: Themes ETFs Expands Leveraged Lineup With Six New Funds"
- **LYEL** +43.27% "Lyell Immunopharma Announces $80 Million Private Placement"
- **STLL** -42.98% No catalyst headline in the packet
- **GENVR** +42.4% "12 Information Technology Stocks Moving In Wednesday's Intraday Session"
- **NRIX** -38.23% "Nurix Therapeutics Insider Executes Share Sale"
- **KD** +30.14% "Kyndryl Teams With AWS On Agentic Modernization Solution Pairing Services-as-Software With AWS Transform To Speed Application, Infrastructure And Core System Modernization"
- **DOX** -30.07% "Dow Rallies 2.9%, Oil Sinks 7% After Midterms: Stock Market Today"
- **ECG** -29.29% "Dow Rallies 2.9%, Oil Sinks 7% After Midterms: Stock Market Today" (also: "Everus Construction Group Q3 2026 Earnings Call Transcript")
- **RYTM** +28.04% "Rhythm Pharmaceuticals Shares Halted On Circuit Breaker To The Upside, Stock Now Up 21.67%" (also: "'AstraZeneca Made $10 Billion Offer For Rhythm Pharmaceuticals; Rhythm Specializes In Treatments For Metabolic Conditions And Severe Obesity' - WSJ Exclusive")
- **LIME** -27.83% "JP Morgan Maintains Overweight on Neutron Holdings, Lowers Price Target to $33"
- **GDXU** +27.23% "This ETF Has Surged An Eye-Watering 470% — And It's Not Even Tech" (also: "Bank of Montreal ETNs BULZ, FNGU, GDXU Trading Following Effect of 1:10 Reverse Split")
- **ALIT** +25.99% "12 Industrials Stocks Moving In Wednesday's Intraday Session"
- **HELE** +25.39% "Helen of Troy Board Unanimously Rejects Unsolicited Acquisition Proposal from Empower Brands" (also: "Helen Of Troy Unanimously Rejects $37/Share Takeover Bid, Citing Undervaluation And Strong Long-Term Growth Prospects")
- **CIFR** -20.02% "Cipher and BIO-key Integrate Technology to Expand Identity Security" (also: "Cipher Stock Plummets After Democrats' Midterm Wins", "Keefe Bruyette & Woods Downgrades Cipher Digital to Market Perform")
- **ARRY** +14.16% "Crude Oil Down 5%; Uber Shares Jump After Q3 Results" (also: "Array Technologies Q3 2026 Earnings Call Transcript")
- **IREN** -11.32% "Microsoft’s $5 Billion AI Spending Shortfall Puts IREN, Nebius Under Spotlight as Satellite Imagery Shows Data Center Delays: Report"
- **RIOT** +9.77% "HC Wainwright & Co. Maintains Buy on Riot Platforms, Raises Price Target to $35"
- **ONDS** -8.97% "Ondas Secures Multi-Million-Dollar Counter-UAS Contracts in Europe and Asia"

## Day Trading Watchlist

Rule (Trend Join Long): gap > 3%, price > $3, market cap > $1B, premarket RVOL > 1.5, and price already breaking above yesterday's high.

No names cleared the day-trading bar today. `day_eligible` is false for all 20. Intraday levels are unavailable and premarket RVOL is null for most names, so the rules engine had little to work with. I'm not overriding the flags.

## Swing Watchlist

Rule: gap >= 8%, price > $3, open > yesterday's high, open > the 200-day SMA, market cap >= $800M, and a real catalyst.

| Ticker | Catalyst | Trend context | Idea | Second-brain check | Conviction |
|---|---|---|---|---|---|
| RYTM | News, no earnings. "'AstraZeneca Made $10 Billion Offer For Rhythm Pharmaceuticals; Rhythm Specializes In Treatments For Metabolic Conditions And Severe Obesity' - WSJ Exclusive". Also "Rhythm Pharmaceuticals Shares Halted On Circuit Breaker To The Upside, Stock Now Up 21.67%". Theme: buyout offer, obesity/metabolic. | Price $110.68 vs 200-day SMA $96.97 and prior-day high $105.17. No open has printed, so the gap price stands in for the open. Market cap about $7.67B. Packet gap is +28.04% off prev_close $86.44, but prior_close is $105.15, so part of that move may already have happened. | Starter idea only: watch the open and whether it holds above the prior-day high. Swing management isn't built yet, so no stop, target or size. This is a "watch and build a plan" name. | Single-brain run. | 🟡 |

Why 🟡: the catalyst is named (WSJ) and real, and price is above the 200-day SMA and prior high. But a takeover offer caps upside and the packet has no intraday levels or RVOL to confirm the strength.

## Market Trends of the Day

- **Relief rally after the midterms.** "Dow scores its best day in 18 months in a broad relief rally after Democrats sweep to power in Congress". Benzinga: "Dow Rallies 2.9%, Oil Sinks 7% After Midterms: Stock Market Today". Bloomberg: "Stock Rotation Rolls On as Chipmakers Retreat: Markets Wrap". FT: "Markets surf the blue wave".
- **Crypto miners and AI hosting are weak.** CIFR (-20.02%) and IREN (-11.32%) are down on RVOL of 37.59 and 40.31 per the packet. Headlines: "Cipher Stock Plummets After Democrats' Midterm Wins", and the Microsoft AI spending shortfall report on IREN. RIOT is up 9.77% on price target raises ("Raises Price Target to $35", "Raises Price Target to $37").
- **Geopolitics.** MarketWatch: "A prolonged war in Iran is the market’s real ‘black swan,’ says this strategist".
- **Earnings reactions in the news:** "Toyota stock rallies after company lowered sales guidance", "Qualcomm’s stock falls as twin forces pressure sales", "Figma’s stock dips as investors worry that AI momentum is coming at a high price".

## Technical Signals for Today

Index levels below are ETF proxies (SPY, DIA, QQQ, IWM), not the cash indices.

- S&P 500 proxy 766.73, prior close 754.38 (+1.64%).
- Dow proxy 533.04, prior close 517.02 (+3.1%).
- Nasdaq proxy 691.68, prior close 685.32 (+0.93%).
- Russell 2000 proxy 283.94, prior close 279.83 (+1.47%).
- VIX, 10Y, 3M, oil and DXY: unavailable (Yahoo failed). No breadth data in the packet.

## Economic Data, Rates and the Fed

Nothing high-impact on the USD calendar today. Tomorrow's jobs data is the next event (see below). No Fed speakers or rate data in the packet.

## Coming Up

- **Tomorrow's events (2026-11-06):**
  - 8:30 AM ET Non-Farm Employment Change: forecast 65K, previous 29K
  - 8:30 AM ET Unemployment Rate: forecast 4.2%, previous 4.2%
  - 8:30 AM ET Average Hourly Earnings m/m: forecast 0.3%, previous 0.1%
- **Earnings:** No `next_earnings_date` was filled in for any gapper (earnings lookups were rate limited), so the packet has no upcoming earnings to list.

## Skips and Traps

- **LYEL** +43.27%: the headline is "Lyell Immunopharma Announces $80 Million Private Placement". That is a dilutive raise, so the pop is suspicious. Market cap is about $379M and it sits below its 200-day SMA ($16.72). Trap.
- **DUOG** +54.25% and **GDXU** +27.23%: leveraged ETF/ETN stories, not company news. DUOG has no market cap and GDXU has a 1:10 reverse split headline. Skip.
- **HELE** +25.39%: the news is a board rejecting a $37/share takeover bid. Flag is not swing eligible. Price $37.04 is below the prior-day high $37.78. Skip.
- **KD** +30.14%: AWS partnership headline, but price $16.84 is below the prior-day high $18.02. Not eligible.
- **CRCT** +48.74%: earnings, but market cap is null so the flags are false. Skip.
- **GENVR** (+42.4%), **ALIT** (+25.99%), **ARRY** (+14.16%): the catalysts are generic "stocks moving" roundups, no real story. Not eligible.
- **No catalyst found:** STLL (-42.98%). Skip.
- **Data caveat:** for most gappers the packet's `price` equals `prior_close`, and `prev_close` is a different, older number. The listed gap percentages may be measured against a stale close. Treat them with care.
- **Downside gappers** (HUTG, NRIX, DOX, ECG, LIME, CIFR, IREN, ONDS): the pipeline only builds long setups. Nothing to trade here.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
