# Premarket Report: September 23, 2026

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** Mixed to slightly green. Nasdaq (QQQ proxy) leads at +0.81%, Russell 2000 (IWM proxy) +0.57%, S&P 500 (SPY proxy) flat at -0.01%, Dow (DIA proxy) lags at -0.36%. VIX, the 10 year, the 3 month, oil, and the dollar all came back null, yfinance rate limited every one of them even after retries.
- **The catch we're watching:** Most of today's "big gap" numbers on the gapper list don't hold up. For most tickers the packet's own `prior_close` field (from the daily bars feed) sits within a percent or two of today's price, while the `gap_pct` field is computed off a different, older `prev_close` value. See Skips and Traps, this affects the majority of today's list including the two biggest headline movers, JAGX and GRML.
- **Two-brain verdict:** Single brain, no second opinion to compare.

## Pre-Market Gappers

- **JAGX** +1190.6%: "Jaguar Health Stock Surged 1200% on Tuesday: Here's Why JAGX Stock Is Trending After Hours"
- **ENRG** +60.3%: no catalyst headline in the packet (`catalyst_found: false`)
- **GRML** +50.2%: "Stock Market Today: S&P 500, Dow, Futures Gain Nasdaq 100 Slips as Trump Administration Targets Iranian Airlines— Lennar, Greenland Mines, Accenture in Focus (UPDATED)"
- **VKTX** +35.7%: "Jaguar Health, IONQ, Viking Therapeutics, Xanadu Quantum and Grab Holdings: Why These 5 Stocks Are on Investors' Radars Today"
- **IMCC** +34.2%: "12 Health Care Stocks Moving In Tuesday's Intraday Session"
- **HUBC** -29.3%: "Hub Cyber Security Signs ~$8.7M Deal To Divest QPoint Group To Malam Team Group"
- **INDP** +29.1%: "Radiant Logistics, Waystar, Forgent Power Solutions And Other Big Stocks Moving Higher On Tuesday"
- **MAZE** +26.8%: "BTIG Reiterates Buy on Maze Therapeutics, Maintains $46 Price Target"
- **STFS** +26.2%: "12 Communication Services Stocks Moving In Tuesday's After-Market Session"
- **NFE** -24.7%: "New Fortress Energy Secures UK Court Approval For Restructuring Plan, With Next Phase Set For U.S. Recognition Hearing And Q3 2026 Implementation Timeline"
- **AIFU** -22.1%: "AIFU Announces Appointment Of Shanyu Chang As CFO Effective Immediately"
- **BFLY** +22.0%: "Butterfly Network Stock Soars After Needham Initiates Buy"
- **XNDU** -21.6%: "Xanadu Stock Hits New Lows: What's Happening?"
- **DCOY** +21.1%: "Why Worthington Enterprises Shares Are Trading Higher By Around 16%; Here Are 20 Stocks Moving Premarket"
- **EDRY** -20.4%: "EuroDry Q2 Adj. EPS $2.44 Beats $1.23 Estimate, Sales $17.700M Miss $17.855M Estimate"
- **AUC** +20.1%: "12 Industrials Stocks Moving In Tuesday's Pre-Market Session"
- **SNDQ** -13.4%: "SanDisk, Lumentum Rally Sparks Bearish Plays As Tradr Rolls Out 2X Short ETFs"
- **SNXX** +13.3%: "SanDisk Earnings Beat Triggers 20% Premarket Hit In These ETFs"
- **GRAB** +8.8%: "Grab Makes $1.49 Billion Fintech Bet, Takes Control of Atome Financial"
- **ONDS** +4.7%: "Ondas Adds Critical Weapons Tech In $205 Million Deal"

## Day Trading Watchlist

No names cleared the day-trading bar today. That flag encodes gap over 3%, price over $3, market cap over $1B, premarket RVOL over 1.5, and price already breaking above yesterday's high.

Five cap-qualified, up-gapping names clear the other legs and are blocked only by "price hasn't broken above yesterday's high yet":

| Ticker | Price now | Prior day high | Gap to clear | RVOL |
|---|---|---|---|---|
| ONDS | $7.73 | $7.75 | -0.3% | 45.4x |
| VKTX | $40.85 | $41.69 | -2.0% | null |
| MAZE | $28.38 | $29.21 | -2.8% | null |
| JAGX | $34.46 | $41.35 | -16.7% | null |
| GRML | $14.15 | $17.92 | -21.0% | null |

ONDS is the closest, a hair under a full percent from its prior day high, and it's the one name here with a confirmed RVOL (45.4x its norm) and a real, specific catalyst, a $205M weapons-tech deal. VKTX and MAZE are close too but their RVOL came back null this run (yfinance rate limited), so that leg can't be confirmed either way. JAGX and GRML are the furthest out, and see Skips and Traps below on why their headline gap sizes are misleading.

This scan ran premarket (7:20am ET), before the real open prints. Treat the table as directional until the actual open is in.

## Swing Watchlist

No names cleared the swing bar either. That flag encodes gap of 8% or more, price over $3, open above yesterday's high, open above the 200-day SMA, market cap of $800M or more, and a real catalyst behind the move.

JAGX, GRML, and VKTX all clear the gap floor, price floor, cap floor, 200-day SMA, and catalyst check, and are blocked only by the same "open above yesterday's high" leg as the day-trading table: VKTX is closest at -2.0%, then JAGX at -16.7%, then GRML at -21.0%.

MAZE fails two legs at once: its open ($28.38) is below both its prior day high ($29.21, -2.8%) and its own 200-day SMA ($33.54, -15.4%).

ONDS doesn't reach the 8% swing floor (4.7% gap), so it's a day-trading-only near-miss, not a swing one.

## Market Trends of the Day

The tape is split by index today rather than moving as one block. Nasdaq (QQQ proxy, +0.81%) and Russell 2000 (IWM proxy, +0.57%) are green, S&P 500 (SPY proxy) is flat at -0.01%, and Dow (DIA proxy) is the laggard at -0.36%. The market news feed backs up a tech/AI lean: "The AI-infrastructure trade is still not over, says this top-performing fund manager" and "Dow Jones Futures: Nasdaq Hits New High; Sandisk, Micron Trigger Buy Signals" both point the same direction, and that Sandisk story lines up with SNDQ and SNXX both showing up on today's gapper list as leveraged ETF products tracking SanDisk (see Skips and Traps).

"Financial stocks are falling as rates rise. Why that's a problem for the broader market" is the one clear headwind story in the news feed, a cross-current against the Nasdaq/Russell strength.

A macro item, "Stock market today: Dow, S&P 500, Nasdaq futures muted as oil falls, markets eye looming Trump-Xi meeting," matches the flat-to-mixed index picture, and a Greenland-related headline ("Trump Administration Targets Iranian Airlines...Lennar, Greenland Mines, Accenture in Focus") is the only company-adjacent context in the packet for GRML's spot on the gapper list, though as noted below it doesn't actually explain the move.

## Technical Signals for Today

Index proxies via Alpaca ETF data: S&P 500 (SPY) -0.01%, Dow (DIA) -0.36%, Nasdaq (QQQ) +0.81%, Russell 2000 (IWM) +0.57%. Nasdaq and Russell both green while Dow is red is a narrow, tech/small-cap-led tape rather than a broad risk-on day. These are ETF stand-ins, not the actual index prints, treat them as directional.

VIX, the 10-year yield, the 3-month yield, WTI crude, and the dollar index all came back null, yfinance rate limited them even after retries. No read on volatility, rates, or the dollar this morning.

## Economic Data, Rates and the Fed

Nothing on the calendar. The econ calendar (high-impact USD only) shows zero events for today, September 23, and zero for tomorrow, September 24.

## Coming Up

- **Tomorrow's events:** None in the calendar for September 24.
- **Earnings:** No forward earnings dates available. Every gapper's `next_earnings_date` field came back null this run, part of the same 85-request failure count noted in the packet's gaps-to-fill.

## Skips and Traps

**Most of today's headline gap sizes don't match the packet's own daily-bars data.** Every gapper carries two different "yesterday" reference prices: `prev_close` (used to compute the `gap_pct` shown on the list) and `prior_close` (pulled separately from the daily bars feed, the same source behind `prior_day_high`). For most of today's list the two disagree, and the price sitting right next to `prior_close` is barely moved. JAGX's `gap_pct` says +1190.6%, but its price ($34.46) is only 2.4% above its `prior_close` ($33.67), the +1200% move the packet's own headline references already happened in a prior session and the reference price used for `gap_pct` never caught up. GRML is the same shape: +50.2% on `gap_pct`, but only +0.4% versus `prior_close` ($14.09). VKTX, IMCC, MAZE, BFLY, XNDU, DCOY, NFE, SNDQ, SNXX, GRAB, and ONDS all show the same pattern, real move under 1% versus `prior_close` while `gap_pct` shows double digits. Treat the `gap_pct` field with real skepticism today, the eligibility engine correctly uses `prior_day_high`/`prior_close` rather than `gap_pct` for the day-trading and swing rules, which is a lot of why both watchlists came back empty despite the huge numbers on the gapper list.

Two names buck that pattern and look like real moves: **STFS** (+18.1% versus `prior_close`, roughly matching its +26.2% `gap_pct`) and **HUBC** (-8.0% versus `prior_close`, smaller than its -29.3% `gap_pct` but a real, same-direction decline). STFS's only headlines are generic "stocks moving" roundups though, no distinct company news behind the real move. HUBC's decline lines up with a real, specific headline, a deal to divest its QPoint Group unit, so the drop is at least explainable, but its $153.7M cap is well under both the $1B day-trading floor and the $800M swing floor either way.

**AUC runs the opposite direction: its real move looks bigger than the headline.** `gap_pct` shows +20.1%, but price versus `prior_close` is +37.9%. Regardless of which number is right, `avg_volume_20d` is 5 shares, essentially untradeable liquidity, so this one's a skip on liquidity alone.

**ENRG is an automatic skip.** `catalyst_found` is false despite a 60.3% `gap_pct`. Nothing in the packet explains why it's moving, and per the rules, no catalyst means no story.

**GRML's catalyst headlines don't actually name GRML.** Its two most relevant-looking headlines are a general "Trump Administration Targets Iranian Airlines...Greenland Mines...in Focus" roundup and a "12 Health Care Stocks Moving" mention, neither explains what's specifically happening at Greenland Mines, and the health-care categorization looks like a miscategorized mover-list mention rather than real GRML news. Combined with the stale `gap_pct` issue above, treat GRML's spot on this list as noisy, not a clean story.

**VKTX and MAZE also have generic, not ticker-specific, catalyst text.** VKTX's headlines are all "stocks moving/radar" roundup mentions. MAZE's most relevant headline, a BTIG buy reiteration with a $46 price target, is real and specific, but its other headlines are Q1/Q2 earnings prints from prior quarters, not today's catalyst. Both are technically `catalyst_found: true`, but neither has a fresh, ticker-specific news story explaining today's number in the packet.

**DCOY is a classic thin-microcap trap.** $2.0M market cap, average 20-day volume of 24,440 shares against 105M shares today, RVOL is effectively off the charts, and its catalyst headlines are all generic mover-roundup mentions, nothing DCOY-specific. Combined with the stale `gap_pct` issue (its real move versus `prior_close` is +0.3%), there's no real story here.

**SNDQ and SNXX are leveraged ETF products tracking SanDisk, not SanDisk itself.** Their headlines reference "Tradr Rolls Out 2X Short ETFs" and "SanDisk Earnings Beat Triggers 20% Premarket Hit In These ETFs." Neither has market cap data (SEC EDGAR has no CIK for either, consistent with derivative products rather than operating companies). Same shape as prior sessions' CRMU/CRMX riding CRML's news.

**NFE and AIFU are declining on real, explainable news, not traps, but neither is a long setup.** NFE's headlines show a CFO resignation and a UK court restructuring approval, a company mid-bankruptcy-proceeding, its decline is consistent with that. AIFU's decline (-5.0% versus `prior_close`) doesn't have an obviously matching negative headline in the packet, just a CFO appointment and a trading-halt resumption notice, worth treating as unexplained rather than confirmed bad news.

**BFLY and GRAB have real, specific catalysts but no market cap data to qualify them.** BFLY: a Needham buy initiation plus a named partnership deal with Merge Labs. GRAB: a $1.49B acquisition of Atome Financial. Both are missing `market_cap` (SEC EDGAR has no CIK or the relevant filing concept for either), so neither can clear the $800M-$1B cap floors on either watchlist even with real news behind them.

**Wide data blackout this run.** 85 requests failed even after retries this scan, the per-ticker enrichment log shows yfinance returning "Too Many Requests" on essentially every single ticker's intraday, news, and earnings pull. That's why RVOL, VWAP, high/low of day, premarket high, premarket volume, and next earnings date are null for most gappers, and why VIX, the 10-year, the 3-month, oil, and the dollar are all null too. Catalyst headlines mostly survived because they came from Alpaca and RSS, not yfinance. Market cap for 6 names (ENRG, BFLY, XNDU, SNDQ, SNXX, GRAB) is unavailable even after the SEC EDGAR fallback.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
