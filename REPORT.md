# Premarket Report: September 10, 2026

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** Broad, quiet risk-off open. S&P proxy (SPY) -0.47%, Dow proxy (DIA) -0.76%, Nasdaq proxy (QQQ) -0.29%, Russell proxy (IWM) -1.36%, small caps leading the slide. Nothing in today's news pull points to a single driver behind it.
- **The catch we're watching:** Both watchlists are basically empty. SIG and YQ are the only cap-qualified up-gappers, and both are missing on a technicality rather than a clean fail: SIG is $0.51 under yesterday's high, and premarket RVOL is null for the entire packet this run (Yahoo rate-limited again), so the RVOL leg couldn't even be checked for either name. Also worth flagging: most of the per-ticker catalyst headlines in this packet are dated to Wednesday's session, not this Thursday premarket, so treat them as the most recent available news, not confirmed fresh catalysts for today's gap.
- **Two-brain verdict:** Single brain, no second opinion to compare.

## Pre-Market Gappers

- **SUNE** +90.3% - "Why Is SUNation Energy Stock Soaring Wednesday?"
- **RIBBU** +47.4% - "Reported Earlier, Ribbon Acquisition Corp Prices $50M Initial Public Offering Of 5M Units At $10/Unit"
- **DICE** -47.1% - "What 9 Analyst Ratings Have To Say About DICE Therapeutics"
- **IRD** +32.0% - "Gene Therapy at Lower Dose Shows Vision Improvements, Opus Genetics Says"
- **TTAN** -30.0% - "Why Is ServiceTitan Stock Sinking Wednesday?"
- **GRNQ** -29.6% - "Trading Halt: Halt status updated at 8:55:00 AM ET: Quotation Resumption: News and Resumption Times"
- **LEXX** -29.6% - "12 Health Care Stocks Moving In Wednesday's Intraday Session"
- **ODD** +26.5% - "Short Squeeze And Earnings: Why ODDITY Tech Stock Spiked Wednesday"
- **RIBB** +25.7% - "Nasdaq (NDAQ) Completed the Dasseti Acquisition to Deepen eVestment's Private-Market Capabilities"
- **WZRD** -24.1% - no catalyst headline in the packet
- **SIG** +24.0% - "Signet CEO Says 'Value' Will Rule Holiday Shopping As Consumers Feel the Squeeze"
- **BBOT** -23.8% - "Stifel Maintains Buy on BridgeBio Oncology, Lowers Price Target to $15"
- **TBBK** -22.3% - "Bancorp Bank To Exit SBL Loan Origination By Year-End 2026; Cuts 64 Jobs, Or 9% Of Workforce; Expects $5.6M Restructuring Charges; Targets $14M Annualized Savings, Or Over $20M Including Prior Reorganization"
- **BRZE** -21.7% - "Braze Stock Falls After Q2 Beat, Guidance Raise: Why Analysts See Buying Opportunity"
- **YQ** +20.6% - "17 Education & Technology Q2 Adj. EPS $0.06 Up From $(0.29) YoY, Sales $13.278M Up From $3.547M YoY"
- **TYRA** -17.7% - "Why Is Tyra Biosciences Stock Sinking Wednesday?"
- **CIFR** -8.8% - "What's Going On With Cipher Digital Stock Wednesday?"
- **CMCSA** -6.7% - "Comcast CFO Says Q3 Broadband Subscriber Losses Unlikely To Improve Year-Over-Year, Citing Pressure From Factors Including Rational Fiber Pricing"
- **ONDS** -4.5% - "Reported Earlier 'US Expanding Long-Range Commercial Drone Testing Program' - Bloomberg News"
- **PCG** -4.2% - "B of A Securities Maintains Neutral on PG&E, Raises Price Target to $14"

## Day Trading Watchlist

The "Trend Join Long" rule: gap over 3%, price over $3, market cap over $1B, premarket RVOL over 1.5, and price already breaking above yesterday's high.

No names cleared the day-trading bar today. The packet marks `day_eligible: false` on all 20 gappers. Only two up-gappers are even cap-qualified (over $1B) to begin with:

- **SIG** $102.48 vs prior high $102.99 (still under by about $0.51, RVOL unavailable)
- **YQ** $4.57 vs prior high $4.47 (already clears the prior-high leg, RVOL unavailable)

`intraday_data_source` is `unavailable` for every gapper this run, so premarket RVOL, premarket high, VWAP, HOD and LOD are all null across the board. That means the RVOL > 1.5 leg genuinely can't be checked for either name today, not that it failed. SIG also still needs about half a percent more to clear yesterday's high. Nothing here to trade off the packet as it stands; watch $102.99 on SIG for a live break later in the session.

## Swing Watchlist

The swing rule: gap of 8% or more, price over $3, open above yesterday's high, open above the 200-day SMA, market cap of $800M or more, and a real catalyst.

**YQ** (17 Education & Technology Group Inc.) is the only name that clears it, `swing_eligible: true`.

| Ticker | Catalyst | Trend context | Idea | Second-brain check | Conviction |
|---|---|---|---|---|---|
| YQ | Earnings on the gap day: Q2 adj. EPS $0.06, up from a $(0.29) loss a year ago, sales $13.278M vs $3.547M a year ago (a real, sizable jump, not a rounding-error beat). | Current price $4.57 is above yesterday's high of $4.47 and above the 200-day SMA of $2.92. Market hasn't opened yet, so this is the gap price standing in for the open, not a confirmed print. | Starter watch-and-build idea only off a real earnings beat. No stop, no target, swing management isn't built yet. | No second brain wired in, nothing to compare. | 🟡 |

**Why 🟡:** the catalyst itself is solid and doesn't trip either data-integrity red flag: market cap is $2,321,704,800 (over the $2B floor), and the $13.278M sales figure quoted in the headline is a real, growing revenue base, not a near-zero number dressed up against a big market cap. What's holding this back from 🟢 is that `intraday_data_source` is `unavailable` for YQ, so there's no premarket high, VWAP, HOD or LOD in the packet to confirm the gap is actually holding rather than fading. Real story, no live price confirmation yet, size down accordingly.

## Market Trends of the Day

Today's news pull is thinner on a single macro thread than most days. The clearest recurring items: the ECB looking "virtually certain" to raise rates with Wall Street bracing for what follows, and diesel prices hitting another record high, which MarketWatch frames as a lead-in to higher grocery costs. Both tie loosely into the inflation conversation ahead of tomorrow's CPI print. Copper is also flagged as trading at all-time highs, a commodities-strength data point sitting alongside the diesel story.

On the skepticism side, Bank of America is quoted saying the bar to disrupt AI "is surprisingly high," a mild counterpoint to the AI-buildout enthusiasm that's shown up in other days' feeds. Elsewhere, the DOJ is reportedly widening its probe into Fox's Roku deal, a regulatory story rather than a broad-tape one, and several of the Yahoo Finance headlines are single-company earnings reactions (Planet Labs, Zscaler, Capital Southwest, Roivant, Genworth, Tilly's, Methode, Yatsen) rather than anything that reads as a sector-wide theme.

Nothing in this pull directly explains the across-the-board red proxy prints below. Worth noting plainly rather than reaching for a story that isn't in the packet.

## Technical Signals for Today

The four major index rows in the packet are Alpaca ETF proxies, not the underlying indices, because the direct index pulls failed: S&P 500 proxy (SPY) 762.42, down 0.47%; Dow proxy (DIA) 524.05, down 0.76%; Nasdaq proxy (QQQ) 716.35, down 0.29%; Russell 2000 proxy (IWM) 290.69, down 1.36%. Treat these as ETF price levels, not literal index points. Russell/small-caps are underperforming the other three by a wide margin this morning.

VIX, the 10-year yield, the 3-month yield, WTI crude, and the Dollar Index all came back null this run (`yfinance_failed`), so there's nothing to report on volatility, rates, or the dollar directly from the packet today.

As covered above, SIG and YQ are the only two levels-based signals worth watching live: SIG needs about $0.51 more to clear yesterday's $102.99 high, and YQ is already through its $4.47 prior high on the gap price alone.

## Economic Data, Rates and the Fed

Today, September 10, brings two releases, both at 8:30am ET: Core PPI m/m (forecast 0.3%, previous 0.2%) and headline PPI m/m (forecast 0.4%, previous 0.0%). Both forecasts step up from last month's actuals. Tomorrow, September 11, is the bigger one: Core CPI m/m (forecast 0.2%, previous 0.2%), Core CPI y/y (forecast 2.4%, previous 2.5%), CPI m/m (forecast 0.4%, previous 0.1%), and CPI y/y (forecast 3.4%, previous 3.4%), all at 8:30am ET. The CPI m/m forecast stepping up 0.3 points from last month is the number to watch given the diesel/inflation framing in today's news pull.

## Coming Up

- **Tomorrow's events:** Core CPI m/m, Core CPI y/y, CPI m/m, and CPI y/y, all 8:30am ET, September 11.
- **Earnings:** `next_earnings_date` is null for every gapper in today's packet, so there's no confirmed date to flag for any of these names from the packet's own data.

## Skips and Traps

- **DICE** -47.1%: Every headline attached is about "DICE Therapeutics," an old ticker/entity, plus an unrelated election-betting ETF piece. Nothing in the packet actually dates to or explains today's -47% move on the current DICE. Market cap is unavailable (no CIK on file at SEC). Catalyst headline mismatch, don't trust the story here.
- **RIBBU** +47.4% / **RIBB** +25.7%: Same underlying company, Ribbon Acquisition Corp. RIBBU's real catalyst is a fresh $50M SPAC IPO (5M units at $10) with a halt notice showing the IPO security was just "Released for Quotation," so this reads like a brand-new listing finding its first trading range, not a tradeable gap. RIBB (the common shares) doesn't carry that headline at all, just generic sector-acquisition roundups (Nasdaq/Dasseti, LTC senior-housing, Ryman Grande Lakes) that aren't about Ribbon specifically. Market caps ($74.7M / $68.6M) are under both floors regardless.
- **GRNQ** -29.6%: Only ticker-specific item is a bare trading-halt/resumption notice, no explanation of why. Market cap $239.8M is under both floors anyway. No real story to trade.
- **LEXX** -29.6%: `catalyst_found: true` but every headline attached is a generic "Health Care Stocks Moving" sector roundup, nothing Lexaria-specific in this packet. Market cap $163.6M, under both floors.
- **WZRD** -24.1%: `catalyst_found: false`, no headlines in the packet at all. Skip automatically per the rules.
- **CIFR** -8.8%: The Cipher Digital headlines ask "why is it surging" on Tuesday and again on Thursday, other days, not an explanation for today's -8.8% red print specifically. Not eligible for either watchlist anyway since it's a down gap.
- **SIG** +24.0%: Covered above as the closest Day Trading miss. Worth repeating here: the one ticker-specific headline is CEO commentary about "value" ruling holiday shopping, thin and not clearly bullish, doesn't obviously explain a 24% pop on its own.
- **TBBK** -22.3%: Real catalyst, and it's bad news: exiting SBL loan origination, cutting 64 jobs (9% of headcount), a $5.6M restructuring charge. That honestly explains the drop, this isn't a trap, it's a name reacting rationally to bad news. Down gap, not eligible for either list.
- **BRZE** -21.7%: Textbook sell-the-news setup. The headline itself says Braze beat Q2 and raised guidance, and the stock is still down over 21%, with the same headline noting analysts see it as a buying opportunity. Not something either rule-based playbook here is built to catch.
- **CMCSA** -6.7%: Comcast's own CFO flagged Q3 broadband subscriber losses "unlikely to improve," real negative guidance behind the drop. Down gap, not eligible for either list.
- **ONDS** -4.5%: Catalyst mismatch. The Bloomberg drone-testing-expansion headline is genuinely Ondas-relevant, but it's framed as positive news attached to a stock that's gapping down, and a separate headline literally asks "why is Ondas falling on Monday," a different day entirely. Nothing here cleanly explains this morning's red print.
- **PCG** -4.2%: Catalyst is BofA maintaining Neutral with a $14 price target, close to where it's already trading. Thin, not a real driver of a 4% move either way, and it's a down gap regardless.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
