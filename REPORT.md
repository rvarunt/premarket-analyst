# Premarket Report: September 2, 2026

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** Index proxies are red across the board this morning: S&P -0.68%, Dow -0.71%, Nasdaq -1.26%, Russell 2000 -1.12% (all via ETF proxies, SPY/DIA/QQQ/IWM, since the direct index tickers failed). VIX, the 10-year, the 3-month, WTI, and the dollar index all came back null again.
- **The catch we're watching:** The news feed points at US-Iran war escalation and an oil price jump as the driver behind the broad risk-off tape, with a Yahoo Finance headline naming both that and "inflation jitters" directly. Layered on top: a live AI infrastructure buildout thread (Microsoft's 20-year AI power deal with Chevron, Nvidia guiding to a 70% revenue jump tied to an exclusive SpaceX deal) running against a Bank of England AI-bubble warning cited in the same headline, plus MongoDB tumbling despite beating estimates.
- **Two-brain verdict:** Single brain, no second opinion to compare.

## Pre-Market Gappers

Data note before the list: intraday levels (VWAP, HOD, LOD, premarket high/volume) came back null for every single gapper this run, both the Alpaca and yfinance legs. 91 requests failed even after retries this scan. What's below is what actually came through.

- **ISRL** +99.0% : "Trading Halt: Halt status updated at 9:30:00 AM ET: Quotation Resumption: IPO security released for quotation" (the rest of its headline history is over a year stale: a Jan 2025 SPAC merger announcement and an Aug 2024 termination of that same deal).
- **SSM** +77.4% : "From Bitcoin to Ball Clubs: Sono Group Stock Soars on Sports One Merger Plan"
- **ALMS** -56.6% : "Why Is Alumis Stock Falling Tuesday?"
- **PMI** -54.4% : no ticker-specific headline in the feed, only generic health care sector-mover listicles.
- **BIAF** +44.5% : "BioAffinity Advances Noninvasive CyPath Lung Test For Post-Treatment Monitoring"
- **RDAC** +41.5% : "Rising Dragon Acquisition Shares Halted On Circuit Breaker To The Upside, Stock Now Up 253.68%" (a separate headline in the same feed says it was also "Halted On Circuit Breaker To The Upside Downside, Stock Now Down -39.49%").
- **SWVL** +31.6% : "Swvl Secures Working Capital Facility With Zelo To Roll Out New Enterprise Accounts In Its UAE Pipeline"
- **FRVO** +28.4% : "Fervo Energy Stock Jumps 24% After Google Signs Utah Geothermal Power Deal"
- **RIBBU** +27.2% : no fresh ticker-specific headline, only a stale Jan 2025 IPO pricing/halt notice and an unrelated Palo Alto Networks earnings story pulled in by the feed.
- **MF** -26.4% : no ticker-specific headline in the feed, only generic Information Technology sector-mover listicles.
- **DBGI** -23.6% : "Digital Brands Group Has Executed A Binding Contract Of $3.3M In Guaranteed Cash Flow For Its U.S. Program From September 1 Through December 31, 2026"
- **AEHL** -23.0% : no fresh headline explaining today's drop, only generic sector listicles and a stale "surges over 100%: what's going on?" recap of an earlier move.
- **MRNX** +19.6% : no MRNX-specific headline in the feed, both attached headlines are about Moderna (MRNA)-linked leveraged ETFs, not this ticker.
- **GWAV** +19.4% : no ticker-specific headline in the feed, only generic Industrials sector-mover listicles.
- **RDIB** +17.2% : no ticker-specific headline in the feed, only generic listicles, including one about Pinterest and Destiny Tech100 that has nothing to do with RDIB.
- **ONDS** -7.9% : "Why Is Ondas Stock Falling on Monday?"
- **BMNR** -7.8% : "Bitmine Buys 53,501 ETH: What Does It Mean for BMNR?"
- **PCG** +5.9% : "B of A Securities Downgrades PG&E to Neutral, Lowers Price Target to $13"
- **BTG** -4.9% : "B2Gold Q2 Adj. EPS $0.03 Misses $0.09 Estimate, Sales $789.354M Miss $879.441M Estimate"
- **SOFI** -4.6% : "SoFi Stock Edges Lower Monday as Geopolitical Tensions and Interest Rate Uncertainty Hit Fintech"

## Day Trading Watchlist

**Rule:** every name here needs `day_eligible: true`, which encodes the "Trend Join Long" setup: gap over 3%, price over $3, market cap over $1B, premarket RVOL over 1.5, and price already breaking above yesterday's high.

No names cleared the day-trading bar today. All 20 gappers came back `day_eligible: false`. Premarket high, VWAP, HOD, and LOD are also null across the board this run, so there wouldn't be levels to build a plan around even for a marginal name.

## Swing Watchlist

**Rule:** every name here needs `swing_eligible: true`, which encodes: gap of 8% or more, price over $3, open above yesterday's high, open above the 200-day SMA, market cap of $800M or more, and a real catalyst.

No names cleared the swing bar either. All 20 gappers came back `swing_eligible: false`. Several of the biggest gappers (SSM, SWVL, FRVO, MRNX, RDIB) also have `market_cap: null` in the packet, so they couldn't clear the $800M floor even if everything else lined up. Nothing to watch and build a plan around today.

## Market Trends of the Day

Risk-off is the dominant theme in the news feed this morning. A Yahoo Finance headline states it directly: "Dow, S&P 500, Nasdaq futures fall as US-Iran war escalates, inflation jitters return." That lines up with the index proxies all being red, Nasdaq the worst of the four at -1.26%. A separate headline in the ALMS/PMI/BIAF catalyst feed adds "Crude Oil Surges 3%; ISM Manufacturing PMI Falls In August," tying the oil jump to the same Iran-risk story.

AI infrastructure buildout is still a live and two-sided thread. On the bullish side: Microsoft signed a 20-year AI power deal with Chevron ("Is Power Becoming the New Chip Shortage?"), Nvidia is guiding to a 70% revenue jump tied to an exclusive SpaceX deal, and Fervo Energy (FRVO, +28.4% today) jumped after Google signed a geothermal power deal in Utah, direct evidence of AI-driven power demand hitting a specific stock. On the skeptical side, that same Nvidia headline notes "Bank of England warns of AI bubble risk" in the same breath, and Tiger Global reportedly cut its Alphabet stake 45% while adding to AMD, framed as a possible rotation from AI platforms to AI chips. MongoDB is also down despite beating estimates, on "disappointing" news about flat Atlas multi-cloud revenue growth for a fifth straight quarter, another data point that good headline numbers aren't enough on their own right now.

Crypto is a smaller thread but present again: BMNR (Bitmine, -7.8%) is down after news it's still buying ETH, and the broader crypto headline flow (Bitcoin, Ethereum, XRP, Dogecoin) is tied to the same Iran escalation story, described as a "retreat" this morning.

PG&E (PCG) is worth a specific note: it's up 5.9% today even though the only fresh headlines attached to it are analyst downgrades (BofA cutting to Neutral with a $13 price target, and a separate "no longer bullish" piece). That's a name gapping up against its own bearish analyst coverage, not with it.

## Technical Signals for Today

S&P 500, Dow, Nasdaq, and Russell 2000 proxies (SPY, DIA, QQQ, IWM) are all lower this morning: S&P -0.68%, Dow -0.71%, Nasdaq -1.26%, Russell 2000 -1.12%. Nasdaq's proxy is the weakest of the four, consistent with the AI-name-specific headlines (Nvidia, MongoDB, Alphabet/AMD rotation chatter) sitting in the news feed.

VIX, the 10-year yield, the 3-month yield, WTI crude, and the dollar index all came back null (yfinance failed on every one of them this run, and there's no Alpaca proxy set up for those). No breadth or volatility read available beyond the four index proxies above.

## Economic Data, Rates and the Fed

The econ calendar itself came back empty for both today and tomorrow: zero high-impact USD releases logged for September 2 or September 3 in `econ_calendar`. That's despite the news feed independently referencing an ISM Manufacturing PMI print for August (cited in a Benzinga market-summary headline attached to a few gappers), which isn't reflected as a scheduled event in the packet's own calendar field. No other Fed or rates commentary appears in the calendar data.

## Coming Up

- **Tomorrow's events:** None in the calendar for Wednesday, September 3.
- **Earnings:** No `next_earnings_date` on file for any of today's 20 gappers, it's null across the board in the packet.

## Skips and Traps

- **RDAC +41.5%:** The feed shows it halted on a circuit breaker "up 253.68%" and, separately, halted again "down -39.49%." That's a whipsaw with no underlying business news behind either move. Pure halt-chaos, not a catalyst.
- **ISRL +99.0%:** The only headline that looks current is a bare IPO-quotation-resumption halt notice. The actual merger story behind it (Gadfin/Israel Acquisitions Corp) is stale by well over a year, including a termination announcement from August 2024. Market cap is also unavailable. Treat the reopen print as a coinflip, not a trade.
- **SSM +77.4%:** Real, fresh merger-plan headline, but market cap is $6.8M and RVOL is over 4,500x average volume. That combination (a near-shell-sized company plus an extreme volume spike on a "merger plan") is classic pump-and-chase risk.
- **MRNX +19.6%:** Both catalyst headlines attached are about Moderna (MRNA)-linked leveraged ETFs, not MRNX itself. There is no MRNX-specific catalyst in the packet at all, this looks like a bad ticker match in the news feed.
- **PMI -54.4%, MF -26.4%, AEHL -23.0%, GWAV +19.4%, RDIB +17.2%, RIBBU +27.2%:** `catalyst_found` came back true for all of these, but every attached headline is a generic sector-mover listicle (or, for RIBBU, a stale IPO notice plus an unrelated Palo Alto Networks earnings story). None of them name an actual driver for today's move. Treat as noise, not setups.
- **DBGI -23.6%:** The attached headline is genuinely positive, a new $3.3M guaranteed cash flow contract through year-end, yet the stock is down almost 24%. That mismatch is worth flagging rather than reading as a straightforward "good news, buy the dip" setup, since something not captured in this headline is likely driving the actual price action.
- **PCG +5.9%:** Gapping up while its only fresh headlines are analyst downgrades (BofA to Neutral, PT cut to $13). Doesn't clear either watchlist bar anyway, but it's backwards enough to call out: don't read the green print as confirmation the tape agrees with the move.
- **Missing market cap:** ISRL, ALMS, SWVL, FRVO, MRNX, and RDIB all came back with `market_cap: null` even after the SEC EDGAR fallback, per the packet's `gaps_to_fill` note. None of these can be sized against the market-cap filter, so treat them with extra caution regardless of catalyst quality.
- **Data blackout, again:** 91 requests failed even after retries this scan (mostly yfinance rate-limiting), and every gapper came back with null VWAP, HOD, LOD, and premarket high/volume. There is no intraday-level picture to trade off of this morning.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
