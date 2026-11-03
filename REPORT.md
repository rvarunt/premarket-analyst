# Premarket Report: November 03, 2026

*Single-brain pass: Claude only. Scan ran 06:12 ET, premarket.*

> Rules pick the watchlist. The AI judges the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** Tech is the weak spot. Index readings are ETF proxies: SPY (S&P 500) 752.04, -0.49%. QQQ (Nasdaq) 681.22, -1.35%. DIA (Dow) 519.29, +0.44%. IWM (Russell 2000) 279.20, -0.06%. Bloomberg: "US Stocks Drift as Midterms Keep Traders Cautious: Markets Wrap".
- **The catch we're watching:** AI worries. MarketWatch: "Nasdaq-100 tumbles into its third correction this year as AI worries mount". Reuters: "Global markets were already fragile. Big AI bets could break them".
- **Two-brain verdict:** Single brain, no second opinion to compare.

**Data gaps this scan:** VIX, 10-year, 3-month, WTI and the dollar index all came back null (Yahoo rate limited). Premarket levels (VWAP, premarket high, HOD, LOD) are null for every gapper, and `today_open` is null because the open hasn't printed yet. RVOL is null for all but the five large caps. No gapper has a next earnings date in the packet.

## Pre-Market Gappers

The packet has 20 gappers. Prices are the current gap price. Headlines are the first catalyst headline in the packet for each name, quoted as written.

- **CASK** +2856.7% (price $17.74, prev close $0.60, market cap $17.7M): "Heritage Distilling To Change Ticker Symbol To IPST Effective September 22, Reflecting Strategic Focus Toward IP Token Treasury Model"
- **VCIG** +168.4% ($8.16, market cap $214.7M): "VCI Global Announces 1-for-18 Reverse Stock Split, Effective November 2, 2026"
- **CLRO** +65.7% ($5.65, market cap $15.1M): "Dow Jumps Over 400 Points; Marriott Posts Upbeat Q3 Earnings"
- **LITZ** +38.0% ($35.79, market cap null): "Sandisk, Lumentum Rally Sparks Bearish Plays As Tradr Rolls Out 2X Short ETFs"
- **MF** +37.6% ($11.49, market cap $238.8M): "12 Information Technology Stocks Moving In Monday's Intraday Session"
- **DRUG** -52.4% ($26.20, market cap $118.5M): "FDA Setback Clouds Timeline For Bright Minds Biosciences' Pediatric Epilepsy Trials"
- **AIOK** -47.8% ($12.63, market cap null): "AI OKTO Shares Halted On Circuit Breaker To The Upside, Stock Now Up 227.53%"
- **SVRN** -39.7% ($17.78, market cap $133.4M): "SVRN Receives Nasdaq Delisting Determination"
- **LITG** -38.0% ($7.99, market cap null): no catalyst headline in the packet
- **LITU** -38.0% ($8.97, market cap null): "Lumentum, AST SpaceMobile Stocks Get Their 2X Funds As Traders Chase AI And Space Plays"
- **LITX** -37.5% ($14.55, market cap null): "Hot Stocks, Double Exposure: Tradr's 2X ETFs Target Sandisk, Western Digital And Lumentum"
- **XMAX** -37.5% ($4.01, market cap $258.7M): "XMax Enters 5-Yr AI Infrastructure Services Agreement With DSH HYPER For High-Performance Computing Capacity"
- **LITC** -37.5% ($12.985, market cap null): no catalyst headline in the packet
- **CMPS** -27.3% ($8.41, market cap $1.16B): "Compass Pathways to Announce Third Quarter 2026 Financial Results on November 3, 2026"
- **PGEN** -25.9% ($5.14, market cap $1.84B): "Precigen Shares Decline Following Approval of Rival RRP Treatment"
- **MRVL** -12.8% ($171.295, market cap $150.2B, RVOL 84.96): "B of A Securities Downgrades Marvell Technology to Neutral, Lowers Price Target to $225"
- **INTC** -8.9% ($59.955, market cap $318.7B, RVOL 61.87): "GF Securities Downgrades Intel Price Target Following Q4 Outlook"
- **ORCL** -8.9% ($119.115, market cap $360.2B, RVOL 53.64): "Oracle Announces $20 Billion Fundraising Plan for AI Cloud Expansion"
- **IREN** -8.1% ($22.035, market cap $7.87B, RVOL 26.59): "B. Riley Securities Maintains Buy on IREN, Lowers Price Target to $64"
- **CIFR** -5.8% ($6.865, market cap $3.13B, RVOL 22.05): "Keefe Bruyette Adjusts Price Target for Cipher Digital"

Almost all of this is a down tape. Only five names are gapping up and four of those are micro caps. The big names in the packet (MRVL, INTC, ORCL, IREN, CIFR) are all lower. The packet is long on stale or generic headlines, so read the catalyst column with that in mind.

## Day Trading Watchlist

No names cleared the day-trading bar today. That flag encodes the "Trend Join Long" rule: gap over 3%, price over $3, market cap over $1B, premarket RVOL over 1.5, and price already breaking above yesterday's high. `day_eligible` is false for all 20 gappers. The only upside gappers are micro caps under $1B or with no market cap, and the large caps are all gapping down.

## Swing Watchlist

No names cleared the swing bar either. That flag encodes: gap of 8% or more, price over $3, open above yesterday's high, open above the 200-day SMA, market cap of $800M or more, and a real catalyst. `swing_eligible` is false for all 20 gappers. Note that `today_open` is null premarket, so the scanner used the gap price as a stand-in.

## Market Trends of the Day

AI is the theme, and it's cutting the wrong way. Headlines in the packet:

- "Nasdaq-100 tumbles into its third correction this year as AI worries mount" (MarketWatch)
- "Apple and Palantir shares slide in premarket trading following post-bell earnings - CNBC"
- "Here’s why Palantir’s stock is down despite a ‘bombastic’ quarter" (MarketWatch)
- "Apple’s iPhone business is booming. Here’s why the stock is falling anyway." (MarketWatch)
- "Marvell and Lumentum shareholders unite in panning merger deal: ‘It’s a trash offer’" (MarketWatch)
- "Traders rushing into a leveraged ETF to make a bullish bet on the Nasdaq-100 just got burned" (MarketWatch)

The gapper list matches. MRVL, ORCL, INTC, IREN and CIFR are all red on huge relative volume. ORCL's catalyst is "Oracle Announces $20 Billion Fundraising Plan for AI Cloud Expansion". Money is leaving AI infrastructure names.

Outside tech, the packet shows "Bayer Shares Jump After Pharma Recovery Prompts Outlook Raise - WSJ" and "Samsung’s Chip Profit Drives Another Record Quarter - WSJ". MarketWatch has "Oil has had a massive run, but a prominent bull sees a turning point on midterm eve". Midterms have traders cautious.

## Technical Signals for Today

These are ETF proxies, not the index levels. Last price vs. prior close:

- SPY 752.04 vs 755.72 (-0.49%)
- QQQ 681.22 vs 690.54 (-1.35%)
- DIA 519.29 vs 517.00 (+0.44%)
- IWM 279.20 vs 279.37 (-0.06%)

The split is clear: Nasdaq proxy weak, Dow proxy up, small caps flat. VIX, yields, oil and the dollar are null, so there's no read on those. No breadth data in the packet.

## Economic Data, Rates and the Fed

Today (high impact, USD): Congressional Elections, 10:16 AM ET. No forecast or previous value in the packet. Nothing else high impact is listed. No rates or Fed data in the packet.

## Coming Up

- **Tomorrow's events:** No high-impact USD events in the calendar for 2026-11-04.
- **Earnings:** No `next_earnings_date` in the packet for any gapper. CMPS has the headline "Compass Pathways to Announce Third Quarter 2026 Financial Results on November 3, 2026", which is today. The packet has no timing. INTC's catalysts include an AMD Q3 earnings preview for Tuesday, but AMD isn't a gapper in the packet.

## Skips and Traps

None of these are on a watchlist, but here is why the tempting ones are skips.

- **CASK** (+2856.7%): market cap $17.7M. The headlines are about a ticker change and a token treasury, and some are dated well before today. Price $17.74 is below the 200-day SMA of $18.23. Skip.
- **VCIG** (+168.4%): market cap $214.7M. The catalyst is "VCI Global Announces 1-for-18 Reverse Stock Split, Effective November 2, 2026". A reverse split is not a catalyst, and a gap this size is likely split math. Skip.
- **CLRO** (+65.7%): market cap $15.1M. Headlines are generic market wraps, not about the company. Skip.
- **MF** (+37.6%): market cap $238.8M. Headlines are generic "12 Information Technology Stocks Moving" lists. Skip.
- **LITZ** (+38.0%): no market cap, headline is about leveraged ETF launches. Skip. **LITG, LITU, LITX, LITC** are the same family: no market cap, and LITG and LITC have no catalyst at all. Skip.
- **SVRN** (-39.7%): "SVRN Receives Nasdaq Delisting Determination". Avoid.
- **AIOK** (-47.8%): the headlines are about a halt on the upside at +227.53% and a CEO buying 130,000 shares at $8.15. Price is $12.63 and market cap is null. Messy and unclear. Skip.
- **DRUG** (-52.4%): "FDA Setback Clouds Timeline For Bright Minds Biosciences' Pediatric Epilepsy Trials". Bad news and a micro cap. Skip.
- **XMAX** (-37.5%): market cap $258.7M. The AI infrastructure deal headline is the catalyst, yet the stock is down. Skip.
- **CMPS** (-27.3%) and **PGEN** (-25.9%): both gapping down, with an earnings date today for CMPS and a rival's approval for PGEN. No longs.
- **MRVL, INTC, ORCL, IREN, CIFR**: all gapping down on heavy volume. The packet has no long setup in any of them. MRVL has a downgrade to Neutral, ORCL is raising $20 billion, and CIFR's headline reads "Cipher Digital's Revenue Plunges, but Its AI Data Center Ambitions Are Growing". No trades from the packet.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
