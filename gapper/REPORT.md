# Premarket Report: November 17, 2026

*Single-brain pass: Claude only. Second brain not wired in yet.*

> Rules pick the watchlist. The AI judges the quality of the setups. This is not financial advice.

**Data warning: read this first.** The packet says "Scan run 2026-11-17 06:08 EST (premarket)." But the gaps mostly aren't premarket gaps. For every cap-qualified name, `price` equals `prior_close` (INTC 55.45 vs 55.45, TU 9.58 vs 9.58, IREN 16.38 vs 16.38, NVDA 156.145 vs 156.15). So `gap_pct` for those names is yesterday's close vs the close before it. That's Monday's session, not this morning's move. Volume and RVOL look like full-day Monday numbers too.

Yahoo rate-limited the scan hard: 95 requests failed even after retries. Intraday data is `unavailable` for all 20 gappers, so VWAP, HOD, LOD, premarket high and premarket volume are null across the board. RVOL is null for the 11 small names. VIX, 10Y, 3M, WTI and the dollar are null. Market cap is null for HZN, CRMX, AVAZ and ASTN. `next_earnings_date` is null for all 20. Index levels are ETF proxies (SPY, DIA, QQQ, IWM), not the indices.

## Summary

- **The tape in one line:** tech-led selling into Nvidia's print. The proxies show SPY -1.89%, QQQ -2.68%, IWM -1.64%, DIA -1.39% vs their `prev_close`, and the overnight headlines are "Nasdaq Futures Slip as Investors Look to Nvidia Earnings" and "Tech Stock Selloff Eases in Countdown to Nvidia: Markets Wrap".
- **The catch we're watching:** Retail Sales at 8:30 AM ET (forecast 0.1%, previous 0.8%) and Core Retail Sales (forecast 0.4%, previous 0.9%). Behind that, Nvidia's earnings: "Nvidia’s interim CEO Colette Kress to make her debut at first earnings."
- **Two-brain verdict:** Single-brain run, no second opinion.

## Pre-Market Gappers

All 20 gappers in the packet. Gap % is `price` vs `prev_close`. Market cap in parentheses. Headline is the first one the packet lists for each ticker, which often isn't the real story or isn't even about the company (see Skips and Traps).

- **HZN** +4753.41% (cap null) : no headline in the packet (`catalyst_found: false`)
- **NCT** +43.94% ($239.0M) : "Intercont (Cayman) Limited Announces 8-for-1 Reverse Share Split"
- **CLRO** +41.84% ($12.8M) : no headline in the packet (`catalyst_found: false`)
- **MTEX** -40.32% ($7.3M) : "Mannatech, Incorporated Announces Third Quarter 2026 Financial Results"
- **BGIN** +35.05% ($592.8M) : "BGIN Blockchain Limited Announces Participation in 15th Annual ROTH Technology Conference"
- **FCUV** -33.33% ($4.6M) : "Focus Universal Inc. (FCUV) Experiences Significant Stock Price Movement"
- **CRMX** -29.95% (cap null) : no headline in the packet (`catalyst_found: false`)
- **AVAZ** -29.75% (cap null) : no headline in the packet (`catalyst_found: false`)
- **RIBBU** +28.25% ($218.2M) : no headline in the packet (`catalyst_found: false`)
- **ASTN** +22.74% (cap null) : no headline in the packet (`catalyst_found: false`)
- **TPEI** +20.37% ($41.9B, see Skips and Traps) : "Here’s how much of Deutsche Bank’s market cap has been wiped away after reports on 15 million leaked documents"
- **TU** +12.24% ($14.8B) : no headline in the packet (`catalyst_found: false`)
- **IREN** -9.83% ($5.85B) : "Blue Owl Managed Funds Lead $2.4 Billion AI Factory Financing for IREN"
- **ONDS** -8.35% ($2.69B) : "Needham Adjusts Ondas Price Target to $14 From $19, Maintains Buy Rating"
- **INTC** -7.06% ($294.7B) : "Class Action Lawsuit Filed Against Intel Corporation"
- **VALE** -6.73% ($34.1B) : "Vale's 'Novas Pontes' Infrastructure Project Reaches 86% Completion"
- **IBIT** -5.52% ($52.8B) : no headline in the packet (`catalyst_found: false`)
- **CIFR** -4.6% ($2.98B) : "Bernstein Maintains Buy Rating on Cipher Digital"
- **NOK** -4.59% ($44.2B) : "Nokia and Partners Form AI Gigafactory Northern Consortium"
- **NVDA** -4.11% ($3.76T) : "NVIDIA Announces Quantum Computing Collaborations with IBM and Fermilab"

## Day Trading Watchlist

The bar is Trend Join Long: gap > 3%, price > $3, market cap > $1B, premarket RVOL > 1.5, and price already breaking above yesterday's high.

No names cleared the day-trading bar today. Every gapper is `day_eligible: false`. Only two up-movers have a known cap over $1B. TU (+12.24%, RVOL 82.89) is at 9.58, under its prior-day high of 9.69. TPEI has null RVOL and no intraday data. With premarket high and HOD null for everyone, there are no live levels to build a plan off even if something had qualified.

## Swing Watchlist

The bar is: gap >= 8%, price > $3, open above yesterday's high, open above the 200-day SMA, market cap >= $800M, and a real catalyst (earnings on the gap day, or news with no earnings).

No names made the swing list today. TPEI came back `swing_eligible: true`, but it fails the catalyst check, so it's in Skips and Traps. Nobody else is flagged.

## Market Trends of the Day

Same story as the last few sessions: the AI trade is unwinding into Nvidia's earnings, and the Huang exit is the overhang. "Nvidia Earnings Are Sideshow as Huang’s Ouster Looms Over Market" (Bloomberg), "Nvidia to report Q3 earnings amid Huang scandal", and NVDA's own feed has "NVIDIA Faces Potential Lawsuits Following CEO Resignation." The 13-F stories pile on: "Tepper, Loeb among fund managers piling into Nvidia and other megacap tech on the eve of October drawdown" and "Stanley Druckenmiller dumped these chip stocks while buying into SpaceX and Palantir."

Every big name on the list is red and they're the AI and crypto complex: NVDA -4.11%, INTC -7.06%, IREN -9.83%, CIFR -4.6%, NOK -4.59%, IBIT -5.52%. Good company news isn't helping. NVDA put out three product releases and IREN got "$2.4 Billion AI Factory Financing" and both still sold off.

It's not just tech. Europe is soft too: "European shares fall as Deutsche Bank slides, tech stocks tumble ahead of Nvidia earnings" (Reuters), with Deutsche Bank losing as much as "€3.8 billion ($4.2 billion)" of market cap on the leaked-documents story. Copper is lower ("Copper falls ahead of Nvidia earnings"). The one hint of relief is Bloomberg's "Tech Stock Selloff Eases," but WSJ still has Nasdaq futures slipping. The packet has no futures numbers, so you can't size that.

One sector call in the feed: strategists "recommend hyperscalers and the health care sector," conditional on "the 10-year stays below this key level." The packet has no 10Y reading, so there's no way to check where that stands.

## Technical Signals for Today

ETF proxy levels from the scan, vs each one's `prev_close`:

- SPY 740.04 (prev 754.27), -1.89%
- QQQ 661.8 (prev 680.01), -2.68%
- IWM 273.0 (prev 277.55), -1.64%
- DIA 515.83 (prev 523.1), -1.39%

QQQ is the weak spot. Same caveat as the gappers: this may be the Monday move rather than this morning's futures. VIX, 10Y, 3M, WTI and DXY are all null, so there's no volatility, rate, oil or dollar read.

Big names vs prior-day high and the 200-day SMA (no VWAP or HOD today, intraday data was unavailable):

- NVDA 156.145, under its prior-day high of 162.53 and well under the 200-day SMA of 204.01. RVOL 41.9.
- INTC 55.45, under its prior-day high of 57.2, way under the 200-day SMA of 87.44. RVOL 23.59.
- IREN 16.38, under its prior-day high of 17.05, way under the 200-day SMA of 42.4. RVOL 33.44.
- IBIT 36.79, under its prior-day high of 37.14 and the 200-day SMA of 41.0.
- TU 9.58, just under its prior-day high of 9.69, under the 200-day SMA of 11.07.

Everything big is under its prior-day high and its 200-day SMA. No sign of a turn in the data.

On volume: RVOL for the big names runs 13.77 to 82.89. Daily bars are Alpaca IEX, a subset of the tape, and the volume looks like a full Monday session against a 20-day average. Don't read those multiples literally.

## Economic Data, Rates and the Fed

From `econ_calendar` (USD, high impact only):

- **Today, 8:30 AM ET:** Core Retail Sales m/m, forecast 0.4%, previous 0.9%.
- **Today, 8:30 AM ET:** Retail Sales m/m, forecast 0.1%, previous 0.8%.
- **Tomorrow, 2:00 PM ET:** FOMC Meeting Minutes. No forecast or previous.

Both retail numbers are expected to cool hard from last month. A soft print helps the rate-cut case and could give the tape some relief. A hot one leans hawkish going into tomorrow's minutes. The packet has no 10Y or 3M reading, so there's no live read on how rates are set up for it.

## Coming Up

- **Tomorrow's events:** FOMC Meeting Minutes at 2:00 PM ET.
- **Earnings:** `next_earnings_date` is null for all 20 gappers, and the packet has no market-wide earnings calendar. Headlines put Nvidia's report this week ("A Big Week Ahead As Nvidia to Report Earnings, Anthropic to Debut IPO") but give no date. Disney is in the feed too ("Disney expected to post another strong earnings report"), also no date.

## Skips and Traps

- **TPEI** +20.37%: flagged `swing_eligible: true`, pulled for no real catalyst. The packet's "catalysts" are RSS matches that aren't about TPEI at all: a Deutsche Bank leaked-documents story, a Reuters Europe wrap, a copper note and an FXStreet Nvidia preview. The data is broken too. The packet names it "BANK OF MONTREAL /CAN/" and the $41.9B cap is the issuer's, not the note's. Prior-day high, prior close and the 200-day SMA are all exactly 44.99, 20-day average volume is 0, and `prev_close` (49.07) doesn't match `prior_close` (44.99). Not a setup. Skip.
- **TU** +12.24%: $14.8B cap, RVOL 82.89, but `catalyst_found: false` (Yahoo news failed for it today) and price 9.58 is under the prior-day high of 9.69 and the 200-day SMA of 11.07. No catalyst in the packet. Skip.
- **HZN** +4753.41%: no cap, no daily bars, no intraday data, no headlines. Price 85.42 vs a 1.76 prev close isn't a real gap. Ignore the number.
- **NCT** +43.94%: $239.0M cap, and the "catalyst" is a reverse split ("Announces 8-for-1 Reverse Share Split"), with a "$200 Million Mixed Shelf Registration" behind it. Reverse split plus shelf is a dilution setup, not a buy. Trap.
- **CLRO** +41.84%, **RIBBU** +28.25%, **ASTN** +22.74%: `catalyst_found: false`. RIBBU's 20-day average volume is 20 shares and ASTN's is 745. Skip.
- **BGIN** +35.05%: $592.8M cap, under both bars, 20-day average volume 1,988, and the newest headline is a conference appearance. Skip.
- **MTEX** -40.32%, **FCUV** -33.33%: sub-$10M caps. FCUV's only fresh headline is "Experiences Significant Stock Price Movement" and it has a warrant exercise in the feed. No long setups.
- **CRMX** -29.95%, **AVAZ** -29.75%: no cap, no headline, 20-day average volume of 217 and 361. Skip.
- **NVDA, INTC, IREN, CIFR, NOK, VALE, IBIT, ONDS** (-4.1% to -9.8%): the AI, crypto and miner unwind. Neither setup is a short or a dip-buy, and all of them are well under their 200-day SMAs. INTC has "Class Action Lawsuit Filed Against Intel Corporation." ONDS has a target cut ("Needham Adjusts Ondas Price Target to $14 From $19"). NVDA reports this week with a CEO-exit overhang, which is binary-event risk. Skip.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
