# Premarket Report: August 1, 2026

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** Markets are closed today (Saturday), but the scanner's live Alpaca screeners still found real gap activity: 20 names cleared the gap/price filter, led by Focus Universal up over 500% on a circuit-breaker halt and Replimune up 107% on a positive FDA panel vote.
- **The catch we're watching:** Not one of the 20 gappers has actually broken above its prior day's high yet, so despite some huge headline gap percentages, the technical trigger this whole pipeline is built around never fired. The closest call is Integer Holdings (ITGR), up 20% and sitting right under its old high on a KKR buyout rumor.
- **Two-brain verdict:** Single brain, no second opinion to compare.

## Pre-Market Gappers

- **FCUV** +517.0%: "Focus Universal Shares Halted On Circuit Breaker To The Upside, Stock Now Up 759.04%"
- **REPL** +107.0%: "Replimune Skin Cancer Therapy Hopes Revive After Positive FDA Panel Vote"
- **JDZG** -88.0%: "JIADE Says Trading In Shares Resumes At 12:00 P.M. ET July 31 After June 4 Nasdaq Halt"
- **DFNS** -67.4%: no headline actually explains this direction (see Skips and Traps)
- **BIOA** -63.6%: "Why Is BioAge Labs Stock Sinking Friday?"
- **FWAC** +63.1%: no catalyst found that's actually about FWAC (see Skips and Traps)
- **TCX** +59.2%: "Tucows Announces $40M Buyback Plan Through February 2027"
- **AXTC** +57.9%: no catalyst headline matched this ticker
- **AXTU** +56.9%: "These AXT ETFs Turned a 30% Stock Rally Into Nearly 50% Returns"
- **AXTX** +56.2%: no catalyst headline matched this ticker
- **INHD** -54.4%: "Inno Holdings Says Texas Court Temporary Restraining Order No Longer In Effect Following Magistrate Judge's Recommendation"
- **IESC** +30.3%: "CORRECTION: IES Hldgs Q3 Adj. EPS $6.70 Beats $4.83 Estimate, Sales $1.243B Beat $1.080B Estimate"
- **AXTI** +28.7%: "AXT Posts Upbeat Q2 Earnings, Joins Newell Brands, SPX Technologies, Amazon And Other Big Stocks Moving Higher On Friday"
- **GLUE** -27.2%: "Monte Rosa Therapeutics Q1 EPS $(0.45) Misses $(0.37) Estimate, Sales $4.210M Miss $10.883M Estimate"
- **ITGR** +20.2%: "'KKR Near Deal To Buy Integer Holdings; Deal For Medical-Device Company Could Be Finalized Soon' - WSJ Exclusive"
- **WU** -17.2%: "Why Is Western Union Stock Falling on Friday?"
- **AMZN** +15.2%: "Amazon Just Left Investors Speechless"
- **AAPL** -7.3%: "Apple CEO sends strong warning on AI and price of Apple products"
- **MU** -5.9%: "DRAM Jumps After Situational Awareness Rescue as Analysts Caution Memory Stocks May Fall Further"
- **RIG** +4.8%: "Susquehanna Maintains Positive on Transocean, Lowers Price Target to $7"

## Day Trading Watchlist

No names cleared the day-trading bar this scan. That flag encodes gap over 3%, price over $3, market cap over $1B, premarket RVOL over 1.5, and price already breaking above yesterday's high, computed straight from the packet. The last piece is what killed every single one of the 20: not one of them is currently trading above its prior day's high, gap size aside. The nearest miss is ITGR, sitting about 1% under its prior high with a live buyout rumor behind it.

One data wrinkle worth flagging: AXTC actually did clear its prior day's high on price alone, but it's still correctly excluded because market cap came back null (yfinance and the SEC EDGAR fallback both missed it) and it has no matched catalyst headline. That's the rules engine working as designed, not a bug, but it means AXTC is worth a manual look if you have another way to check its market cap.

## Swing Watchlist

No names cleared the swing bar either. That flag encodes gap of 8% or more, price over $3, open above yesterday's high, open above the 200-day SMA, market cap of $800M or more, and a real catalyst. Same blocker as the day list: nobody's above their prior high yet. REPL is the one worth watching if that changes: real FDA catalyst, market cap $940M (clears the swing floor), sitting only about $1.25 under the trigger level.

## Market Trends of the Day

Two real threads in the news feed, both earnings-driven. Amazon's report has the market's attention ("Amazon Just Left Investors Speechless," with a Morgan Stanley note flagging a blind spot in the bull case even as the stock gapped up 15%). Apple is the other side of that coin: its CEO put out what's being described as a "strong warning" on AI and Apple product pricing, and the stock is down over 7% in this scan alongside a Micron-adjacent DRAM/memory-stocks caution piece.

Below the mega-caps, the AXT cluster is worth understanding as one story, not four. AXTI (AXT Inc) posted an upbeat Q2 beat and is up nearly 29%; AXTC, AXTU, and AXTX are almost certainly leveraged single-stock products tracking AXTI, which is why they're all posting similarly outsized (and in AXTU's case explicitly "nearly 50%") moves off the same underlying earnings beat.

Most of the rest of the day's MarketWatch feed (estate executor disputes, tax policy, a passport-website scam, Medicare Part D premiums, CD and mortgage rates) is personal-finance content, not market news, so it's left out of this section.

## Technical Signals for Today

Partial data this run. S&P 500, Dow, Nasdaq, and Russell 2000 came through via Alpaca's ETF proxies (SPY/DIA/QQQ/IWM) since the raw index symbols hit Yahoo's rate limit: S&P proxy +0.7%, Dow proxy +0.55%, Nasdaq proxy +0.63%, Russell proxy -0.46%. VIX, the 10-year, the 3-month, WTI crude, and the dollar index all came back null, Alpaca's free tier doesn't cover those instrument types and yfinance was rate-limited for all of them. No breadth or VIX read possible today.

## Economic Data, Rates and the Fed

Nothing on deck. The econ calendar shows zero USD high-impact events for today (Saturday, August 1) or tomorrow (Sunday, August 2). Markets are closed both days regardless.

## Coming Up

- **Tomorrow's events:** None in the calendar for Sunday, August 2.
- **Earnings:** No gapper-level next-earnings dates came through clean this scan (see gaps_to_fill in the packet, that field is still partial). Nothing in today's news feed flags specific names reporting next week either.

## Skips and Traps

- **AXTC, AXTX:** no catalyst headline matched either ticker. Per the rules, no catalyst is a skip regardless of the gap size.
- **FWAC:** technically has "catalyst_headlines," but none of them are actually about FWAC, they're about PhenomeX, 22nd Century Group, and ON Semiconductor moving on the same days. Treat this as no real catalyst.
- **DFNS:** the best-matched headline calls it a "surge" and asks what's "driving the momentum," but the packet has this ticker down 67.4%. That's either a stale headline or a mismatch, don't trust it as an explanation for today's move.
- **FCUV:** the catalyst is real (an AI product launch plus a circuit-breaker halt to the upside), but this is a $24M market cap stock up over 500% and repeatedly halted. That's outside anything either watchlist's market cap floor is built for, extreme speculative risk.
- **RIG:** the only headline that's specifically about Transocean is an analyst note that's mixed on its face (price target lowered even while the rating stays positive). Thin conviction if you were tempted to chase the 4.8% gap.
- No up-gapper in this batch showed a clear "bad news pop" pattern (dilution, a probe, or a miss paired with a gap up), so that specific trap check didn't fire today. The real caution here is simpler: every single name is still below its prior day's high, so nothing on this list has actually earned an entry yet by the rules in this repo.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
