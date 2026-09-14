# Premarket Report: September 14, 2026

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** Packet's own index proxies are green this morning, S&P proxy (SPY) +0.83%, Dow proxy (DIA) +0.94%, Nasdaq proxy (QQQ) +0.87%, Russell proxy (IWM) +0.4%, but that sits flat against a market news feed dominated by "Dow, S&P 500, Nasdaq futures fall as Anthropic's AI warning spooks tech traders" and "AI stocks get drilled because of Anthropic CEO Dario Amodei's 3,800 word warning."
- **The catch we're watching:** That mismatch is real, not a data error on our end, both pulls are literally in the packet. The index proxies show gains while the news wire is all AI-slowdown fear. Take the green proxy numbers as the actual premarket tape and the "futures fall" headlines as sentiment color that hasn't shown up in the proxy prices yet, or hadn't as of this scan's timestamp. Both watchlists are empty today: `day_eligible` and `swing_eligible` are `false` on all 20 gappers in the packet, and `intraday_data_source` is `unavailable` across the board again, so premarket high, VWAP, HOD and LOD are null for every name.
- **Two-brain verdict:** Single brain, no second opinion to compare.

## Pre-Market Gappers

- **MKDW** +52.0% - "Why Scholar Rock Shares Are Trading Higher By Around 12%; Here Are 20 Stocks Moving Premarket"
- **ACVA** +44.2% - "Frequency Electronics, ACV Auctions, HP And Other Big Stocks Moving Higher On Friday"
- **FEIM** +42.4% - "Frequency Electronics, ACV Auctions, HP And Other Big Stocks Moving Higher On Friday"
- **GTBP** +39.3% - "GT Biopharma Q2 EPS $(0.12) Misses $(0.08) Estimate"
- **SMZ** +35.5% - "NuScale Stock Ticks Higher as AI Integration Promises 80% Efficiency Gain"
- **VACI.U** -34.3% - no catalyst headline in the packet
- **SMUP** -31.4% - no catalyst headline in the packet
- **SMU** -31.2% - "NuScale And Oklo Heat Up, These Leveraged Nuclear ETFs Are Soaring Past 30%"
- **SMRX** -31.0% - "NuScale And Oklo Heat Up, These Leveraged Nuclear ETFs Are Soaring Past 30%"
- **KRSA** +29.9% - "Trading Halt: Halt status updated at 8:55:00 AM ET: Quotation Resumption: News and Resumption Times"
- **COLA** +27.8% - "WISeKey Unit Files Amended Registration for WISeSat SPAC Deal, Business Combination Expected to Trade on Nasdaq Under WSAT"
- **CVV** -25.4% - "CVD Equipment Says Following Quarter-End, The Customer Associated With The $800K System Order Filed A Prepackaged Chapter 11 Bankruptcy Proceeding. Although Unsecured Trade Creditors Are Expected To Be Unimpaired Under The Proposed Plan, The Company Is Evaluating The Potential Impact On The Order And Its Backlog, Financial Results, Financial Position, And Cash Flows."
- **HPEL** +24.8% - no catalyst headline in the packet
- **DLLL** +23.5% - "Why Is Dell Technologies Stock Falling Monday?"
- **ATEC** +19.7% - "UBS Maintains Buy on Alphatec Holdings, Raises Price Target to $16"
- **HPE** +12.4% - "Hewlett Packard Enterprise (HPE) Surges 19% in a Week — What to Watch For Next?"
- **SMCI** +7.2% - "What Is Going On With SMCI Stock on Friday?"
- **CIFR** +5.7% - "Why Is Cipher Mining Stock Surging on Friday?"
- **NOK** +5.0% - "What's Going On With Nokia Stock Friday?"
- **MARA** +4.8% - "MARA Holdings, Coinbase Global, Ternium And Other Big Stocks Moving Higher On Friday"

## Day Trading Watchlist

The "Trend Join Long" rule: gap over 3%, price over $3, market cap over $1B, premarket RVOL over 1.5, and price already breaking above yesterday's high.

No names cleared the bar today, `day_eligible: false` across all 20 gappers. But this run isn't the usual blackout, five megacaps actually have real market cap and RVOL data and are just missing the last leg. HPE ($82.4B cap, RVOL 34.9x) is sitting at $62.08 against a prior-day high of $62.15, about 0.1% away. NOK ($63.9B cap, RVOL 21.7x) is at $11.135 against a $11.16 prior high, also about 0.2% away. ATEC ($1.63B cap) is at $10.58 against a $10.60 prior high, 0.2% away, though its RVOL field is null so we can't confirm the volume leg. SMCI ($26.3B cap, RVOL 28.2x) and CIFR ($6.99B cap, RVOL 19.2x) and MARA ($4.6B cap, RVOL 29.8x) are further back, roughly 1 to 4% under their respective prior highs. None of these have a confirmed premarket high in the packet (`intraday_data_source: unavailable` on all of them), so there's no live level to actually trade off, but if you're watching for a break of yesterday's high once the open prints, HPE, NOK and ATEC are the closest.

## Swing Watchlist

The swing rule: gap of 8% or more, price over $3, open above yesterday's high, open above the 200-day SMA, market cap of $800M or more, and a real catalyst.

No names clear it, `swing_eligible: false` across all 20. Closest fit is **ACVA** (ACV Auctions): +44.2% gap, price $10.41 already above the 200-day SMA ($6.70), and only $0.05 below yesterday's high ($10.46), practically a rounding error. It fails purely on that last tick. The catalyst headline that names it, "Frequency Electronics, ACV Auctions, HP And Other Big Stocks Moving Higher On Friday," is a shared movers roundup rather than an ACVA-specific story, so even setting the price gap aside, there's no real explanation in the packet for a 44% move. **MKDW** and **FEIM** are the same shape: both clear market cap ($1.09B and $872M) and 200-day SMA, both sit a few dollars under yesterday's high ($8.11 vs $7.75 for MKDW, $89.25 vs $88.375 for FEIM), and neither has a headline in the packet that actually explains the gap. Nothing here to build a swing thesis on today.

## Market Trends of the Day

The news pull is almost entirely AI-slowdown fear. Anthropic CEO Dario Amodei published a 3,800-word warning calling for a pause in frontier AI development, and it's driving most of today's market copy: "AI stocks get drilled," "Dow Jones Futures: Techs Tumble As Anthropic Leads Call For AI Slowdown," "How investors are reacting to the AI pause calls from Anthropic and other frontier labs" (described as a negative but not catastrophic reaction), and Citigroup separately warning that a pause in AI development could hit the earnings revisions that have been driving stock gains this year. There's also a report that Anthropic itself was profitable for a second straight quarter, with the piece flagging "a very important caveat" that isn't detailed further in the packet's summary field.

Set against all that AI-fear copy, the packet's own index proxies (S&P, Dow, Nasdaq, Russell) are all positive premarket, see Summary. We're not going to reconcile that tension with a story that isn't in the packet, just flagging it plainly.

On rates and energy: one headline citing "Rate Hike Odds Jump to 90% as Record Diesel Lifts Inflation," and a separate MarketWatch piece saying the 10-year Treasury yield is "sitting on the doorstep of 5%" and framing it as the bond market pushing for Fed rate hikes despite hikes not bringing down gas prices. Neither the fed-funds odds number nor the 10-year yield level is confirmed anywhere in the packet's own market_snapshot (`US 10Y` came back null, `yfinance_failed`), so treat those as headline claims we can't verify against the packet's own numbers this run, not confirmed data.

Nuclear/AI-power names (NuScale, Oklo, Bloom Energy) show up repeatedly in the news pull and are the source of the catalyst matches on SMZ, SMU and SMRX below, none of which are actually about those three tickers themselves, see Skips and Traps.

## Technical Signals for Today

Index proxies: S&P proxy (SPY) 764.14, up 0.83%; Dow proxy (DIA) 525.79, up 0.94%; Nasdaq proxy (QQQ) 714.89, up 0.87%; Russell proxy (IWM) 288.89, up 0.4%. These are Alpaca ETF proxies standing in for the underlying indices, not the indices themselves.

VIX, the 10-year yield, the 3-month yield, WTI crude and the Dollar Index all came back null this run (`yfinance_failed`), so there's nothing to report on volatility, rates or the dollar directly from the packet.

Five names carry confirmed RVOL despite HOD/LOD/VWAP being null everywhere: HPE (34.9x), MARA (29.8x), SMCI (28.2x), NOK (21.7x) and CIFR (19.2x), all megacaps trading many multiples of their 20-day average volume this morning.

## Economic Data, Rates and the Fed

The packet's own econ calendar (`ff_calendar_thisweek.json`, USD/high-impact only) is empty for both today, September 14, and tomorrow, September 15. No scheduled high-impact releases either day per that source. That sits oddly next to the "Fed Meeting Ahead" and "Rate Hike Odds Jump to 90%" language showing up in today's news pull, but the packet's calendar itself doesn't carry a dated Fed event this week, so we can't confirm a specific date or time for it from the data we have. Flagging the gap rather than guessing a date.

## Coming Up

- **Tomorrow's events:** None. The packet's econ calendar has no high-impact USD releases listed for September 15.
- **Earnings:** `next_earnings_date` is null for every one of today's 20 gappers, so there's no confirmed date to flag for any of these names from the packet's own data.

## Skips and Traps

- **GTBP** +39.3%: Bad-news-pop. The only ticker-specific headline in the packet is a Q2 earnings miss ("EPS $(0.12) Misses $(0.08) Estimate"), and the stock is gapping up 39% on it. That's a trap shape, not a green light, even though it wouldn't have cleared either watchlist anyway (cap $388M is under both floors).
- **MKDW, ACVA, FEIM**: All three clear real market cap floors ($1.09B, $1.77B, $872M) and all three have `catalyst_found: true`, but none of the attached headlines actually explain a 40 to 52% move. They're all shared "stocks moving" roundups or a market-wide futures piece. Treat these the same as no catalyst until a ticker-specific story shows up.
- **SMZ, SMU, SMRX**: `catalyst_found: true` only because the packet matched them to NuScale/Oklo/Bloom Energy nuclear-power headlines, not stories about SMZ, SMU or SMRX themselves. No real catalyst behind any of these three moves per the packet.
- **VACI.U, SMUP, HPEL**: `catalyst_found: false`, no headlines in the packet at all. Skip automatically per the rules.
- **KRSA** +29.9%: Only headline is a trading-halt resumption notice with no news content attached, no real story, and market cap ($149M) is well under both floors anyway.
- **COLA** +27.8%: Real, ticker-specific catalyst, WISeKey's SPAC merger into Columbus Acquisition Corp. But market cap is $47.7M, far under both the $1B day-trading and $800M swing floors.
- **CVV** -25.4%: Down gap explained by real bad news, a customer's Chapter 11 bankruptcy tied to an $800K order. Rational sell-off, not a trap, just not eligible for either list since it's a down gap.
- **DLLL** +23.5%: The only headline attached is "Why Is Dell Technologies Stock Falling Monday?" describing Dell (DELL) falling, while DLLL itself is gapping up 23.5%. The packet has no DLLL-specific headline, so this looks like a ticker/headline mismatch rather than a confirmed catalyst. Not asserting what DLLL actually is since that's not in the packet.
- **HPE** +12.4%: Headline set is internally split, "Hewlett Packard Enterprise (HPE) Surges 19% in a Week" alongside "Why Is Hewlett Packard Stock Falling Monday?" The packet's own gap for HPE this morning is +12.4%, up, matching the surge headline, not the falling one. Also a near-miss on the day-trading bar, see Day Trading Watchlist.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
