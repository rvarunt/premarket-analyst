# Premarket Report: August 28, 2026

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** Green across the board but nothing dramatic. Index proxies show S&P (SPY) +0.68%, Nasdaq (QQQ) +1.39%, Dow (DIA) +0.17% and Russell 2000 (IWM) +0.29%. Nasdaq is the leader, tracking a wave of strong tech earnings from Nvidia, Salesforce, CrowdStrike and Okta.
- **The catch we're watching:** Total intraday blackout again, all 20 gappers come back `intraday_data_source: unavailable`, so there's no premarket high, VWAP, HOD or LOD to confirm a breakout for anyone. On top of that, the rules engine flagged **GENVR** (mapped to Gen Digital Inc.) as `swing_eligible: true`, the first name to clear that bar in weeks, but none of its five headlines are actually about Gen Digital, they're all generic "stocks moving" listicles, and its 20-day average volume is a paper-thin 1,024 shares for a name carrying a $2.93B market cap. That combination looks like a bad ticker match more than a real trade, so it comes off the watchlist under the catalyst check. VIX, the 10-year, the 3-month, oil and the dollar all came back null again (113 failed requests even after retries), and market cap is missing for 7 of the 20 gappers.
- **Two-brain verdict:** Single-brain run today, no second opinion to compare against.

## Pre-Market Gappers

- **DSPC** +158.9% - "Want To Bet Against Cathie Wood? There's A New ETF For That" (all four of DSPC's headlines in the packet are 2021 SPAC-era stories, none dated today or specific to DSPC)
- **OKTG** +56.94% - "Okta Earnings Spark 53% Surge in This ETF: What Traders Need to Know" (per the headline itself, a leveraged ETF tracking Okta, riding OKTA's earnings pop)
- **CRMG** +44.26% - no catalyst found in the packet
- **CRWL** +39.83% - "CrowdStrike's AI-Fueled Plot Twist Has These ETFs Flying 38% Higher" (per the headline, a leveraged ETF tracking CrowdStrike)
- **CRWC** +39.7% - "CrowdStrike's AI-Fueled Plot Twist Has These ETFs Flying 38% Higher" (same story, a second leveraged CrowdStrike-linked ETF)
- **BRNX** -38.14% - "BrenX Shares Halted On Circuit Breaker To The Upside, Stock Now Up 54.49%" (a stale halt notice describing an earlier upside move, contradicts today's -38.14% gap down)
- **USDE** +34.95% - "12 Information Technology Stocks Moving In Thursday's Intraday Session" (none of USDE's five headlines name the company specifically, all generic mover-list mentions)
- **WNW** +33.47% - "Meiwu Technology (WNW) Stock Soars 48% After Hours: Here's What You Need to Know"
- **WETO** -33.45% - "12 Industrials Stocks Moving In Thursday's After-Market Session" (no WETO-specific headline dated today, the rest are generic listicles and a stale Fed inflation-gauge market summary)
- **FVNNU** -33.31% - "Trading Halt: Halt status updated at 10:35:00 AM ET: Quotation Resumption: IPO Security - Released for Quotation" (dated 2024, unrelated to today's move)
- **OKTA** +28.63% - "Macquarie Maintains Outperform on Okta, Raises Price Target to $185"
- **BBW** -27.26% - "Build-A-Bear Stock Sinks as Weak Traffic, Guidance Cut Hit Sentiment"
- **GENVR** +24.37% - "12 Information Technology Stocks Moving In Tuesday's Intraday Session" (none of GENVR's five headlines name Gen Digital specifically, all generic mover-list mentions)
- **CRM** +22.58% - "Snowflake Stock Rises as Salesforce's Beat Lifts Enterprise Software"
- **PURR** +10.86% - "Hyperliquid Strategies Q4 EPS $6.24, Sales $6.334M Beat $3.000M Estimate"
- **NVDA** +8.77% - "Nvidia Posts Record $96.2B Revenue, Shares Jump on $108B Outlook"
- **ONDS** +6.7% - "Reported Earlier \"US Expanding Long-Range Commercial Drone Testing Program\" - Bloomberg News"
- **MARA** +5.61% - "Why Is MARA Stock Surging Friday?" (this headline's article ID places it a week before today, it reads like it's about last Friday, not a same-day catalyst)
- **KEEL** +4.32% - "Keel Infrastructure Q2 Earnings Miss Estimates as Bitcoin Wind-Down Continues" (an older headline in the packet, not dated to today's specific move)
- **INTC** +4.28% - "Why Is Intel Stock Surging on Thursday?" (yesterday's session, carrying over into today's premarket, tied to Nvidia's reported equity stake in Intel)

## Day Trading Watchlist

The "Trend Join Long" rule: gap over 3%, price over $3, market cap over $1B, premarket RVOL over 1.5, and price already breaking above yesterday's high.

No names cleared the day-trading bar today. This is a total intraday blackout, all 20 gappers have `intraday_data_source: unavailable`, so there's no premarket high, VWAP, HOD or LOD to check a breakout against. Even setting the blackout aside, every large-cap name with a real catalyst is sitting below yesterday's high on its stand-in price: NVDA ($228.17 vs. prior day high $230.47), CRM ($252.05 vs. $254.36), ONDS ($8.76 vs. $8.84), INTC ($92.03 vs. $92.94) and KEEL ($3.50 vs. $3.77) all miss on that one line.

## Swing Watchlist

The swing rule: gap of 8% or more, price over $3, open above yesterday's high, open above the 200-day SMA, market cap of $800M or more, and a real catalyst.

The packet flags **GENVR** as `swing_eligible: true`, the first name to clear this bar in weeks. It's the only one, and it doesn't hold up. Yes, it clears every numeric line: gap of 24.37% well over the 8% floor, price ($4.90) and market cap ($2.93B) both clear, its stand-in open sits above both yesterday's high ($4.90 vs. $4.46) and its 200-day SMA ($4.90 vs. $2.30). But there is no real catalyst behind it. All five headlines attached to it in the packet are generic "12 Information Technology Stocks Moving" listicles from earlier in the week, none of them name Gen Digital specifically or explain why it's up 24.37% today. Its 20-day average volume is also just 1,024 shares, oddly thin for a name mapped to a $2.93B market cap, which points to a likely bad ticker match (GENVR isn't Gen Digital's actual common stock ticker, GEN is) rather than a real story. Per the catalyst-found judgment rule, this is a skip, not a swing trade, so the watchlist is empty today. No other positive-gap name in the packet clears the $800M market cap floor with a same-day catalyst: PURR (10.86% gap, real earnings beat) and NVDA (8.77% gap, real earnings beat) both clear the gap, price, market cap and catalyst bars but fail on open vs. yesterday's high (PURR $12.815 vs. $14.14, NVDA $228.17 vs. $230.47).

## Market Trends of the Day

AI earnings are the dominant force again. Nvidia posted record $96.2B revenue with shares jumping on a $108B outlook, Bank of America is doubling down on the stock, and Nvidia also reported $7.8B in Q2 equity-portfolio gains from stakes that include Intel, SpaceX and CoreWeave, which is showing up as a secondary lift in INTC's own gap. Salesforce jumped on its earnings beat, with Snowflake and the rest of enterprise software getting pulled up alongside it, and headlines also tie Salesforce to Anthropic, whose $2 trillion valuation is separately drawing coverage of how it trades in a new tokenized market. CrowdStrike and Okta both had strong earnings reactions that spilled into leveraged single-stock ETFs (CRWL, CRWC, OKTG), which is where most of today's biggest percentage gappers actually come from rather than the underlying names themselves.

Fed and rates news centers on tomorrow's setup: the market_news feed reports Fed Chair Kevin Warsh and Treasury Secretary Scott Bessent are said to be acting in a coordinated way to push down long-term bond yields, a story framed as good news for bank stocks like Bank of America.

Retail and consumer had a mixed session: Build-A-Bear (BBW) is down 27.26% on weak traffic and a guidance cut, while PayPal is reportedly sinking after suitors walked away from a takeover bid.

Crypto sentiment is still split, with MARA caught in the middle of an AI-bitcoin debate (bulls calling for bitcoin to double, Peter Schiff calling the AI pairing a "threat") without a same-day, ticker-specific catalyst of its own today.

## Technical Signals for Today

Index proxies are green across the board: S&P 500 proxy SPY +0.68%, Nasdaq proxy QQQ +1.39%, Dow proxy DIA +0.17%, Russell 2000 proxy IWM +0.29%. Nasdaq is out front, consistent with the tech-earnings story driving today's gappers. VIX, the 10-year yield, the 3-month yield, WTI crude and the dollar index all came back null, yfinance failed on every one of those even after retries, so there's nothing to call on volatility, rates or the dollar this run.

## Economic Data, Rates and the Fed

Two high-impact USD events land at the same time today, 10:00 AM ET: new Fed Chairman Kevin Warsh speaks, and the Preliminary Benchmark Payrolls Revision prints (previous reading was -911K, no forecast given). The news feed separately reports Warsh and Treasury Secretary Bessent are seen as coordinating to bring down long-term bond yields, which gives his 10am appearance some added weight. Nothing is on the calendar for tomorrow.

## Coming Up

- **Tomorrow's events:** Nothing on the calendar for August 29.
- **Earnings:** No gapper in the packet has a populated `next_earnings_date`. Worth flagging from the headlines though: Intel's coverage frames Nvidia's reported equity stake as a factor in its own move, and a Benzinga options piece on INTC ("The IV Crush Is Only Half The Story") suggests earnings-related option positioning is still active in the name.

## Skips and Traps

**GENVR** (+24.37%) is the biggest miss of the day. It clears every numeric line on the swing rule including `swing_eligible: true` in the packet, but none of its five headlines are actually about Gen Digital, they're all generic mover-list mentions, and its 20-day average volume of 1,024 shares is far too thin for a name carrying a $2.93B market cap. That combination reads like a ticker mismatch (Gen Digital's real ticker is GEN, not GENVR) rather than a genuine catalyst, so it's a skip under the catalyst-found rule despite the flag.

**CRMG** (+44.26%) has `catalyst_found: false`, no headline in the packet at all. Per the ground rules that's an automatic skip regardless of gap size.

Several names cleared the gap filter but the packet has no headline that actually explains today's specific move: **DSPC** (headlines are all 2021 SPAC-era stories), **USDE** (generic "stocks moving" listicles, no USDE-specific line), **WETO** (generic listicles and a stale market summary, no headline dated to today's -33.45% drop), **MARA** (its "surging Friday" headline reads like it's from a week ago, not today) and **KEEL** (its most specific headlines, an earnings miss and a CEO buy, are both older and don't line up with today's 4.32% pop).

**FVNNU** (-33.31%) and **BRNX** (-38.14%) are both gapping down on headlines that don't match today's move: FVNNU's only headline is a 2024 IPO trading-halt notice, and BRNX's most specific headline describes an earlier circuit-breaker halt to the upside, the opposite direction of today's gap. BRNX also carries a market cap of just $2.76M, well under any threshold here.

**BBW** (-27.26%) is down on real, specific news, weak traffic and a guidance cut on its Q2 call. That's a coherent move, not a trap, but neither watchlist here trades the short side so there's nothing to do with it.

**OKTG**, **CRWL** and **CRWC** are real moves tied to real earnings (Okta and CrowdStrike), but per their own headlines they're leveraged single-stock ETFs, not the underlying companies, and all three come back with no market cap (`sec_unavailable_no_cik`) since ETFs don't file the SEC concept the fallback needs. None of them have live intraday data either, so there's no way to confirm a breakout even if they were otherwise in scope.

**OKTA**, **CRM**, **NVDA**, **ONDS**, **INTC** and **PURR** all have real, well-sourced catalysts (earnings beats, analyst price-target raises, a drone-testing contract) but every one of them is sitting below yesterday's high on today's stand-in price, so none of them clear either watchlist's trend requirement. See the Day Trading and Swing sections above for the exact numbers.

Market cap is missing for 7 of the 20 gappers even after the SEC EDGAR fallback (DSPC, OKTG, CRMG, CRWL, CRWC, USDE, OKTA), so eligibility for several of the largest percentage movers on this list, including OKTA itself, can't actually be confirmed either way.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
