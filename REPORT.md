# Premarket Report: August 27, 2026

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** Quiet and mixed by the numbers. Index proxies show S&P (SPY) +0.02%, Nasdaq (QQQ) +0.09%, Dow (DIA) -0.16% and Russell 2000 (IWM) -0.11%, basically flat. Single names are doing the work today: Nvidia and Salesforce are both getting called out for strong earnings reactions, and Abercrombie & Fitch (ANF) is up 35.67% premarket on a beat-and-raise plus a $100M tariff refund.
- **The catch we're watching:** Total intraday blackout again. All 20 gappers come back `intraday_data_source: unavailable`, so there's no premarket high, VWAP, HOD or LOD to check a breakout against, and both watchlists are empty as a result. Even setting that aside, no positive-gap name clears every rule: ANF is the closest miss on the swing bar, its stand-in open ($147.75) is only about 4.5% under yesterday's high ($154.44), everything else it clears. VIX, the 10-year, the 3-month, oil and the dollar all came back null too (95 failed requests even after retries), and market cap is missing for 8 of the 20 gappers.
- **Two-brain verdict:** Single-brain run today, no second opinion to compare against.

## Pre-Market Gappers

- **CRE** +164.98% - "Why Is Cre8 Enterprise Stock Gaining Wednesday?" (the only CRE-specific headline in the packet, and it never actually answers its own question)
- **CAPA** +133.15% - "Cathie Wood Added To Stake In This Medical Technology Company As Its Shares Surged 6% On Friday" (all five of CAPA's headlines in the packet are 2021 Butterfly Network/Quantum-Si stories, none are dated today or clearly about CAPA itself)
- **XPON** +74% - "12 Industrials Stocks Moving In Wednesday's Intraday Session" (none of XPON's five headlines name the company specifically, all generic mover-list mentions)
- **RDIB** +61.89% - "Why Salesforce Shares Are Trading Higher By Over 11%; Here Are 20 Stocks Moving Premarket" (none of RDIB's headlines are ticker-specific either)
- **GRML** -48.09% - "Greenland Mines Prices Its $20M Public Offering Of 4M Shares"
- **PSNYW** +44.24% - "What's Going On With Polestar Shares On Monday?" (a Polestar-linked warrant, the rest of its headlines are a stale halt notice and a 52-week-low listicle from 2023)
- **WETO** -38.96% - "Wetour Robotics Enters Sales Agreement With Rodman & Renshaw To Sell Up To $75M Of Shares"
- **ANF** +35.67% - "Abercrombie's $100 Million Tariff Refund Stole the Headlines. The Business Did Even Better."
- **DAIC** +32.73% - "12 Information Technology Stocks Moving In Wednesday's After-Market Session" (no DAIC-specific headline in the packet)
- **WSHP** +31.88% - "12 Communication Services Stocks Moving In Wednesday's After-Market Session" (no WSHP-specific headline in the packet)
- **DVXB** -31.44% - no catalyst found in the packet
- **DVXV** -31.02% - no catalyst found in the packet
- **DVIN** -31.02% - no catalyst found in the packet
- **WVVIP** +24.61% - "Willamette Valley Vineyards Announces $1.75M Offering Of Preferred Stock At $3.45 Per Share"
- **GENB** -20.8% - "Generate Biomedicines Q2 EPS $(0.52) Beats $(0.57) Estimate, Sales $6.314M Miss $6.625M Estimate"
- **BWET** -20.53% - "BWET ETF Up More Than 1,600% in 2026: Here's Why It's Beating QQQ and SPY" (that's about its 2026 run, not today's -20.53% move)
- **QFIN** -18.91% - "JP Morgan Downgrades Qfin Holdings to Underweight, Lowers Price Target to $9"
- **BHVN** +17.87% - "Biohaven Licenses Kv7 Platform And Epilepsy Candidate Opakalim To SK Biopharmaceuticals In Deal Worth Up To $795M, Biohaven To Receive $400M Upfront"
- **IREN** -6.23% - "IREN Missed Last Quarter's Estimates by 16 Cents. Can It Turn the Page Thursday?" (a preview of today's earnings, not a result yet)
- **MARA** -5.11% - "Why Is MARA Stock Surging Friday?" (stale, dated last Friday's session, not today's)

## Day Trading Watchlist

The "Trend Join Long" rule: gap over 3%, price over $3, market cap over $1B, premarket RVOL over 1.5, and price already breaking above yesterday's high.

No names cleared the day-trading bar today. This is a total intraday blackout, all 20 gappers have `intraday_data_source: unavailable`, so there's no premarket high, VWAP, HOD or LOD to check a breakout against, and no RVOL confirmation for anyone. Even setting the blackout aside, the only two positive-gap names with market cap over $1B are ANF ($6.56B) and BHVN ($2.56B), and neither is above yesterday's high using the pre-open stand-in price: ANF ($147.75 vs. a prior day high of $154.44) and BHVN ($16.95 vs. $18.23).

## Swing Watchlist

The swing rule: gap of 8% or more, price over $3, open above yesterday's high, open above the 200-day SMA, market cap of $800M or more, and a real catalyst.

No names cleared the swing bar today, every gapper comes back `swing_eligible: false`. The closest miss is **ANF**: its gap of 35.67% clears the 8% floor, its price ($147.75) and market cap ($6.56B) clear easily, its stand-in open sits well above its 200-day SMA ($147.75 vs. $94.50), and it has a real, named catalyst (a beat-and-raise quarter plus a $100M tariff refund). It fails on exactly one line: open above yesterday's high. The stand-in open of $147.75 is about 4.5% under the prior day high of $154.44. **BHVN** is a similar near miss on the same line (open $16.95 vs. prior day high $18.23, about 7% short) with its own real catalyst, a $795M SK Biopharmaceuticals licensing deal with $400M upfront. No other positive-gap name in the packet clears the $800M market cap floor: the next closest by gap size, WVVIP, has a market cap of just $20.7M.

## Market Trends of the Day

AI earnings are still the dominant force. Nvidia is described as climbing premarket after "another set of blockbuster results," and Salesforce stock is jumping too, tied to both its earnings and its Anthropic relationship. The Bank of Korea hiked rates a second straight time while raising growth forecasts, credited directly to an "Nvidia-led AI expansion." Hugging Face, the open-source AI startup, is reportedly catching Nvidia's eye for a deal.

Retail earnings are the other big story, and it shows up directly in the gapper list. Abercrombie & Fitch (ANF) is up 35.67% premarket on a strong quarter plus a $100M tariff refund, with headlines noting it's being priced at higher price points and customers are still buying.

Energy has its own cluster of stories, mostly framed around AI-driven demand or standalone catalysts: Baker Hughes is called a "key winner from the AI boom," Morgan Stanley sees ExxonMobil breaking its record high, Expand Energy is building out natural gas (with a note the growth story may be at risk), Ventural Global is riding the LNG boom, and Talen Energy (down 23% this year) is flagged by Mizuho for a possible rebound. Big oil is also reportedly betting billions on nuclear fusion.

Healthcare and biotech had real deal and earnings flow: Biohaven's $795M SK Biopharmaceuticals licensing deal (BHVN +17.87%), Novo Nordisk getting downgraded to sell by Deutsche Bank after a 70% drop from its peak, and Generate Biomedicines posting an EPS beat but a revenue miss (GENB -20.8%).

Crypto sentiment is split in the feed: one MarketWatch piece has analysts calling for bitcoin to double by next year and reach $500,000 by the end of the decade, while a Benzinga piece quotes Peter Schiff calling the AI-bitcoin pairing "a threat," not bullish. MARA (-5.11% today) shows up in both sides of that debate without a same-day, ticker-specific catalyst of its own.

## Technical Signals for Today

Index proxies are flat to mixed: S&P 500 proxy SPY +0.02%, Nasdaq proxy QQQ +0.09%, Dow proxy DIA -0.16%, Russell 2000 proxy IWM -0.11%. No index is running away from the pack, all four are within a quarter point of flat. VIX, the 10-year yield, the 3-month yield, WTI crude and the dollar index all came back null, yfinance failed on every one of those even after retries, so there's nothing to call on volatility, rates or the dollar this run.

## Economic Data, Rates and the Fed

Nothing on the calendar for today. For tomorrow, August 28, two high-impact USD events land at the same time, 10:00 AM ET: new Fed Chairman Kevin Warsh speaks, and the Preliminary Benchmark Payrolls Revision prints (previous reading was -911K, no forecast given). The news feed frames tomorrow's Warsh appearance, tied to Jackson Hole, as his chance to build credibility with Fed colleagues and markets still wary of his inflation approach and prior ties.

## Coming Up

- **Tomorrow's events:** Fed Chairman Kevin Warsh speaks (10:00 AM ET). Preliminary Benchmark Payrolls Revision (10:00 AM ET, previous -911K).
- **Earnings:** No gapper in the packet has a populated `next_earnings_date`. Worth flagging from the headlines though: IREN's own coverage frames today, Thursday, as its earnings day ("Can It Turn the Page Thursday?"), and SelectQuote's Q4 2026 earnings call is in the news feed as already having happened.

## Skips and Traps

**WVVIP** (+24.61%) is up on a dilutive preferred stock offering, "$1.75M Offering Of Preferred Stock At $3.45 Per Share," priced well under its current $4.15 price. A capital raise priced below the market is normally a reason for a stock to gap down, not up, so this pop looks worth treating with suspicion rather than chasing.

Several names cleared the gap filter but the packet has no headline that actually explains today's specific move: **CAPA** (all five headlines are 2021 stories about a different company entirely), **XPON**, **RDIB**, **DAIC** and **WSHP** (all generic "stocks moving" listicle mentions with no ticker-specific line), **PSNYW** (a stale halt notice and a 2023 52-week-low listicle, nothing dated today), **BWET** (its headlines are about a 1,600% 2026 run, not today's -20.53% drop) and **MARA** (general AI/bitcoin sentiment pieces, no same-day MARA-specific news). **CRE**'s only ticker-specific headline asks "Why Is Cre8 Enterprise Stock Gaining Wednesday?" without ever answering it.

**DVXB**, **DVXV** and **DVIN** have `catalyst_found: false`, no headline in the packet at all. Per the ground rules that's an automatic skip regardless of gap size.

**GRML** and **WETO** are both gapping down hard (-48.09% and -38.96%) on real, specific dilutive-offering news, a $20M public offering for GRML and a $75M share sale agreement for WETO. That's a coherent down move, not a trap, but neither watchlist here trades the short side so there's nothing to do with either name.

**QFIN** is down 18.91% on a real JP Morgan downgrade plus a soft Qifu Technology earnings print (EPS and sales both down sharply year over year). Also a coherent, explained move, also not tradeable under either long-only rule set.

Market cap is missing for 8 of the 20 gappers even after the SEC EDGAR fallback (CRE, CAPA, RDIB, PSNYW, WSHP, DVXB, DVXV, DVIN), so eligibility for several of the largest percentage movers on this list can't actually be confirmed either way.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
