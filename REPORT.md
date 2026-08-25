# Premarket Report: August 25, 2026

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** No numbers today. Every price call in the scan hit Yahoo's rate limit even after three retries with backoff, so there's no index snapshot, no gapper list, nothing quantitative to report. One headline in the packet says S&P 500 and Nasdaq futures are recovering into Nvidia earnings and the Fed's Jackson Hole summit, but that's a secondhand claim from a news feed, not data we pulled ourselves.
- **The catch we're watching:** Nvidia earnings and Jackson Hole land this week, right on top of a market where the surface looks fine but the internals don't: one piece in the feed says nearly two-thirds of the S&P 500 has already sold off, and a separate market fragility gauge just hit its highest possible reading for the first time since December 2024.
- **Two-brain verdict:** Single brain, no second opinion to compare.

## Pre-Market Gappers

No gappers made it through the pipeline this scan. Candidate source was the static universe fallback (the live day_gainers and most_actives screeners were rate-limited too), and Yahoo rate-limited the batched daily-bars request for all 40 tickers in that fallback universe, three retries in a row, before the scan gave up. Zero candidates reached the gap filter. This is a data outage, not a quiet market: it's a Tuesday and markets are open.

## Day Trading Watchlist

No names cleared the day-trading bar today. That flag encodes gap over 3%, price over $3, market cap over $1B, premarket RVOL over 1.5, and price already breaking above yesterday's high. With zero gappers in the packet, there's nothing to check that rule against.

## Swing Watchlist

No names cleared the swing bar either. That flag encodes gap of 8% or more, price over $3, open above yesterday's high, open above the 200-day SMA, market cap of $800M or more, and a real catalyst behind the move. Same story: no gappers means nothing to evaluate.

## Market Trends of the Day

No price data this run, but the news feed still gives a read on what's in the air:

AI spending is getting more scrutiny, not less. One piece flags that "the debt-fueled AI build-out may already be too big to fail," pointing to the Fed's pandemic-era corporate credit facilities as a backstop that's still on the table. Nvidia itself is framed as facing a "growth test" heading into earnings, with its Rubin chip debut running into AI-financing scrutiny. Layer on an AI chipmaker (Enflame) pricing a near-$900 million Shanghai IPO, and the AI-financing theme shows up from multiple angles at once, not just one story.

Under the surface, breadth looks worse than the headline indexes suggest. One report says nearly two-thirds of the S&P 500 has already sold off in a big way, and a separate market fragility measure hit its highest possible reading on August 19, the first time since December 2024, with a note that the last time it hit that level, volatility spiked.

There's tension in the rates and policy story too. Treasury Secretary Bessent's plan to double the buyback of longer-dated Treasurys is being credited with part of Bitcoin's push to the $80,000 level, but the same policy is drawing public criticism from Stanley Druckenmiller, who used to mentor Bessent. Oil is sliding (WTI and Brent both down roughly 3% on their October contracts) as investors shrug off Bessent's "economic D-Day" rhetoric on Iran. And a value-stocks call from BofA is making the case that value still works better than growth in a higher-rate, higher-inflation regime, which cuts against the AI-growth story above.

On trade, US-Canada talks broke down right after investors had piled into Canadian ETFs, so that's a position that just got caught offside.

## Technical Signals for Today

No data. All nine readings in the market snapshot (S&P 500, Dow, Nasdaq, Russell 2000, VIX, 10-year yield, 3-month yield, WTI crude, dollar index) came back null, same Yahoo rate limit that killed the gapper scan. Nothing to call on breadth, VIX, or index levels from this packet.

## Economic Data, Rates and the Fed

Nothing on the calendar today (Tuesday, August 25). Tomorrow (Wednesday, August 26) has two high-impact USD releases, both at 8:30 AM ET: Core PCE Price Index m/m (forecast 0.2%, previous 0.1%) and Prelim GDP q/q (forecast 1.5%, previous 1.5%). Separately, the news feed flags the Fed's Jackson Hole summit as happening this week, alongside Nvidia's earnings, though neither of those has a packet-sourced date or time attached.

## Coming Up

- **Tomorrow's events:** Core PCE Price Index m/m (forecast 0.2%, previous 0.1%) and Prelim GDP q/q (forecast 1.5%, previous 1.5%), both 8:30 AM ET.
- **Earnings:** No gapper-level earnings dates to report, zero gappers this scan. Worth flagging from the news feed: Nvidia earnings are described as landing this week, framed as a "growth test" for the stock around its Rubin chip debut.

## Skips and Traps

Nothing to flag. There were no candidates to screen for bad-news pops or missing catalysts this scan.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
