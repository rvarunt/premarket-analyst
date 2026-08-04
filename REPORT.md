# Premarket Report: August 4, 2026

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** Broad green premarket. S&P 500 proxy +1.46%, Nasdaq proxy +1.77%, Dow proxy +1.32%, Russell 2000 proxy +1.71% (all via Alpaca ETF proxies, SPY/QQQ/DIA/IWM, since direct index data failed this scan).
- **The catch we're watching:** Intraday level data (premarket high, HOD, LOD, VWAP) came back empty for all 20 gappers this scan, yfinance got rate limited on every single enrichment call. That means neither watchlist could be built today, not because nothing gapped, but because the trigger prices the rules need aren't in the packet.
- **Two-brain verdict:** N/A, single-brain run today.

## Pre-Market Gappers

- **DFNS** +122.2%: "From Reverse Splits to Goodwill Surge - Fugazi Research Claims T3 Defense Is "Uninvestable""
- **UPC** +105.1%: "12 Health Care Stocks Moving In Monday's Pre-Market Session"
- **PN** -51.2%: "Apple, Stryker, Coinbase And Other Big Stocks Moving Lower In Friday's Pre-Market Session"
- **IPCX** -48.8%: "A1R WATER To Go Public Via SPAC Deal With Inflection Point Acquisition Corp. III, Trading As "WATR" On Nasdaq Post-Close; Closing Expected in 2025"
- **INHD** -47.7%: "INNO HOLDINGS Resumes Nasdaq Trading"
- **CORD** -39.0%: "REX Shares Drops Three ETFs To Bet Big On Bitcoin Mining, AI Cloud, Stablecoins"
- **CRWU** +38.9%: "REX Shares Drops Three ETFs To Bet Big On Bitcoin Mining, AI Cloud, Stablecoins"
- **CWVX** +38.8%: "CoreWeave Stock Jumps as AI Data-Center Demand Skyrockets Ahead of Q2 Earnings"
- **CRWG** +38.7%: "Why Is CoreWeave Stock Soaring Friday?"
- **CRWX** +37.9%: no catalyst headline in the packet
- **ATKR** +28.2%: "Roth Capital Downgrades Atkore to Neutral, Raises Price Target to $92"
- **TE** +18.6%: "T1 Energy Shares Jump as Q2 Sales Beat Estimates, Microsoft AI Capex Lifts Sector"
- **ONDS** +11.8%: "What's Going on With Ondas Stock Monday?"
- **EOSE** +11.1%: "Eos Energy Enterprises Announces A Strategic Partnership With The Department Of War To Enhance The Resilience Of National Defense Infrastructure"
- **SOFI** +10.6%: "SoFi Stock Surges Monday: What's Driving the Post-Earnings Rebound?"
- **ORCL** +9.2%: "Careful MSFT, AMZN, ORCL Bulls: Trouble at OpenAI, Anthropic Could Trigger 'Sustained' AI Selloff, 'Big Short' Legend Says"
- **IREN** +8.0%: "Stock Market Today: Microsoft Ignites Chip Rebound as SanDisk Jumps 24%"
- **AAL** +5.1%: "American Airlines, Citi, Mastercard Rolling Out New Enhanced Premium Travel, Lifestyle Upgrades For American Airlines Travelers"
- **MSFT** +4.9%: "Stock Market Today: S&P 500, Dow and Nasdaq Futures Rise After Strong Monday Gains, McDonald's, AMD, Palantir in Focus"
- **AMZN** +4.7%: "Amazon CEO Andy Jassy's AI Spending Pitch Won Wall Street Over, Jim Cramer Says, While Meta and Alphabet Are Still Struggling to Explain Theirs: 'The Same Numbers...'"

## Day Trading Watchlist

Rule: gap > 3%, price > $3, market cap > $1B, premarket RVOL > 1.5, and price already breaking above yesterday's high. This is the "Trend Join Long" setup.

No names cleared the day-trading bar today. Every gapper in the packet came back `day_eligible: false`. Worth flagging: `premarket_high`, `hod`, `lod`, and `vwap` are null for all 20 names because the intraday-levels fetch failed across the board (`intraday_data_source: "unavailable"` on every one). The breakout-above-yesterday's-high leg of this rule can't be confirmed without that data, so today's empty list is partly a real "nothing qualified" and partly "the data to check couldn't be pulled." Not overriding the flags either way, just flagging why the list looks the way it does.

## Swing Watchlist

Rule: gap >= 8%, price > $3, open > yesterday's high, open > the 200-day SMA, market cap >= $800M, and a real catalyst. Entry/exit management for swing names isn't built yet either way, these would be watch-and-build-a-plan names, not full trade plans.

No names cleared the swing bar today. Every gapper came back `swing_eligible: false`. Same caveat as above: today's open (`today_open`) is null for every ticker (premarket, not printed yet) and the scanner falls back to the current gap price as a stand-in per its own documented limitation, plus the intraday level outage above. So this is also a mix of genuinely-not-qualifying names (several are gapping down, several have no real catalyst, see Skips and Traps) and names where the data needed to check the rule cleanly wasn't available.

## Market Trends of the Day

Q2 earnings season is in full swing (`market_news` literally has a Reuters "Morning Bid: Earnings overload" headline) and it's dragging the tape green pretty broadly, all four index proxies are up over 1% premarket. AI infrastructure and AI capex is the thread running through a lot of today's movers: T1 Energy cites "Microsoft AI Capex Lifts Sector" in its own catalyst, CoreWeave-linked names (CWVX, CRWG) are up double digits on Q2 earnings anticipation and AI data-center demand headlines, and Amazon's catalyst is Andy Jassy's AI spending pitch landing well with investors. Palantir's "otherworldly" quarter gets name-checked across several unrelated tickers' catalyst lists (MSFT, AMZN), which tells you it's a sentiment driver for the whole tape today, not just PLTR. On the pharma side, Pfizer and Merck both beat on earnings per `market_news`, adding to the general "beats are landing well" mood.

## Technical Signals for Today

All four major index proxies are green: S&P 500 (via SPY) +1.46%, Dow (via DIA) +1.32%, Nasdaq (via QQQ) +1.77%, Russell 2000 (via IWM) +1.71%. That's the full extent of what's usable today. VIX, US 10Y, US 3M, WTI oil, and the dollar index (DXY) all came back null, `data_source: "yfinance_failed"` on every one, so there's no breadth or rates read to offer this morning. Note also that oil gets a mention in `market_news` ("Oil prices rise after vessel reports being hit in Strait of Hormuz") but there's no actual WTI print in the packet to attach a number to that.

## Economic Data, Rates and the Fed

Empty. The econ calendar in the packet has no high-impact USD releases listed for today or tomorrow (`econ_calendar.today` and `econ_calendar.tomorrow` are both empty arrays). Nothing to read into the rates path off today's calendar.

## Coming Up

- **Tomorrow's events:** None listed. The econ calendar's `tomorrow` field is empty, no high-impact USD releases flagged for August 5.
- **Earnings:** No dates available. `next_earnings_date` is null for all 20 gappers in this packet, the earnings-calendar pull failed across the board this scan (same yfinance rate limiting as the intraday levels).

## Skips and Traps

- **DFNS** (+122.2%): This is the one to actually watch out for. The gap looks explosive, but the real news behind it is a short-seller report from Fugazi Research titled "T3 Defense Is 'Uninvestable'" and a follow-up piece "Running Back the Same Ruthless Scheme," plus a headline noting shares got halted on a circuit breaker to the upside. Up huge on a short attack, not on good news, that's the up-on-bad-news trap pattern by the book. Skip.
- **UPC** (+105.1%): Market cap is $3,650,430, under four million dollars. None of its five catalyst headlines actually mention UPC by name, they're generic "12 Health Care Stocks Moving" listicles that happen to include it. A double-digit percent move with essentially no real story behind it and a market cap that thin is a pass.
- **CRWX** (+37.9%): `catalyst_found: false`. No catalyst headlines came back for it at all. Per the ground rules, no catalyst means no story, this one gets skipped outright regardless of what the gap number looks like.
- **CORD** (-39.0%) and **CRWU** (+38.9%): Both only matched the same single generic headline about REX Shares launching new Bitcoin mining/AI cloud/stablecoin ETFs, a headline that doesn't name either ticker specifically. Thin, keyword-matched "catalyst" at best.
- **PN** (-51.2%), **IPCX** (-48.8%), **INHD** (-47.7%): All gapping down hard, not long setups either way. IPCX and INHD do have real news behind the move (IPCX is a completed SPAC merger resuming trade as WATR, INHD is resuming from a trading halt), PN's headlines are generic "stocks moving lower" listicles with nothing PN-specific.
- **ATKR** (+28.2%): Roth Capital just downgraded it to Neutral, with a $92 price target that's already below where it's trading ($93.55). An analyst calling the stock fully priced right as it pops is worth a second look before chasing it.
- **ONDS** (+11.8%) and **ORCL** (+9.2%): Neither has a headline that reads like real, specific news. ONDS's catalyst list is all competitor-comparison and "stock whisper index" pieces. ORCL's top match is actually a bearish AI-selloff warning piece ("Trouble at OpenAI, Anthropic Could Trigger 'Sustained' AI Selloff"), not a bullish story, odd thing to be the top catalyst match on a stock that's up 9.2%.
- **IREN** (+8.0%), **MSFT** (+4.9%), **AAL** (+5.1%): Catalyst headlines for all three are mostly market-wide or sector context (chip-sector rebound, general futures-up pieces, a travel-perks product announcement) rather than a discrete, ticker-specific reason for the gap. These read more like broad-tape and AI-theme sympathy than a standalone catalyst.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
