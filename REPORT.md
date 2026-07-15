# Premarket Report: July 15, 2026

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** Mixed: S&P proxy (SPY) +0.38%, Dow proxy (DIA) +0.24%, Russell proxy (IWM) +0.43%, but Nasdaq proxy (QQQ) -0.28%, dragged down by a real memory-chip selloff (Micron -8.02%, Intel -4.43%).
- **The catch we're watching:** Today's PPI print came in cooler than forecast ("US Producer Prices Fall 0.3% In June" shows up across several tickers' feeds, beating the 0.0% consensus) and Fed Chairman Warsh testified at 10am ET. Tomorrow's calendar is empty, so the next real catalyst is whatever headlines carry over from today's chip selloff and the PayPal takeover chatter.
- **Two-brain verdict:** Single-brain run, no GPT pass to compare against yet.

## Pre-Market Gappers

- **SOXS** +968.84% — "EXCLUSIVE: SK Hynix Is Where AI Infrastructure, Chips, Memory Converge, Says Direxion as It Launches Leveraged ETF"
- **ELVA** +49.05% — "12 Industrials Stocks Moving In Wednesday's Intraday Session"
- **AEHG** +42.21% — "Aehr Test Systems Gets New 2X Leveraged ETF Amid AI Semiconductor Rally"
- **SNWV** -39.21% — "Will the Market Recognize the True Potential of Elevance Health (ELV)?"
- **NVVE** +36.46% — "Nuvve Holding Q1 EPS $(28.96) Up From $(2.79 thousand) YoY, Sales $1.393M Up From $900.000K YoY"
- **JLHL** +36.08% — "12 Industrials Stocks Moving In Wednesday's After-Market Session"
- **JTAI** -35.52% — "12 Industrials Stocks Moving In Wednesday's Intraday Session"
- **PYPU** +35.0% — "Adobe, PayPal, UnitedHealth Just Got 2X ETFs — Direxion Builds Out The Leverage Trade"
- **PYPG** +34.37% — no catalyst headline in the feed
- **VEEE** -30.95% — "10 Consumer Discretionary Stocks Moving In Wednesday's Intraday Session"
- **GRRR** -29.1% — "Why Gorilla Technology Stock Is Falling Wednesday"
- **LCID** +28.79% — "Lucid Motors CEO Silvio Napoli Issues Satement Regarding Recent Rumors And Speculation"
- **CHRN** +28.77% — "12 Information Technology Stocks Moving In Wednesday's After-Market Session"
- **AAOG** -26.47% — "Seagate, SanDisk Stocks Get 2X ETF Boost As Themes Expands Leveraged AI Trade With 9 Funds"
- **AEHR** +21.91% — "12 Information Technology Stocks Moving In Wednesday's Intraday Session"
- **IOVA** +20.61% — "Iovance Biotherapeutics Files Prospectus For Offering Mixed Shelf; Terms Undisclosed"
- **PYPL** +17.2% — "Wall Street Gave Up on PayPal, But the Stock Just Had Its Best Day Ever"
- **MU** -8.02% — "$100 Invested In Micron Technology 5 Years Ago Would Be Worth This Much Today"
- **INTC** -4.43% — "Intel Has Reached 'Very Important Milestone' With Its $400 Million Chipmaking Machine, ASML CEO Says"
- **AAPL** +4.02% — "New Magnificent 10 ETF Targets Nvidia, Microsoft and AI Leaders With Daily Income Strategy"

## Day Trading Watchlist

`day_eligible` encodes the Trend Join Long rule: gap > 3%, price > $3, market cap > $1B, premarket RVOL > 1.5, and price already breaking above yesterday's high.

One name cleared it.

| Ticker | Catalyst | Levels | Plan | Second-brain check | Conviction |
|---|---|---|---|---|---|
| LCID | CEO Silvio Napoli directly denied bankruptcy/going-private rumors as "completely false," and the stock is rebounding hard off that denial (RVOL 78.81). | Prior day's high is $5.76, price ($5.95) is already above it. Today's HOD so far is $6.00, price is $0.05 below that. VWAP is $5.52, price is holding above it. Premarket high isn't in the packet (zero premarket volume logged), so that leg of the trigger can't be pinned to a number. | Rule calls for a break of premarket high and prior HOD inside the 10am-3:30pm ET window; the prior-HOD leg ($5.76) is already cleared, the premarket-high leg is unknown. Stop (1R) is 1% below premarket high or the LOD, whichever is lower; with premarket high unavailable, the only computable reference is the LOD ($4.63). Scale 1/3 off at +1R, 1/3 at +2R, trail the rest on the 21-EMA (not in the packet, watch it live), flat by 3:51pm ET. | n/a, single-brain run | 🟡 |

## Swing Watchlist

`swing_eligible` encodes: gap >= 8%, price > $3, open > yesterday's high, open > the 200-day SMA, market cap >= $800M, and a real catalyst.

Two names cleared it. Both were checked against the standing red-flag rule (market cap under $2B, or a catalyst headline quoting near-zero revenue against the market cap) and neither triggered it: AEHR's market cap is $2.76B and PYPL's is $48.97B, both above the $2B floor, and no catalyst headline for either quotes a revenue figure.

| Ticker | Catalyst | Trend context | Idea | Second-brain check | Conviction |
|---|---|---|---|---|---|
| AEHR | No company-specific headline in the packet, every matched item is a generic "stocks moving" wrap or general AI-semiconductor-rally coverage. The one real signal is that a new 2X leveraged ETF tracking AEHR just launched (that headline landed under a different ticker, AEHG, in the packet, but it names AEHR directly). | Open ($98.16) is well above the 200-day SMA ($49.68) and above yesterday's high ($73.37). | The trend legs both clear, but price ($87.79) has already faded about 20% off today's high ($109.88) and sits below VWAP ($95.94). Thin, non-specific catalyst plus a hard fade off highs, this clears the rule on a technicality more than on conviction. Watch-and-build-a-plan only, no stop, no target. | n/a, single-brain run | 🔴 |
| PYPL | "Stripe Proposes $53 Billion PayPal Acquisition: What Do Prediction Markets Say About the Deal?" and "Wall Street Gave Up on PayPal, But the Stock Just Had Its Best Day Ever." | Open ($54.80) is just above the 200-day SMA ($53.01) and comfortably above yesterday's high ($47.38). | News catalyst, no earnings involved: real, named takeover speculation. Price ($55.52) is sitting right at VWAP ($55.08) and within $0.36 of today's HOD ($55.88), holding near the top of the range, and it's moving against a red Nasdaq today, not just riding sector beta. Watch-and-build-a-plan only, no stop, no target. | n/a, single-brain run | 🟢 |

## Market Trends of the Day

Today split by index: Dow, S&P, and Russell all green, but Nasdaq (QQQ proxy) was the one red at -0.28%, dragged by a real memory-chip selloff. Micron fell 8.02% and Intel fell 4.43%, and the feed ties both to the same story: "Memory-Chip Selloff Drags Nasdaq 100 Lower, SanDisk Sinks 13%."

A second theme: a wave of brand-new leveraged single-stock ETFs (Direxion, Themes) launched today tracking names like PayPal and Aehr Test Systems. Several of today's biggest gappers (SOXS, AEHG, PYPU, AAOG) are catalyst-matched almost entirely to these ETF-launch headlines rather than to any news about an actual operating business, worth keeping in mind since their gap size is closer to mechanical leverage than a stock-specific story.

PYPL stands out as the one clean, idiosyncratic mover: a Stripe acquisition proposal reported at $53 billion, driving what one headline calls PayPal's best day ever, and it's doing that against a red Nasdaq rather than riding a sector wave.

LCID is rebounding hard (+28.79%) off Monday's bankruptcy-rumor-driven selloff, after the CEO directly denied the rumor. VEEE, flagged as a trap in each of the last two reports over its reverse-merger structure, gave back 30.95% today after its multi-day run.

## Technical Signals for Today

- S&P 500 proxy (SPY): 754.77, +0.38% from prior close (751.94).
- Dow proxy (DIA): 526.00, +0.24% from prior close (524.75).
- Nasdaq proxy (QQQ): 717.70, -0.28% from prior close (719.71). The one laggard of the four.
- Russell 2000 proxy (IWM): 295.77, +0.43% from prior close (294.49). Strongest of the four.
- VIX, 10-year yield, 3-month yield, WTI crude, and the dollar index all failed to load this run (data source outage), so there's no vol or rates read to lean on today.
- Micron ($903.84) is still far above its 200-day SMA ($472.39) even after today's 8.02% drop, a pullback inside an uptrend, not a trend break.
- Apple closed within $1.12 of today's high ($328.70 HOD vs. $327.58 last) and well above its 200-day SMA ($273.06), holding its gap into the close.
- Intel ($102.99) is now trading below both today's own prior-day-high reference ($109.17) and its VWAP ($102.13 is basically where it's sitting), a weaker close than two sessions ago when it held near its highs.

## Economic Data, Rates and the Fed

Today already had its events: Core PPI m/m (forecast 0.3% vs. previous 0.4%), PPI m/m (forecast 0.0% vs. previous 1.1%), and Fed Chairman Warsh testifying at 10am ET. The actual print looks like it beat the cooler forecast: "US Producer Prices Fall 0.3% In June" shows up across several tickers' matched headlines, a bigger deceleration than the flat 0.0% consensus.

Tomorrow: nothing on the calendar.

## Coming Up

- **Tomorrow's events:** None in the calendar for July 16.
- **Earnings:** The structured next-earnings-date field is null for all 20 gappers again this run, the per-ticker lookup was rate-limited across the board, so this is a data gap, not a finding that nothing's on the calendar.

## Skips and Traps

- **SOXS, AEHG, PYPU, AAOG:** All four are catalyst-matched almost entirely to brand-new leveraged ETF product launches (Direxion, Themes) tracking other names, not to news about their own underlying business. Treat the size of these gaps as mechanical leverage, not a stock story.
- **PYPG (+34.37%):** No catalyst found in the feed. No story, no trade, regardless of the size of the gap.
- **NVVE (+36.46%):** An $11.3M market cap name that reported a Q1 EPS of $(28.96) and was halted on upside circuit breakers twice in the same session (first at +100.76%, then again at +44.05%). Extreme, thin, and speculative.
- **ELVA (+49.05%):** The headline Amazon commercial relationship is real, but the company is paying for it with 13,880,345 warrants to purchase its own shares, real dilution attached to otherwise good news.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
