# Premarket Report: November 24, 2026

*Single-brain pass: Claude only. Second brain not wired in yet.*

> Rules pick the watchlist. The AI judges the quality of the setups. This is not financial advice.

**Data warning: read this first.** The packet says "Scan run 2026-11-24 07:24 EST (premarket)." Same issue as the last few days: these aren't this morning's gaps. For nearly every name `price` is on or within a cent of `prior_close` (NVDA 165.185 vs 165.19, INTC 59.64 vs 59.64, AMD 453 vs 453.0, IREN 14.64 vs 14.64, SMCI 24.545 vs 24.55). So `gap_pct` is really Monday's close vs Friday's close. The index proxies agree: SPY's `prev_close` of 690.68 is the same number yesterday's report showed as Friday's SPY last. MarketWatch's "Nvidia's 31% stock surge" lines up with NVDA's +31.46%. Read every number below as Monday's session. The packet has no futures numbers for this morning, only headlines.

Yahoo rate-limited the scan again: 134 requests failed even after retries. Intraday data is `unavailable` for all 20 gappers, so VWAP, HOD, LOD, premarket high and premarket volume are null across the board. Per-ticker Yahoo news failed, so catalysts are Alpaca headlines plus RSS matches only, and none of them carry a published date. VIX, 10Y, 3M, WTI and the dollar are null. Index levels are ETF proxies (SPY, DIA, QQQ, IWM). `next_earnings_date` and `today_open` are null for all 20.

The SEC market cap fallback mismatched four names to "BANK OF MONTREAL /CAN/" this morning: TAWN ($7.51B), TPEI ($31.69B), AIQD ($43.44B) and BERZ ($17.77B). Don't trust those caps. Market cap is null for 4 more (ATHX, ANSS, NVDX, NVD).

## Summary

- **The tape in one line:** Monday was a big rip off Friday's crash. SPY +4.62%, QQQ +6.79%, IWM +3.52%, DIA +3.01%, led by NVDA +31.46% after "NVIDIA Reinstates Jensen Huang as President and CEO." This morning the follow-through is fading: "U.S. futures, European markets fade following Nvidia rally" (Washington Post). The packet has no futures numbers to size the fade.
- **The catch we're watching:** whether Monday was a real bottom or a one-man relief rally. MarketWatch asks "How much of the stock market should ride on one man?" and notes "Nvidia still has an investigation to finish." Every AI name that bounced Monday is still under its prior-day high and its 200-day SMA (AMD is the only one above its 200-day).
- **Two-brain verdict:** Single-brain run, no second opinion.

## Pre-Market Gappers

All 20 gappers in the packet. Gap % is `price` vs `prev_close` (mostly Monday's move, see the warning above). Market cap in parentheses. The headline is the first one the packet lists for each ticker.

- **ATHX** +19487.43% (cap null): no headline in the packet (`catalyst_found: false`)
- **BNAI** +117.86% ($56.0M): "Brand Engagement Network Reports Third Quarter 2026 Results"
- **OTLY** +109.08% ($9.06B): "Oatly Board Recommends Shareholders Not Tender Shares in Verlinvest Offer"
- **ANSS** -95.93% (cap null): no headline in the packet (`catalyst_found: false`)
- **NVDX** +63.13% (cap null): no headline in the packet (`catalyst_found: false`)
- **NVD** -63.06% (cap null): no headline in the packet (`catalyst_found: false`)
- **TAWN** +55.66% ($7.51B, mismatched to Bank of Montreal): "The bull and bear cases that could surprise investors next year, according to Bank of America"
- **TPEI** -54.22% ($31.69B, mismatched to Bank of Montreal): "The bull and bear cases that could surprise investors next year, according to Bank of America"
- **AIQD** -35.52% ($43.44B, mismatched to Bank of Montreal): "The bull and bear cases that could surprise investors next year, according to Bank of America"
- **NVDA** +31.46% ($3.98T): "NVIDIA Reinstates Jensen Huang as President and CEO"
- **BERZ** -28.48% ($17.77B, mismatched to Bank of Montreal): "The bull and bear cases that could surprise investors next year, according to Bank of America"
- **IREN** +23.86% ($5.23B): "Blue Owl Managed Funds Lead $2.4 Billion AI Factory Financing for IREN"
- **INTC** +16.1% ($316.99B): "BNP Paribas Adjusts Price Target on Intel to $60 From $70"
- **CIFR** +13.89% ($2.82B): "Cipher Digital Faces Regulatory Headwinds Following Potential Overseas Data-Center Penalties"
- **SMCI** +13.19% ($16.18B): "Supermicro and Other Server Manufacturers Reportedly Raising Prices on AI Servers Post-Contract"
- **WULF** +10.72% ($5.46B): "B. Riley Adjusts TeraWulf Price Target to $22"
- **SNDK** +10.36% ($12.44B): "Morgan Stanley Adjusts Price Target on Sandisk to $218 From $218.75"
- **NOK** +9.59% ($43.30B): "Nokia Places Additional Orders for AI Photonics Systems with Aixtron"
- **AAL** +6.8% ($8.43B): "American Airlines Retires International First-Class Cabin"
- **AMD** +6.76% ($742.96B): "Bernstein Initiates Coverage on AMD with Buy Rating"

## Day Trading Watchlist

The bar is Trend Join Long: gap > 3%, price > $3, market cap > $1B, premarket RVOL > 1.5, and price already breaking above yesterday's high.

No names cleared the day-trading bar today. Every gapper is `day_eligible: false`. The cap-qualified up-gappers (NVDA, OTLY, IREN, INTC, CIFR, SMCI, WULF, SNDK, NOK, AAL, AMD) are all sitting under their prior-day high. INTC is closest: 59.64 vs a prior high of 59.73. And with premarket high and HOD null for everyone, there are no live levels to build a plan off even if something had qualified.

## Swing Watchlist

The bar is: gap >= 8%, price > $3, open above yesterday's high, open above the 200-day SMA, market cap >= $800M, and a real catalyst (earnings on the gap day, or news with no earnings).

No names made the swing list today. Every gapper is `swing_eligible: false`. Same reason as the day list: no gapper's effective open is above its prior-day high. Most of the AI names are also far under their 200-day SMA. OTLY is the one interesting near-miss, covered in Skips and Traps.

## Market Trends of the Day

Monday was the mirror image of Friday. Friday was the AI unwind going vertical. Monday was the Huang relief rally. QQQ +6.79% vs DIA +3.01% says tech led both ways. The packet's headline is "NVIDIA Reinstates Jensen Huang as President and CEO," and MarketWatch puts a number on it: "Jensen Huang's return was worth nearly $950 billion to Nvidia." NVDA closed +31.46% on RVOL 72.1.

The whole AI complex bounced with it, on huge volume: IREN +23.86% (RVOL 41.46), INTC +16.1% (RVOL 32.99), CIFR +13.89% (RVOL 19.35), SMCI +13.19% (RVOL 33.33), WULF +10.72% (RVOL 18.43), SNDK +10.36% (RVOL 189.99), NOK +9.59% (RVOL 18.56), AMD +6.76% (RVOL 44.16). AMD lagged. Its headlines still include "Law Firms Announce Securities Investigations into Advanced Micro Devices, Inc." and the Hunterbrook China-ties report.

Retail drove a chunk of it. MarketWatch: "Retail investors who bought shares in the chip giant last week saw an average gain of 11% on Monday." Not everyone joined in. MarketWatch also flags "why Medicare Advantage insurers missed Monday's rally."

This morning the mood is cooler. The Washington Post has "U.S. futures, European markets fade following Nvidia rally." The bears are out too. Jim Mellon "warns the S&P 500 could fall by a third" and is "bearish on the AI sector and U.S. stocks generally." BofA's Hartnett says "stay risk off until global rate hikes start to dry up next spring."

Retail earnings are the other story this morning. "Best Buy reports comparable sales growth of 6.1%, highest in five years" (CNBC). "Dollar Tree Boosts Earnings Guidance as Discount Retail Meets Early Holiday Demand" (Barron's). "Disney Earnings Boosted by Strong Streaming and Parks Growth" (Morningstar). None of BBY, DLTR or DIS are in the gapper list, so the packet has no price on any of them.

Overseas: "Europe's earnings boom challenges Wall Street, but may prove fleeting" (Reuters), and "China wanted families to put savings in shares not homes" before "markets fell" (FT).

## Technical Signals for Today

ETF proxy levels from the scan vs each one's `prev_close` (this is Monday's session, not this morning's futures):

- SPY 722.56 (prev 690.68), +4.62%
- DIA 495.71 (prev 481.23), +3.01%
- QQQ 651.18 (prev 609.75), +6.79%
- IWM 265.75 (prev 256.72), +3.52%

Monday was a broad, tech-led rip, small caps included. VIX, 10Y, 3M, WTI and DXY are all null, so there's no volatility, rate, oil or dollar read.

Cap-qualified names vs prior-day high and the 200-day SMA (no VWAP or HOD today, intraday data was unavailable):

- NVDA 165.185: under its prior-day high of 171.47 and well under the 200-day SMA of 203.24. RVOL 72.1.
- AMD 453: under its prior-day high of 477.53, but back above the 200-day SMA of 430.99. RVOL 44.16. The only AI name above its 200-day.
- INTC 59.64: a hair under its prior-day high of 59.73, way under the 200-day SMA of 87.59. RVOL 32.99.
- IREN 14.64: under its prior-day high of 15.99, about a third of the 200-day SMA of 41.59. RVOL 41.46.
- SMCI 24.545: under its prior-day high of 26.37 and the 200-day SMA of 32.32. RVOL 33.33.
- CIFR 6.19: under its prior-day high of 6.82 and the 200-day SMA of 16.93. RVOL 19.35.
- WULF 10.895: under its prior-day high of 12.01 and the 200-day SMA of 17.92. RVOL 18.43.
- NOK 7.54: under its prior-day high of 7.71 and the 200-day SMA of 10.4. RVOL 18.56.
- AAL 12.73: under its prior-day high of 12.85 and just under the 200-day SMA of 13.43. RVOL 28.8.
- OTLY 14.5: under its prior-day high of 14.79, above the 200-day SMA of 11.07.
- SNDK 87.455: under its prior-day high of 99.0. The 200-day SMA of 1280.44 doesn't fit with the price. See Skips and Traps.

Every name closed Monday off its intraday high. That's a bounce that got sold into late, not a close at the highs.

On volume: daily bars are Alpaca IEX, a subset of the tape, and the volume figures look like a full Monday session against a 20-day average. Don't read those RVOL multiples literally.

## Economic Data, Rates and the Fed

From `econ_calendar` (USD, high impact only):

- **Today (Tuesday, November 24):** nothing high-impact listed.
- **Tomorrow (Wednesday, November 25):**
  - 8:30 AM ET, Core PCE Price Index m/m: forecast 0.3%, previous 0.3%.
  - 8:30 AM ET, Prelim GDP q/q: forecast 3.5%, previous 3.4%.

The calendar's `note` field is empty, so the packet doesn't flag a fetch problem. Today is clear, so the tape trades on AI headlines and retail earnings. Tomorrow morning is the real macro test: the Fed's preferred inflation gauge plus GDP at the same minute. No 10Y or 3M reading, so there's no rates read. The only rate-path color in the packet is Hartnett's "stay risk off until global rate hikes start to dry up next spring," which suggests hikes, not cuts, are the worry. The packet doesn't say what the Fed itself is planning.

## Coming Up

- **Tomorrow's events:** Core PCE m/m (forecast 0.3%, previous 0.3%) and Prelim GDP q/q (forecast 3.5%, previous 3.4%), both 8:30 AM ET.
- **Earnings:** Best Buy, Dollar Tree and Disney results are already out this morning per the headlines above. "Ollie's Bargain Outlet Holdings, Inc. Announces Third Quarter Fiscal 2026 Earnings Release Date and Conference Call Information," but the packet doesn't include the date. `next_earnings_date` is null for all 20 gappers, and the packet has no market-wide earnings calendar.

## Skips and Traps

- **OTLY** +109.08%: this is a buyout story. "Verlinvest Commences Technical Tender Offer for Oatly Group AB," and the board replied with "Oatly Board Recommends Shareholders Not Tender Shares in Verlinvest Offer." A real catalyst, but a tender offer pins the stock to a deal price, so there's not much trend left to ride. It's also under its prior-day high (14.5 vs 14.79), the SEC-derived $9.06B cap hasn't been cross-checked, and the 20-day average volume on the IEX feed is just 13,858. Skip.
- **BNAI** +117.86%: $56.0M cap, too small for either list. The headlines mix Q3 results with "Receives Nasdaq Non-Compliance Notification" and "Announces $1.05 Million Private Placement." A micro-cap with a listing notice and a raise. Skip.
- **TAWN**, **TPEI**, **AIQD**, **BERZ**: all four matched to "BANK OF MONTREAL /CAN/" by the SEC fallback, so the caps are wrong. All four got the same two headlines (a BofA outlook piece and a banker hiring story), which mentions none of them. That's an RSS false match, not a catalyst. TPEI's `prior_day_high`, `prior_close` and `sma_200` are all exactly 44.99 again, with 20-day average volume 0. TAWN's is 64. AIQD has no daily bars. Skip all four.
- **ATHX** +19487.43%: prev close 0.1 to 19.94, no daily bars, no name, no cap, no catalyst. That's a data artifact, not a gap. Skip.
- **ANSS** -95.93%: prev close 374.3 to 15.22, no daily bars, no name, no cap, no catalyst. The packet doesn't say why. Skip.
- **NVDX** +63.13% and **NVD** -63.06%: ticker-only rows with no name, no cap and no catalyst in the packet. Both prev closes (5.75 and 10.45) don't match their `prior_close` (9.37 and 3.92), so the gap math is off for these too. Skip.
- **SNDK** +10.36%: the numbers still don't fit. A 200-day SMA of 1280.44 against a price of 87.455, and RVOL 189.99. The headlines are mostly bad ("Weak NAND Flash Price Outlook," "Commerce Department Regulatory Update," "Kioxia Pricing Warning"). Under its prior-day high. Skip.
- **CIFR** +13.89%: up on a bad-news headline. The lead catalyst is "Cipher Digital Faces Regulatory Headwinds Following Potential Overseas Data-Center Penalties," and Morgan Stanley's target cut link reads "to-27-50-from-51-50." The bounce is the sector, not the news. Trap.
- **SMCI** +13.19%: "Supermicro Faces DOJ Investigation Over Alleged Smuggling to China" is in the headlines next to the server price-hike story. A probe hanging over a sector bounce. Under its prior-day high and 200-day. Skip.
- **NVDA** +31.46%: the biggest real story in the packet, but it's yesterday's move, and it closed under the prior-day high of 171.47 and way under the 200-day of 203.24. "NVIDIA Former CEO Jensen Huang Agrees to Senate Testimony" means there's still a headline event ahead. Watch it as the tell for the whole tape, not as a list name.
- **INTC** +16.1%: "Intel Secures First External Customer for 18A Chip Technology" is a real headline (the link reads "intel-shares-rise-pre-bell-on-signing-first-external-customer"), but the packet doesn't date it, and the lead headline is a price target cut from $70 to $60. Just under its prior-day high, well under its 200-day. Not on either list.
- **IREN**, **WULF**, **NOK**, **AAL**, **AMD**: all bounced with the tape and closed under their prior-day highs. Headlines are analyst notes, partnerships, executive changes, or older news. WULF still has "Lansing Town Board Votes to Ban AI Data Centers" hanging over it, and AMD still has the securities investigations. Nothing new here that explains the move besides the rally. Skip.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
