# Premarket Report: November 19, 2026

*Single-brain pass: Claude only. Second brain not wired in yet.*

> Rules pick the watchlist. The AI judges the quality of the setups. This is not financial advice.

**Data warning: read this first.** The packet says "Scan run 2026-11-19 06:07 EST (premarket)." Same story as the last three mornings: most gaps aren't this morning's gaps. For most names `price` sits on or within a few cents of `prior_close` (SKYA 4.13 vs 4.13, GDX 74.83 vs 74.83, BTG 4.485 vs 4.49, CRWV 47.845 vs 47.84, NUAI 3.99 vs 3.98), so `gap_pct` is Wednesday's close vs Tuesday's close. The index proxies match: SPY's `prev_close` of 732.41 is exactly what yesterday's report showed as SPY's last. So read the numbers below as Wednesday's session. The packet has no futures numbers for this morning.

Yahoo rate-limited the scan again: 74 requests failed even after retries. Intraday data is `unavailable` for all 18 gappers, so VWAP, HOD, LOD, premarket high and premarket volume are null across the board. Per-ticker Yahoo news failed, so catalysts are Alpaca headlines only. VIX, 10Y, 3M, WTI and the dollar are null. Market cap is null for 10 of 18 gappers (SDC, HY, RMIX, OKTG, MSTZ, NVD, GDX, NVDL, PATH, CRWV). `next_earnings_date` is null for all 18. Index levels are ETF proxies (SPY, DIA, QQQ, IWM), not the indices.

## Summary

- **The tape in one line:** the proxies show a split Wednesday: DIA -1.12% and SPY -0.28%, while QQQ +0.38% and IWM +0.44% held green. Overnight the feed is earnings: "Palo Alto Networks Stock Rises After Earnings Beat" (Barron's) and "Alibaba Earnings Rebound Sharply as AI Profitability Improves" (WSJ).
- **The catch we're watching:** "Walmart is set to report earnings before the bell" (CNBC). It's the one scheduled catalyst in the packet that lands before the open, and the Dow proxy was already the weakest of the four.
- **Two-brain verdict:** Single-brain run, no second opinion.

## Pre-Market Gappers

All 18 gappers in the packet. Gap % is `price` vs `prev_close` (mostly Wednesday's move, see the warning above). Market cap in parentheses. Headline is the first one the packet lists for each ticker.

- **SDC** +33144.4% (cap null) : no headline in the packet (`catalyst_found: false`)
- **SKYA** +90.32% ($210.0M) : "SkyAI, Inc. Announces Final Results of Cash Tender Offer"
- **CUE** +68.2% ($39.8M) : "B. Riley Cuts Price Target on Cue Biopharma to $25 From $83"
- **CLRO** +46.19% ($18.5M) : no headline in the packet (`catalyst_found: false`)
- **HY** -41.07% (cap null) : "Hyster-Yale Announces Proposed $125 Million Convertible Senior Notes Offering"
- **PRE** -36.62% ($174.6M) : "Prenetics Reports Q3 2026 Financial Results and Reaffirms Guidance"
- **NCT** -34.26% ($176.6M) : "Intercont (Cayman) Limited Announces 8-for-1 Reverse Share Split"
- **RIBBU** +31.25% ($264.2M) : no headline in the packet (`catalyst_found: false`)
- **NUAI** +24.69% ($560.9M) : "Roth Capital Raises Price Target for New Era Energy & Digital"
- **RMIX** +24.46% (cap null) : "Linden Capital L.P. Files Schedule 13G for Haymaker Acquisition Corp. 4"
- **OKTG** +24.09% (cap null) : no headline in the packet (`catalyst_found: false`)
- **MSTZ** +12.74% (cap null) : no headline in the packet (`catalyst_found: false`)
- **BTG** -6.17% ($6.01B) : "BTG Consulting PLC Releases Q3 2026 Red Flag Alert Research"
- **NVD** +6.06% (cap null) : no headline in the packet (`catalyst_found: false`)
- **GDX** -5.92% (cap null) : no headline in the packet (`catalyst_found: false`)
- **NVDL** -5.87% (cap null) : no headline in the packet (`catalyst_found: false`)
- **PATH** -5.33% (cap null) : "UiPath Releases 'The Context Gap' Research on Decision-Making Costs"
- **CRWV** -4.16% (cap null) : "Nvidia Discloses CoreWeave's Adoption of Vera CPU and Updates Financing Commitments"

## Day Trading Watchlist

The bar is Trend Join Long: gap > 3%, price > $3, market cap > $1B, premarket RVOL > 1.5, and price already breaking above yesterday's high.

No names cleared the day-trading bar today. Every gapper is `day_eligible: false`. Only one gapper has a known cap over $1B: BTG ($6.01B), and it's gapping down 6.17%. Every up-mover is either under $1B or has a null cap. With premarket high and HOD null for everyone, there are no live levels to build a plan off even if something had qualified.

## Swing Watchlist

The bar is: gap >= 8%, price > $3, open above yesterday's high, open above the 200-day SMA, market cap >= $800M, and a real catalyst (earnings on the gap day, or news with no earnings).

No names made the swing list today. Every gapper is `swing_eligible: false`. Nothing up 8% or more has a known cap of $800M or higher. The biggest known cap among the up-movers is NUAI at $560.9M, and it's under its 200-day SMA (3.99 vs 4.76) anyway.

## Market Trends of the Day

It's an earnings morning, and the AI trade is still the frame. Palo Alto is the clean beat: "Palo Alto Networks’ stock gets a fresh AI-fueled boost from earnings" (MarketWatch), with the company boosting its outlook on the "current threat environment and demand we see ahead of us." Barron's has it rising after the beat.

Alibaba is the two-sided one. WSJ says "Alibaba Earnings Rebound Sharply as AI Profitability Improves," but Barron's frames AI as both the stock's best hope and its biggest danger, and Yahoo ran "Why Is Alibaba Stock Crashing Before Earnings?" Up next is Walmart before the bell.

On sentiment, the tone is nervous. MarketWatch's top feed has "This closely-watched guru just sold everything" (Panmure Liberum's Joachim Klement), and a reader question leading with "Nvidia’s turmoil has me spooked." On the other side: "Anthropic Shares Indicated More Than 20% Higher on Gray Markets" (Yahoo Finance).

Wednesday's tape on the proxies was a rotation day, not a risk-off day. DIA took the hit (-1.12%) while QQQ and IWM finished up. Gold miners went the other way from tech: GDX -5.92% and B2Gold (BTG) -6.17%, both on huge volume (RVOL 27.63 and 23.74). The packet has no gold price, so it can't tell you why.

In the AI names that did show up, CRWV fell 4.16% on a 41.42 RVOL, with "Nvidia Discloses CoreWeave's Adoption of Vera CPU and Updates Financing Commitments" as its top headline. NVDL and NVD moved in opposite directions (-5.87% and +6.06%). The packet has no name or cap for either, so you can't confirm what they track from the packet alone.

Overseas, StoneX has "RBA Unemployment Forecasts Miss and Markets Swap Hikes for Cuts." None of today's gappers connect to it.

## Technical Signals for Today

ETF proxy levels from the scan, vs each one's `prev_close` (this is Wednesday's session, not this morning's futures):

- SPY 730.33 (prev 732.41), -0.28%
- DIA 501.7 (prev 507.37), -1.12%
- QQQ 659.57 (prev 657.06), +0.38%
- IWM 270.14 (prev 268.96), +0.44%

SPY slipped again, but only -0.28%, and QQQ and IWM finished green. DIA did the damage. Yesterday's report flagged that MarketWatch had the S&P 500 under its 200-day moving average. The packet has no 200-day level for SPY, so you can't check whether it got back over. VIX, 10Y, 3M, WTI and DXY are all null: no volatility, rate, oil or dollar read.

Cap-qualified and high-volume names vs prior-day high and the 200-day SMA (no VWAP or HOD today, intraday data was unavailable):

- BTG 4.485, under its prior-day high of 4.6 and just under the 200-day SMA of 4.82. RVOL 23.74.
- GDX 74.83, under its prior-day high of 76.75 and well under the 200-day SMA of 89.31. RVOL 27.63.
- CRWV 47.845, under its prior-day high of 51.03 and about half the 200-day SMA of 88.36. RVOL 41.42.
- PATH 11.73, under its prior-day high of 12.39 and the 200-day SMA of 12.32. RVOL 37.87.
- NVDL 15.24, under its prior-day high of 17.05 and far under the 200-day SMA of 61.18. RVOL 125.34.

On volume: daily bars are Alpaca IEX, a subset of the tape, and the volume looks like a full Wednesday session against a 20-day average. Don't read those RVOL multiples literally. RVOL is null for every micro-cap.

## Economic Data, Rates and the Fed

From `econ_calendar` (USD, high impact only):

- **Today (Thursday, November 19):** nothing high-impact listed.
- **Tomorrow (Friday, November 20):** nothing high-impact listed.

The calendar's `note` field is empty, so the packet doesn't flag a fetch problem, it just lists zero events. The packet has nothing on Fed speakers and no 10Y or 3M reading, so there's no rates read going into today. Macro-wise, the day is about earnings, not data.

## Coming Up

- **Tomorrow's events:** No high-impact USD releases in the calendar for Friday, November 20.
- **Earnings:** `next_earnings_date` is null for all 18 gappers, and the packet has no market-wide earnings calendar. From the feed: Walmart reports before the bell today (CNBC). Palo Alto Networks and Alibaba have already reported. Morningstar also has "SSE: What We Think of the Stock After Earnings," also already out.

## Skips and Traps

- **SDC** +33144.4%: `prev_close` of 0.07 against a price of 24.9333, no daily bars, no cap, no headline. That's broken data, not a gap. Ignore it.
- **CUE** +68.2%: up on a downgrade. The top headline is "B. Riley Cuts Price Target on Cue Biopharma to $25 From $83," and the feed also has "Cue Biopharma, Inc. Executes 1-for-30 Reverse Stock Split." $39.8M cap, 20-day average volume 18,079. A reverse-split micro-cap popping on a target cut is a trap.
- **SKYA** +90.32%: $210.0M cap. The story is a tender offer ("Announces Tender Offer for Up to 95% of Outstanding Securities," "Announces Final Results of Cash Tender Offer") plus "SkyAI Liquidates Solana Holdings and Announces $201M Share Buyback." If most of the float got tendered, what's left trades thin: 20-day average volume is 68,122. Under both cap bars. Skip.
- **NUAI** +24.69%: $560.9M cap. "Roth Capital Raises Price Target for New Era Energy & Digital" is real news, but B. Riley cut its target ("to $10 From $13" per the link), and the feed has "Announces $64 Million Private Placement." Under the 200-day SMA (3.99 vs 4.76) and under both cap bars. Skip.
- **RMIX** +24.46%: cap null. Every headline is about Haymaker Acquisition Corp. 4 (a 13G filing, a name and ticker change, a Haymaker V IPO). Nothing explains a 24% move. Skip.
- **CLRO** +46.19%, **RIBBU** +31.25%, **OKTG** +24.09%, **MSTZ** +12.74%, **NVD** +6.06%: `catalyst_found: false`. No catalyst found, so no trade. RIBBU's 20-day average volume is 20 shares and OKTG's is 419.
- **HY** -41.07%: "Hyster-Yale Announces Proposed $125 Million Convertible Senior Notes Offering." Dilution risk on a name that's already far below its 200-day SMA (15.44 vs 33.96). Not a long. Skip.
- **PRE** -36.62%: the feed has "Prenetics Global Limited Subject to Trading Halt" next to "Reports Q3 2026 Financial Results and Reaffirms Guidance." The packet doesn't say why it was halted. 20-day average volume is 6,993. Two of its five headlines are about Pensana PLC, a different company. Skip.
- **NCT** -34.26%: "Announces 8-for-1 Reverse Share Split," and the feed also has a "$200 Million Mixed Shelf Registration." Price 6.62 is well under the 9.09 prior close and the 10.07 prev close, so the numbers may be mixing pre- and post-split prices. Skip.
- **BTG** -6.17%: the only gapper with a cap over $1B ($6.01B), but `catalyst_found: true` is a false match. Every headline is about BTG Consulting PLC, a different company from B2Gold. The real driver isn't in the packet. GDX fell 5.92% the same session, so read it as a gold-miner move, not company news. Gap-down, not a long. Skip.
- **CRWV** -4.16% and **PATH** -5.33%: gap-downs, caps null. PATH's headlines (a research report, a Gemini for Healthcare partnership, an India hire) don't explain the drop. Both are well under their 200-day SMAs. Skip.
- **GDX** -5.92% and **NVDL** -5.87%: `catalyst_found: false`, caps null, gap-downs. Skip.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
