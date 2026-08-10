# Premarket Report: August 10, 2026

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** Mild risk-on premarket. All four Alpaca ETF proxies are green: SPY (S&P 500) +0.59%, DIA (Dow) +0.24%, QQQ (Nasdaq) +1.15%, IWM (Russell 2000) +1.09%. VIX, rates, oil, and the dollar all came back null again, yfinance rate-limited every one of those legs.
- **The catch we're watching:** Total intraday blackout this run. All 20 gappers show `day_eligible: false` and `swing_eligible: false`, and this time it's not partial, `premarket_high`, `hod`, `lod`, `vwap`, and `today_open` are null for every single one of them. 125 requests failed even after retries this scan per the packet's own notes. On top of that, the econ calendar came back completely empty for both today and tomorrow, no high-impact USD releases scheduled either day. There's no fresh macro catalyst and no intraday data to grade setups against, so today's story is entirely about individual tickers and how much to trust their catalysts.
- **Two-brain verdict:** Single brain today, no GPT cross-check to compare against.

## Pre-Market Gappers

- **YJ** +176.4%: "Yunji Shares Halted On Circuit Breaker To The Upside, Stock Now Up 790.24%"
- **MB** +137.9%: "MasterBeef Group Enters Into Franchisee Arrangement With Premium Thai Tea Beverage And Dessert Brand From Thailand To Develop, Operate Outlets In Hong Kong And Macau Markets"
- **RCEL** +63.6%: "BTIG Upgrades AVITA Medical to Buy, Announces $7 Price Target"
- **VATE** +63.4%: "Innovate Stock Soars Over 42% Overnight: Here's What You Need to Know"
- **PN** -61.3%: "PN Smart Energy Prices Registered Direct Offering Of Up To 1,428,572 Shares And Pre-Funded Warrants At $3.50 Per Share"
- **GENVR** +55.7%: "12 Information Technology Stocks Moving In Friday's After-Market Session" (a sector roundup mentioning GENVR, not a dedicated story)
- **WYHG** -54.9%: "Wing Yip Food Holdings Group Shares Halted On Circuit Breaker To The Upside, Stock Now Up 609.17%" (a prior-session halt-to-the-upside headline, doesn't match today's -54.9% move)
- **NAMI** +51.5%: "Jinxin Technology Holding Company Regained Compliance with Nasdaq's Minimum Bid Price Requirement"
- **QNST** +38.5%: "QuinStreet Stock Jumps Over 25% Overnight: Here's Why"
- **CRSR** +35.2%: "Corsair Gaming Stock Surges Following Beat-and-Raise Q2 Results"
- **SEZL** -33.9%: "Keefe, Bruyette & Woods Maintains Market Perform on Sezzle, Lowers Price Target to $155"
- **LASR** -25.6%: "Trade Desk Posts Downbeat Q2 Results, Joins Sezzle, Resmed, Ouster And Other Big Stocks Moving Lower In Friday's Pre-Market Session" (a group mention, not a dedicated LASR story)
- **YXT** -24.8%: "Why Avalon Holdings Shares Are Trading Higher By More Than 10%; Here Are 20 Stocks Moving Premarket" (a sector roundup mentioning YXT, not a dedicated story)
- **QDEL** -24.7%: "Trade Desk Posts Downbeat Q2 Results, Joins Sezzle, Resmed, Ouster And Other Big Stocks Moving Lower In Friday's Pre-Market Session" (a group mention, not a dedicated QDEL story)
- **BTG** +22.9%: "B2Gold Q2 Adj. EPS $0.03 Misses $0.09 Estimate, Sales $789.354M Miss $879.441M Estimate"
- **CDE** +11.2%: "Coeur Mining Q2 Adj. EPS $0.12 Misses $0.32 Estimate, Sales $1.086B Miss $1.286B Estimate"
- **TE** +5.6%: "T1 Energy Files Prospectus For Resale Of 13,615,979 Shares"
- **CIFR** -5.5%: "JP Morgan Maintains Overweight on Cipher Digital, Lowers Price Target to $22"
- **MARA** -5.3%: "Marathon Digital Holdings Q2 EPS $(1.60) Misses $0.26 Estimate, Sales $174.881M Miss $203.668M Estimate"
- **ONDS** +4.4%: "Ondas U.S. Unit Mistral Receives $50M+ Order From The U.S. Army For Tactical Lethal Unmanned Systems"

## Day Trading Watchlist

Rule: gap over 3%, price over $3, market cap over $1B, premarket RVOL over 1.5, and price already breaking above yesterday's high. This is the Trend Join Long setup.

No names cleared the day-trading bar today. All 20 gappers came back `day_eligible: false`, and this run every single one is missing `premarket_high`, `hod`, `lod`, and `vwap`, so the "breaking above yesterday's high" leg can't even be checked from premarket data. Using the packet's gap-price stand-in against `prior_day_high` instead, three names are sitting close: **ONDS** ($9.105 vs a $9.13 prior high, 2.5 cents short) has a market cap of $4.51B and volume-based RVOL of 36.25x, and its catalyst is real (Army and Air Force contracts, an NFL stadium security deal). **BTG** ($5.035 vs $5.08, 4.5 cents short) and **CDE** ($17.39 vs $17.50, 11 cents short) both have RVOL north of 45x, but both are gapping up on quantified earnings misses, see Skips and Traps below before treating either as a clean watch name. Nothing here is a trade yet, just names to watch if the premarket data fills in.

## Swing Watchlist

Rule: gap of 8% or more, price over $3, open above yesterday's high, open above the 200-day SMA, market cap of $800M or more, and a real catalyst. Entry and exit management for swing names isn't built yet either way, these would be watch-and-build-a-plan names, not full trade plans.

No names cleared the swing bar either. `today_open` hasn't printed yet (premarket), so the packet uses each ticker's current gap price as a stand-in, and the closest misses are all failing on the "open above yesterday's high" leg by single-digit cents: **GENVR** ($3.94 vs a $4.00 prior high, 6 cents short, $2.36B market cap, but its only catalyst in the packet is a generic sector-roundup mention, not a dedicated story), **QNST** ($21.08 vs $21.28, 20 cents short, $1.21B cap, real earnings-jump catalyst), and **CRSR** ($14.35 vs $14.58, 23 cents short, $1.55B cap, real beat-and-raise catalyst). **BTG** and **CDE** are also close on price (4.5 and 11 cents short) but both carry the earnings-miss red flag from Skips and Traps. None of these are gradeable as a real miss until the actual open prints.

## Market Trends of the Day

The proxies lean risk-on this morning, Nasdaq (QQQ, +1.15%) and Russell 2000 (IWM, +1.09%) are out front, Dow (DIA, +0.24%) is the laggard. Beyond that four-line snapshot there's no breadth or rates read, VIX, 10-year yield, 3-month yield, oil, and the dollar all came back null.

Earnings season still splits the gap list. On the clean-beat side: Corsair Gaming (CRSR) surged on a beat-and-raise Q2, and QuinStreet (QNST) jumped over 25% overnight on its own results. On the miss side: B2Gold (BTG) missed both EPS ($0.03 vs $0.09 estimate) and sales ($789.354M vs $879.441M estimate) and is still up 22.9%, Coeur Mining (CDE) missed both lines too ($0.12 vs $0.32 EPS, $1.086B vs $1.286B sales) and is up 11.2%, and MARA Holdings missed by a wide margin ($(1.60) vs $0.26 EPS, $174.881M vs $203.668M sales) and is down 5.3%, at least MARA's move points the right direction for its news.

Ondas (ONDS) is the one name running on a genuinely fresh, dedicated, positive catalyst stack today: an Army order for its Mistral unit, an Air Force Research Laboratory contract, and a Jacksonville Jaguars stadium security deal, all inside the packet. Most of the rest of the list is either a low-float name moving on circuit-breaker halt chains (YJ, WYHG), a micro-cap with a market cap under $250M or missing entirely (MB, RCEL, VATE, PN, WYHG, YJ), or a catalyst that's really just a sector-roundup mention rather than a dedicated story (GENVR, YXT, LASR, QDEL). WYHG stands out for a mismatched catalyst: the attached headline says "halted on circuit breaker to the upside" from a prior session while today's move is -54.9%, treat that headline as stale noise, not an explanation for today's drop.

## Technical Signals for Today

Only the four index ETF proxies are usable this run. Alpaca has SPY (S&P 500 proxy) at 773.16, up 0.59% from a 768.64 prior close. DIA (Dow proxy) is at 539.58, up 0.24% from 538.31. QQQ (Nasdaq proxy) is at 722.89, up 1.15% from 714.70. IWM (Russell 2000 proxy) is at 301.51, up 1.09% from 298.25. VIX, US 10-year yield, US 3-month yield, WTI crude, and the dollar index all came back null, yfinance rate-limited every one of those legs and there's no Alpaca proxy wired in for them. No breadth or rates read beyond the four levels above.

## Economic Data, Rates and the Fed

The packet's econ calendar is empty, zero high-impact USD releases listed for today (August 10) and zero for tomorrow (August 11). No scheduled data catalyst either day per this feed. The one Fed-adjacent item in the packet is a news headline, not a calendar entry: "Morning Bid: Fed's Cook grilled again," from the market news feed, worth knowing it's out there but the packet doesn't carry any detail on what it says.

## Coming Up

- **Tomorrow's events:** Nothing on the high-impact USD calendar for Tuesday, August 11, per the packet.
- **Earnings:** `next_earnings_date` came back null for all 20 gappers in this packet, nothing scheduled to report from today's list.

## Skips and Traps

**BTG** is up 22.9% despite missing both EPS ($0.03 vs $0.09 estimate) and sales ($789.354M vs $879.441M estimate), a classic up-on-bad-news pop. RBC also lowered its price target to $5 in the same headline set. Worth a hard second look before trusting the move, not a green light just because RVOL is high.

**CDE** is up 11.2% on the same pattern, EPS $0.12 vs a $0.32 estimate and sales $1.086B vs a $1.286B estimate, both misses, while Scotiabank maintained its rating but lowered its price target to $26.50. Gold-sector strength may be doing more work here than the actual print.

**TE** is up 5.6% with a dilutive-flavored headline attached, a prospectus for the resale of 13,615,979 shares. That's a resale registration for existing holders, not a fresh primary raise, but it's still a share-supply overhang worth flagging next to a modest 5.6% pop.

**PN**, **SEZL**, and **MARA** are all down on real, explained bad news rather than an "up on bad news" trap, PN priced a dilutive registered direct offering at $3.50/share, Sezzle drew a price-target cut to $155 from KBW after Q2 results, and MARA missed Q2 by a wide margin on both lines. None of these are buy-the-dip setups off this packet, the down moves match the news.

**WYHG** carries a stale, mismatched catalyst, the attached headline is a prior-session "halted on circuit breaker to the upside" story while today's actual move is -54.9%. Don't treat that headline as an explanation for today's drop, the packet doesn't have a fresh one.

**YJ**, **MB**, **RCEL**, **VATE**, and **GENVR** are all extreme-percentage gappers on thin or missing fundamentals, YJ and PN have no market cap at all (SEC has no filing on record), and MB ($153M), RCEL ($240M), and VATE ($165M) all fail the swing watchlist's $800M cap floor outright. Several of these moves are tied to circuit-breaker halt chains rather than a single clean story. Not tradeable off this packet regardless of how the eligibility flags eventually resolve.

**YXT**, **LASR**, and **QDEL** all carry `catalyst_found: true`, but the only headlines attached to any of them are sector-roundup or group-mention pieces ("12 ... Stocks Moving In...", "...Joins Sezzle, Resmed, Ouster..."), not a dedicated story for the specific ticker. Treat the catalyst flag as technically true, not as confirmation of a real story.

Beyond those, **ONDS** is the closest miss on the day-trading side (2.5 cents below its prior-day high, real defense-contract catalysts, $4.51B market cap), and **GENVR**, **QNST**, and **CRSR** are the closest misses on the swing side (6, 20, and 23 cents below their prior-day highs on the pre-open stand-in price). Worth a watch once the real open prints and intraday data comes back, not a trade yet.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
