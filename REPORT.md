# Premarket Report: September 24, 2026

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** Broad red morning via the ETF proxies. Russell 2000 (IWM proxy) leads down at -1.8%, Nasdaq (QQQ proxy) -0.84%, S&P 500 (SPY proxy) -0.71%, Dow (DIA proxy) -0.67%. VIX, the 10 year, the 3 month, oil, and the dollar all came back null, yfinance rate limited every one of them even after retries.
- **The catch we're watching:** Almost none of today's gapper list is actually gapping. 18 of 20 names show a real move under 2% versus the packet's own `prior_close` field, while `gap_pct` (computed off a stale `prev_close`) shows double or triple digits for the same names. Only **HVIIU** (a real -58.6% crash tied to a SPAC unit resuming quotation) and **AIFU** (a real +13.0% move) are genuinely moving today. See Skips and Traps for the full breakdown, this is why both watchlists came back empty.
- **Two-brain verdict:** Single brain, no second opinion to compare.

## Pre-Market Gappers

- **WHLR** +190.9%: "Wheeler Real Estate Investment Trust Announces 1-For-9 Reverse Stock Split Effective September 21, 2026"
- **VSA** +83.8%: "VisionSys AI Shares Halted On Circuit Breaker To The Upside, Stock Now Up 87.88%"
- **ARTL** +76.1%: "Artelo Biosciences Files Provisional Patent Application For ART27.13 As Monotherapy And In Combination With GLP-1 Receptor Agonists"
- **JAGX** -74.1%: "Jaguar Health Stock Plunges Wednesday: What's Happening?"
- **HVIIU** -55.3%: "Trading Halt: Halt status updated at 10:35:00 AM ET: Quotation Resumption: IPO Security - Released for Quotation"
- **HVII** -50.9%: "Hennessy Capital Investment (HVII) Rebounds 17% After Hours — ONE Nuclear Merger Complete"
- **IPDN** +39.0%: "12 Industrials Stocks Moving In Wednesday's Pre-Market Session"
- **TJGC** +37.8%: "TJGC Group Announces $2M Stock Repurchase Program"
- **HUBC** -24.3%: "Hub Cyber Security Announces 1-For-25 Reverse Stock Split, Effective Sept. 11"
- **DCOY** +24.2%: "12 Health Care Stocks Moving In Wednesday's Pre-Market Session"
- **EOSU** -23.4%: "New ETF Gives Traders 2X Exposure To A Buzzing Energy Storage Name"
- **CGEM** -22.2%: "BTIG Maintains Buy on Cullinan Therapeutics, Raises Price Target to $40"
- **NFE** -21.5%: "New Fortress Energy Announces 1-For-50 Reverse Stock Split Effective September 11"
- **GRML** -20.9%: "Greenland Mines Fully Funds 2027 Milestones With $42M Raise At $12.00 Per Share, Wraps Sarfartoq NdPr Field Program"
- **ALKT** -19.3%: "Alkami Concludes Strategic Review, Will Remain Independent Public Company; Reaffirms Full-Year Revenue Guidance Of $528M-$531M"
- **AIFU** +19.0%: "AIFU Announces Appointment Of Shanyu Chang As CFO Effective Immediately"
- **CDE** -5.7%: "Coeur Mining Says It Expects To Invest Record $158M In Exploration In 2026; Figure Reflects The Midpoint Of Guidance As Published By Coeur On August 5, 2026."
- **ONDS** -4.5%: "Ondas Acquires Three Defense Businesses, Insignito, Ottopia Defense And Caribou Labs, For $56M In Cash Or ONDS Stock With Total Potential Earnout Of Up To $32M"
- **IONQ** +4.4%: "IonQ Removes Major Quantum Barrier, Driving Investor Debate Over Commercial Timelines"
- **HL** -4.0%: "RBC Capital Maintains Outperform on Hecla Mining, Lowers Price Target to $20"

## Day Trading Watchlist

No names cleared the day-trading bar today. That flag encodes gap over 3%, price over $3, market cap over $1B, premarket RVOL over 1.5, and price already breaking above yesterday's high.

One name is a genuine near miss, blocked on a leg the data can't confirm either way:

| Ticker | Price now | Prior day high | Above prior high | RVOL | Market cap |
|---|---|---|---|---|---|
| AIFU | $10.17 | $9.00 | +13.0% | null (yfinance rate limited) | $11.5B |

AIFU is the only ticker on today's list actually sitting above its prior day high right now, and its $11.5B market cap clears the $1B floor easily. The only leg keeping it off the list is premarket RVOL, which came back null this run, so it can't be confirmed above the 1.5x bar or ruled out. Its catalyst is a CFO appointment, thin on its own for a real 13% move, and there's also a same-morning trading halt/resumption notice in the packet, so there's real volatility here even if the "why" isn't fully nailed down. Watch it, don't assume the setup is live until RVOL confirms.

TJGC's price ($23.28) sits exactly at its prior day high ($23.28), not above it, so it doesn't clear this leg either.

This scan ran premarket (7:21am ET), before the real open prints. Treat this as directional until the actual open is in.

## Swing Watchlist

No names cleared the swing bar either. That flag encodes gap of 8% or more, price over $3, open above yesterday's high, open above the 200-day SMA, market cap of $800M or more, and a real catalyst behind the move.

AIFU is the closest thing to a candidate: its real move (+13.0% versus `prior_close`) clears the 8% floor, price is over $3, market cap is $11.5B, and it has a catalyst. But its open ($10.17, standing in for the real open since it's still premarket) sits below its 200-day SMA ($12.51), about 19% under, so it fails that leg outright. No other name on the list shows a real move anywhere close to 8%, see Skips and Traps below for why the headline `gap_pct` numbers can't be trusted for that check today.

## Market Trends of the Day

This is a risk-off morning led by small caps: the Russell 2000 (IWM proxy) is down 1.8%, worse than the Nasdaq (-0.84%), S&P 500 (-0.71%), and Dow (-0.67%). The market news feed backs up a rates-driven story behind it: "The market is pricing in too many Fed hikes, says one former Dallas Fed chief" and "Black Monday's stock-market warning signal came from the bond market, and it's back, says Wall Street veteran" both point at rate anxiety as the pressure point, and a headline surfaced in IONQ's own catalyst list, "Nasdaq 100 Slips, 10-Year Yields Hit 19-Year Highs," lines up with that.

Mining and metals are taking it on the chin specifically: HL's catalyst headlines include "Warsh's Remarks Are Sinking Mining Stocks: Here's Why," and both HL and CDE are red this morning, a sector-specific hit layered on top of the broader risk-off tape (see Skips and Traps for a note on RBC and Jefferies still carrying constructive ratings on HL despite the drop).

There's an AI-trade undercurrent running against the risk-off grain: "As the Trump-Xi meetings unfold, investors should watch for this hidden AI trade" and "Meta sees a price-target boost as JPMorgan says Muse agent has potential to become the top AI application since ChatGPT" are both in today's news feed, and IONQ's quantum-computing catalyst cluster ("IonQ Removes Major Quantum Barrier," "IonQ Makes First On-Premise Quantum Deployment At NVIDIA Research Center") fits the same AI-adjacent theme, though IONQ's real gap (+4.4%) isn't big enough to clear either watchlist.

## Technical Signals for Today

Index proxies via Alpaca ETF data: S&P 500 (SPY) -0.71%, Dow (DIA) -0.67%, Nasdaq (QQQ) -0.84%, Russell 2000 (IWM) -1.8%. Small caps underperforming large caps by more than a point is a classic risk-off signature, not a narrow single-sector pullback.

VIX, the 10-year yield, the 3-month yield, WTI crude, and the dollar index all came back null, yfinance rate limited them even after retries. No direct read on volatility, rates, or the dollar this morning from the snapshot data. The one rates data point in the packet is secondhand, a headline in market_news referencing 10-year yields at 19-year highs, not a hard snapshot number, so treat it as color, not confirmed.

## Economic Data, Rates and the Fed

The econ calendar came back completely empty. The packet's own note: "Live fetch failed and no cache available: 429 Client Error: Too Many Requests." Zero events for today, zero for tomorrow, and the calendar couldn't even resolve what "today" and "tomorrow" are supposed to be. No calendar read at all this morning.

What color there is comes from the separate market_news feed, which did work: "The market is pricing in too many Fed hikes, says one former Dallas Fed chief" and "Black Monday's stock-market warning signal came from the bond market, and it's back, says Wall Street veteran" both point at hawkish Fed positioning as a live worry today, and mining stocks (HL, CDE) are reacting to "Warsh's Remarks" per HL's own catalyst headlines.

## Coming Up

- **Tomorrow's events:** None available, the calendar fetch failed (429 rate limited, no cache to fall back on).
- **Earnings:** No forward earnings dates available. Every gapper's `next_earnings_date` field came back null this run, part of the same request-failure count noted in the packet's gaps-to-fill.

## Skips and Traps

**Most of today's headline gap sizes are stale, not real.** Every gapper carries two different "yesterday" reference prices: `prev_close` (used to compute the `gap_pct` shown on the gapper list) and `prior_close` (pulled from the daily bars feed, the same source behind `prior_day_high`). For 18 of today's 20 names, the two disagree badly, real move versus `prior_close` is under 2% while `gap_pct` shows double or triple digits. WHLR is the extreme case: `gap_pct` says +190.9%, but price ($5.44) is actually 0.91% below `prior_close` ($5.49), a small decline, not a huge gap up. JAGX (`gap_pct` -74.1%, real move -0.45%), GRML (-20.9% vs +1.63% real), ARTL (+76.1% vs +0.55% real), CGEM (-22.2% vs 0.0% real), ALKT (-19.3% vs +0.07% real), IPDN, TJGC, HUBC, DCOY, EOSU, NFE, CDE, ONDS, IONQ, and HL all show the same shape. The eligibility engine correctly uses `prior_day_high`/`prior_close` rather than `gap_pct` for both watchlists, which is exactly why both came back empty despite the huge numbers up top. Treat the `gap_pct` column with real skepticism today.

**AIFU and HVIIU are the two real movers.** AIFU is up a genuine 13.0% versus `prior_close`, discussed above as the lone day-trading-shape near miss. HVIIU is down a genuine 58.6%, its only headline is a trading-halt/quotation-resumption notice tagging it as an "IPO Security," and it's paired with HVII (same Hennessy Capital Investment/ONE Nuclear Energy complex) whose headlines show a shareholder vote approving the business combination and a "Rebounds 17% After Hours" note. This looks like a SPAC-to-operating-company conversion event, not a tradeable premarket gap, and HVIIU has no market cap data either (SEC EDGAR has no matching filing concept). Skip both, this is corporate-action noise, not a setup.

**WHLR has no real catalyst behind it, its own headlines are about other companies.** Three of its five headlines are generic "stocks moving premarket" roundups naming Worthington Enterprises, Alaunos Therapeutics, SAIC, and General Mills, not WHLR. The only WHLR-specific item is a week-old reverse split announcement (effective September 21). Combined with the stale `gap_pct` above and a $10.5M market cap, there's no story here.

**IPDN and DCOY have no ticker-specific catalyst at all.** Every headline the packet has for either is a generic sector "stocks moving" roundup or a mention of a different company (Worthington Enterprises, Thor Industries). `catalyst_found` is technically true because some headline exists, but neither headline explains what's actually happening at either company. Skip on catalyst quality.

**EOSU looks like a leveraged ETF, not the underlying stock.** Its only headline: "New ETF Gives Traders 2X Exposure To A Buzzing Energy Storage Name." It has no market cap (SEC EDGAR has no CIK for it) and no company name resolved in the packet. Same shape as leveraged single-stock ETPs flagged in prior sessions, treat this as a derivative product, not an operating company.

**TJGC's catalyst is mixed, not clean.** Its headlines show both a $2M stock buyback (bullish signal) and a $100M mixed shelf prospectus filing (a large potential future dilution overhang) around the same time. Real move versus `prior_close` is 0.0% though, so nothing has actually happened price-wise yet, worth a watch for how the market resolves that tension, not a trade today.

**CGEM and ALKT are both down on `gap_pct` despite genuinely good news, and neither actually moved.** CGEM's headlines include a BTIG Buy reiteration with a $40 price target, an HC Wainwright Buy at $30, and positive Phase 3 trial data from earlier this month, none of that is bad news. ALKT's headline shows it concluded a strategic review by staying independent, reaffirmed full-year guidance of $528M-$531M, and got a JPMorgan price-target raise to $24. Both show a 0% real move versus `prior_close`, so the negative `gap_pct` numbers (-22.2% and -19.3%) are pure stale-reference artifacts, not a market reaction to bad news.

**ARTL has a real, specific catalyst that the price hasn't caught up to.** "Artelo Biosciences Files Provisional Patent Application For ART27.13 As Monotherapy And In Combination With GLP-1 Receptor Agonists" is a genuine ARTL-specific headline, but the real move versus `prior_close` is only +0.55%. The +76.1% `gap_pct` number is noise from the stale reference price, not a reaction to this news.

**HUBC and NFE both carry recent reverse splits, not fresh news, behind their large `gap_pct` numbers.** HUBC did a 1-for-25 split effective September 11, NFE did a 1-for-50 effective September 11 (NFE also shows a CFO resignation and a "halt news pending" notice). Both show real moves near flat versus `prior_close` (+1.26% and -1.54%), so today's headline percentages don't reflect anything new happening today.

**Wide data blackout this run.** The packet logs 87 failed requests even after retries, the per-ticker enrichment log shows yfinance returning "Too Many Requests" on essentially every ticker's intraday, news, and earnings pull. That's why RVOL, VWAP, high/low of day, and premarket high are null for nearly every gapper, why VIX, the 10-year, the 3-month, oil, and the dollar are all null, and why every `next_earnings_date` came back empty. The econ calendar failed outright (429, no cache). Market cap is unavailable even after the SEC EDGAR fallback for HVIIU, HVII, and EOSU specifically.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
