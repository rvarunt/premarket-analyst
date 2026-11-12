# Premarket Report: 2026-11-12

*Single-brain pass: Claude only. Second brain not wired in yet.*

> Rules pick the watchlist. The AI judges the quality of the setups. This is not financial advice.

**Data warning: read this first.** The scan ran at 06:24 ET and Yahoo was rate-limited or blocked again. 109 requests failed even after retries. VIX, 10Y, 3M, oil and dollar are null. Premarket high, VWAP, HOD, LOD and premarket volume are null for every gapper (`intraday_data_source: unavailable` across the board). Market cap is null for 12 of 20 names (CRWX, CORD, CWVX, CRWG, CRWU, SFWL, AXTU, LWLX, AXTQ, AXTX, AXTC, NBIG).

The bigger catch: **the "gap" numbers in this packet are Wednesday's regular session, not this morning's premarket.** The index rows and the five large-cap names come from Alpaca's daily bar (latest bar close vs the bar before). Before the open that's Wednesday's close vs Tuesday's close. You can see it in the packet. CIFR, INTC, AMD, WULF and IREN all show `price` exactly equal to `prior_close`, and 12 of the 20 gappers are within 0.5% of `prior_close`. So "AMD +7.32%" means AMD closed up 7.32% on Wednesday, not that it's gapping 7.32% this morning. Read every gap % below with that in mind.

## Summary

- **The tape in one line:** Wednesday closed strong (SPY +1.32%, QQQ +2.31%, IWM +0.89%, DIA +0.51% on the ETF proxies). Then the overnight news flipped hard: "Nasdaq futures fall as Nvidia sinks 8% after hours on report board may oust Huang". The packet has no live futures number, so the size of this morning's drop isn't in the data.
- **The catch we're watching:** Nvidia's leadership. "Nvidia's stock drops as the board reportedly prepares to remove CEO Jensen Huang", "Jensen Huang built Nvidia into a behemoth. His scandal puts the entire AI boom in jeopardy.", and "Nvidia's Leadership Crisis Weighs on Asian Markets - WSJ". Whatever the board does sets the tone for every AI name on this list. AMD's headlines show the other side: "Nvidia Stock Sinks as Jensen Huang Ouster Report Sends Investors Toward AMD, Broadcom".
- **Two-brain verdict:** Single-brain run, no second opinion.

## Pre-Market Gappers

All 20 gappers from the packet. Gap % is vs the packet's `prev_close`, which for most names is Tuesday's close (see the warning above). Market cap in parentheses where available.

- **RETO** +65.95% ($269M) : "ReTo Advances Brushless DC Water Pump Technology"
- **CRWX** +49.9% (market cap null) : no catalyst headline found
- **CORD** -49.57% (market cap null) : "These 3 ETFs Doubled Investors' Money in October as AI Stocks Crashed"
- **CWVX** +49.5% (market cap null) : "CoreWeave Powers MasterClass AI Agents In New Cloud PartnershipCoreWeave"
- **CRWG** +48.85% (market cap null) : "Why Is CoreWeave Stock Soaring Friday?"
- **CRWU** +48.29% (market cap null) : "REX Shares Drops Three ETFs To Bet Big On Bitcoin Mining, AI Cloud, Stablecoins"
- **SFWL** +43.88% (market cap null) : "12 Industrials Stocks Moving In Wednesday's Pre-Market Session"
- **SMX** -41.87% ($20.1M) : "SMX Announces Development of AI-Powered Scientific Intelligence Platform"
- **AXTU** +40.07% (market cap null) : "These AXT ETFs Turned a 30% Stock Rally Into Nearly 50% Returns"
- **LWLX** -38.86% (market cap null) : no catalyst headline found
- **AXTQ** -38.63% (market cap null) : no catalyst headline found
- **AXTX** +38.53% (market cap null) : no catalyst headline found
- **BGS** +37.97% ($298M) : "B&G Foods Reports Q3 2026 Financial Results Exceeding Expectations"
- **AXTC** +37.74% (market cap null) : no catalyst headline found
- **NBIG** +32.11% (market cap null) : "Nebius Group Stock Is Falling Wednesday: What's Going On?"
- **CIFR** +9.05% ($3.24B) : "Why Is Cipher Digital Stock Surging on Wednesday?"
- **INTC** +7.57% ($332B) : "Intel Continues Enabling GPU D-Series 'Crescent Island' Driver Support for Linux 7.5"
- **AMD** +7.32% ($907B) : "William Blair Upgrades Advanced Micro Devices to Outperform"
- **WULF** +6.7% ($6.71B) : "TeraWulf Stock Rises With AI Infrastructure Stocks After CoreWeave Earnings"
- **IREN** +5.63% ($7.44B) : "Voters Rejected Data Centers In 10 States, Raising Regulatory Risk for CoreWeave, Nvidia and AI Build-Out"

## Day Trading Watchlist

The bar is Trend Join Long: gap > 3%, price > $3, market cap > $1B, premarket RVOL > 1.5, and price already breaking above yesterday's high.

No names cleared the day-trading bar today. Every gapper has `day_eligible: false`. The five names with a market cap over $1B are all sitting under their prior-day high: CIFR 7.11 vs 7.40, INTC 62.51 vs 64.05, AMD 552.82 vs 567.62, WULF 13.38 vs 13.76, IREN 20.83 vs 21.75. That's just Wednesday's close under Wednesday's high, since the price is the close. There are no premarket high, VWAP, HOD or LOD values for anyone, so there's no trigger to build anyway.

## Swing Watchlist

The bar is: gap >= 8%, price > $3, open above yesterday's high, open above the 200-day SMA, market cap >= $800M, and a real catalyst. The real open hasn't printed yet, so the current price stands in for it.

No names cleared the swing bar today. Every gapper has `swing_eligible: false`. The only name with a gap >= 8% and a known market cap >= $800M is CIFR (+9.05%, $3.24B). It fails on trend: 7.11 is under prior-day high 7.40 and way under the 200-day SMA of 17.31.

## Market Trends of the Day

AI is the whole story, and it split overnight. Wednesday was a big AI-infra day. The CoreWeave and AI-compute crowd ran ("TeraWulf Stock Rises With AI Infrastructure Stocks After CoreWeave Earnings", "Why Is Cipher Digital Stock Surging on Wednesday?"), and half the gapper list is CoreWeave, AXT and Nebius tickers. Their own headlines point to leveraged single-stock ETFs ("Leverage Shares Launches 3 New Leveraged ETFs On CoreWeave, Circle, And WeBull", "These AXT ETFs Turned a 30% Stock Rally Into Nearly 50% Returns").

Then came the Nvidia board story after the close. The feed says Nvidia sank 8% after hours and dragged "other chip makers" and Nasdaq futures down. It "weighs on Asian markets", and China's AI firms "fear Jensen Huang's turmoil could cut off their Nvidia lifeline". The one rotation angle in the packet is money moving toward AMD and Broadcom on that news. The packet has no live AMD premarket price to confirm whether that's actually happening this morning.

Outside the US the tape looks firmer: "European shares hit record high helped by strong earnings and lower energy prices - Reuters" and "Europe's STOXX 600 hits record high on strong earnings, easing Mideast tensions - Reuters".

Earnings trickle: Yeti and Aurora Mobile Q3 snapshots, "FIS stock drops after earnings report", "Telefonica Raises Earnings Guidance", and Morningstar raising its Moderna fair value.

## Technical Signals for Today

Packet levels are ETF proxies at Wednesday's close, not index levels and not premarket: SPY 759.8 (prev 749.93), DIA 524.47 (prev 521.8), QQQ 690.4 (prev 674.82), IWM 283.09 (prev 280.58). VIX, 10Y, 3M, WTI and DXY are null. There's no volatility, rate or dollar read, and nothing live on futures.

Daily context on the large caps (price vs 200-day SMA):

- AMD 552.82 vs 420.02. The only big name in a clear uptrend, and it closed under Wednesday's high of 567.62.
- INTC 62.51 vs 87.28, below.
- CIFR 7.11 vs 17.31, way below.
- WULF 13.38 vs 18.01, below.
- IREN 20.83 vs 43.01, way below.

The miners and AI-hosting names bounced Wednesday inside longer downtrends.

RVOL caveat: the large-cap RVOLs (AMD 51.17, INTC 28.76, IREN 35.11) look inflated. The packet's `volume` is full-session volume, while `avg_volume_20d` comes from Alpaca's IEX feed, which is only a subset of the tape. Don't read those as real 30x to 50x volume days.

## Economic Data, Rates and the Fed

Today (USD high-impact only): nothing. `econ_calendar.today` is empty for 2026-11-12.

Tomorrow, Friday 2026-11-13, brings producer prices at 8:30 AM ET:

- **Core PPI m/m:** forecast 0.3%, previous 0.7%
- **PPI m/m:** forecast 0.4%, previous 1.3%

After this week's hot CPI story (yesterday's packet headlines), PPI is the next inflation read that matters for the Fed path. The packet has no 10Y or 3M reading today, so there's no rate level to anchor on.

## Coming Up

- **Tomorrow's events:** Core PPI m/m (forecast 0.3%, prev 0.7%) and PPI m/m (forecast 0.4%, prev 1.3%), both 8:30 AM ET.
- **Earnings:** `next_earnings_date` is null for every gapper, and the packet has no market-wide earnings calendar. Morningstar has "What to Watch in Nvidia Earnings: Huang's Future, Data Center Concerns Take Center Stage", but the packet gives no NVDA report date. Results already out, per the feed: Yeti, Aurora Mobile, FIS, Telefonica, Moderna, B&G Foods (BGS).

## Skips and Traps

- **CRWX, LWLX, AXTQ, AXTX, AXTC:** `catalyst_found: false`. No catalyst, skip. Market cap is null on all five.
- **CWVX, CRWG, CRWU, AXTU, NBIG:** the headlines are about the underlying stock (CoreWeave, AXT, Nebius) or about ETF launches, not about these tickers. Market cap is null because SEC has no CIK, which fits ETFs. Their 20-day average volume is tiny (CRWU 2,612, AXTU 1,051). Leveraged single-stock products are not what either setup was backtested on. Skip.
- **RETO** +65.95%: "Advances Brushless DC Water Pump Technology" on a $269M cap, alongside an 8-to-1 share consolidation and a "Halt News Pending" headline. A reverse split plus a halt is not a clean story. Skip.
- **SFWL** +43.88%: the only "catalysts" are generic "stocks moving" roundups. 20-day average volume is 27 shares. Market cap null. Skip.
- **BGS** +37.97%: a real beat ("Q3 Adj. EPS $0.21 Beats $0.15 Estimate, Sales $459.800M Beat $435.016M Estimate") and a raised sales guide. But it's a $298M cap, price 3.67 is under the 200-day SMA of 4.03, and the move looks like Wednesday's (price 3.67 vs prior close 3.65). Too small for either list. Watch only.
- **CIFR** +9.05%: Wednesday's surge, with Jefferies and Morgan Stanley both cutting targets ($10 and $27.5). Well under the 200-day SMA. Not eligible.
- **WULF** +6.7% and **IREN** +5.63%: Wednesday's AI-infra rally. WULF has at least four analyst target cuts in its headlines. IREN's top headline is "Voters Rejected Data Centers In 10 States, Raising Regulatory Risk". Both are under prior-day high and the 200-day SMA, and the Nvidia story hits this group first. Not eligible.
- **INTC** +7.57%: the headlines are driver and microcode updates plus "Shares Climb Nearly 4% After Key Trading Signal". That's not much of a catalyst for a $332B name. Under the 200-day SMA. Not eligible.
- **AMD** +7.32%: the best-looking name in the packet (William Blair upgrade, above its 200-day SMA, a rotation story off Nvidia). But it's under Wednesday's high and there's no premarket data. Not eligible. If it breaks 567.62 on real volume after 10:00, it's the one to have on the screen.
- **CORD, SMX:** gapping down, no long setups. SMX's list includes "SMX Announces Reverse Stock Split".

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
