# Premarket Report: September 22, 2026

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** All four index proxies are green: S&P 500 (via SPY) +1.56%, Dow (via DIA) +0.77%, Nasdaq (via QQQ) +2.78%, Russell 2000 (via IWM) +0.52%. Tech is leading. VIX, the 10 year, the 3 month, oil, and the dollar all came back null, yfinance rate limited every one of them even after retries.
- **The catch we're watching:** Seven large caps (AAL, BMNR, WBD, IBIT, SMCI, INTC, GRAL) are sitting between dead even and 2.4% under yesterday's high, real names with real stories (crypto, AI/chips, an M&A ruling), but this scan ran at 7:13am ET, before the open, so none of them have actually broken through yet. Both watchlists are empty for now.
- **Two-brain verdict:** Single brain, no second opinion to compare.

## Pre-Market Gappers

- **GRML** +230.5%: "Greenland Stocks Explode After Trump's Denmark Deal — GRML Up 245%"
- **VEEE** +100.9%: "12 Consumer Discretionary Stocks Moving In Monday's After-Market Session"
- **CRMU** +76.0%: "Trump, Greenland Deal Sparks CRML Trading Frenzy: These ETFs Rocket 75%"
- **CRMX** +74.8%: "Trump, Greenland Deal Sparks CRML Trading Frenzy: These ETFs Rocket 75%"
- **AVAZ** +70.7%: no catalyst headline in the packet (`catalyst_found: false`)
- **CRMLW** +65.0%: no catalyst headline in the packet (`catalyst_found: false`)
- **TXXS** +53.7%: "Trading Halt: Halt status updated at 9:40:00 AM ET: Quotation Resumption: New Issue Available"
- **SUIL** +53.7%: no catalyst headline in the packet (`catalyst_found: false`)
- **SVRN** +45.2%: "12 Industrials Stocks Moving In Monday's Intraday Session"
- **CRML** +38.6%: "Trump, Greenland Deal Sparks CRML Trading Frenzy: These ETFs Rocket 75%"
- **ARMA** +35.6%: "Corgi's ETF Pack Grows Yet Again with 24 New Leveraged and Buffer Launches"
- **SMX** -35.5%: "SMX Says Digital Material Passport Platform Can Support Tokenization Of Real-World Assets By Linking Authenticated Physical Materials To Digital Records; Extending Infrastructure Through Plastic Cycle Token"
- **GRAL** +33.7%: "Low False Positives and High Accuracy: FDA Document Fueling Grail Stock Surge"
- **NUAI** +30.6%: "New Era Locks in 20-Year Vistra Power Deal for Texas AI Data Center"
- **INTC** +12.0%: "Intel Shares Rise Over 5% After Key Trading Signal"
- **WBD** +10.7%: "Paramount's $110B Warner Bros. Discovery Merger Clears Legal Hurdle; Elizabeth Warren Says Letting Trump-Aligned Entity 'Dominate' News Is 'Disastrous'"
- **BMNR** +8.8%: "Why Is BitMine Immersion Stock Surging Monday?"
- **IBIT** +6.5%: "Bitcoin and ethereum prices today, Monday, September 21, 2026: Crypto prices hit highest levels in 8 months"
- **SMCI** +5.3%: "Super Micro Says AI Opportunity Could Reach $4 Trillion: 'The Sky's the Limit'"
- **AAL** +4.8%: "Why Is American Airlines Stock Surging on Thursday?"

## Day Trading Watchlist

No names cleared the day-trading bar today. That flag encodes gap over 3%, price over $3, market cap over $1B, premarket RVOL over 1.5, and price already breaking above yesterday's high.

Six of the cap-qualified names clear every leg of that rule except the last one, they just haven't broken above yesterday's high yet:

| Ticker | Price now | Prior day high | Gap to clear |
|---|---|---|---|
| AAL | $13.59 | $13.59 | 0.0% |
| BMNR | $28.235 | $28.33 | -0.3% |
| WBD | $30.80 | $30.92 | -0.4% |
| IBIT | $48.99 | $49.22 | -0.5% |
| SMCI | $41.18 | $41.72 | -1.3% |
| INTC | $121.73 | $124.69 | -2.4% |
| GRML | $9.42 | $11.64 | -19.1% |

AAL is sitting exactly on yesterday's high, it just needs one tick up to trigger. Two more names are close but incomplete on other legs: CRML is only 3.1% under its prior day high but its $978M market cap misses the $1B day-trading floor, and GRAL is only 3.0% under its prior day high but its RVOL field came back null this run (yfinance rate limited), so it can't be confirmed as clearing that leg either way.

GRML is the biggest gap of the day by far but it's the least close of this group, still 19.1% under yesterday's high, so despite RVOL of 2922x its 20-day average, it's not a near-miss.

This scan ran at 7:13am ET, well before the open, and the packet's own gaps-to-fill note says the scanner uses the current gap price as a stand-in for the real open. Treat the table above as directional, not exact, until the actual open prints.

## Swing Watchlist

No names cleared the swing bar either. That flag encodes gap of 8% or more, price over $3, open above yesterday's high, open above the 200-day SMA, market cap of $800M or more, and a real catalyst behind the move.

BMNR, WBD, GRAL, INTC, and NUAI all clear the 8% gap floor, the $800M cap floor, the 200-day SMA, and the catalyst check. All five are blocked only by the same "open above yesterday's high" leg as the day-trading table above, from -0.3% (BMNR) to -3.5% (NUAI, see the Skips and Traps note on that one).

CRML clears the gap, price, cap, and catalyst legs but fails two at once: its open ($9.33) is below both its prior day high ($9.63) and its own 200-day SMA ($9.67).

GRML clears the cap and catalyst legs easily and its 200-day SMA is tiny ($0.78) so that leg isn't close, but it's 19.1% under yesterday's high on the open-vs-high leg, same gap as the day-trading table.

IBIT, SMCI, and AAL don't even reach the 8% swing floor (6.5%, 5.3%, 4.8%), so they're day-trading-only near-misses, not swing near-misses.

## Market Trends of the Day

Tech is doing the heavy lifting this morning. Nasdaq (QQQ proxy) is up 2.78%, well ahead of the other three indices, and the market news feed backs that up: "Meta's stock is enjoying its best month in 13 years thanks to the company's hot new AI assistant," and INTC's own catalyst headline references "Meta's Muse Hits No. 1, Carrying AMD Into the $1-Trillion Club." AI infrastructure names (INTC, SMCI, NUAI's Vistra power deal) are all part of the same thread.

Crypto is the other clear group move. Bitcoin is at an 8-month high per the market news feed, "extreme greed" language is showing up in BMNR's own catalyst headlines, and both BMNR (+8.8%) and IBIT (+6.5%) are gapping up on it together, a coherent pair, not a coincidence.

Energy is a cross-current. "Morning Bid: As oil swoons, AI recharges" suggests oil is falling even as stocks rally, but the packet's own WTI Oil field came back null (yfinance rate limited), so there's no number to confirm that today. A separate item warns "Global diesel shortage from Iran, Ukraine wars to last into 2027," and airlines are "cutting capacity again amid $1B surge in Q4 fuel costs," a headline that lines up with AAL sitting on today's gapper list.

There's also a small geopolitical cluster driving several of today's biggest gap percentages: the Trump administration's Denmark/Greenland deal is the named catalyst behind GRML (+230.5%) and CRML (+38.6%), and that same CRML rally is what's cited (not always cleanly) for CRMU and CRMX too, see Skips and Traps.

Elsewhere, gold is "holding as Chinese gold imports set record" (a risk hedge even during a risk-on tech rally), and Home Depot's CFO is flagging a "frozen" housing market with a key metric at a historic low, worth knowing if that's relevant to any other positions.

## Technical Signals for Today

All four major index proxies came through green via Alpaca ETF data: S&P 500 (SPY proxy) +1.56%, Dow (DIA proxy) +0.77%, Nasdaq (QQQ proxy) +2.78%, Russell 2000 (IWM proxy) +0.52%. Nasdaq's lead over the other three is the clearest signal here, a tech-led tape. These are ETF stand-ins, not the actual index prints, so treat them as directional.

VIX, the 10-year yield, the 3-month yield, WTI crude, and the dollar index all came back null, yfinance rate limited them even after retries. No read on volatility, rates, or the dollar this morning.

## Economic Data, Rates and the Fed

Nothing on the calendar. The econ calendar (high-impact USD only) shows zero events for today, September 22, and zero for tomorrow, September 23.

## Coming Up

- **Tomorrow's events:** None in the calendar for September 23.
- **Earnings:** No forward earnings dates available. Every gapper's `next_earnings_date` field came back null this run. The packet's own gaps-to-fill note says 108 requests failed even after retries this scan, and the per-ticker enrichment log shows yfinance returning "Too Many Requests" on every single ticker's intraday, news, and earnings pull.

## Skips and Traps

**NUAI's gap has a real catalyst and a real red flag sitting side by side.** The Vistra 20-year power deal for a Texas AI data center is a genuine, specific, bullish catalyst and is likely what's actually driving the +30.6% move. But the packet also carries a fresh headline on the same ticker: "New Era Energy & Digital Q2 EPS $(0.21) Misses $(0.09) Estimate, Sales $36.497K Miss $433.333K Estimate," sales in the thousands against an $815M market cap. That's the kind of mismatch worth being suspicious of even though it's not the headline driving today's pop. NUAI was also the closest swing near-miss after BMNR/WBD/GRAL/INTC, 3.5% under its prior day high, so keep this one on the "watch, don't trust blindly" list if it does clear that leg later.

**CRMU and CRMX don't have their own news, they're riding CRML's.** Both tickers' only catalyst headline on file is "Trump, Greenland Deal Sparks CRML Trading Frenzy: These ETFs Rocket 75%," a story about CRML, a different ticker. Neither has market cap data (SEC EDGAR has no CIK for either, consistent with these being leveraged or derivative products rather than operating companies). If they're CRML-tracking products the indirect catalyst makes some sense, but there's nothing in the packet that says so directly. Thin data, don't treat as a clean trade.

**AVAZ, CRMLW, and SUIL are automatic skips.** `catalyst_found` is false for all three despite gaps of 70.7%, 65.0%, and 53.7%. Nothing in the packet explains why any of them are moving. Per the rules, no catalyst means no story, and no story means don't trade it.

**VEEE, SVRN, and ARMA have thin or generic catalysts.** VEEE and SVRN's only headlines are "stocks moving" roundup mentions, not distinct company news. ARMA's only headline is a generic leveraged-ETF product launch announcement, not anything specific to ARMA. `catalyst_found` is technically true for all three, but there's no real, fresh, ticker-specific story behind any of them in the packet.

**TXXS looks like a brand-new ETF listing, not a company move.** Its headlines are a "21shares 1-For-10 Reverse Stock Split" announcement and a trading halt tied to a new issue resuming quotation, alongside coverage of a new Sui-token leveraged ETF launch. A reverse split plus a new-issue halt right out of the gate makes gap and volume math unreliable here.

**GRML is the biggest gap on the board with a real catalyst, but it's not close to either bar.** The Trump-Denmark/Greenland deal is a genuine, fresh, ticker-specific story, but GRML is still 19.1% under yesterday's high, the furthest of any cap-qualified name, and RVOL is 2922x its 20-day average, extreme even for a gapper. Watch it, don't chase it.

**AAL's featured headline is stale.** "Why Is American Airlines Stock Surging on Thursday?" predates this scan by several sessions, today is Tuesday. The gap and price numbers are current, but the catalyst text on file isn't necessarily what's moving the stock this morning.

**Wide data blackout this run.** yfinance rate limited essentially every per-ticker intraday, news, and earnings pull, 108 requests failed even after retries. That's why VWAP, high/low of day, premarket high, premarket volume, and next earnings date are null for every single gapper, and why VIX, the 10-year, the 3-month, oil, and the dollar are all null too. Catalyst headlines mostly survived because they came from Alpaca and RSS, not yfinance.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
