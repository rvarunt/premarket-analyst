# Premarket Report: 2026-10-21

*Single-brain pass (Claude only).*

> Rules pick the watchlist. The AI judges the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** Index ETF proxies (SPY, DIA, QQQ, IWM) are mixed: S&P 500 proxy +0.32%, Dow proxy +1.01%, Nasdaq proxy -0.15%, Russell 2000 proxy +1.66%. Small caps are leading. VIX, 10Y, 3M, oil and DXY came back null (Yahoo rate limited), so there's no read on vol or rates.
- **The catch we're watching:** Data quality. Several big gap numbers are measured against a stale `prev_close` that doesn't match `prior_close` (BRZE, SAIQ, ATGL, and others below), and 84 requests failed even after retries. Treat the percentages with suspicion.
- **Two-brain verdict:** Single-brain run, no second opinion.

## Pre-Market Gappers

Source: Alpaca screener. Intraday levels (VWAP, premarket high, HOD, LOD) and RVOL are mostly null, so nothing could be tested on those. Headlines are quoted from the packet; many names only have generic "stocks moving" roundups.

- **SAIQ** +100.6% : "WISeQey Remains WISeSat.Space's Largest Shareholder With Approximately 88.5% Beneficial Ownership, Targets Commercial Execution Across Secure Semiconductors, Digital Identity And Satellite Connectivity". Market cap null.
- **ATGL** +52.6% : "Why Super Micro Computer Shares Are Trading Higher By 13%; Here Are 20 Stocks Moving Premarket" (generic roundup). Market cap $105.8M.
- **BKHAU** -52.4% : "Reported Earlier, Black Hawk Revises Trust Amendment Proposal To Replace Per-Share Formula With Flat $150K Monthly Extension Deposit". SPAC unit, market cap $17.2M.
- **BRZE** +51.7% : "BTIG Downgrades Braze to Neutral". Market cap $5.18B.
- **AIXI** +40.9% : "12 Information Technology Stocks Moving In Tuesday's Intraday Session" (generic). Market cap $171.2M.
- **WORX** +36.6% : "12 Health Care Stocks Moving In Tuesday's Intraday Session" (generic). Market cap $328,627.
- **WLDSW** +34.2% : "Wearable Devices Receives Notice Of Allowance For Its Pressure-Based Gesture Control Patent Application From China's National Intellectual Property Administration". Market cap $94.6M.
- **PMI** -32.2% : "12 Health Care Stocks Moving In Tuesday's After-Market Session" (generic). Market cap $24.5M.
- **MYGN** +31.6% : "Myriad Genetics Offloads Struggling Prenatal Unit for $210 Million to Labcorp". Market cap $529.9M.
- **RAIL** -31.4% : "FreightCar America Completes Acquisition Of Trinity Equipment Company, Terms Undisclosed; Transaction Expected To Be Immediately Accretive To FreightCar". Market cap $131.7M.
- **PCTTU** +30.3% : "8 Stocks Halted In Tuesday's Session" (generic, from 2022 per the link). Market cap $916.1M.
- **GOW** +29.5% : "GOWell Energy Technology Announces Nasdaq Trading Debut Under Ticker GOW Following Business Combination With Inflection Point Acquisition Corp. V". Market cap null.
- **AIOK** +23.9% : no headline found. Market cap null.
- **EVAX** +21.6% : "Evaxion Reports Sustained Clinical Responses in Three-Year Follow-Up of EVX-01 Phase 2 Trial". Market cap $1.69B.
- **CD** +21.2% : "12 Financials Stocks Moving In Tuesday's Intraday Session" (generic). Market cap $931.7M.
- **CCG** +20.7% : "12 Financials Stocks Moving In Tuesday's Intraday Session" (generic). Market cap null.
- **LCU** -20.2% : "Lion Copper Corp. Commences Trading on Nasdaq". Market cap $1.96B. No daily bars or 200-day SMA in the packet.
- **GLE** -19.2% : "BofA Projects Robust Q3 Results for Societe Generale" (unrelated roundup). Market cap $50.4M. Packet also shows a 1-for-10 reverse split effective Oct. 8.
- **LVLU** -18.9% : "11 Consumer Discretionary Stocks Moving In Thursday's Intraday Session" (generic). Market cap $30.9M.
- **IREN** -4.0% : "What's Going On With IREN Stock Tuesday?". Market cap $9.51B. Most-actives pick, not a true gapper.

## Day Trading Watchlist

The day flag encodes Trend Join Long: gap > 3%, price > $3, market cap > $1B, premarket RVOL > 1.5, and price breaking above yesterday's high.

No names cleared the day-trading bar today. Every gapper has `day_eligible: false`.

## Swing Watchlist

The swing flag encodes: gap >= 8%, price > $3, open above yesterday's high and the 200-day SMA, market cap >= $800M, and a real catalyst.

No names cleared the swing bar today. Every gapper has `swing_eligible: false`.

## Market Trends of the Day

From the headlines in the packet:

- AI and space are the loud theme. "Why SpaceX's stock is surging — and lifting the broader AI universe along with it" (MarketWatch), "SpaceX earnings soar past expectations as AI business surges - Axios". SAIQ's headlines are all SpaceX/satellite adjacent.
- Earnings cheer is propping up the tape: "Stocks eke out modest gains thanks to earnings cheer - Reuters".
- Netflix is the loser: "Netflix stock sinks after announcing Q3 earnings, Q4 revenue forecast falls short of estimates - Yahoo Finance".
- Braze looks like a deal story: "After Braze, Could Klaviyo Be Big Tech's Next Billion-Dollar Bet?" plus a string of downgrades.
- IREN is in AI-infrastructure credit worry territory: "'CoreWeave Is the Canary in the Coal Mine': Expert Warns More AI Debt Will Slide into Distress".

## Technical Signals for Today

Index levels are ETF proxies, not the real indexes: SPY 769.09 vs 766.60 prior close, DIA 524.21 vs 518.98, QQQ 717.21 vs 718.31, IWM 275.80 vs 271.30. VIX is null. No breadth data in the packet.

## Economic Data, Rates and the Fed

The packet's calendar (USD, high impact only) shows nothing today (2026-10-21). 10Y and 3M yields are null, so there's no rates read.

## Coming Up

- **Tomorrow's events:** No high-impact USD releases in the packet for 2026-10-22.
- **Earnings:** No `next_earnings_date` for any gapper. From headlines only, Meta and IBM are being previewed ahead of earnings, per Barron's. Timing is not in the packet.

## Skips and Traps

- **BRZE:** The +51.7% is measured against a `prev_close` of $30.04, but `prior_close` is $45.58 and price is $45.57, so it's flat on the prior close. The move already happened. Headlines are four downgrades (BTIG to Neutral, Wells Fargo to Equal-Weight, Oppenheimer to Perform, Stifel to Hold) with targets at $47.5. That reads as a deal-capped stock. Skip.
- **SAIQ, ATGL, AIXI, WORX, WLDSW, PMI, BKHAU, GLE, LVLU, RAIL:** Same pattern or micro-cap: sub-$500M market caps, most with near-zero 20-day average volume, and several with `prev_close` far from `prior_close`. Many have only generic roundup headlines, so effectively no catalyst. Skip.
- **WLDSW:** Packet also shows "Wearable Devices Announces Warrant Inducement Agreement, Raising $1.2M In Gross Proceeds" and trading halts. A dilution-plus-halt microcap is a trap.
- **MYGN:** Gap is real news (prenatal unit sale for $210M), but market cap is $529.9M, open is below yesterday's high ($5.54 vs $5.95), and it fails the swing rules. No setup.
- **EVAX:** Good clinical headline, $1.69B cap, but price $4.05 is below yesterday's high of $4.11, and no premarket volume or RVOL. Close, but not through. Watch only.
- **PCTTU, CD, GOW, CCG, AIOK, LCU:** SPAC/unit/new-listing or null-cap names with no usable catalyst or data. PCTTU's only headline is a 2022 halt roundup. AIOK has no catalyst at all. Skip.
- **IREN:** Down 4.0%, below its 200-day SMA ($45.24), not a gap-up setup.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
