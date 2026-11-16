# Premarket Report: 2026-11-16

*Single-brain pass: Claude only. Second brain not wired in yet.*

> Rules pick the watchlist. The AI judges the quality of the setups. This is not financial advice.

**Data warning: read this first.** The scan ran at 06:09 ET Monday and Yahoo rate-limited it hard. 89 requests failed even after retries. VIX, 10Y, 3M, oil and dollar are null. Premarket high, VWAP, HOD, LOD and premarket volume are null for every gapper (`intraday_data_source: unavailable` across the board). RVOL is null for 18 of 20 names. Market cap is null for RMIX and NMAX. `next_earnings_date` is null for everyone. The econ calendar did load this time.

Same catch as last week: **the "gap" numbers are mostly Friday's regular session, not this morning's premarket.** For VTSI, NMAX and AMD, `price` is exactly `prior_close`, and most of the rest sit within a few cents of it. So "AMD -8.8%" means AMD closed Friday down 8.8% from Thursday, which lines up with the headline "AMD Sinks 10.5% as Chip Rally Unwinds, Nasdaq 100 Falls 1.7%". A few names (MTEX, LFWD, LVLU, BKHA) have a `price` that differs from `prior_close`, and FCUV's `prev_close` of 3.0 doesn't match its `prior_close` of 7.06, so treat those gap figures with suspicion too.

## Summary

- **The tape in one line:** risk-off into a big week. ETF proxies are red: SPY -0.38%, QQQ -1.19%, IWM -0.31%, DIA flat at +0.12%. The feed says "S&P 500, Nasdaq futures slide as Nvidia earnings, Anthropic debut loom". The packet has no live futures number, so no size on that slide.
- **The catch we're watching:** Nvidia's first earnings since Huang left, plus the Anthropic IPO. "The Market's Resilience Faces Its Toughest Week Yet, and It Starts With Nvidia". The packet doesn't give either date. Closer in: Fed Chair Warsh speaks at 12:00 PM ET today.
- **Two-brain verdict:** Single-brain run, no second opinion.

## Pre-Market Gappers

All 20 gappers from the packet. Gap % is vs `prev_close` (mostly Thursday's close, see the warning above). Market cap in parentheses where available. Headline is the first one listed for each ticker in the packet.

- **FCUV** +136% ($7.0M) : "Why Take-Two Interactive Software Shares Are Trading Higher; Here Are 20 Stocks Moving Premarket"
- **VTSI** +61.83% ($48M) : "12 Industrials Stocks Moving In Friday's Intraday Session"
- **ZYN** -45.55% ($116M) : "FDA To Expedite Nicotine Pouch Reviews In Pilot Program Under Trump Pressure: Report"
- **BGIN** +40.58% ($439M) : "12 Information Technology Stocks Moving In Friday's Intraday Session"
- **SHIM** +38.89% ($139M) : "12 Industrials Stocks Moving In Friday's Intraday Session"
- **SBC** +37.64% ($756M) : "Intesa Sanpaolo Raises Price Target for Sicily by Car"
- **RMIX** -37.44% (market cap null) : "Suncrete Q3 EPS $(0.01) Misses $0.08 Estimate, Sales $141.000M Miss $146.078M Estimate"
- **NPCE** -37.1% ($260M) : "12 Health Care Stocks Moving In Friday's Intraday Session"
- **BKHA** +35.81% ($30M) : "Black Hawk Acquisition Extends Deadline for Business Combination"
- **NMAX** +31.41% (market cap null) : "Maxim Group Maintains Buy Rating on Newsmax"
- **GRDX** -31% ($27M) : "GridAI Technologies Signs Definitive Agreement to Acquire Pronghorn Resources"
- **LFTO** +30.63% ($4.14B) : "Analyst Rating and Price Target Updates for Liftoff Mobile, Inc."
- **MTEX** -29.84% ($12M) : "Mannatech, Incorporated Announces Third Quarter 2026 Financial Results"
- **LFWD** -29.02% ($11.5M) : "Lifeward Reports Third Quarter 2026 Financial Results"
- **MOD** +27.86% ($7.22B) : "AMD Sinks 10.5% as Chip Rally Unwinds, Nasdaq 100 Falls 1.7%: Stock Market Today"
- **RETO** -27.84% ($243M) : "ReTo Eco-Solutions, Inc. Experiences Multiple Trading Halts"
- **LVLU** -27.6% ($24M) : "11 Consumer Discretionary Stocks Moving In Friday's Intraday Session"
- **CADL** -26.1% ($486M) : "Multiple Financial Institutions Update Ratings and Price Targets for Candel Therapeutics"
- **AMD** -8.8% ($876B) : "Nvidia's Jensen Huang Controversy Could Backfire on China, Chamath Palihapitiya Says — Washington May Get the Chip Controls It's Been Seeking"
- **IREN** -6.73% ($6.49B) : "AMD Sinks 10.5% as Chip Rally Unwinds, Nasdaq 100 Falls 1.7%: Stock Market Today"

The first headline often isn't the real story. The ticker-specific ones that actually explain the move: VTSI "Why Is VirTra Stock Surging Friday?", SHIM "Shimmick Lowers FY2026 Sales Guidance from $525.000M-$575.000M to $500.000M-$525.000M vs $499.800M Est", SBC "SBC Medical Group Announces Strategic Alliance and Investment in NeuroBrain Dynamics", NPCE "Multiple Analysts Downgrade NeuroPace Following Q3 Revenue Miss", LFTO "Why Is Liftoff Mobile Stock Skyrocketing Friday?", MOD "Modine Manufacturing in Acquisition Talks with Samsung Electronics", RETO "ReTo Eco-Solutions, Inc. Announces 8-to-1 Share Consolidation", CADL "Block & Leviton Investigates Candel Therapeutics for Potential Securities Law Violations", IREN "Why Is IREN Stock Falling on Friday?".

## Day Trading Watchlist

The bar is Trend Join Long: gap > 3%, price > $3, market cap > $1B, premarket RVOL > 1.5, and price already breaking above yesterday's high.

No names cleared the day-trading bar today. Every gapper has `day_eligible: false`. Only two names are up more than 3% with a cap over $1B: LFTO and MOD. Both have null RVOL, and both sit under their prior-day high (LFTO 24.44 vs 24.69, MOD 135.66 vs 146.12). There are no premarket high, VWAP, HOD or LOD values for anyone, so there's no trigger to build anyway.

## Swing Watchlist

The bar is: gap >= 8%, price > $3, open above yesterday's high, open above the 200-day SMA, market cap >= $800M, and a real catalyst. The real open hasn't printed yet, so the current price stands in for it.

No names cleared the swing bar today. Every gapper has `swing_eligible: false`. The two up-movers with enough size both miss on trend:

- LFTO: $4.14B, +30.63%, above its 200-day SMA (24.44 vs 20.37), but 5 cents under the prior-day high of 24.69.
- MOD: $7.22B, +27.86%, but 135.66 is under the prior-day high of 146.12 and way under the 200-day SMA of 214.3.

SBC is the closest small name and still misses the cap bar at $756M.

## Market Trends of the Day

The AI trade is cracking and the week is loaded. Friday's tape: "AMD Sinks 10.5% as Chip Rally Unwinds, Nasdaq 100 Falls 1.7%". AMD closed at 534.15 from 585.69. IREN fell again ("Why Is IREN Stock Falling on Friday?"), and Nebius is still in the headlines ("Nebius Crashes 20% as Jensen Huang Shock Rocks AI Stocks"). There's a policy angle on the build-out too: "Voters Rejected Data Centers In 10 States, Raising Regulatory Risk for CoreWeave, Nvidia and AI Build-Out".

This morning is a wait-and-see into Nvidia and Anthropic. Four separate wraps say the same thing ("Stocks dip as caution sets in before Nvidia earnings, Anthropic IPO", "Tech Stocks Slide as Nvidia, Anthropic Tests Await"). QQQ -1.19% vs DIA +0.12% fits that. Tech is selling and the rest is flat.

The strategist chatter is split. Bull: "Why Morgan Stanley says it's time to go 'max' overweight on stocks". Bear: "Here's how much the stock market could crumble if AI is a bubble that bursts" (Furman's 25% drop scenario). Somewhere in between: "Why Nvidia can avoid the fate of most stocks that reached the apex by market cap".

The one AI-adjacent winner is Modine, on a buyout story: "Modine Manufacturing in Acquisition Talks with Samsung Electronics" (data center cooling). Outside of that, the gapper list is mostly small-cap earnings reactions, a SPAC, a reverse split, and a law-firm probe. Not a theme, just Friday's noise.

## Technical Signals for Today

The packet levels are ETF proxies, not index levels, and not timestamped: SPY 754.27 (prev 757.16), DIA 523.1 (prev 522.46), QQQ 680.01 (prev 688.2), IWM 277.55 (prev 278.42). QQQ is the weak spot. VIX, 10Y, 3M, WTI and DXY are all null. No volatility, rate or dollar read, nothing live on futures.

Large caps, price vs 200-day SMA:

- AMD 534.15 vs 423.1. Still well above the long-term trend even after Friday's hit. It's under Friday's high of 571.0.
- LFTO 24.44 vs 20.37, above. Pinned just under the prior-day high of 24.69.
- MOD 135.66 vs 214.3, well below, even after the +27.86% pop.
- IREN 18.165 vs 42.59, way below.

Data artifacts to ignore: RETO's 200-day SMA of 1.6 vs a price of 5.6 is almost certainly the 8-to-1 consolidation not being adjusted. AMD's RVOL of 51.39 and IREN's 29.88 are inflated. The daily bars come from Alpaca's IEX feed, which covers only part of the tape, so don't read those as real 30x to 50x volume days.

## Economic Data, Rates and the Fed

From `econ_calendar` (USD, high impact only):

- **Today, 12:00 PM ET:** Fed Chairman Warsh Speaks. No forecast or previous (it's a speech).
- **Tomorrow, 8:30 AM ET:** Core Retail Sales m/m, forecast 0.4%, previous 0.9%.
- **Tomorrow, 8:30 AM ET:** Retail Sales m/m, forecast 0.2%, previous 0.8%.

Both retail numbers are expected to cool hard from last month. A hot print would lean hawkish; a soft one helps the rate-cut camp. The packet has no 10Y or 3M reading, and no rates headlines in today's news feed, so there's no live read on where yields are going into Warsh's noon remarks. That noon speech is the one scheduled intraday event that could move the tape.

## Coming Up

- **Tomorrow's events:** Retail Sales m/m (forecast 0.2%, previous 0.8%) and Core Retail Sales m/m (forecast 0.4%, previous 0.9%), both at 8:30 AM ET.
- **Earnings:** `next_earnings_date` is null for every gapper, and the packet has no market-wide earnings calendar. The feed says Nvidia reports this week ("Nvidia's first post-Jensen earnings and Anthropic's IPO: What to watch this week"), but it doesn't give the day or time. Check a calendar.

## Skips and Traps

- **SHIM** +38.89%: **trap.** Up big on a sales miss ("Sales $135.798M Miss $139.850M Estimate") and a guidance cut ("Shimmick Lowers FY2026 Sales Guidance"). The EPS beat is the only good line. That's up on bad news. $139M cap. Skip.
- **FCUV** +136%: $7.0M cap, 20-day average volume 9,171, and the only "catalysts" are generic movers roundups plus "Experiences Significant Stock Price Movement". The `prev_close` of 3.0 doesn't match the `prior_close` of 7.06, so the gap figure itself is suspect. Skip.
- **VTSI** +61.83%: Q3 results and Roth reiterating Buy are real news, but it's a $48M cap. Skip.
- **BGIN** +40.58%: the only company-specific headline is a conference appearance ("Announces Participation in 15th Annual ROTH Technology Conference"). That's not a catalyst. $439M cap. Skip.
- **SBC** +37.64%: real news (the NeuroBrain alliance), but $756M is under both bars. Skip.
- **BKHA** +35.81%: a SPAC around a shareholder vote and redemptions. $30M cap. Skip.
- **NMAX** +31.41%: a decent quarter story ("Newsmax Delivers Its Strongest Quarter Since Going Public"), but market cap is null, so it can't clear either bar. Skip.
- **LFTO** +30.63%: the best-looking up name in the packet. $4.14B, above its 200-day SMA, analysts raising targets (Wells Fargo to $27, Piper Sandler to $24). It's not eligible: 5 cents under the prior-day high, null RVOL, no premarket data. Note Piper's new $24 target is already below the 24.44 price. If it clears 24.69 on real volume after 10:00, it's the one to have on screen.
- **MOD** +27.86%: a buyout rumor ("in Acquisition Talks with Samsung Electronics"), and the packet itself says it was first "Reported On November 12". Rumors are binary. It's also under the prior-day high and way under its 200-day SMA. Skip.
- **ZYN** -45.55%: the packet name is "PTL Ltd" but one headline calls ZYN "A New ETF Trading On Smoke, Strategy". The data doesn't agree on what this ticker is. Skip.
- **RMIX, NPCE, MTEX, LFWD, LVLU:** down on misses, downgrades and falling sales. No long setups.
- **CADL** -26.1%: a law-firm probe ("Block & Leviton Investigates Candel Therapeutics") and a pushed BLA timeline. Binary risk. Skip.
- **GRDX** -31% and **RETO** -27.84%: halts, a share-funded acquisition, and an 8-to-1 reverse split. Skip.
- **AMD** -8.8% and **IREN** -6.73%: down with the AI unwind. AMD is still above its 200-day SMA, IREN is far below. With Nvidia earnings ahead this week, catching either one isn't either setup.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
