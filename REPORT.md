# Premarket Report: September 16, 2026

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** All four index proxies are red this morning: S&P proxy (SPY) -0.44%, Dow proxy (DIA) -0.62%, Nasdaq proxy (QQQ) -0.65%, Russell proxy (IWM) -0.95%. Broad, uniform risk-off going into the day.
- **The catch we're watching:** Today is the Fed. The packet's own econ calendar has the Federal Funds Rate decision at 2:00pm ET (forecast 4.00% versus 3.75% previous), plus FOMC Economic Projections, the FOMC Statement, and the Press Conference all this afternoon. The news pull is fixated on it too ("Fed expected to hike interest rates for first time in 3 years"), and crypto's already leaning risk-off into the decision, both BMNR and ETHA are gapping down on it this morning.
- **Two-brain verdict:** Single brain, no second opinion to compare.

## Pre-Market Gappers

- **NFEGP** +776.0% - no catalyst headline in the packet
- **AT** +563.1% - "Atlantic Power Q1 EPS $0.00, Sales $72.00M Down From $72.80M YoY"
- **VEEA** +149.3% - "Veea Stock Surges Tuesday: What's Driving the Action?"
- **HQWWW** +73.0% - "IonQ vs. Rigetti Computing: Which Pure-Play Quantum Stock Actually Has the Technology Edge?"
- **HVIIU** +36.8% - "Trading Halt: Halt status updated at 10:35:00 AM ET: Quotation Resumption: IPO Security - Released for Quotation"
- **PSIG** +34.6% - "12 Industrials Stocks Moving In Tuesday's Intraday Session"
- **VRA** +34.5% - "Vera Bradley Q2 2027 Earnings Call Transcript"
- **FTFT** -28.6% - "Future FinTech Shares Fall After Announcing 1-for-4 Reverse Split: What You Need To Know"
- **SWMR** -28.4% - "Swarmer Strikes $224 Million Deal for Ukrainian Combat-Robot Maker Ratel"
- **HQ** +27.7% - "IonQ vs. Rigetti Computing: Which Pure-Play Quantum Stock Actually Has the Technology Edge?"
- **BMGL** -25.2% - "12 Health Care Stocks Moving In Tuesday's Intraday Session"
- **ENVA** -23.4% - "Kestra Medical Technologies Posts Mixed Q1 Results, Joins Enova International, Dave and Buster's And Other Big Stocks Moving Lower In Tuesday's Pre-Market Session"
- **XRPT** -23.3% - "Trading Halt: Halt status updated at 8:55:00 AM ET: Quotation Resumption: News and Resumption Times"
- **CRCA** -23.2% - "ProShares Announces 1-For-10 Reverse Share Split In CRCA And ZSL ETFs"
- **UXRP** -23.2% - no catalyst headline in the packet
- **XXRP** -23.0% - "Take Note XRP Traders: This Leveraged ETF Is 'Designed To Be Traded Each Day'"
- **CIR** -23.0% - "CIRCOR International Announces Completion Of Acquisition By KKR And Welcomes Dan Daniel As Board Chair"
- **RIG** +8.7% - "Transocean Stock Gains Following $80 Million Ultra-Deepwater Contract Award"
- **BMNR** -8.3% - "What's Going On With Bitmine Immersion Stock Tuesday?"
- **ETHA** -5.0% - "Bitcoin and ethereum prices today, Tuesday, September 15, 2026: Crypto prices sliding this morning ahead of Fed meeting"

## Day Trading Watchlist

The "Trend Join Long" rule: gap over 3%, price over $3, market cap over $1B, premarket RVOL over 1.5, and price already breaking above yesterday's high.

`day_eligible: false` on all 20 gappers. `intraday_data_source` is `unavailable` across the board again this run, so premarket high, VWAP, HOD and LOD are null for every single name, that leg can't be confirmed for anyone regardless of the other numbers. Closest fit is **RIG** (Transocean): cap $6.62B clears the $1B floor, gap +8.7% clears the 3% floor, price $5.93 is over $3, RVOL 24.23x is well over the 1.5x floor, and it has a real, current, ticker-specific catalyst (an $80M ultra-deepwater contract award). It misses on the last leg only: price $5.93 is one cent under yesterday's high of $5.94. Nothing else on the list has real cap and RVOL data clean enough to even get this close.

## Swing Watchlist

The swing rule: gap of 8% or more, price over $3, open above yesterday's high, open above the 200-day SMA, market cap of $800M or more, and a real catalyst.

`swing_eligible: false` across all 20. **RIG** is the closest miss here too: gap +8.7% just clears the 8% floor, cap $6.62B clears $800M, price $5.93 is above its 200-day SMA ($5.61), and the catalyst is real and ticker-specific. Same problem as the day-trading leg: price is a cent below yesterday's high ($5.93 vs $5.94), so the "open above yesterday's high" test fails by a hair. No other name in the packet combines a gap this size with a clean cap and a catalyst that actually names the ticker; the other double-digit gappers (NFEGP, AT, HQWWW, HVIIU) either have no real catalyst or cap data that's obviously broken (see Skips and Traps).

## Market Trends of the Day

Today's news pull is almost entirely about the Fed. "Fed meeting live updates: Anticipation builds with Fed expected to hike interest rates for first time in 3 years," "Morning Bid: A time to hike?," and "Dow Jones Futures Rise As ServiceNow, Twilio Lead 8 New Buys; Will Market Bid Bond Voyage After Fed Rate Hike?" all frame today's 2:00pm ET decision as the day's single event. Gold and silver are both trading around the decision too: "Gold price today, Wednesday, September 16, 2026: Gold holds in the $4,300 range, awaiting the Fed's decision" and "Silver price today... rise in anticipation of the Fed." Worth noting the "Dow Jones Futures Rise" headline sits oddly against the packet's own index proxies, which are all red this morning, that's a mismatch between the news pull's framing and what the packet's snapshot actually shows, not something the packet itself explains.

Not everyone agrees a hike is the right call: "This BlackRock strategist opposes a Fed hike. Here are the funds she recommends," and "What history says about longer-term bond yields after the first Fed hike" digs into what usually happens after the first hike in a cycle. Rates context: "5% Treasury yields mean America's debt bill just got a lot bigger" ties into the same rate-hike backdrop, though the packet's own 10-year field came back null this run so there's no live yield number to check it against.

Crypto is leaning risk-off into the decision, and it shows up directly in today's gappers: BMNR (Bitmine Immersion) is down 8.3% with its own headline reading "Bitcoin, Ethereum, XRP, Dogecoin Sink Amid Crypto Bill Failure, Rate Hike Expectations," and ETHA (the iShares Ethereum Trust ETF) is down 5.0% on "Crypto prices sliding this morning ahead of Fed meeting." Elsewhere, "How the Iran war is transforming the relationship between stocks, bonds and oil" is a geopolitical thread running alongside the rate story, and "What Altman, Amodei, Huang and Zuckerberg are saying about the raging AI debate" keeps the AI-bubble debate in the mix without a specific gapper tied to it today.

## Technical Signals for Today

Index proxies: S&P proxy (SPY) 757.42, down 0.44%; Dow proxy (DIA) 521.26, down 0.62%; Nasdaq proxy (QQQ) 704.60, down 0.65%; Russell proxy (IWM) 285.16, down 0.95%. These are Alpaca ETF proxies standing in for the underlying indices, not the indices themselves.

VIX, the 10-year yield, the 3-month yield, WTI crude and the Dollar Index all came back null this run (`yfinance_failed`), so there's nothing to report on volatility, rates or the dollar directly from the packet.

RVOL is confirmed on a handful of names despite HOD/LOD/VWAP being null everywhere: BMNR 27.15x, ETHA 24.29x, RIG 24.23x, all trading many multiples of their 20-day average volume this morning. VEEA's RVOL field reads 2716.13x, current volume of 202.1M against a 20-day average of just 74,411 shares, a real number given the inputs, but with premarket high, VWAP, HOD and LOD all null for VEEA there's no way to confirm how that volume is actually behaving intraday from this packet.

## Economic Data, Rates and the Fed

Today is the event: Federal Funds Rate at 2:00pm ET (forecast 4.00%, previous 3.75%, implying a quarter-point hike), FOMC Economic Projections at 2:00pm ET, the FOMC Statement at 2:00pm ET, and the FOMC Press Conference at 2:30pm ET. Tomorrow's calendar (September 17) is empty in the packet.

## Coming Up

- **Tomorrow's events:** Nothing in the packet's econ calendar for September 17.
- **Earnings:** `next_earnings_date` is null for every one of today's 20 gappers, so there's no confirmed date to flag for any of these names from the packet's own data.

## Skips and Traps

- **NFEGP** +776.0%: `catalyst_found: false`, no headline at all in the packet. A gap this size with no story and a $140.7B market cap attached to a stock that closed at $56.22 yesterday reads like a data artifact, possibly a thinly-traded preferred or legacy share class rather than a real premarket move. Skip.
- **AT** +563.1%: `catalyst_found: true`, but every headline in the packet is stale, an earnings report and sector pieces from 2021, nothing dated to today. No real catalyst behind today's number.
- **HQWWW** +73.0% and **HQ** +27.7%: Both matched to the identical "IonQ vs. Rigetti" piece, which never names either ticker. Both also carry obviously broken market cap fields ($7 and $13 respectively), clearly bad SEC EDGAR fallback data, not usable for the cap leg either way.
- **HVIIU** +36.8%: Only headline in the packet is a stale IPO trading-halt resumption notice, not a story that explains a 36.8% gap. `avg_volume_20d` is 19 shares, essentially no liquidity regardless.
- **PSIG** +34.6% and **BMGL** -25.2%: `catalyst_found: true` only via generic "N Sector Stocks Moving" roundup headlines that don't name either ticker specifically. Treat as no real catalyst.
- **VRA** +34.5%: Real, ticker-specific catalyst (a Q2 2027 earnings call transcript posted today). Market cap is $117.3M, well under both watchlist floors regardless.
- **FTFT** -28.6%: Down gap explained by real, ticker-specific news, a 1-for-4 reverse split. Rational move on real news, not a trap, and a down gap doesn't fit either watchlist's up-move rule anyway.
- **SWMR** -28.4%: Down 28.4% despite headlines that read as good news, a $224M acquisition deal and a strategic partnership announcement. The gap direction doesn't match the headline tone; the packet doesn't say why, so no explanation is offered here beyond flagging the mismatch.
- **ENVA** -23.4%: Down gap with a real, ticker-specific headline naming ENVA directly as moving lower alongside other stocks this morning. Rational decline, not a trap.
- **XRPT** -23.3%, **CRCA** -23.2%, **UXRP** -23.2%, **XXRP** -23.0%: All four are leveraged or futures-linked crypto ETPs, gapping down together with the broader crypto selloff into the Fed decision (see Market Trends). CRCA's only headline is a February 2026 reverse-split notice; UXRP has `catalyst_found: false` with no headline at all; XRPT's headline is a bare trading-halt notice; XXRP's is generic XRP-ETF background, not dated to today. Sector-wide crypto weakness, not individual stock catalysts. Skip all four regardless of gap size.
- **CIR** -23.0%: Every headline in the packet is about CIRCOR International's 2023 acquisition by KKR, nearly three years stale and not behind today's move. Treat as no real catalyst behind the actual gap.
- **RIG** +8.7%: Closest miss on both watchlists, covered above. Real, current catalyst, misses only on being a cent under yesterday's high, with intraday levels unconfirmed either way.
- **BMNR** -8.3%, **ETHA** -5.0%: Both real, ticker-specific down moves tied to the same crypto-weakness-into-the-Fed story. Rational declines given the news, not traps, and both are down gaps so neither fits the watchlists' up-move rules anyway.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
