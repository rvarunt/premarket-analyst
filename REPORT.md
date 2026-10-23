# Premarket Report: 2026-10-23

*Single-brain run: Claude only.*

> Rules pick the watchlist. The AI judges the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** Tech is getting hit. The Nasdaq proxy (QQQ) is -2.85% and the S&P proxy (SPY) is -1.18%, while the Dow proxy (DIA, +0.04%) and Russell 2000 proxy (IWM, +0.07%) are flat. Index figures are ETF proxies, not the index levels. Futures were not in the packet.
- **The catch we're watching:** AI and chip weakness. Headlines in the packet point to AI spending fears, an Nvidia warning, and a CoreWeave debt stress story. If that keeps bleeding, nothing long in tech works.
- **Two-brain verdict:** Single-brain run, no second opinion.

Data quality is poor today. 111 requests failed after retries, mostly Yahoo rate limits. No gapper has premarket high, VWAP, or premarket volume, and VIX, 10Y, 3M, oil and DXY are all null. Eligibility flags came back false across the board.

## Pre-Market Gappers

All 20 gappers in the packet, biggest absolute gap first. Most of these gap down.

- **TANH** +181.84%: "Tantech Holdings LTD Announces Yefang Zhang Resigns As Chairman; Yao L Xu Appointed Chairman Effective Oct 1"
- **XLAB** +73.16%: "12 Information Technology Stocks Moving In Thursday's Pre-Market Session"
- **AVTX** -39.23%: "HC Wainwright & Co. Downgrades Avalo Therapeutics to Neutral"
- **MRNX** -34.80%: "Bulls Pile Into Moderna As FDA Decision Nears, Ignites 60% Surge In This ETF"
- **NVEC** -33.68%: "Glancy Prongay Wolke & Rotter LLP Announces Investigation into NVE Corporation"
- **MTSG** -31.83%: no catalyst found
- **SIMX** -30.33%: no catalyst found
- **FOMG** -30.14%: no catalyst found
- **LNOK** -30.08%: "Defiance Launches 2X Leveraged Nokia ETF As Earnings, EU Tailwinds Fuel Bullish Bets"
- **KRRO** +29.71%: "Korro Bio Announces Preclinical Results Showing KRRO-111 Potential To Treat Both Lung And Liver Manifestations Of Alpha-1 Antitrypsin Deficiency"
- **CCG** +29.51%: "Maxim Group Downgrades Cheche Group to Hold"
- **TTMI** -27.67%: "Needham Maintains Buy on TTM Technologies, Lowers Price Target to $150"
- **KALU** -25.31%: "Kaiser Aluminum Q3 Adj. EPS $1.89 Misses $2.36 Estimate, Sales $1.214B Inline"
- **BHVN** +25.02%: "Biohaven Shares Rise After FDA Accepts Vyglxia Resubmission for Review"
- **MRNA** -17.50%: "Merck And Moderna Report Phase 3 Melanoma Trial Results For Personalized mRNA Cancer Therapy; Intismeran Plus KEYTRUDA Cuts Melanoma Recurrence Or Death Risk By 42%"
- **NOK** -15.12%: "Nokia and ICEYE Sign MoU with Ukraine Ministry of Defense for Satellite Communications"
- **WULF** -11.35%: "ATB Cormark Capital Markets Maintains TeraWulf Buy Rating, Lowers Price Target"
- **IREN** -8.41%: "CoreWeave Debt Stress Mounts: Bond Yield Hits Record as Stock Suffers $44 Billion Wipeout"
- **INTC** -7.98%: "SK Hynix Shelves Solidigm IPO Plans Amid Chip-Stock Correction and Market Volatility: Says Does Not Reflect Any Change in 'Growth Prospects or Investment Needs'"
- **NVDA** -4.34%: "Nvidia's China Market Has Effectively Vanished: 'Every Restriction Also Gives Chinese Suppliers a Larger Captive Market,' Says Shay Boloor"

## Day Trading Watchlist

What "eligible" means here: Trend Join Long. Gap above 3%, price above $3, market cap above $1B, premarket RVOL above 1.5, and price breaking above yesterday's high.

No names cleared the day-trading bar today. Every gapper came back `day_eligible: false`. The packet also has no premarket high, VWAP or premarket volume for any name, so there are no live levels to build a plan from.

## Swing Watchlist

What "eligible" means here: gap of 8% or more, price above $3, open above yesterday's high, open above the 200-day SMA, market cap of $800M or more, and a real catalyst.

No names cleared the swing bar today. Every gapper came back `swing_eligible: false`. Note the open isn't real yet this early, so the scanner uses the current gap price as a stand-in.

## Market Trends of the Day

Risk-off in tech and AI. The packet shows SPY at -1.18% and QQQ at -2.85% against flat DIA and IWM, so it's a megacap and growth sell-off, not a broad one.

The gapper headlines tell the same story. Chip and AI infrastructure names are down: NVDA -4.34%, INTC -7.98%, IREN -8.41%, WULF -11.35%, NOK -15.12%. Headlines tied to that group cover AI spending fears, an Nvidia warning, a "chip-stock correction" and CoreWeave bond stress. One MarketWatch headline says the AI trade "is on the ropes."

Rates are the other thread. MarketWatch says Treasury yields logged their biggest drop since the 2023 banking crisis. I have no yield levels, since the 10Y and 3M came back null.

Biotech is a stock-picker's tape: BHVN is up on an FDA resubmission acceptance, MRNA is down on melanoma data after an alleged leak, and KRRO is up on preclinical results.

## Technical Signals for Today

- **S&P 500 proxy (SPY):** 764.03 vs 773.13 prior close, -1.18%.
- **Nasdaq proxy (QQQ):** 704.56 vs 725.25, -2.85%.
- **Dow proxy (DIA):** 527.91 vs 527.70, +0.04%.
- **Russell 2000 proxy (IWM):** 276.64 vs 276.46, +0.07%.
- **VIX, 10Y, 3M, WTI oil, DXY:** not available, the fetches failed.
- **200-day SMA:** NVDA at 212.27 sits above its 200-day (203.55). INTC at 85.50 is right at its 200-day (85.58). TTMI (73.89 vs 128.01), KALU (114.99 vs 153.61), WULF (11.32 vs 18.12) and IREN (25.50 vs 45.03) are well below theirs.

These are ETF prices, not index levels, and this is a premarket read. Breadth, futures and intraday levels were not in the packet.

## Economic Data, Rates and the Fed

The packet has no high-impact USD releases for today (Fri 2026-10-23). The calendar is filtered to high-impact USD events only. Nothing to report on rates or the Fed from the calendar.

Headline context only: a Reuters-sourced item in the news feed says the "Fed meeting" is a pivotal test for the AI rally. No date or figures were given, so I'm not adding any.

## Coming Up

- **Tomorrow's events:** None in the packet. Tomorrow is Saturday 2026-10-24, with no high-impact USD events listed.
- **Earnings:** No `next_earnings_date` came back for any gapper, so there's nothing to list. Market-wide earnings coverage in the scanner is partial.

## Skips and Traps

Nothing here is tradeable by the rules, but these are worth knowing as traps or skips.

- **No catalyst found:** MTSG, SIMX, FOMG. Skip.
- **TANH +181.84%:** The market cap is $154M and the packet shows trading halts in the headlines. The only company-specific headline is a chairman change. Market cap is under $1B, so it fails the rules anyway. Skip.
- **XLAB +73.16%:** The only headlines are generic "stocks moving" roundups, which don't name a catalyst. Market cap is null and the price is below its 200-day SMA (4.71 vs 8.26). Skip.
- **CCG +29.51%:** Up on a headline that is a downgrade ("Maxim Group Downgrades Cheche Group to Hold"). That's a suspicious pop, not a buy. Market cap is null.
- **KRRO +29.71%:** Preclinical results, but market cap is $177M, well under the bars. Skip.
- **BHVN +25.02%:** FDA accepted a resubmission, which is a real catalyst. But the price (14.69) is below yesterday's high (16.52), so it fails the swing rule. Not a name for the list.
- **MRNX -34.80%, LNOK -30.08%:** The headlines are about Moderna and Nokia ETFs (Defiance). I can't tell from the packet what these tickers are beyond that. Market cap is null. Skip.
- **Gap-down names with bad news:** AVTX (downgrade), NVEC (law firm investigation), KALU (EPS miss, $1.89 vs $2.36 estimate), MRNA (alleged data leak). The rules here are long-only, so there's nothing to play. They're shown as red flags.
- **Big tech gap-downs (NVDA, INTC, IREN, WULF, NOK, TTMI):** all below the long-side bar. No long setups until the tape stabilizes.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
