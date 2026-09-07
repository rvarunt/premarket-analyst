# Premarket Report: September 7, 2026

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** Today is Labor Day. The packet's own news feed carries a MarketWatch headline asking "Is the stock market open today for Labor Day? What about bond trading and mail delivery?" There's no regular equity session today, so the "gappers" below aren't a real premarket move, they're leftover pricing from Friday, September 4's close.
- **The catch we're watching:** The scan doesn't know it's a holiday. Every gapper in this packet came back with `intraday_data_source: unavailable`, meaning no premarket high, VWAP, HOD, or LOD could be pulled for anyone, and the econ calendar is empty for both today and tomorrow. That combination (no intraday data, no econ prints, blank holiday) all points the same direction: don't trade off this packet today.
- **Two-brain verdict:** Single brain, no second opinion to compare.

## Pre-Market Gappers

Every name below is a rules-engine hit on gap size, not a confirmed premarket move (see the catch above). Full catalyst headline quoted as-is from the packet where one was found.

- **AOUT** +44.7% — "Gold Falls Over 1%; American Outdoor Brands Shares Jump After Q1 Results"
- **BANL** -40.7% — "CBL International Regains Nasdaq Compliance"
- **TRBG** -38.0% — "12 Industrials Stocks Moving In Friday's After-Market Session"
- **LULG** -35.1% — "New Leverage Shares ETFs Let Traders Go 2X On Lululemon — And Other Companies"
- **PATX** -33.2% — "Tradr Fires Up High-Octane 2x ETFs Targeting Rare Earths, AI, Defense"
- **IPEXU** -31.0% — no catalyst found in the packet
- **GRNQ** +30.8% — "Greenpro Capital Q1 EPS $(0.10) Down From $(0.08) YoY, Sales $405.386K Up From $352.755K YoY"
- **RIBBU** -30.0% — "Reported Earlier, Ribbon Acquisition Corp Prices $50M Initial Public Offering Of 5M Units At $10/Unit"
- **WZRD** +29.0% — no catalyst found in the packet
- **NX** +22.2% — "Conference Call: Quanex Building Prods Sees Q4 Sales $499.596M-$504.494M vs $497.355M Est"
- **GWRE** -19.9% — "Oppenheimer Maintains Outperform on Guidewire Software, Raises Price Target to $210"
- **AIFU** -19.2% — "AIFU Announces Appointment Of Shanyu Chang As CFO Effective Immediately"
- **LULU** -17.4% — "LULU Stock Got Crushed 17% — Ross Gerber Says Lululemon Is in 'Shambles' as Michael Burry Calls His Largest Position a 'Trickster'"
- **IREN** +7.3% — "BTIG Reiterates Buy on IREN, Maintains $80 Price Target"
- **TSLA** -6.0% — "TSLA Critic Gordon Johnson Rips Cybercab Launch After Elon Musk's 'Storm of Cybercabs' Promise: 'The Robotaxi Story Was Never About Robotaxis'"
- **MU** +5.9% — "Micron and SanDisk Stocks Rebound as Investors Bet on AI Boom, Cheap Valuations"
- **BMNR** -5.5% — "What's Going On With BitMine Immersion Stock Friday?"
- **NFLX** -5.4% — "Netflix Stock Is Trending Higher: What's Happening?" (this headline's own framing doesn't match the -5.4% number below it, more on that in Skips and Traps)
- **SMCI** +4.5% — "Super Micro Stock Rises in Sympathy After Dell's Blowout Quarter"
- **INTC** +4.5% — "AMD and Intel Soared as Nvidia Lagged: Has the AI Trade Changed?"

## Day Trading Watchlist

This flag encodes "Trend Join Long": gap over 3%, price over $3, market cap over $1B, premarket RVOL over 1.5, and price already breaking above yesterday's high.

No names cleared the day-trading bar today. Every single gapper in the packet has `day_eligible: false`. Part of that is real (most of these names are micro-caps or already fading on bad news), but part of it is also that the breakout check can't even run: premarket high, VWAP, HOD, and LOD are null for all 20 gappers because the intraday feed came back unavailable this scan. There's no live tape to trigger against anyway since markets are closed for Labor Day.

## Swing Watchlist

This flag encodes: gap of 8% or more, price over $3, open above yesterday's high, open above the 200-day SMA, market cap of $800M or more, and a real catalyst.

No names cleared the swing bar either. `swing_eligible` is false across the board. A few names here (AOUT, GRNQ, NX) clear the gap-size and catalyst bar on paper, but the rules engine still says no, most likely because `today_open` is null and the trend checks against yesterday's high and the 200-day SMA can't be confirmed without a real open. Nothing here to add to the list today.

## Market Trends of the Day

Take this with the holiday caveat up top: none of it is today's live tape, it's Friday's session repeating through Monday's stale prices.

The AI trade looks like it's rotating hardware to hardware. Micron and SanDisk rebounded on cheap-valuation buying, Intel and AMD "soared as Nvidia lagged" per the packet's own framing, and Super Micro rode Dell's "blowout quarter" in sympathy. Jensen Huang's net worth is cited as up $36B on the same AI-eyes-record-high story. At the same time, Sam Altman is quoted flagging "first signs" of a bubble, and crypto miners/proxies like IREN and BMNR are mixed, IREN up on an analyst reiteration, BMNR down with bitcoin, ethereum, and dogecoin all soft as "Iran War Uncertainty Persists."

Consumer discretionary took the hardest single hit: Lululemon is down sharply with Ross Gerber calling the company "in shambles" and Michael Burry reportedly calling his own largest position a "trickster." That's a real, ugly, single-name story, not a sector rotation.

Tesla is fighting its own narrative battle post-Cybercab launch. Two separate critics (Gordon Johnson, Gary Black) are quoted pushing back hard on the robotaxi story and the marketing spend behind it, even as Cathie Wood is quoted putting Tesla among her "top bets" on the AI theme.

## Technical Signals for Today

The only clean numbers this run are ETF-proxy fills, not the real indices, and half the board is blank:

- S&P 500 (proxied via SPY): 770.18, down 0.38% from prior close.
- Dow (proxied via DIA): 534.04, down 0.52%.
- Nasdaq (proxied via QQQ): 719.10, up 0.20%.
- Russell 2000 (proxied via IWM): 295.94, up 0.26%.
- VIX, US 10Y, US 3M, WTI crude, and the dollar index (DXY) all came back null, yfinance failed on every one of them.

Mixed and roughly flat across the proxies, but again, none of this is a live Labor Day tape. Treat these as reference points, not something to trade against this morning.

## Economic Data, Rates and the Fed

The packet's econ calendar is empty both today and tomorrow, zero high-impact USD releases either day per the feed. That's consistent with the holiday: no major data is scheduled to print on Labor Day.

## Coming Up

- **Tomorrow's events:** None listed on the high-impact USD calendar for September 8.
- **Earnings:** No `next_earnings_date` was populated for any gapper in this packet, nothing to flag.

## Skips and Traps

- **IPEXU and WZRD:** No catalyst behind either move (`catalyst_found: false`). Skip both on that alone, gap size means nothing without a story.
- **GRNQ:** The catalyst headline itself is the red flag. Its own quoted earnings print is $405,386 in quarterly sales against a $339M market cap, that's a business generating four-tenths of one percent of its market cap in a quarter. Reverse split history and a prior trading halt on top of that. This is a name to leave alone even though it's not on the swing list.
- **LULG and PATX:** Both look like leveraged single-stock-style ETF products (LULG tracks Lululemon exposure, PATX ties to a "2x ETFs targeting rare earths, AI, defense" launch) riding their underlying's move at an amplified multiple, not a company-specific catalyst. Treat the size of the move as leverage, not signal.
- **BANL, TRBG, RIBBU:** Thin or stale catalysts. BANL's most relevant headline is Nasdaq-compliance news with no clear tie to a 40% drop, TRBG's only "catalyst" is a generic "stocks moving" listicle mention, and RIBBU's headline is January IPO pricing news for what looks like a SPAC, none of that explains today's number.
- **GWRE:** Worth a second look before anyone reads this as a straightforward drop. The stock is down nearly 20% on the gap, but the two most recent headlines are Oppenheimer and Wells Fargo both maintaining bullish ratings and raising price targets. That's a real mismatch between the quoted analyst commentary and the price action, the packet doesn't explain it, so don't assume you know the story here.
- **NFLX:** The headline quoted above, "Netflix Stock Is Trending Higher," directly contradicts the -5.4% gap next to it. Likely a stale or mistimed headline in the feed. Either way, nothing in the packet actually explains today's number, skip it.
- **AIFU:** A CFO appointment doesn't explain a 19% drop. Thin catalyst, skip.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
