# Premarket Report: September 11, 2026

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** Red again across the board. S&P proxy (SPY) -0.6%, Dow proxy (DIA) -0.6%, Nasdaq proxy (QQQ) -1.06%, Russell proxy (IWM) -1.02%, tech and small caps leading the slide into a CPI morning.
- **The catch we're watching:** Both watchlists are empty today, and not on close technicalities like yesterday. Every up-gapper in the packet is a micro-cap (market cap from $3.5M up to $35.7M, or unresolved entirely), well under both the $1B day-trading floor and the $800M swing floor. The five names that do clear $1B market cap (AIFU, INTC, CIFR, ORCL, MARA) are all down gaps, so the long-only rules don't touch them either. On top of that, `intraday_data_source` is `unavailable` for all 20 gappers this run (Yahoo rate-limited every single enrichment call), so premarket high, VWAP, HOD and LOD are null across the board. Also flagging: Oracle carries two headlines calling its print a beat that's sending the "stock rises," while the packet itself has ORCL gapping down -5.3% this morning. Genuine mismatch, not a data error, see Skips and Traps.
- **Two-brain verdict:** Single brain, no second opinion to compare.

## Pre-Market Gappers

- **TNON** +117.2% - "12 Health Care Stocks Moving In Thursday's After-Market Session"
- **DBGI** +81.1% - "Digital Brands Group Has Executed A Binding Contract Of $3.3M In Guaranteed Cash Flow For Its U.S. Program From September 1 Through December 31, 2026"
- **MKDW** -48.5% - "MKDWELL Tech Files $100M Shelf Registration For Future Offerings Of Shares, Warrants, Debt Securities And Units"
- **LEXX** -38.6% - "12 Health Care Stocks Moving In Thursday's Intraday Session"
- **WZRD** -38.1% - no catalyst headline in the packet
- **SKIL** -34.2% - "Skillsoft Q2 2027 Earnings Call: Complete Transcript"
- **ALP** -31.5% - "Alpha Compute Reports Total Gamee Revenue And Alpha-01 Cash Receipts For July Were $1.57M, Posts $57K EBITDA"
- **PCLA** +31.0% - "11 Information Technology Stocks Moving In Thursday's Intraday Session"
- **WLDSW** +30.7% - "Wearable Devices Announces Warrant Inducement Agreement, Raising $1.2M In Gross Proceeds"
- **RML** -26.5% - "Limoneira Posts Downbeat Q3 Results, Joins Cooper Companies, Navan And Other Big Stocks Moving Lower In Thursday's Pre-Market Session"
- **HVIIU** +25.5% - "Trading Halt: Halt status updated at 10:35:00 AM ET: Quotation Resumption: IPO Security - Released for Quotation"
- **SUNE** -25.3% - "Why Is SUNation Energy Stock Soaring Wednesday?"
- **FGL** -24.9% - "12 Industrials Stocks Moving In Thursday's Intraday Session"
- **NAVN** -21.8% - "These Analysts Revise Their Forecasts On Navan After Q2 Results"
- **VNCE** -21.2% - "Vince Holding Announces Acquisition Of OVO Operating Business, Will Serve As Core Apparel Licensee Overseeing Design, Merchandising, And Retail Stores; Terms Not Disclosed"
- **AIFU** -19.7% - "AIFU Announces Appointment Of Shanyu Chang As CFO Effective Immediately"
- **INTC** -5.6% - "What's Going On With Intel Stock Thursday?"
- **CIFR** -5.5% - "Why Is Cipher Digital Stock Falling on Thursday?"
- **ORCL** -5.3% - "Oracle Beats Revenue and EPS Estimates, Raises FY27 EPS Guidance — Stock Rises"
- **MARA** -4.2% - "Why Is MARA Stock Falling on Thursday?"

## Day Trading Watchlist

The "Trend Join Long" rule: gap over 3%, price over $3, market cap over $1B, premarket RVOL over 1.5, and price already breaking above yesterday's high.

No names cleared the day-trading bar today. The packet marks `day_eligible: false` on all 20 gappers. The five names that clear the $1B market cap floor (AIFU $14.1B, INTC $505.7B, ORCL $440.9B, CIFR $6.6B, MARA $4.4B) are all down gaps this morning, so a long-only breakout rule doesn't apply to any of them regardless of premarket levels. Every up-gapper today (TNON, DBGI, PCLA, WLDSW, HVIIU) has a market cap in the low tens of millions or unresolved entirely, nowhere near the $1B floor. On top of the cap problem, `intraday_data_source` is `unavailable` for every gapper this run, so premarket high, VWAP, HOD and LOD are all null across the board too. Nothing here to trade off the packet as it stands.

## Swing Watchlist

The swing rule: gap of 8% or more, price over $3, open above yesterday's high, open above the 200-day SMA, market cap of $800M or more, and a real catalyst.

No names clear it either, `swing_eligible: false` across all 20. Closest structural fit is **WLDSW** (Wearable Devices Ltd.): gap +30.7%, price $12.40 already above both yesterday's high ($6.65) and the 200-day SMA ($4.17). It fails purely on market cap, $35.7M versus the $800M floor. Worth flagging even setting the cap aside: the only ticker-specific headline attached is a warrant inducement agreement raising $1.2M, a dilutive financing move, not a bullish catalyst, alongside two trading-halt notices. This reads like a halt-driven pop on a dilutive raise, not a name to build a swing thesis on. **HVIIU** also clears the gap/price/trend legs (open $13.30 above prior high $12.56 and the 200-day SMA $10.89), but market cap is unresolved (`sec_unavailable_no_concept`) and its only headline is an IPO-release halt notice, consistent with this being a brand-new listing finding its trading range rather than a real catalyst gap.

## Market Trends of the Day

Today's news pull pulls two ways at once. On the bullish side: a piece framed around "the four reasons stocks are about to embark on a face-ripper rally," and Oracle's own earnings beat (revenue and EPS ahead of estimates, FY27 EPS guidance raised, cloud/AI momentum cited as the driver) shows up twice, both times cast as a positive. Set against that: Bank of America is quoted saying the real threat to the economy sits somewhere other than bond yields, Bridgewater's investment chief is quoted saying AI could "wipe out humanity" (about as skeptical as a sentiment headline gets), and Adobe's print is described as leaving Wall Street wanting more, a soft read out of software sitting right next to Oracle's beat.

On commodities and inflation: WTI dipped below $100 even as diesel hit a fresh record above $6, a divergence worth watching into today's CPI print. Enbridge buying Tallgrass Crude Pipeline for $2.55B is straight energy-infrastructure M&A, not obviously tied to the day's direction either way.

None of this cleanly explains why Oracle itself, the name getting the bullish earnings-beat headlines in this pull, is actually a -5.3% gapper in the packet this morning. See Skips and Traps below. Worth noting plainly rather than reaching for a story that isn't in the packet. Also notable: HIVE brought in an enterprise veteran to scale its BUZZ HPC AI cloud business, a crypto-miner-pivoting-to-AI-compute story that sits oddly next to MARA and CIFR both gapping down this morning on that same crypto-adjacent theme.

## Technical Signals for Today

The four major index rows in the packet are Alpaca ETF proxies again, not the underlying indices, because the direct index pulls failed: S&P proxy (SPY) 757.87, down 0.6%; Dow proxy (DIA) 520.89, down 0.6%; Nasdaq proxy (QQQ) 708.73, down 1.06%; Russell proxy (IWM) 287.73, down 1.02%. Treat these as ETF price levels, not literal index points. Tech and small caps are underperforming the broader tape this morning.

VIX, the 10-year yield, the 3-month yield, WTI crude, and the Dollar Index all came back null this run (`yfinance_failed`), so there's nothing to report on volatility, rates, or the dollar directly from the packet today.

Five names carry a real `rvol` reading despite every other intraday field being null: ORCL (78.2x), INTC (32.3x), CIFR (26.5x), MARA (25.8x), and TNON (4,246.8x, but that's a $3.5M microcap on a 117% gap off a razor-thin 20-day average volume, take that multiple with a grain of salt). The four large caps (ORCL, INTC, CIFR, MARA) are trading many multiples of normal volume on their down gaps this morning, real premarket activity even without HOD/LOD/VWAP in the packet to confirm live levels.

## Economic Data, Rates and the Fed

Today, September 11, is a CPI morning: Core CPI m/m (forecast 0.2%, previous 0.2%), Core CPI y/y (forecast 2.4%, previous 2.5%), CPI m/m (forecast 0.4%, previous 0.1%), and CPI y/y (forecast 3.4%, previous 3.4%), all at 8:30am ET. The headline CPI m/m forecast stepping up to 0.4% from last month's 0.1% is the number to watch, especially against the diesel-price-record story in today's news pull. Tomorrow, September 12, has no high-impact USD releases in the packet's econ calendar.

## Coming Up

- **Tomorrow's events:** None. The packet's econ calendar has no high-impact USD releases listed for September 12.
- **Earnings:** `next_earnings_date` is null for every gapper in today's packet, so there's no confirmed date to flag for any of these names from the packet's own data.

## Skips and Traps

- **TNON** +117.2%: `catalyst_found: true`, but every attached headline is a generic health care sector roundup or unrelated macro piece (Kimball Electronics, crude oil, Nasdaq/PPI). Nothing Tenon-specific in the packet. Market cap $3.5M, far under both floors.
- **DBGI** +81.1%: Real, ticker-specific catalyst ($3.3M guaranteed cash flow contract through year-end), but market cap $6.3M is far under both floors.
- **MKDW** -48.5%: The real driver here looks like the $100M shelf registration for future stock/warrant/debt offerings, a dilutive filing, which explains a rational sell-off rather than a trap. Down gap, not eligible for either list anyway.
- **LEXX** -38.6%: `catalyst_found: true` but every headline is a generic "Health Care Stocks Moving" sector roundup or unrelated (ABM earnings). Nothing Lexaria-specific in this packet. Down gap regardless.
- **WZRD** -38.1%: `catalyst_found: false`, no headlines in the packet at all. Skip automatically per the rules.
- **SKIL** -34.2%: Real catalyst, a Q2 earnings call transcript, consistent with a post-earnings sell-off. Down gap, not eligible for either list.
- **ALP** -31.5%: Real, ticker-specific catalysts (Nasdaq compliance extension, a small monthly revenue/EBITDA report), but a $1.57M revenue print and $87.1M market cap don't point to a name worth chasing down. Down gap anyway.
- **PCLA** +31.0%: `catalyst_found: true` but every headline is a generic sector-mover roundup or about unrelated names (RH, AeroVironment). Nothing PicoCELA-specific. Market cap $11.2M, far under both floors, and price ($9.72) is still below yesterday's high ($10.58) anyway.
- **WLDSW** +30.7%: Covered above as the closest Swing structural fit. Worth repeating: the one ticker-specific headline is a dilutive warrant inducement raise, not a bullish story, alongside two halt notices. Looks like a halt-driven pop, not a trend to join.
- **RML** -26.5%: The one headline that reads ticker-relevant only mentions RML by proximity ("joins Cooper Companies, Navan and other big stocks moving lower"), it's not actually about RML specifically. Market cap unavailable (no SEC concept on file). No real story to trade.
- **HVIIU** +25.5%: Only headline in the packet is an IPO-release halt notice, this reads like a brand-new listing finding its first trading range, not a tradeable gap. Market cap unresolved.
- **SUNE** -25.3%: Headline says the stock was "soaring Wednesday," the opposite direction from today's -25.3% print. Stale headline, doesn't explain today's move. Down gap, not eligible either way.
- **FGL** -24.9%: `catalyst_found: true` but every headline is a generic industrials sector roundup or about an unrelated name (Mission Produce). Nothing Founder Group-specific. Down gap regardless.
- **NAVN** -21.8%: Real catalyst, analysts revising forecasts after Q2 results, a plausible explanation for the drop. Market cap unavailable (no SEC concept on file). Down gap, not eligible either way.
- **VNCE** -21.2%: Real catalysts, an earnings call transcript plus an acquisition announcement (OVO Operating Business, terms undisclosed). Down gap, not eligible for either list.
- **AIFU** -19.7%: Only ticker-specific headline is a CFO appointment, a routine personnel item that doesn't obviously explain a -19.7% move. Thin story for the size of the drop.
- **INTC** -5.6%: The one ticker-specific headline just asks "what's going on," no explanation attached in the packet. RVOL 32.3x says something real is happening, but the packet doesn't say what. Down gap, not eligible either way.
- **CIFR** -5.5%: Ticker-specific and direction-matched ("why is Cipher Digital falling"), but the packet gives no reason beyond the headline itself. Down gap, not eligible either way.
- **ORCL** -5.3%: Genuine mismatch. The attached headline says Oracle "beats revenue and EPS estimates, raises FY27 EPS guidance, stock rises," and the market news pull separately calls it a "cloud momentum" beat. The packet's own gap field has ORCL at -5.3% this morning. Either the headline is from an earlier session's reaction or premarket has since faded hard; either way, don't trust the "stock rises" framing against what the packet actually shows.
- **MARA** -4.2%: Ticker-specific and direction-matched, tied to a Bitcoin pullback per a separate headline. Down gap, not eligible either way.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
