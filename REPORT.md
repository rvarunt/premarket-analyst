# Premarket Report: 2026-11-11

*Single-brain pass: Claude only. Second brain not wired in yet.*

> Rules pick the watchlist. The AI judges the quality of the setups. This is not financial advice.

**Data warning:** the scan ran at 06:23 ET and Yahoo was rate-limited or blocked. 89 requests failed even after retries. VIX, 10Y, 3M, oil and dollar are null in the packet. The index rows are ETF proxies (SPY, DIA, QQQ, IWM) from Alpaca, not the indices themselves. Premarket high, VWAP, HOD, LOD and premarket volume are null for every gapper. RVOL is null for 13 of 20 names. Market cap is null for 7 names (PGRW, ZIP, HIMC, HIMZ, AMRC, MHX, CCG). Nothing below is filled in. Where the packet is blank, this report says so.

## Summary

- **The tape in one line:** Risk-off lean. SPY -0.37%, DIA -0.29%, QQQ -0.58%, IWM -0.68% vs prior close. The headlines are all about Tuesday's inflation print: "Why Goldman Sachs is now changing its Federal Reserve interest-rate forecast" and "Hot CPI Pushes 10-Year Yield to 5%, Nvidia Sinks 6%: Stock Market Today".
- **The catch we're watching:** Rates. Goldman is "pencilling in additional Fed tightening" after the hot CPI, and the packet has no 10Y reading to tell you where yields sit right now. Against that, "Global markets broadly rise on AI chip demand despite Wall Street's retreat on inflation data" and "Nvidia shares rebound 4% as Huang faces scrutiny ahead of earnings" point to a possible chip bounce. Which one wins sets the day.
- **Two-brain verdict:** Single-brain run, no second opinion.

## Pre-Market Gappers

All 20 gappers from the packet. Gap % and price are from the packet. Market cap in parentheses where available.

- **PGRW** +147.2% (price 25.4865, prior close 10.31, market cap null) : "Reported Late Tuesday, Progress Acquisition Corp. Regains NASDAQ Compliance Following Filing Of Delayed Quarterly Report"
- **SMX** +105.9% ($34.6M) : "SMX Announces Development of AI-Powered Scientific Intelligence Platform"
- **PEPG** +92.9% ($319M) : "PepGen Announces Proposed $125.0 Million Public Offering of Common Stock"
- **TANH** +58.0% ($190M) : "Tantech Holdings LTD Announces Yefang Zhang Resigns As Chairman; Yao L Xu Appointed Chairman Effective Oct 1"
- **ZIP** +53.6% (market cap null) : "UBS Maintains Neutral on ZipRecruiter, Raises Price Target to $5"
- **PXLW** +39.8% ($44.1M) : "Pixelworks Partners With Meta to Bring TrueCut Motion Cinematic Content to Newly Launched Meta VR Glasses"
- **NCI** +39.7% ($132M) : "Neo-Concept International Group Holdings Announces 2-For-1 Forward Stock Split, Effective Nov. 10"
- **FF** -38.5% ($137M) : "FutureFuel Corp. Announces Third Quarter 2026 Financial Results"
- **APPS** -35.8% ($884M) : "Digital Turbine Shares Crash Tuesday: What's Going On?"
- **HIMC** -33.7% (market cap null) : "Mid-Day Market Update: NASDAQ Rises 2%; Neurocrine Biosciences Shares Plunge"
- **HIMZ** -33.6% (market cap null) : "Trading Halt: Halt status updated at 8:55:00 AM ET: Quotation Resumption: News and Resumption Times"
- **AMRC** +23.0% (market cap null) : "Ameresco Reports Q3 2026 Financial Results and Provides Updated Guidance"
- **SECZ** +22.4% ($1.39B) : "Securitize Stock Jumps After Q3 Revenue Beat, $50 Million Buyback"
- **MHX** +21.2% (market cap null) : no catalyst headline found
- **CCG** +21.1% (market cap null) : "Cheche Group Signs Strategic Cooperation Agreement with CAR Inc."
- **OPI** +20.2% ($362M) : "Office Properties Income Trust Announces Third Quarter 2026 Results"
- **MARA** +10.7% ($2.85B) : "MARA Rises Despite Q3 Miss as Analysts Focus on First HPC Lease"
- **IREN** -7.8% ($7.05B) : "JP Morgan Maintains Overweight on IREN, Lowers Price Target to $55"
- **ONDS** -6.4% ($3.18B) : "Ondas Receives Purchase Order for Next-Generation Tactical Attack Drones"
- **NVDA** -5.5% ($4.07T) : "Reports of NVIDIA H200 Chips Found at Chinese University"

## Day Trading Watchlist

The bar is Trend Join Long: gap > 3%, price > $3, market cap > $1B, premarket RVOL > 1.5, and price already breaking above yesterday's high.

No names cleared the day-trading bar today. Every gapper has `day_eligible: false`. Only two up-gappers have a market cap over $1B: SECZ (price 8.53, under prior-day high 9.87, RVOL null) and MARA (price 7.35, under prior-day high 7.58, RVOL 48.84). Neither is breaking yesterday's high. No premarket high, VWAP, HOD or LOD came through for anyone, so there are no levels to build a trigger from anyway.

## Swing Watchlist

The bar is: gap >= 8%, price > $3, open above yesterday's high, open above the 200-day SMA, market cap >= $800M, and a real catalyst. The real open hasn't printed yet, so the current gap price stands in for it.

No names cleared the swing bar today. Every gapper has `swing_eligible: false`. The closest was MARA (gap +10.7%, $2.85B), but price 7.35 is under both prior-day high 7.58 and the 200-day SMA of 10.66. SECZ fails the same way (8.53 vs prior-day high 9.87 and 200-day SMA 10.32).

## Market Trends of the Day

Inflation and rates are the story. The news feed keeps coming back to Tuesday's hot CPI: Goldman changing its Fed forecast toward more tightening, "Hot CPI Pushes 10-Year Yield to 5%", and "Tech Gains Boost Stocks as Bonds Slide on Fed Bets: Markets Wrap - Bloomberg.com". SMX's headline list even includes "Nasdaq Down Over 200 Points; US Consumer Prices Increase 0.4% In October". The ETF proxies are red across the board this morning, small caps worst (IWM -0.68%).

AI and chips are the counter-current. NVDA is -5.5% in the packet on China headlines ("Reuters Reported Earlier, People's Liberation Army-Linked Chinese University Bought Nvidia H200 Chips Despite US Blacklist"), but the news feed also has "Nvidia shares rebound 4% as Huang faces scrutiny ahead of earnings - CNBC" and "Global markets broadly rise on AI chip demand". CoreWeave is in the feed twice on a revenue beat and "$9 billion in planned prepayments". Crypto-miner and AI-compute names split: MARA +10.7% on a buyback and its first HPC lease, IREN -7.8% with a JP Morgan target cut.

The rest of the gapper list is small-cap noise: reverse/forward splits, halts, offerings, and compliance notices. That's not a theme, it's a casino.

## Technical Signals for Today

Packet levels (ETF proxies, not index levels): SPY 749.93 (prev 752.72), DIA 521.8 (prev 523.3), QQQ 674.82 (prev 678.77), IWM 280.58 (prev 282.49). VIX, 10Y, 3M, WTI and DXY are all null because the Yahoo batch failed, so there's no volatility, rate or dollar read from the packet. Intraday levels for every gapper are null.

Where the packet has daily context: NVDA (168.785) is below its 200-day SMA of 204.54 and below prior-day high 174.66. IREN (19.72) is way under its 200-day SMA of 43.21. ONDS (5.58) is under 8.8. MARA (7.35) is under 10.66. Of the larger names, nobody is in a clean uptrend on these numbers.

## Economic Data, Rates and the Fed

Today (the packet filters to USD high-impact only): nothing. `econ_calendar.today` is empty for 2026-11-11.

The Fed angle comes from headlines, not data: "Why Goldman Sachs is now changing its Federal Reserve interest-rate forecast" ("Following Tuesday's hot CPI data, Goldman Sachs is now pencilling in additional Fed tightening") and "Hot CPI Pushes 10-Year Yield to 5%". The packet has no actual 10Y or 3M figure, so the 5% number is a headline, not a packet reading. With no data on the calendar, the market is left to chew on that CPI print all day.

## Coming Up

- **Tomorrow's events:** none in the packet (no USD high-impact releases for 2026-11-12).
- **Earnings:** `next_earnings_date` is null for every gapper, and the packet has no market-wide earnings calendar. The CNBC headline says Huang faces scrutiny "ahead of earnings", but the packet has no NVDA earnings date. Recent-results headlines in the feed (not upcoming dates): CoreWeave, Cloudflare, Firefly, Vestas, RWE, Nissan, plus gappers FF, AMRC, SECZ, OPI, MARA.

## Skips and Traps

- **PGRW** +147.2%: the catalyst is regaining Nasdaq listing compliance after a late filing, plus a "Short Volatility Alert". That's housekeeping, not a reason for a 2.5x. Market cap null, no 200-day SMA or prior-day high in the packet. Skip.
- **SMX** +105.9%: "AI-Powered Scientific Intelligence Platform" with a limited commercial launch planned for Q2 2027, on a $34.6M cap, and it already hit a circuit-breaker halt. Buzzword pop on a micro cap. Skip.
- **PEPG** +92.9%: this is the up-on-bad-news trap. The headlines include "PepGen Announces Proposed $125.0 Million Public Offering of Common Stock". A $125M offering on a $319M cap is heavy dilution. The Wedbush target raise to $10 doesn't cancel that. Trap.
- **TANH** +58.0%: same story as yesterday's report. A chairman change plus generic "stocks moving premarket" headlines about other companies. $190M cap, and a trading-halt headline. Skip.
- **ZIP** +53.6%: the headline is a UBS target raise to $5 while UBS stays Neutral, and price is already 6.59. Market cap null. Skip.
- **PXLW** +39.8%: real news (Meta partnership on VR glasses), but a $44.1M cap. Too small for either list. Watch only.
- **NCI** +39.7%: a forward split, a halt with news pending, and a prospectus for 4.4M shares sold on behalf of selling shareholders. Selling shareholders into a pop is a trap. Skip.
- **CCG** +21.1%: a cooperation agreement, but market cap null and the only other headline is an extraordinary general meeting. Skip.
- **AMRC** +23.0%: Q3 results and updated guidance, but market cap is null so it can't be checked against either bar. Price 27.62 is right at prior-day high 27.69. Watch only.
- **SECZ** +22.4%: a decent catalyst ("Q3 Revenue Beat, $50 Million Buyback") on a $1.39B cap, but price 8.53 is under prior-day high 9.87 and the 200-day SMA of 10.32. Not eligible. Watch only.
- **OPI** +20.2%: Q3 results with NOI up 14.8%, but a $362M cap. Below both bars. Watch only.
- **MARA** +10.7%: "Rises Despite Q3 Miss". The pop is on the buyback and HPC lease, not the quarter. Under prior-day high and the 200-day SMA. Not eligible.
- **MHX** +21.2%: `catalyst_found: false`. No catalyst, skip. Market cap is null too.
- **FF, APPS, HIMC, HIMZ, IREN, ONDS, NVDA**: gapping down, no long setups. APPS has a law-firm securities investigation headline. NVDA has China export-control headlines and a Schumer headline on the Huang story.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
