# Premarket Report: 2026-11-13

*Single-brain pass: Claude only. Second brain not wired in yet.*

> Rules pick the watchlist. The AI judges the quality of the setups. This is not financial advice.

**Data warning: read this first.** The scan ran at 06:09 ET and Yahoo rate-limited it again. 101 requests failed even after retries. VIX, 10Y, 3M, oil and dollar are null. Premarket high, VWAP, HOD, LOD and premarket volume are null for every gapper (`intraday_data_source: unavailable` across the board). Market cap is null for 7 of 20 names (POAS, CDNL, NBIC, NBIZ, NBIL, NEBX, NBIG). **The econ calendar fetch failed too** (429 Too Many Requests, no cache), so the packet has no econ data for today or tomorrow.

Same catch as yesterday: **the "gap" numbers are Thursday's regular session, not this morning's premarket.** For CTVA, SMCI, ONDS, AMD, AAL, NVDA, IBIT and PSFE, `price` is exactly `prior_close`, and most of the rest sit within a few cents of it. `prev_close` is Wednesday's close. So "AMD +5.95%" means AMD closed Thursday up 5.95%, not that it's gapping that much right now.

## Summary

- **The tape in one line:** Thursday closed red on the ETF proxies (SPY -0.35%, DIA -0.38%, QQQ -0.32%, IWM -1.65%), with small caps hit hardest. Overnight the headline is "Stock Market Today: Dow Jones, S&P 500 Futures Rise, Nvidia CEO Exit Remains in Focus — CSCO, AMAT, NU in Focus". The packet has no live futures number, so there's no size on that bounce.
- **The catch we're watching:** rates. "Bond yields just saw their biggest surge since 2022 as expectations grow for more Fed rate hikes." The packet has no 10Y reading and no econ calendar, so we can't see where yields are or what prints today.
- **Two-brain verdict:** Single-brain run, no second opinion.

## Pre-Market Gappers

All 20 gappers from the packet. Gap % is vs `prev_close` (mostly Wednesday's close, see the warning above). Market cap in parentheses where available.

- **POAS** +234.18% (market cap null) : "12 Information Technology Stocks Moving In Thursday's After-Market Session"
- **ADXN** +83.04% ($782M) : "Addex Therapeutics Spin-Out Neurosterix Closes $105 Million Series B Financing"
- **CDNL** -62.37% (market cap null) : "Cardinal Infrastructure Pulls 2026 Forecast After Project Costs Hammer Profits"
- **SMX** -56.75% ($8.7M) : "SMX Shares Halted On Circuit Breaker To The Upside, Stock Now Up 114.44%"
- **ADIG** -49.85% ($746M) : "ADI Global Distribution Records $659M Goodwill Impairment On Residential Market Weakness, Lower Projections & Share Price Decline"
- **PSFE** -43.26% ($200M) : "Paysafe Q3 Adj. EPS $0.44 Misses $0.55 Estimate, Sales $439.572M Miss $448.530M Estimate"
- **ADVB** +42.67% ($5.5M) : "12 Health Care Stocks Moving In Friday's Pre-Market Session"
- **NBIC** -35.16% (market cap null) : no catalyst headline found
- **NBIZ** +34.38% (market cap null) : "Nebius Crashes 20% as Jensen Huang Shock Rocks AI Stocks: One ETF Is Having a Field Day"
- **NBIL** -34.15% (market cap null) : "Nebius Q2 Outlook: Will Goldman’s $35.5 Billion Revenue Forecast Overpower Jim Cramer’s ‘Sell’ Warning?"
- **NEBX** -34.06% (market cap null) : "Double Or Nothing: Tradr Rolls Out 6 High-Octane ETFs Promising Big Swings"
- **NBIG** -33.75% (market cap null) : "What Is Going on With Nebius Stock on Thursday?"
- **CTVA** -24.3% ($6.13B) : "Corteva Q3 Adj. EPS $0.06 Misses $0.10 Estimate, Sales $1.590B Miss $1.764B Estimate"
- **SMCI** -11.31% ($17.8B) : "Supermicro Faces DOJ Investigation Over Alleged Smuggling to China"
- **ONDS** -7.22% ($3.04B) : "Ondas Holdings Q3 EPS $(0.10) Beats $(0.14) Estimate, Sales $167.500M Beat $148.039M Estimate"
- **IREN** -6.51% ($6.96B) : "Why Is IREN Stock Falling on Thursday?"
- **AMD** +5.95% ($961B) : "AMD Management Expresses Confidence in CPU Revenue Doubling by 2027"
- **AAL** -5.4% ($8.82B) : "American Airlines Group Faces FAA Investigation Over Possible Gear Issue"
- **NVDA** -4.48% ($4.00T) : "Cathie Wood Says Nvidia ‘Cannot Be Just The Jensen Show’ After Huang’s Exit, Warns NVDA’s Five-Year CAGR Could Be Cut in Half"
- **IBIT** -4.44% ($57.9B) : "Bitcoin Dumps Below $73,000 as NVDA Plunges 8% on Huang Ouster Report"

## Day Trading Watchlist

The bar is Trend Join Long: gap > 3%, price > $3, market cap > $1B, premarket RVOL > 1.5, and price already breaking above yesterday's high.

No names cleared the day-trading bar today. Every gapper has `day_eligible: false`. Only five names are up more than 3%, and four of them are tiny or have no market cap (POAS null, ADXN $782M, ADVB $5.5M, NBIZ null). The fifth is AMD: $961B, +5.95%, but price 585.69 is under the prior-day high of 593.93. There are no premarket high, VWAP, HOD or LOD values for anyone, so there's no trigger to build anyway.

## Swing Watchlist

The bar is: gap >= 8%, price > $3, open above yesterday's high, open above the 200-day SMA, market cap >= $800M, and a real catalyst. The real open hasn't printed yet, so the current price stands in for it.

No names cleared the swing bar today. Every gapper has `swing_eligible: false`. Four names are up 8% or more, and none of them clears the market cap bar. POAS and NBIZ have null caps. ADXN is $782M, under $800M, and 5.29 is also under both the 200-day SMA (5.76) and the prior-day high (6.43). ADVB is $5.5M.

## Market Trends of the Day

Nvidia is still the whole story. Wednesday night's ouster report turned into an exit: "Nasdaq Falls Over 100 Points; Nvidia CEO Jensen Huang Resigns". NVDA closed Thursday at 166.07, down 4.48% from 173.85, on 749M shares. The fallout runs through everything AI-adjacent. Nebius got hit ("Nebius Crashes 20% as Jensen Huang Shock Rocks AI Stocks"), IREN fell, and half the gapper list is Nebius single-stock ETFs (NBIC, NBIZ, NBIL, NEBX, NBIG) moving 33% to 35% either way. Bitcoin went with it ("Bitcoin Dumps Below $73,000 as NVDA Plunges 8% on Huang Ouster Report").

AMD is the other side of that trade. It ran 5.95% to 585.69 on "AMD Management Expresses Confidence in CPU Revenue Doubling by 2027". The tape was mixed rather than a straight dump: "Nasdaq 100 Turns Green Despite Nvidia's 5% Drop on Huang Exit".

Earnings were mostly misses. CTVA ("Corteva CEO Says Brazil Was 'Materially Weaker Than Anticipated'"), PSFE (miss plus a BTIG downgrade), ADIG ($659M goodwill impairment), and CDNL (pulled its forecast) all got crushed. ONDS was the exception, with a beat and a raised outlook, and it still closed down 7.22%. This morning's movers list in the feed points at Cisco and Applied Materials outlooks.

Two more things in the feed. Rates are spiking: "Bond yields just saw their biggest surge since 2022 as expectations grow for more Fed rate hikes". And there's a plumbing problem: "Microsoft Outage Gums Up Markets, Forces Traders to Use Phones - Bloomberg.com". The packet doesn't say whether the outage is still going.

## Technical Signals for Today

The packet levels are ETF proxies at Thursday's close, not index levels and not premarket: SPY 757.16 (prev 759.8), DIA 522.46 (prev 524.47), QQQ 688.2 (prev 690.4), IWM 278.42 (prev 283.09). IWM's -1.65% is the weak spot, so small caps are lagging. VIX, 10Y, 3M, WTI and DXY are null. There's no volatility, rate or dollar read, and nothing live on futures.

Large caps, price vs 200-day SMA:

- AMD 585.69 vs 421.69. Still the only big name in a clear uptrend, and it closed under Thursday's high of 593.93.
- NVDA 166.07 vs 204.33, well below. It closed near Thursday's high of 167.14.
- SMCI 26.98 vs 32.56, below.
- IBIT 40.35 vs 41.09, just below.
- AAL 13.32 vs 13.47, just below.
- ONDS 5.33 vs 8.73, below.
- IREN 19.475 vs 42.8, way below.
- CTVA 9.19 vs 69.96. That SMA is roughly 7x the price, which looks like a data artifact (maybe a corporate action). Don't trust it.

RVOL caveat: the large-cap RVOLs (NVDA 104.76, SMCI 62.49, AMD 59.78, CTVA 58.23) are inflated. `volume` is full-session volume, while `avg_volume_20d` comes from Alpaca's IEX feed, which only covers part of the tape. Don't read them as real 50x to 100x volume days.

## Economic Data, Rates and the Fed

The econ calendar didn't load this morning. `econ_calendar` reports: "Live fetch failed and no cache available: 429 Client Error: Too Many Requests". `today` and `tomorrow` are empty and the dates are null. The packet has nothing on what releases today, the forecasts, or the prior readings. Yesterday's committed report listed producer prices for this morning. That isn't in today's packet, so check a calendar yourself before 8:30 ET.

On rates, the packet has headlines but no numbers. There's "Bond yields just saw their biggest surge since 2022 as expectations grow for more Fed rate hikes" (summary: "Fed Chair Warsh’s quiet style of communicating interest-rate policy has led to more volatile markets"), and on the other side, "The Fed has a history of not 'disappointing the markets': Strategist - CNBC". The 10Y and 3M rows are null.

## Coming Up

- **Tomorrow's events:** none in the packet, because the econ calendar fetch failed. Tomorrow is Saturday anyway.
- **Earnings:** `next_earnings_date` is null for every gapper, and the packet has no market-wide earnings calendar. Results already out, per the feed: Corteva, Paysafe, ADI Global, Cardinal Infrastructure, Ondas, Legence. Cisco and Applied Materials outlooks are in this morning's "what's moving markets" headline.

## Skips and Traps

- **NBIC:** `catalyst_found: false`. No catalyst, skip.
- **NBIZ, NBIL, NEBX, NBIG:** these are Nebius single-stock ETFs. The headlines are about Nebius or about ETF launches, not these tickers. Market cap is null (no SEC CIK). Leveraged products aren't what either setup was backtested on. Skip. NBIZ's +34.38% is an inverse-style payoff on Nebius falling ("One ETF Is Having a Field Day"), not a bullish story.
- **POAS** +234.18%: the only "catalysts" are generic "stocks moving" roundups. Market cap null, 20-day average volume 13,904. The move went from 0.9 to 3.01, so it's barely over the $3 floor. Skip.
- **ADXN** +83.04%: the news is about a spin-out's financing ("Neurosterix Closes $105 Million Series B"), not Addex itself. $782M cap, 20-day average volume 5,718, under the 200-day SMA. Skip.
- **ADVB** +42.67%: $5.5M cap, 20-day average volume 249, and only generic roundup headlines. Skip.
- **SMX, CDNL, ADIG, PSFE, CTVA:** gapping down on bad news (circuit-breaker chaos, a pulled forecast, a goodwill impairment, misses). No long setups.
- **SMCI** -11.31%: "Supermicro Faces DOJ Investigation Over Alleged Smuggling to China". That's an open probe, a binary risk. Skip.
- **ONDS** -7.22%: a beat and a raise, and the stock still fell, with Needham cutting its target to $14. It's under the 200-day SMA. Not a long setup today.
- **AAL** -5.4%: "Faces FAA Investigation Over Possible Gear Issue". Skip.
- **NVDA, IREN, IBIT:** down with the Huang exit fallout and under their 200-day SMAs. Catching that knife isn't either setup.
- **AMD** +5.95%: still the best-looking name in the packet (uptrend, a rotation story off Nvidia, CPU revenue guidance). But that's Thursday's move, it's under Thursday's high of 593.93, and there's no premarket data. Not eligible. If it takes out 593.93 on real volume after 10:00, it's the one to have on screen.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
