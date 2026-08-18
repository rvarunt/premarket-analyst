# Premarket Report: August 18, 2026

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** Red across every major index proxy this morning. SPY proxy for the S&P is -0.47%, DIA/Dow is -0.48%, QQQ/Nasdaq is -0.15%, IWM/Russell 2000 is -0.34%. The news feed backs it up: "Stock market today: Dow, S&P 500, Nasdaq futures extend losses amid US-Iran tensions" and "Bonds, stocks jolted as Middle East tensions shatter market calm," alongside "U.S. 30-year Treasury yield hits highest level since 2007 amid global bond sell-off."
- **The catch we're watching:** Total intraday blackout again. Every one of today's 20 gappers has `intraday_data_source: unavailable`, so premarket high, VWAP, HOD and LOD are null across the board and both watchlists come back empty on missing data, not weak setups. On top of that, 102 requests failed even after retries this scan (per the packet's own note), forcing market cap for 12 of the 20 gappers through the SEC EDGAR fallback and leaving 8 with no market cap at all. Two data points not to trust here: SIC is up 243.92% but every catalyst headline attached to it is dated 2021 (the old Select Interior Concepts buyout), nothing ties to today's move. And AIFU shows a $19.57B market cap on a stock with a 20-day average volume of just 35 shares, that combination doesn't add up.
- **Two-brain verdict:** Single-brain run today, no second opinion to compare against.

## Pre-Market Gappers

- **SIC** +243.92% - "Select Interior Concepts Acquired By Affiliate Of Sun Capital Partners For $14.50/Share" (note: every headline attached to this ticker is dated 2021, none of them explain today's move)
- **IPST** +235.89% - "IP Strategy Files Prospectus To Offer Up To $75M Of Securities"
- **WETO** +199.15% - no ticker-specific headline in the packet, only generic "Industrials Stocks Moving" mover-list mentions
- **EYPT** -66.98% - "JP Morgan Downgrades EyePoint to Neutral"
- **ZTG** -66.70% - no ticker-specific headline in the packet, only generic "Industrials Stocks Moving" mover-list mentions
- **AIFU** -52.48% - "Trading Halt: Halted at 7:50:00 p.m. ET - Trading Halt: Halt News Pending" (also halted/resumed the next morning per a second headline, plus a same-week CFO appointment)
- **AXTU** +35.49% - "These AXT ETFs Turned a 30% Stock Rally Into Nearly 50% Returns" (about semiconductor ETFs generally, not ticker-specific to AXTU)
- **AXTL** +35.27% - "These AXT ETFs Turned a 30% Stock Rally Into Nearly 50% Returns" (same generic ETF piece, not ticker-specific to AXTL)
- **AXTX** +35.05% - no catalyst headline in the packet
- **AXTC** +34.17% - no catalyst headline in the packet
- **SLE** +33.04% - "Stock Market Today: Dow Jones, S&P 500 Futures Fall as Trump Rejects Extending Ceasefire With Iran, Home Depot, Super League, Flexsteel in Focus" (Super League named only in passing in a market roundup, no dedicated story)
- **GRNQ** +31.24% - "Greenpro Capital Board Approves 1-For-10 Reverse Stock Split, Effective On Or About July 26"
- **CBRX** +30.28% - no current headline; the packet's catalyst list for this ticker is old Columbia Labs/Juniper Pharmaceuticals news from 2015
- **CBRG** +30.15% - no current headline; the packet's catalyst list includes an unrelated 2024 SPAC merger story and a correction noting "Corebridge Financial Ticker Is CRBG," not CBRG
- **CBRZ** -29.76% - "Looking Beyond Nvidia? Tradr's New ETFs Target The Chip Stock Cathie Wood Is Snapping Up" (generic ETF piece, not ticker-specific to CBRZ)
- **FTK** -20.01% - "Flotek Industries Announces Puerto Rico Oversight Board Members Have Voted To Direct PREPA To Terminate The Contract; PREPA Has Not Delivered A Formal Notice Of Termination; Reaffirms FY2026 Sales Of $340M-$350M And Adjusted EBITDA Of $47M-$51M"
- **HIVE** +13.73% - "HC Wainwright & Co. Reiterates Buy on HIVE Digital Technologies, Maintains $7 Price Target"
- **KEEL** +7.12% - "Keel Infrastructure Form4 Filing Shows CEO Benjamin Gagnon Purchases 58,888 Shares At An Average Price Of $3.33, Raising Direct Holdings To 1.35M Shares" (same week as "Keel Infrastructure Q2 Earnings Miss Estimates as Bitcoin Wind-Down Continues")
- **MARA** +5.54% - "Morgan Stanley Maintains Underweight on MARA Holdings, Raises Price Target to $6"
- **NKE** -4.10% - "NKE Stock Erases $200 Billion in Market Cap Since 2021 Peak: Arvy CIO Warns of a 'Stage 4' Decline"

## Day Trading Watchlist

The "Trend Join Long" rule: gap over 3%, price over $3, market cap over $1B, premarket RVOL over 1.5, and price already breaking above yesterday's high.

No names cleared the day-trading bar today. This is a total intraday blackout: every one of today's 20 gappers has `intraday_data_source: unavailable`, so premarket high, VWAP, HOD and LOD are null for all of them, there's no real premarket level to check the "breaking above yesterday's high" leg against for anyone. The two cap-and-gap-qualified up-gappers worth naming are KEEL ($2.32B cap, +7.12% gap) and MARA ($3.75B cap, +5.54% gap), both clear $1B and the 3% gap floor, but both fail the break check on the numbers the packet does have: KEEL's price ($3.76) sits under its `prior_day_high` ($3.91), and MARA's price ($9.71) sits under its `prior_day_high` ($9.80). Where the packet does carry an `rvol` number at all (IPST 7504.08, EYPT 332.35, HIVE 73.2, KEEL 29.43, MARA 36.77), `premarket_volume` is null for every one of them too, so that ratio is full-day volume against the 20-day average, not the premarket-specific read this rule actually calls for. Missing data is why this list is empty, not the setups themselves.

## Swing Watchlist

The swing rule: gap of 8% or more, price over $3, open above yesterday's high, open above the 200-day SMA, market cap of $800M or more, and a real catalyst.

No names cleared the swing bar either. The closest name is HIVE: a real catalyst (HC Wainwright reiterating Buy with a $7 price target), $840.66M market cap clears the $800M floor, price is over $3, and `today_open_effective` ($3.065) is already above its 200-day SMA ($3.03). But it's $0.085 under its `prior_day_high` ($3.15), missing the "open above yesterday's high" leg narrowly. Worth a manual look if it clears $3.15. Everything else that clears the 8% gap and has a market cap either fails on the cap floor or the catalyst check: IPST ($5.07M), WETO ($540.98M), SLE ($5.12M) and GRNQ ($182.0M) are all well under $800M, AXTX and AXTC have `catalyst_found: false`, and SIC, AXTU, AXTL, CBRX and CBRG have no market cap in the packet at all (SEC EDGAR has no CIK on file for any of them). Worth remembering the packet's own caveat here too: before 9:30am ET the real open hasn't printed, so `today_open_effective` is standing in for the actual open and could shift once the bell rings.

## Market Trends of the Day

The dominant story this morning is macro, not sector. Middle East tensions are driving the tape ("Bonds, stocks jolted as Middle East tensions shatter market calm," "Trump Rejects Extending Ceasefire With Iran"), and it's showing up as a genuine risk-off open with all four index proxies red, no green line to point to today. Layered on top of that, the 30-year Treasury yield just hit its highest level since 2007 amid a global bond sell-off, a rates story that's bearish for anything duration-sensitive heading into tomorrow's FOMC minutes.

Underneath that macro backdrop, today's gapper list is thin on real, dated, ticker-specific stories. A large chunk of the list (SIC, WETO, ZTG, SLE, CBRX, CBRG, CBRZ, AXTU, AXTL) is either stale news, generic mover-roundup mentions, or headlines about a different, similarly-named company entirely, not fresh catalysts that explain today's gap size. The bitcoin-mining cluster (MARA, HIVE, KEEL) is a genuine but mixed group: HIVE gets a sell-side reiterate-Buy, MARA gets a bearish Underweight reiteration even while it gaps up, and KEEL pairs insider buying against a same-week earnings miss tied to its own Bitcoin wind-down. FTK is the one clean single-name story: down 20% on a Puerto Rico contract-termination vote even as it reaffirms its FY2026 sales and EBITDA guidance in the same release, the market's reading the termination risk over the reaffirm this morning.

## Technical Signals for Today

Index proxies (via Alpaca ETF fallback since the direct index pulls failed): SPY proxy -0.47%, DIA proxy -0.48%, QQQ proxy -0.15%, IWM proxy -0.34%. Everything is red, Nasdaq is the smallest decliner.

Every other technical read needed a straight yfinance pull, and all five of those calls failed today: VIX, US 10Y, US 3M, WTI Oil and the Dollar Index all came back null (`data_source: yfinance_failed`). No breadth data is in the packet either. Same story as the intraday blackout above: this is a data-availability problem, not a "nothing's moving" read. The news feed's own color (30-year yield at its highest since 2007) is the only rates signal available this morning, there's no numeric US 10Y or US 3M read to hand you.

## Economic Data, Rates and the Fed

The high-impact USD calendar came back empty for today under the packet's filter, nothing scheduled. Tomorrow carries one event: FOMC Meeting Minutes at 2:00 PM ET (no forecast or previous figure given in the packet). The news feed fills in some color the calendar doesn't: "U.S. 30-year Treasury yield hits highest level since 2007 amid global bond sell-off," tied to "concerns about inflation and more debt supply," and a separate headline frames the morning read as "Morning Bid: Yields give way." Read together with tomorrow's minutes release, rates are the thing to watch into the close today and through tomorrow afternoon.

## Coming Up

- **Tomorrow's events:** FOMC Meeting Minutes, 2:00 PM ET. No forecast or previous value listed in the packet.
- **Earnings:** `next_earnings_date` is null for every gapper in this packet, so there's nothing confirmed to report here.

## Skips and Traps

- **SIC**: +243.92%, but every catalyst headline attached to this ticker is dated 2021 (the old Select Interior Concepts buyout by Sun Capital Partners at $14.50/share), and market cap is unavailable (no CIK match). Nothing in the packet ties to a live 2026 catalyst. Treat this as stale or mismatched data, not a tradeable gap. Skip.
- **IPST**: +235.89% on a $5.07M market cap, well under both watchlist floors. The one dated, company-specific headline in the packet is a June prospectus filing to offer up to $75M of securities, dilutive, not the kind of catalyst that should be chased into a 236% gap. 20-day average volume is 13,847 shares against a reported 103.9M-share volume print today, treat the size of that move with real skepticism. Skip.
- **WETO**: +199.15% with no ticker-specific catalyst in the packet at all, only generic "Industrials Stocks Moving" roundups that don't mention Wetour Robotics by name. Market cap ($540.98M) comes from the SEC EDGAR fallback. Skip.
- **EYPT**: -66.98% on a real, named-source catalyst (JPMorgan downgrade to Neutral). Down on bad news is the expected read here, not a trap, just not a long setup either way.
- **ZTG**: -66.70% with no ticker-specific headline, only generic "Industrials Stocks Moving" mentions. Nothing here to trade off of either direction.
- **AIFU**: -52.48% on trading-halt and CFO-appointment headlines, no single dated story clearly explains the drop. Also worth flagging hard: the packet reports a $19.57B market cap on a stock with a 20-day average volume of just 35 shares. That combination doesn't add up, this is an SEC EDGAR fallback figure and shouldn't be trusted at face value.
- **AXTU / AXTL**: +35.49% and +35.27% respectively, sharing the same single catalyst headline in the packet, a generic piece about AXT-branded semiconductor ETFs, not company-specific news for either ticker. Market cap unavailable for both. Skip.
- **AXTX / AXTC**: +35.05% and +34.17%. `catalyst_found: false` for both, no headlines in the packet at all. No catalyst, no story, skip regardless of gap size.
- **SLE**: +33.04% on a $5.12M market cap. The only mention of Super League in the packet is a passing name-check inside a broader market roundup headline, not a dedicated story. Skip.
- **GRNQ**: +31.24% on a $182.0M market cap. The catalyst list includes a 1-for-10 reverse stock split and a separate unregistered private placement of 8.5M restricted shares, both dilutive/structural flags, against Q1 sales of just $405K. Well under the swing cap floor regardless, but worth treating this pop with real skepticism if it ever qualifies.
- **CBRX**: +30.28%, market cap unavailable, and every catalyst headline in the packet is old Columbia Labs/Juniper Pharmaceuticals news from 2015 plus a generic ETF piece. No current story. Skip.
- **CBRG**: +30.15%, market cap unavailable. The catalyst list is an unrelated 2024 SPAC merger story, and one of the headlines is literally a correction noting "Corebridge Financial Ticker Is CRBG," not CBRG, a sign this news match may not even be for the right company. Skip.
- **CBRZ**: -29.76%, market cap unavailable, only a generic Nvidia-adjacent ETF headline attached, nothing ticker-specific to explain the drop.
- **FTK**: -20.01% on a $1.04B market cap. Today's actual headline is the Puerto Rico Oversight Board's vote to direct PREPA to terminate its contract with Flotek, even though the same release reaffirms FY2026 sales and EBITDA guidance. Down on the news as reported, not a bad-news-pop trap since it's falling, not popping.
- **HIVE**: +13.73% on a real catalyst (HC Wainwright reiterates Buy, $7 price target) and a market cap ($840.66M) that clears the swing floor. Misses swing eligibility by $0.085, `today_open_effective` ($3.065) is just under `prior_day_high` ($3.15). Worth a manual look if it clears $3.15, but the intraday blackout means there's no premarket confirmation either way right now.
- **KEEL**: +7.12% on real insider buying (CEO Form 4 purchase) landing the same week as a Bitcoin-wind-down earnings miss, mixed signal. $2.32B cap clears both watchlist floors, but the gap is under the swing's 8% floor and price ($3.76) is already below `prior_day_high` ($3.91), so there's no day-trading break to point to either.
- **MARA**: +5.54% on a $3.75B market cap and a gap over the 3% day floor, but Morgan Stanley maintains an Underweight rating even as the stock gaps up, a genuine mixed signal. Price ($9.71) sits under `prior_day_high` ($9.80), so no break confirmed, and the gap is well under the swing's 8% floor.
- **NKE**: -4.10% on a bearish, multi-year-decline narrative ("Stage 4 decline"). Down gap, not eligible for either watchlist by rule.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
