# Premarket Report: August 31, 2026

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** Index proxies are red across the board this morning (S&P, Dow, Nasdaq, Russell 2000 all down small via ETF proxies), Brent crude broke back above $90 on fresh US-Iran fighting, and Fed Governor Warsh's Jackson Hole comments have the market pricing in higher odds of a rate hike.
- **The catch we're watching:** That same Iran flare-up and rate-hike repricing is what's bleeding into risk names this morning. Crypto and crypto-adjacent stocks (MARA, BMNR, PURR) are all down on heavy volume, and IREN is down double digits despite a batch of AI-deal headlines. Tomorrow's ISM Manufacturing PMI is the next data point that could move the rate story further.
- **Two-brain verdict:** Single brain, no second opinion to compare.

## Pre-Market Gappers

Data note before the list: intraday levels (VWAP, HOD, LOD, premarket high/volume) came back unavailable for every name this run, and the broad market snapshot lost VIX, the 10-year, the 3-month, WTI, and the dollar index to the same rate limiting. 100+ requests failed even after retries. What's below is what actually came through.

- **WETO** -50.3% : no ticker-specific headline in the feed, only generic sector mover listicles ("12 Industrials Stocks Moving In Friday's After-Market Session").
- **VISN** -47.9% : "Vistance Networks Authorized Additional $150M Buyback Plan"
- **SWVL** +41.2% : "Swvl Holdings Announces $1.5M Private Placement Of Shares To Sofico Holdings At $1.46 Per Share"
- **CRE** -33.7% : no ticker-specific headline, only generic sector mover listicles.
- **AEHL** -30.5% : "Antelope Enterprise Holdings Announces $18.99M Private Placement Of 15M Class A Ordinary Shares At $1.266/Share With Warrants For 15M Shares At $0.50/Share; Expects Close In Q3 2026"
- **PYPU** -26.0% : only match is an unrelated March story, "Adobe, PayPal, UnitedHealth Just Got 2X ETFs - Direxion Builds Out The Leverage Trade."
- **PYPG** -25.7% : no catalyst found in the feed at all.
- **ESTC** +19.3% : "Wells Fargo Maintains Equal-Weight on Elastic, Raises Price Target to $100"
- **AKTX** +18.8% : "Akari Therapeutics Says Strategic Research Collaboration With Whitehawk Therapeutics Expands Potential Application Of Akari's PH1 Platform Into Dual-Payload ADCs"
- **IREN** -12.6% : "IREN's New AI Contract Adds to $2.8 Billion in Deals as Company Targets $4 Billion ARR, Analysts Say"
- **MRVL** -10.3% : no MRVL-specific headline, just appears in "5 Stocks Investors Couldn't Stop Buzzing About This Week: NVDA, MRVL, CRM and More."
- **MARA** -10.1% : "MARA Holdings Stock Slides Amid Bitcoin Pullback: What's Happening?"
- **ONDS** -9.7% : "Ondas Announces Deal To Acquire Aran Defense For About $33M In Cash Or Stock; Expects Close In Q3 2026"
- **PURR** -9.4% : "Hyperliquid Strategies Q4 EPS $6.24, Sales $6.334M Beat $3.000M Estimate"
- **KEEL** -7.7% : "Keel Infrastructure Q2 Earnings Miss Estimates as Bitcoin Wind-Down Continues"
- **PCG** -7.5% : "Mizuho Downgrades PG&E to Neutral, Lowers Price Target to $16"
- **BMNR** -7.2% : "Bitcoin, Ethereum, XRP, Dogecoin Fall Amid Fresh US-Iran Escalation: Analyst Says BTC Facing 'Final Hurdle' Before Attacking the Highs"
- **SOFI** -5.9% : no real driver in the feed, just a filler headline, "SoFi Stock Edges Lower Friday: What's Going On?"
- **NVDA** -4.7% : no NVDA-specific news, just the broad tape: "Stock Market Today: S&P 500, Dow Futures Fall as US-Iran Tensions Flare Up."
- **AMZN** +4.0% : no clear driver in the feed, closest match is "Performance Comparison: Amazon.com And Competitors In Broadline Retail Industry."

## Day Trading Watchlist

**Rule:** every name here needs `day_eligible: true`, which encodes the "Trend Join Long" setup: gap over 3%, price over $3, market cap over $1B, premarket RVOL over 1.5, and price already breaking above yesterday's high.

No names cleared the day-trading bar today. All 20 gappers came back `day_eligible: false`. On top of that, premarket high, VWAP, HOD, and LOD are all null this run, so there wouldn't be levels to build a plan around even for a marginal name.

## Swing Watchlist

**Rule:** every name here needs `swing_eligible: true`, which encodes: gap of 8% or more, price over $3, open above yesterday's high, open above the 200-day SMA, market cap of $800M or more, and a real catalyst.

No names cleared the swing bar either. All 20 gappers came back `swing_eligible: false`. Several of the bigger up-movers (SWVL, ESTC, AKTX) had a real gap, but none of them cleared the full stack of conditions, so nothing to watch and build a plan around today.

## Market Trends of the Day

The tape is trading off Iran and rates this morning, not earnings. Brent crude jumped back above $90 after the US and Iran exchanged fire for the first time in a month, and that escalation is showing up directly in the news feed and the index proxies (all four major benchmarks are red). Layered on top of that, Fed Governor Warsh's Jackson Hole remarks have futures pricing in higher odds of a rate hike, which is the second leg pressuring risk assets.

Crypto is getting hit the hardest of the visible themes. Bitcoin, Ethereum, XRP, and Dogecoin are all lower on the Iran escalation, and that's dragging crypto-adjacent equities with it: MARA (Bitcoin miner) and BMNR (Bitcoin treasury vehicle) are both down on heavy relative volume, and PURR (Hyperliquid Strategies) is giving back part of last week's 20% surge despite an actual earnings beat.

AI infrastructure financing is the other thread worth flagging. IREN is down double digits despite headlines about a $2.4B debt deal to buy Nvidia chips and $2.8B in cumulative AI compute deals targeting $4B ARR, so the market looks like it's reading the debt raise as leverage risk rather than cheering the growth story. A separate Yahoo Finance piece frames the broader trend directly: AI data center buildout is pulling private equity into the trades. Apple's leadership transition is also in the feed: John Ternus becomes CEO with AI as his first big challenge.

Two small caps (SWVL, AEHL) are worth a callout as a pattern, not just individual names: both have dilutive private placements priced well under the current tape, which is exactly the kind of thing that can make a gap look tradeable when it isn't. More on both below.

## Technical Signals for Today

S&P 500, Dow, Nasdaq, and Russell 2000 proxies (SPY, DIA, QQQ, IWM) are all lower: S&P -0.25%, Dow -0.02%, Nasdaq -0.66%, Russell 2000 -1.35%. Russell's the laggard, consistent with a risk-off, small-cap-hurts-most tape.

VIX, the 10-year yield, the 3-month yield, WTI crude, and the dollar index all came back null (yfinance failed on every one of them this run). No breadth or volatility read available beyond the four index proxies above.

## Economic Data, Rates and the Fed

Nothing on the calendar today (Monday, August 31): zero high-impact USD events.

Tomorrow (Tuesday, September 1): ISM Manufacturing PMI at 10:00am ET, forecast 55.2 versus a previous reading of 55.6. A small step down expected, not a shock number either way.

## Coming Up

- **Tomorrow's events:** ISM Manufacturing PMI, 10:00am ET, forecast 55.2 vs. previous 55.6.
- **Earnings:** No earnings dates on file for any of today's gappers (`next_earnings_date` is null across the board). This packet only tracks each gapper's own next earnings date, not a full market earnings calendar, so this isn't a read on the broader market's earnings slate.

## Skips and Traps

- **SWVL (+41.2%):** Trap. The move is being carried by "Swvl Holdings Announces $1.5M Private Placement Of Shares To Sofico Holdings At $1.46 Per Share," a private placement priced at $1.46 while the stock trades at $3.12. That's steep dilution dressed up as a pop. On top of that, today's price is sitting right at yesterday's high (both $3.12), so there's no real breakout underneath it either.
- **AEHL (-30.5%):** Not a dip to buy, just an explained drop. The $18.99M placement priced at $1.266 against a $3.54 tape is real dilution, and the crash tracks it.
- **VISN (-47.9%):** The only catalyst on file is a buyback authorization, which doesn't square with a stock getting cut nearly in half. Treat this as an unreliable catalyst match, not a real story, and skip it.
- **WETO (-50.3%) and CRE (-33.7%):** No ticker-specific catalyst in the feed for either, just generic sector-mover listicles. No catalyst found, no story, skip both.
- **PYPU (-26.0%) and PYPG (-25.7%):** These read as leveraged single-stock ETFs tracking PayPal, not operating companies (no CIK, no market cap, near-zero volume). PYPG has zero catalyst headlines and PYPU's only hit is an unrelated March ETF-launch story. Skip both.
- **AKTX (+18.8%):** The market cap on file ($1.67 trillion) is obviously broken for a stock trading 331 shares a day on average. Don't trust any cap-based read on this name today, and the paper-thin volume means the gap barely means anything regardless.
- **IREN (-12.6%):** Headlines read bullish (AI contract, $2.4B debt deal for Nvidia chips) but the stock is down double digits on 68x RVOL. Market's pricing the debt raise as leverage risk, not celebrating the deals. Worth watching once it settles, not a name to chase down here.
- **ONDS (-9.7%):** Same pattern as IREN: a real defense acquisition headline, but the stock is sliding. It's also flagged in a short-seller watch-list headline, so today's move could be short-covering noise as much as fundamentals. Skip for now.
- **PURR (-9.4%):** Not a trap, just profit-taking. The Q4 print actually beat (EPS $6.24 vs. $3.00 est., sales beat too), and the stock is giving back part of last week's 20% surge.
- **SOFI (-5.9%), NVDA (-4.7%), AMZN (+4.0%), MRVL (-10.3%):** No stock-specific news behind any of these, just riding the broad Iran/rate-hike tape. Nothing here to trade off the headline.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
