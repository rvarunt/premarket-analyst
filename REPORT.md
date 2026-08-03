# Premarket Report: August 3, 2026

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** Futures are green into the open (S&P proxy +0.7%, Dow proxy +0.55%, Nasdaq proxy +0.63% via Alpaca ETF proxies), Russell proxy is the outlier at -0.46%, and it's tracking a Mideast de-escalation headline (Trump calling off a planned Iran attack) plus oil sliding to a three-week low.
- **The catch we're watching:** The screener found 20 real gappers this morning, several with genuine catalysts (a KKR buyout of Integer Holdings at $127/share, a positive FDA panel vote for Replimune), but yfinance got rate-limited on every single per-ticker enrichment call. That means premarket high, VWAP, HOD/LOD are null across the board, so neither watchlist can technically trigger no matter how good the catalyst looks.
- **Two-brain verdict:** Single brain, no second opinion to compare.

## Pre-Market Gappers

- **FCUV** +517.0%: "Why Is Focus Universal Stock Soaring on Monday?"
- **REPL** +107.0%: "Replimune Skin Cancer Therapy Hopes Revive After Positive FDA Panel Vote"
- **JDZG** -88.0%: "JIADE Says Trading In Shares Resumes At 12:00 P.M. ET July 31 After June 4 Nasdaq Halt"
- **DFNS** -67.4%: "T3 Defense Stock Continues Surge: What's Driving the Momentum?" (headline says "surge," packet shows the stock down 67.4%, see Skips and Traps)
- **BIOA** -63.6%: "Why Is BioAge Labs Stock Sinking Friday?"
- **FWAC** +63.1%: no catalyst headline in the packet is actually about FWAC (see Skips and Traps)
- **TCX** +59.2%: "Tucows Announces $40M Buyback Plan Through February 2027" (this headline is from February, stale relative to today's move, see Skips and Traps)
- **AXTC** +57.9%: no catalyst headline found for this ticker
- **AXTU** +56.9%: "These AXT ETFs Turned a 30% Stock Rally Into Nearly 50% Returns"
- **AXTX** +56.2%: no catalyst headline found for this ticker
- **INHD** -54.4%: "Inno Holdings Says Texas Court Temporary Restraining Order No Longer In Effect Following Magistrate Judge's Recommendation"
- **IESC** +30.3%: "CORRECTION: IES Hldgs Q3 Adj. EPS $6.70 Beats $4.83 Estimate, Sales $1.243B Beat $1.080B Estimate"
- **AXTI** +28.7%: "B. Riley Securities Maintains Neutral on AXT, Raises Price Target to $55"
- **GLUE** -27.2%: "Monte Rosa Therapeutics Q1 EPS $(0.45) Misses $(0.37) Estimate, Sales $4.210M Miss $10.883M Estimate"
- **ITGR** +20.2%: "Integer Holdings To Be Acquired By KKR For $127 Per Share Cash In Transaction Valued At EV Of ~$5.7B"
- **WU** -17.2%: "Why Is Western Union Stock Falling on Friday?"
- **AMZN** +15.2%: "Stock Market Today: Amazon Jumps 15%, Apple Wipes Out $475 Billion"
- **AAPL** -7.3%: "Stock Market Today: Amazon Jumps 15%, Apple Wipes Out $475 Billion"
- **MU** -5.9%: "Micron Technology Stock Is Falling Monday: What's Going On?"
- **RIG** +4.8%: "Susquehanna Maintains Positive on Transocean, Lowers Price Target to $7"

## Day Trading Watchlist

No names cleared the day-trading bar this scan. That flag encodes gap over 3%, price over $3, market cap over $1B, premarket RVOL over 1.5, and price already breaking above yesterday's high, computed straight from the packet.

This one comes with a real caveat: intraday data (VWAP, HOD, LOD, premarket high) is null for all 20 gappers, yfinance rate-limited every single enrichment call this run. So even names with strong catalysts and big gaps, like ITGR (KKR buyout, gap to $121.21, prior day high $122.56, only about a dollar away) or REPL (FDA panel win, gap to $11.20, prior day high $12.46), can't be confirmed against the breakout rule with the data this scan actually has.

One name is worth a manual look: AXTC is already trading above its prior day's high ($17.20 vs $11.04) on price alone, but it's correctly excluded because it has no market cap (SEC EDGAR has no CIK on file for it) and no matched catalyst headline. Rules engine working as designed, but flag it if you have another way to check its float and market cap.

## Swing Watchlist

No names cleared the swing bar either. That flag encodes gap of 8% or more, price over $3, open above yesterday's high, open above the 200-day SMA, market cap of $800M or more, and a real catalyst. Same blocker as the day list, nobody's confirmed above their prior day's high with today's data gap. ITGR is the name worth watching if that changes: real M&A catalyst (KKR at $127/share, about 5% above the current $121.21), market cap $4.1B (clears the swing floor easily), sitting only about 1% under its prior day's high.

## Market Trends of the Day

Geopolitics is doing the heavy lifting in the news feed today. Trump reportedly called off a planned attack on Iran, and that's showing up everywhere: oil down to a three-week low, futures reported higher across the board, and a separate piece on a joint U.S.-Japanese yen intervention questioning whether it'll hold. On the Fed side, Williams is quoted expecting inflation to ease with the Fed ready to act if it doesn't, while a bond-market column argues Warsh has effectively tightened policy just by pausing instead of cutting.

The AXT cluster is one story, not four, same pattern as recent scans: AXTI (AXT Inc) is up nearly 29% on an upbeat Q2 and analyst price-target raises, while AXTC, AXTU, and AXTX are almost certainly leveraged single-stock products tracking AXTI, all posting outsized moves off the same underlying beat, and two of the three (AXTC, AXTX) don't even have a catalyst headline of their own in this packet.

Big tech earnings from last week are still working through the tape. Amazon and Apple's post-earnings reaction (Amazon up big, Apple down over 7%) shows up as today's reference gap, and Micron is sliding on a DRAM/memory-stocks caution piece even as AMD's Q2 earnings, due out this week, get previewed in the news feed as the next test for the AI trade.

A KKR buyout of Integer Holdings at $127/share and an AstraZeneca/Bristol-Myers Squibb tie-up rumor are the two live M&A stories moving individual names outside of that group.

## Technical Signals for Today

Partial data this run. S&P 500, Dow, Nasdaq, and Russell 2000 came through via Alpaca's ETF proxies (SPY/DIA/QQQ/IWM) since the raw index symbols hit yfinance's rate limit: S&P proxy +0.7%, Dow proxy +0.55%, Nasdaq proxy +0.63%, Russell proxy -0.46%. VIX, the 10-year, the 3-month, WTI crude, and the dollar index all came back null, same rate limit, Alpaca's free tier doesn't cover those instrument types. No breadth or VIX read possible today.

## Economic Data, Rates and the Fed

One event on today's calendar: ISM Manufacturing PMI at 10:00 AM ET, forecast 54.0, previous 53.3. Nothing else listed for today, and nothing listed for tomorrow. On the Fed commentary side, from the news feed rather than the econ calendar, Fed's Williams is quoted expecting inflation to ease with the Fed ready to act if it doesn't.

## Coming Up

- **Tomorrow's events:** None in the calendar for tomorrow.
- **Earnings:** No gapper-level next-earnings dates came through clean this scan, that field in the packet is still partial (see gaps_to_fill). Worth flagging from the news feed though: AMD is set to report Q2 results this week, with chip stocks described as "continuing to waver" heading in.

## Skips and Traps

- **AXTC, AXTX:** no catalyst headline matched either ticker. Per the rules, no catalyst is a skip regardless of the gap size.
- **FWAC:** has catalyst headlines attached, but none of them are actually about FWAC, they're about PhenomeX, 22nd Century Group, and ON Semiconductor moving on unrelated days back in 2023. Treat this as no real catalyst.
- **DFNS:** the best-matched headline calls it a "surge" and asks what's "driving the momentum," but the packet has this ticker down 67.4%. Either a stale headline or a mismatch, don't trust it as an explanation for today's move.
- **TCX:** the only distinctly TCX-specific headline is a $40M buyback plan announced back in February, well before today's 59.2% gap. Nothing in the packet actually explains today's move.
- **FCUV:** the catalyst is real (an AI product story plus circuit-breaker halts to the upside repeatedly this week), but this is a $24M market cap stock up over 500% on 6,774x relative volume. That's outside anything either watchlist's market cap floor is built for, extreme speculative risk.
- **RIG:** the only Transocean-specific headline is an analyst note that's mixed on its face (price target lowered to $7 even while the rating stays positive). Thin conviction if you were tempted to chase the 4.8% gap.
- No up-gapper in this batch showed a clear "bad news pop" pattern (dilution, a probe, or a miss paired with a gap up), so that specific trap check didn't fire today. The bigger caution across the board: intraday data (premarket high, VWAP, HOD/LOD) is null for all 20 names this run, so nothing on this list has actually been confirmed against the breakout rules either watchlist is built on.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only

---

**Pipeline note:** yfinance rate-limited every per-ticker enrichment call this run (intraday bars, per-ticker news, and earnings dates for all 20 gappers, 108 failed requests total even after retries). The gapper list, catalyst headlines, and market snapshot above came through via Alpaca and SEC EDGAR instead, which is why the gap list and headlines are real but every VWAP/HOD/LOD/premarket high field is null. No price, level, or catalyst data was invented to fill those gaps, they're reported as null where the packet has them as null.
