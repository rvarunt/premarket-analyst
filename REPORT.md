# Premarket Report: November 9, 2026

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** Rebound attempt after last week's AI-led rout. ETF proxies in the packet: SPY +0.27%, QQQ +1.27%, IWM +0.95%, DIA -0.46%. VIX, 10Y, 3M, oil and dollar all came back null (Yahoo rate-limited), so no volatility or rates read today.
- **The catch we're watching:** CPI at 8:30 AM ET tomorrow (CPI m/m forecast 0.3%, core 0.2%). Headlines say the strong jobs report keeps a December rate hike alive, so a hot print could hit a tape that's only just stabilizing.
- **Two-brain verdict:** Single brain, no second opinion to compare.

## Pre-Market Gappers

Data caveat first. Intraday fields (premarket high, VWAP, HOD, LOD, premarket volume, RVOL for the small caps) are all null. 118 requests failed even after retries. Also, for most names the packet's `price` sits at or near `prior_close`, so these gap percentages look like Friday's move versus Thursday's close, not a fresh overnight gap. Treat them as a "what moved last session" list.

- **STAK** +82.1%: "STAK Inc. Discloses Initial Progress in Gas-Powered Generator Business"
- **FLYT** +73.0%: "As With Stocks, Robinhood Users Like Their ETFs Risky"
- **GOGO** +71.5%: "Gogo Inc. Announces Third Quarter 2026 Financial Results"
- **LASC** +57.6%: no catalyst found in the packet
- **BDSX** -57.0%: "Johnson Fistel, PLLP Initiates Investigation into Biodesix Following Stock Decline"
- **SKIN** +51.8%: "Beauty Health Q3 EPS $(0.14) Beats $(0.26) Estimate, Sales $69.200M Beat $67.943M Estimate"
- **QNTU** +51.1%: "Tradr Bets on Quantum Boom With 5 New 2X ETFs on Quantinuum, Ciena"
- **OBX** +44.4%: "Obsidian Therapeutics Announces Positive Updated Results for Amsoki-cel in Advanced Melanoma"
- **KRMN** +42.1%: "These Analysts Revise Their Forecasts On Karman After Upbeat Q3 Results"
- **FLY** +36.8%: "Firefly Aerospace Onboarded as Vendor for NASA's $10 Billion CLPS 2 Contract"
- **IRTC** -30.7%: "iRhythm Technologies Faces Investor Investigation Following Q3 Earnings Miss and Guidance Update"
- **IREN** +20.1%: "Jones Trading Upgrades IREN to Buy, Announces $40 Price Target"
- **CIFR** +18.1%: "AI Stocks Got Hammered After Midterms, but This Analyst Says the Panic Is Overblown"
- **ONDS** +18.1%: "Ondas Inc. Announces Acquisition of Stemme GmbH and U.S. Manufacturing Expansion"
- **WULF** +13.4%: "Needham Maintains Buy on TeraWulf, Lowers Price Target to $25"
- **RIOT** +13.2%: "Needham Maintains Buy Rating and Raises Price Target on Riot Platforms"
- **AMD** +10.9%: "Oppenheimer Upgrades Advanced Micro Devices to Outperform, Announces $600 Price Target"
- **MCHP** -10.1%: "Jefferies Maintains Buy on Microchip Technology, Lowers Price Target to $85"
- **INTC** +7.9%: "Micron, AMD, SanDisk Lead AI Stock Bounce as Investors Buy the Dip"
- **MU** +4.7%: "Nasdaq Gains Over 1% as Chipmakers Recover: Investor Sentiment Improves, but Fear & Greed Index Remains in 'Extreme Fear' Zone"

## Day Trading Watchlist

No names cleared the day-trading bar today. That flag encodes gap over 3%, price over $3, market cap over $1B, premarket RVOL over 1.5, and price already breaking above yesterday's high. Every gapper came back `day_eligible: false`. Note that with premarket high and VWAP null, the levels needed for a trigger aren't in the packet anyway.

## Swing Watchlist

No names cleared the swing bar either. That flag encodes gap of 8% or more, price over $3, open above yesterday's high, open above the 200-day SMA, market cap of $800M or more, and a real catalyst. Every gapper came back `swing_eligible: false`. The open isn't printed yet, so the scan used the current price as a stand-in.

## Market Trends of the Day

AI trade trying to bounce after a brutal week. Benzinga: "Nasdaq 100 Rebounds 2% After Worst Day Since 2020, Payrolls Smash Estimates: Stock Market Today" and "Nasdaq Gains Over 1% as Chipmakers Recover: Investor Sentiment Improves, but Fear & Greed Index Remains in 'Extreme Fear' Zone". Asian stocks climbed after the earlier tech rout (Al Jazeera), and US futures are mixed ahead of Berkshire earnings, Nvidia news and AI regulation plans (Yahoo Finance).

Sentiment is still fragile. Citi says it's better to sit out the global tech trade until AI sentiment improves. Morgan Stanley's chief strategist says the correction is entering its final phase but to wait before buying the dip. MarketWatch also has "How Wall Street is reacting to the news of Nvidia's investigation into Jensen Huang spy claims".

Group moves from the gapper list: chip names bounced (AMD +10.9%, INTC +7.9%, MU +4.7%) while MCHP is down 10.1% with a string of analyst price target cuts. Bitcoin miners and AI data-center names are up (IREN, CIFR, WULF, RIOT, all +13% to +20%), though IREN's headlines include "CoreWeave and IREN Stocks Face Pressure as Microsoft Reassesses Its Computing Deals".

## Technical Signals for Today

Only ETF proxies are available: SPY last 735.40 vs prev close 733.43 (+0.27%). QQQ 656.31 vs 648.05 (+1.27%). IWM 273.59 vs 271.01 (+0.95%). DIA 512.21 vs 514.56 (-0.46%). VIX is null. No breadth data in the packet. Nasdaq and small caps are leading, the Dow is lagging.

## Economic Data, Rates and the Fed

Nothing high-impact on the USD calendar today. Headlines tie the jobs beat to rate-hike odds: Bloomberg via Google News, "Gold Holds Decline as US Jobs Data Fan December Rate Hike Bets", and Benzinga, "Nasdaq 100 Has Worst Day Since 2020, Jobs Beat Keeps Fed Hike Alive: This Week on Wall Street". Yields are null this scan.

## Coming Up

- **Tomorrow's events (Nov 10):** 8:30 AM ET CPI m/m (forecast 0.3%, previous 0.6%). 8:30 AM ET Core CPI m/m (forecast 0.2%, previous 0.3%).
- **Earnings:** `next_earnings_date` is null for every gapper. The only earnings mentions in the market news are Q3 snapshots for Dole and Barrick Mining, and SoftBank's second-quarter earnings (Reuters headline). No timing given in the packet.

## Skips and Traps

- **LASC:** no catalyst found. Skip. Market cap also null.
- **FLYT:** headlines are generic ETF stories, not about the company. Market cap null. Skip.
- **QNTU:** the only headline is a July ETF launch piece, not a real catalyst for a +51% move. Market cap null. Skip.
- **STAK:** +82%, but the headline says the buyer LOI is "Non-Binding... No Purchase Commitment", market cap about $62.6M. Pure micro-cap hype.
- **GOGO:** +71.5% with a market cap of about $527M, under the $800M swing floor. Earnings plus a term loan amendment.
- **SKIN:** +51.8%, market cap about $102.8M, and the headlines include guidance narrowing and a class action settlement. Too small and messy.
- **BDSX, IRTC:** big gap downs with investor-investigation headlines. Long-only rules, so not on any list. IRTC also has "Citigroup Downgrades iRhythm Holdings to Neutral, Lowers Price Target to $124".
- **OBX (+44.4%, market cap about $856M):** good news, but not flagged eligible, and price is below its 200-day SMA (17.27) in the packet.
- **KRMN, FLY:** real catalysts, but flagged ineligible and below their 200-day SMAs.
- **Miners and AI infra (IREN, CIFR, WULF, RIOT, ONDS):** all trade far below their 200-day SMAs, flagged ineligible, and the Microsoft pullback headline on IREN is a reminder that this group is headline-driven.
- **MCHP:** down on a wave of price target cuts. Not a long.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
