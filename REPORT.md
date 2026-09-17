# Premarket Report: September 17, 2026

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** No live tape today. Yahoo rate-limited every batched price request this run (market snapshot, both live screeners, and the static universe daily bars), so the index snapshot and the entire gapper scan came back empty.
- **The catch we're watching:** Yesterday's Fed decision is still the story. The packet's news feed has the Fed rolling out its first interest-rate hike in three years, and the commentary is split: one piece has a Wall Street strategist arguing stocks can still advance after a hike, another has Tom Lee saying his predicted "face-ripping" rally is just delayed, not off. With zero gappers and a null index snapshot, there's no way to see this morning which side of that argument the tape is actually taking.
- **Two-brain verdict:** Single brain, no second opinion to compare.

## Pre-Market Gappers

No gappers made it through the pipeline this scan. Candidate source was the static universe fallback, and Yahoo rate-limited the day_gainers and most_actives screeners plus the static universe daily-bars batch, even after retries with backoff. The gap filter kept 0 of 0 candidates.

## Day Trading Watchlist

No names cleared the day-trading bar today. That flag encodes gap over 3%, price over $3, market cap over $1B, premarket RVOL over 1.5, and price already breaking above yesterday's high. With zero gappers in the packet, there's nothing to check that rule against.

## Swing Watchlist

No names cleared the swing bar either. That flag encodes gap of 8% or more, price over $3, open above yesterday's high, open above the 200-day SMA, market cap of $800M or more, and a real catalyst behind the move. Same story: no gappers means nothing to evaluate.

## Market Trends of the Day

No index or breadth data this run, but the news feed still has real signal, and it's almost entirely about the Fed's first rate hike in three years, which just landed. The reaction is split. A Wall Street strategist piece argues stocks can keep advancing after a hike, pointing to energy and information technology as the sectors that historically do best a year out. Tom Lee is on the other side of the same coin, saying the "face-ripping" rally he called is delayed, not cancelled, which reads as a hedge on a call that hasn't paid off yet. There's also a headline about a "mysterious trader" moving $122 million ahead of the 2pm decision, a reminder that positioning into this hike was active, not passive.

Outside the Fed story, a few single-name threads stand out even without gapper data to confirm them live: Generac is called out as soaring more than 30% on an Amazon deal tied to AI power infrastructure, and Intel's stock is flagged as rising on hopes that memory chips drive its turnaround. Both would be exactly the kind of names this scan is built to catch, but neither shows up as a gapper this run because the whole scan came back empty.

Macro-wise, the Bank of Japan is set to raise rates to a 31-year high on inflation risk, which pairs with the Fed hike into a broader global tightening story. Oil has its own thread too: a Saudi pipeline outage is squeezing a market that's already short on spare buffers, a supply-side story distinct from the rate narrative.

## Technical Signals for Today

No data. All nine readings in the market snapshot (S&P 500, Dow, Nasdaq, Russell 2000, VIX, 10-year yield, 3-month yield, WTI crude, dollar index) came back null, rate-limited on every retry. Nothing to call on breadth, VIX, or index levels this morning.

## Economic Data, Rates and the Fed

The packet's econ calendar (high-impact USD only) has nothing scheduled today or tomorrow, both `today` and `tomorrow` lists came back empty. The real action already happened: per the news feed, the Fed rolled out its first interest-rate hike in three years, and the market is now bracing for more increases. Layer the Bank of Japan's expected move to a 31-year high in rates on top of that, and the read is a synchronized tightening moment across two major central banks, even though neither shows up as a calendar line item in this packet.

## Coming Up

- **Tomorrow's events:** None listed on the high-impact USD calendar for September 18.
- **Earnings:** No gapper-level earnings dates to report, zero gappers this scan.

## Skips and Traps

Nothing to flag. There were no candidates to screen for bad-news pops or missing catalysts this scan.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
