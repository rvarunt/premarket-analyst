# Premarket Report: November 20, 2026

*Single-brain pass: Claude only. Second brain not wired in yet.*

> Rules pick the watchlist. The AI judges the quality of the setups. This is not financial advice.

**Data warning: read this first.** The packet says "Scan run 2026-11-20 07:05 EST (premarket)." Same problem as the last four mornings: most gaps aren't this morning's gaps. For most names `price` sits on or within a few cents of `prior_close` (INSM 144.46 vs 144.46, AMD 489.44 vs 489.44, SOXS 63.2 vs 63.2, SA 18.06 vs 18.08, SNEX 39.45 vs 39.41, LQDT 33.03 vs 32.99), so `gap_pct` is really Thursday's close vs Wednesday's close. The index proxies line up with that: SPY's `prev_close` of 730.33 is exactly what yesterday's report showed as SPY's last. So read the numbers below as Thursday's session. The packet has no futures numbers for this morning.

Yahoo rate-limited the scan again: 91 requests failed even after retries. Intraday data is `unavailable` for all 20 gappers, so VWAP, HOD, LOD, premarket high and premarket volume are null across the board. Per-ticker Yahoo news failed, so catalysts are Alpaca headlines plus RSS matches only. VIX, 10Y, 3M, WTI and the dollar are null. Market cap is null for 6 of 20 gappers (MACIU, POAS, IPFXU, ZOAR, PDDL, SOXS). `next_earnings_date` is null for all 20. `today_open` is null for all 20 (it's premarket). Index levels are ETF proxies (SPY, DIA, QQQ, IWM), not the indices themselves.

## Summary

- **The tape in one line:** Thursday was a broad flush. SPY -1.98%, DIA -2.18%, QQQ -2.19%, IWM -2.2%, and MarketWatch says all four major indexes are "on pace for their worst week since President Trump’s “liberation day” tariffs of April 2025." The Anthropic IPO popped and didn't help: "Global stock markets slump as Anthropic IPO fails to stem AI sell-off" (The Guardian).
- **The catch we're watching:** whether the AI unwind keeps feeding on itself. "Stocks Hit Worst Run Since 2023 as AI Trade Cracks" (Bloomberg), "The post earnings slide in Nvidia stock is getting uglier by the day" (Yahoo Finance), and Citi says "a key stock-market signal is close to flashing red." A seventh straight down day for the S&P is the risk. MarketWatch's six-session-streak history piece is the bull case.
- **Two-brain verdict:** Single-brain run, no second opinion.

## Pre-Market Gappers

All 20 gappers in the packet. Gap % is `price` vs `prev_close` (mostly Thursday's move, see the warning above). Market cap in parentheses. The headline is the first one the packet lists for each ticker.

- **FVNNU** +84.27% ($398.9M): no headline in the packet (`catalyst_found: false`)
- **MPU** +67.61% ($164.4M): "Mega Matrix Inc. Announces Share Consolidation of Class A Ordinary Shares"
- **MACIU** +43.2% (cap null): no headline in the packet (`catalyst_found: false`)
- **BKHAU** -41.71% ($47.1M): "Farm fresh: Farmers markets around Athens - The Red & Black"
- **POAS** +36.64% (cap null): "Phaos Technology Holdings (Cayman) Limited Responds to Unusual Market Activity"
- **IPFXU** +35.86% (cap null): no headline in the packet (`catalyst_found: false`)
- **ZOAR** -31.77% (cap null): "Zoar Limited Completes Business Combination with Impact Biomedical Inc."
- **SA** -29.32% ($1.66B): no headline in the packet (`catalyst_found: false`)
- **SNEX** -26.71% ($4.76B): "StoneX Group Inc. Reports Fiscal 2026 Fourth Quarter and Full Year Financial Results"
- **FISN** +25.83% ($200.9M): "ThinkEquity Initiates Coverage of Deep Fission, Inc. with Buy Rating"
- **SAIH** -25.24% ($245.0M): "SAIHEAT Limited (SAIH) Subject to Trading Halt"
- **LQDT** -24.88% ($1.04B): "Liquidity Services Announces Fiscal Year 2026 Financial Results"
- **BKHA** -24.74% ($26.9M): "Black Hawk Acquisition Extends Deadline for Business Combination"
- **UVIX** +24.22% ($561.0M): no headline in the packet (`catalyst_found: false`)
- **PDDL** +22.21% (cap null): no headline in the packet (`catalyst_found: false`)
- **INSM** +20.58% ($31.69B): "Sanofi Reportedly Considering Acquisition of Insmed"
- **SOXS** +8.39% (cap null): no headline in the packet (`catalyst_found: false`)
- **AMD** -7.73% ($802.72B): "Advanced Micro Devices Shares Decline Following Hunterbrook Media Report on China Ties"
- **IREN** -5.39% ($5.15B): "Blue Owl Managed Funds Lead $2.4 Billion AI Factory Financing for IREN"
- **SOFI** -4.08% ($17.55B): "SoFi Releases National Report on Cryptocurrency Trends"

## Day Trading Watchlist

The bar is Trend Join Long: gap > 3%, price > $3, market cap > $1B, premarket RVOL > 1.5, and price already breaking above yesterday's high.

No names cleared the day-trading bar today. Every gapper is `day_eligible: false`. Only one up-mover has a cap over $1B: INSM ($31.69B, +20.58%). Its RVOL is null, and its price of 144.46 is under its prior-day high of 149.07. Every other gapper with a known cap over $1B (SA, SNEX, LQDT, AMD, IREN, SOFI) is gapping down. With premarket high and HOD null for everyone, there are no live levels to build a plan off even if something had qualified.

## Swing Watchlist

The bar is: gap >= 8%, price > $3, open above yesterday's high, open above the 200-day SMA, market cap >= $800M, and a real catalyst (earnings on the gap day, or news with no earnings).

No names made the swing list today. Every gapper is `swing_eligible: false`.

The near miss is INSM, and it's worth knowing why it missed. It's up 20.58%, has a $31.69B cap, sits above its 200-day SMA (144.46 vs 122.6), and has a real catalyst: "Sanofi Reportedly Considering Acquisition of Insmed" (via MarketScreener). It fails on one check: the scanner's stand-in open (144.46) is under yesterday's high of 149.07. That means it faded off the high on the rumor day. It's a buyout rumor, not a confirmed deal, so the move can fully reverse on a denial. If it opens above 149.07, it's a name to watch and build a plan on. Swing management isn't built yet either way.

## Market Trends of the Day

This is an AI-unwind tape, and it's global. "Asia’s stock markets dive as Anthropic debut fails to allay AI bubble fears" (Al Jazeera). "Stocks Hit Worst Run Since 2023 as AI Trade Cracks" (Bloomberg). Reuters has "Taiwan stock exchange says it will ensure stable operation of capital markets," and you don't publish that on a calm day. Reuters also has "India's AI-free appeal draws record foreign buying": money is hunting for markets that don't depend on the AI trade.

Anthropic is the headline irony. MarketWatch has "Anthropic’s stock surges in its debut" but "the rest of the market dives anyway," and a separate piece says it "has so far failed to provide a broad lift to the technology sector." SOFI shows up in the packet as a "Broker-Dealer for Anthropic IPO" and still fell 4.08%.

Nvidia is still the center of it. "The post earnings slide in Nvidia stock is getting uglier by the day" (Yahoo Finance), and WSJ has "Nvidia’s Finance Chief Kress to Lead First Earnings Call Following Huang’s Ouster." In the gapper list, AMD fell 7.73% on a 65.2 RVOL, with "Advanced Micro Devices Shares Decline Following Hunterbrook Media Report on China Ties" as its top headline. IREN fell 5.39% even with "Blue Owl Managed Funds Lead $2.4 Billion AI Factory Financing for IREN" on the tape. Good news isn't getting bought in this group right now. SOXS was up 8.39% on a 69.82 RVOL. The packet has no name or cap for it, so it can't confirm what it tracks.

Earnings aren't saving anyone either: "Intuit Earnings Beat Isn’t Enough to Boost the Stock" (Barron's). SNEX (-26.71%) and LQDT (-24.88%) both dropped hard right after reporting. The packet has the release headlines but not the numbers, so it can't tell you whether they missed.

The one green shoot in the feed: "Shares of Apple climbed in premarket trading" after job postings for engineers to build an agentic AI system (MarketWatch). That's the only premarket direction in the packet.

On positioning, Citi "turned risk averse more than a month ago" and says if sentiment gets worse, "buying long-duration bonds is the answer." The packet has no 10Y reading, so there's no way to check whether bonds are catching a bid.

Gold miners took another hit: SA fell 29.32% with no catalyst in the packet. Yesterday's report had GDX and B2Gold down the same way. The packet has no gold price and no GDX row today, so the why isn't here.

## Technical Signals for Today

ETF proxy levels from the scan vs each one's `prev_close` (this is Thursday's session, not this morning's futures):

- SPY 715.84 (prev 730.33), -1.98%
- DIA 490.75 (prev 501.7), -2.18%
- QQQ 645.1 (prev 659.57), -2.19%
- IWM 264.21 (prev 270.14), -2.2%

Wednesday was a split tape. Thursday was everything down about 2%, with small caps, tech and the Dow all moving together. That's de-risking, not rotation. MarketWatch frames it as a six-session S&P losing streak. VIX, 10Y, 3M, WTI and DXY are all null, so there's no volatility, rate, oil or dollar read. UVIX ("VS Trust" in the packet) was up 24.22%, but with no VIX row there's nothing to check it against.

Cap-qualified and high-volume names vs prior-day high and the 200-day SMA (no VWAP or HOD today, intraday data was unavailable):

- INSM 144.46: under its prior-day high of 149.07, above the 200-day SMA of 122.6. RVOL null. The only cap-qualified gapper that's up and above its 200-day.
- AMD 489.44: well under its prior-day high of 554.99, still above the 200-day SMA of 428.61. RVOL 65.2.
- IREN 14.4: under its prior-day high of 16.66, about a third of the 200-day SMA of 41.87. RVOL 44.34.
- SOFI 13.52: under its prior-day high of 14.37 and the 200-day SMA of 17.17. RVOL 24.11.
- SNEX 39.45: under its prior-day high of 49.52, well under half the 200-day SMA of 91.37. RVOL null.
- LQDT 33.03: under its prior-day high of 38.52 and the 200-day SMA of 37.83. RVOL null.
- SA 18.06: under its prior-day high of 22.3 and the 200-day SMA of 29.41. RVOL null.

On volume: daily bars are Alpaca IEX, a subset of the tape, and the volume figures look like a full Thursday session against a 20-day average. Don't read those RVOL multiples literally. RVOL is null for everything except SOXS, AMD, IREN and SOFI.

## Economic Data, Rates and the Fed

From `econ_calendar` (USD, high impact only):

- **Today (Friday, November 20):** nothing high-impact listed.
- **Tomorrow (Saturday, November 21):** nothing high-impact listed.

The calendar's `note` field is empty, so the packet doesn't flag a fetch problem. It just lists zero events. The packet has nothing on Fed speakers and no 10Y or 3M reading, so there's no rates read going into today. No data on the calendar means the tape trades on AI and sentiment headlines today, not on macro releases.

## Coming Up

- **Tomorrow's events:** Saturday. No high-impact USD releases in the calendar.
- **Earnings:** `next_earnings_date` is null for all 20 gappers, and the packet has no market-wide earnings calendar. From the feed: WSJ says Nvidia's "Finance Chief Kress to Lead First Earnings Call Following Huang’s Ouster," but the packet gives no date for that call. Intuit, Lowe's, StoneX and Liquidity Services have already reported.

## Skips and Traps

- **INSM** +20.58%: not a trap, just not a list name. The catalyst is a "Reportedly Considering" buyout rumor, and price sits under the prior-day high of 149.07. See the Swing section. Watch it, don't chase it.
- **FVNNU** +84.27%: `catalyst_found: false`, 20-day average volume of 0, and the packet's numbers don't agree with each other (price 70.3, `prev_close` 38.15, `prior_close` 19.9, 200-day SMA 12.33). That's broken data on a SPAC unit, not a gap. Ignore it.
- **MPU** +67.61%: up on "Announces Share Consolidation of Class A Ordinary Shares." That's a reverse split, and a 200-day SMA of 1.01 against a 4.76 price says the history probably mixes pre- and post-split prices. $164.4M cap, 20-day average volume 2,049. Trap.
- **POAS** +36.64%: cap null. The headlines are "Responds to Unusual Market Activity," "Issues Going Concern Disclosure," and an equity facility of up to $10 million (per the link). A going-concern micro-cap issuing an unusual-activity response is a pump warning, not a catalyst. Trap.
- **FISN** +25.83%: "ThinkEquity Initiates Coverage of Deep Fission, Inc. with Buy Rating" is real news, but the Q3 results link in the packet reads "development spending surged but current liquidity falls short of the funding runway needed." $200.9M cap, under the 200-day SMA (3.41 vs 6.98). Under both cap bars. Skip.
- **MACIU** +43.2%, **IPFXU** +35.86%, **PDDL** +22.21%, **UVIX** +24.22%, **SOXS** +8.39%: `catalyst_found: false`. No catalyst found, so no trade. MACIU's 20-day average volume is 5 shares, IPFXU's is 11, and PDDL's is 157.
- **AMD** -7.73%: "Advanced Micro Devices Shares Decline Following Hunterbrook Media Report on China Ties," plus "AMD Insider Executes Significant Share Sale." A short-seller-style report and insider selling, on a gap-down. Not a long. Skip.
- **SNEX** -26.71% and **LQDT** -24.88%: both dropped right after earnings ("Reports Fiscal 2026 Fourth Quarter and Full Year Financial Results," "Announces Fiscal Year 2026 Financial Results"). The packet doesn't say what disappointed. Gap-downs, both under their 200-day SMAs. Skip.
- **SA** -29.32%: $1.66B cap, `catalyst_found: false`, well under the 200-day SMA. Gap-down with no story. Skip.
- **SAIH** -25.24%: "Subject to Trading Halt," "Executes 1-for-15 Reverse Stock Split," and "Files $300 Million Mixed Shelf Registration" next to a merger with Canopy Wave. 20-day average volume 140. Skip.
- **BKHAU** -41.71%: `catalyst_found: true` is a false match. Both headlines are unrelated RSS hits ("Farm fresh: Farmers markets around Athens," a Black Friday stock list). The real driver isn't in the packet. 20-day average volume is 5. Skip.
- **BKHA** -24.74%: "Black Hawk Acquisition Extends Deadline for Business Combination." $26.9M SPAC. Skip.
- **ZOAR** -31.77%: "Completes Business Combination with Impact Biomedical Inc." and a name and ticker change. No daily bars, no cap, no 200-day SMA. Skip.
- **IREN** -5.39% and **SOFI** -4.08%: real news on both (the Blue Owl financing, the Anthropic IPO broker-dealer role), but both gapped down on it and sit far under their 200-day SMAs. Skip.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
