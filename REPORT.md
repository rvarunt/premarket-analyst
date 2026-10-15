# Premarket Report: October 15, 2026

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** Risk-off. Using ETF proxies at scan time (07:20 ET), SPY is -1.08%, QQQ -1.97%, IWM -1.91%, DIA -0.08%. Tech is getting hit hardest.
- **The catch we're watching:** Hot inflation plus AI funding worries. Headlines in the packet say chipmakers are being hammered, CoreWeave's bonds fell to 81 cents on the dollar, and today's PPI and Retail Sales prints land at 8:30 AM ET.
- **Two-brain verdict:** Single brain, no second opinion to compare.

## Pre-Market Gappers

20 gappers in the packet (Alpaca screener). Premarket levels (VWAP, HOD, LOD, premarket high, premarket volume) came back null for every name, and yfinance was rate-limited for much of the enrichment, so treat the data as thin. Where a ticker had several headlines, the most relevant one is quoted in full.

- **MGOL** +3838.8% (price 14.57 vs prev close 0.37, market cap $42.3M): "MGO Global's Stockholders Approve Business Combination With Heidmar". That gap is wildly out of scale. I can't verify from the packet whether it's a split or bad data, so don't trust it.
- **GLND** +76.5%: "Greenland Energy Responds To Short-Seller Report, Defending Its Exploration Strategy, Finances And 13B-Barrel Potential; Says "GLND Is An Exploration-Stage Oil And Gas Company Focused On The Development And Advancement Of Its Exploration Activities In Greenland. We Currently Have No Earnings, No Production And No Proved Reserves. Our First Well Has Not Been Drilled. We Said All Of This Ourselves In Our Prospectus And Our 10-Q, In Plainer Language Than Fugazi Uses.""
- **RPGL** -65.2%: no company-specific headline, only "12 Information Technology Stocks Moving In Wednesday's After-Market Session"
- **BSP** +41.2%: "Berkshire Hathaway Doubles Down on Bending Spoons with $330 Million Investment, Sending Shares Soaring 45%"
- **BKHA** -38.0%: "Black Hawk Acquisition Shareholders Approve Its Proposed Business Combination With Vesicor Therapeutics"
- **NXGL** +34.8%: "NEXGEL Announces 1-For-20 Reverse Stock Split, Effective Immediately"
- **AEHL** +34.4%: "Antelope Enterprise Shares Halted On Circuit Breaker To The Downside, Stock Now Up 45.96%"
- **LQDA** +26.6%: "HC Wainwright & Co. Maintains Buy on Liquidia, Raises Price Target to $65"
- **SKYD** -23.8%: "Skydance Stock Closes Down Nearly 24% Despite Warrant Clarification"
- **WULF** -12.8%: "Morgan Stanley Maintains Overweight on TeraWulf, Raises Price Target to $65"
- **CIFR** -12.5%: "Cipher Digital Prices $850M Offering Of Senior Notes Due 2032"
- **IREN** -12.3%: "IREN Stock Tanks: What's Going On?"
- **ORCL** -8.9%: "Oracle Stock Tumbles: What's Going On?"
- **MMED** -8.8%: "Medtronic Announces Oversubscribed MiniMed Exchange Offer Results; Accepts 55,032,401 Of Its Shares For All Remaining 252,813,348 MiniMed Shares"
- **ONDS** -8.4%: "Ondas Says European Aviation Regulator Certified Its Missile Protection System On Bombardier Global 7500 Jet"
- **SOFI** -6.5%: "SoFi Stock Falls Toward Its 52-Week Low as BofA Miss Weighs on Banking Stocks"
- **AAL** -5.7%: "American Airlines Cut 3 Destinations. What Does It Save Before Earnings?"
- **BAC** -4.7%: "Baird Upgrades Bank of America to Outperform, Maintains Price Target to $62"
- **NOK** -4.7%: "Nokia to Offload Private Wireless Business As It Sharpens Strategic Focus"
- **INTC** -4.6%: "SK Hynix Stock Plunges 11% in Seoul, Slips After Hours in New York as Hot CPI, Fed Hike Bets and AI Funding Worries Weigh"

## Day Trading Watchlist

No names cleared the day-trading bar today. That flag encodes a gap over 3%, price over $3, market cap over $1B, premarket RVOL over 1.5, and price already breaking above yesterday's high. Every gapper came back `day_eligible: false`.

## Swing Watchlist

No names cleared the swing bar either. That flag encodes a gap of 8% or more, price over $3, open above yesterday's high, open above the 200-day SMA, market cap of $800M or more, and a real catalyst. Every gapper came back `swing_eligible: false`. Note the actual open hasn't printed yet at scan time, so the scanner used the current gap price as a stand-in.

## Market Trends of the Day

It's a tech and AI sell-off. Headlines in the packet: "The AI trade is splintering as inflation fears rattle hyped-up tech stocks," "Tech sell-off gathers pace as chipmakers hammered" (Reuters), and "Global stocks sell-off deepens as chipmakers tumble" (Financial Times). MarketWatch has "CoreWeave's AI bonds tumble, raising red flags for the wider market" and "Why the AI trade is not set up for a rebound like July's, according to JPMorgan."

The gapper list matches. Most of the cap-qualified names are down: the AI and bitcoin-miner/neocloud group (WULF, CIFR, IREN), plus ORCL, INTC and SOFI. Banks are weak too, with BAC down 4.7% and a headline pointing to its Q3 results.

One bright spot is TSMC. The packet has "TSMC's CEO sees no sign of a slowdown as chip foundry reports record profit," but another headline says the stock fell anyway after the blowout earnings.

## Technical Signals for Today

Index levels below are ETF proxies (SPY, DIA, QQQ, IWM), not the actual indices. The prices are ETF prices.

- S&P 500 proxy (SPY): 769.65, -1.08%
- Dow proxy (DIA): 515.65, -0.08%
- Nasdaq proxy (QQQ): 728.99, -1.97%
- Russell 2000 proxy (IWM): 271.39, -1.91%

VIX, 10-year yield, 3-month yield, WTI crude and the dollar index all came back null (yfinance failed). No breadth data in the packet. One headline cites "479 Stocks Hit 52-Week Lows on Wednesday, While Only 60 Set Highs."

## Economic Data, Rates and the Fed

Today (USD high impact), with forecast and previous:

- 8:30 AM ET: Core PPI m/m, forecast 0.3%, previous 0.2%
- 8:30 AM ET: Core Retail Sales m/m, forecast 0.6%, previous 1.4%
- 8:30 AM ET: PPI m/m, forecast 0.6%, previous 0.4%
- 8:30 AM ET: Retail Sales m/m, forecast 0.3%, previous 1.2%
- 11:30 PM ET: Fed Chairman Warsh Speaks (time as listed in the calendar)

The actual results aren't in the packet. With inflation worries already driving the tape ("Hot CPI, Fed Hike Bets" shows up in a headline), a hot PPI on top of the forecast 0.6% is the risk. The packet doesn't say more about the Fed path than that.

## Coming Up

- **Tomorrow's events:** None in the calendar for Friday, October 16.
- **Earnings:** No `next_earnings_date` was populated for any gapper (enrichment calls were rate-limited). AAL has a headline saying "before earnings," but no date is in the packet.

## Skips and Traps

All 20 gappers get skipped, since none cleared either rules flag. Notes on the ones worth a warning:

- **MGOL:** The +3838% gap is almost certainly not a real tradable move as shown. Market cap $42M, premarket data null. Skip.
- **GLND:** Up 76% with a headline that is a response to a short-seller report. That's not a clean catalyst. Market cap $170M, below the bar. Skip.
- **CIFR:** Down on an $850M senior notes offering. Financing overhang, no long.
- **RPGL, BKHA, NXGL, AEHL:** Micro-cap or unknown cap, and the headlines are a SPAC deal vote, a reverse split and a circuit-breaker halt. Reverse-split and halt names are classic traps. Skip.
- **RPGL and BSP:** Market cap unavailable from any source, so flags are false by default.
- **LQDA:** Up 26.6% on analyst price-target moves, but it's sitting below its 200-day SMA (33.94 vs 53.92) and below yesterday's high (38.58). Not eligible.
- **Down names (SKYD, WULF, IREN, ORCL, MMED, ONDS, SOFI, AAL, BAC, NOK, INTC):** The rules only build long watchlists. The gap-down moves are macro driven in most cases, and the packet doesn't give a setup for any of them.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
