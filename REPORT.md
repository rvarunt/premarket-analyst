# Premarket Report: September 1, 2026

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** Index proxies are mixed and mostly flat to slightly red: S&P -0.31%, Dow -0.69%, Russell 2000 -0.63%, Nasdaq roughly flat at +0.03% (all via ETF proxies, SPY/DIA/QQQ/IWM). VIX, the 10-year, the 3-month, WTI, and the dollar index all came back null.
- **The catch we're watching:** California utilities are getting hit hard this morning. EIX is down 23% ("worst day since 2001") and PCG is down 20%, both tied to a wildfire liability bill headline. Layer that on top of a news feed still leaning on Iran-driven oil risk and jumping global bond yields, plus the ISM Manufacturing PMI print at 10am ET.
- **Two-brain verdict:** Single brain, no second opinion to compare.

## Pre-Market Gappers

Data note before the list: intraday levels (VWAP, HOD, LOD, premarket high/volume) came back null for every single gapper this run, both the Alpaca and yfinance legs. 89 requests failed even after retries this scan, mostly the per-ticker enrichment calls. What's below is what actually came through.

- **AEHL** +83.3% : no ticker-specific headline in the feed, only generic sector-mover listicles and a "surges over 100%: what's going on?" recap that doesn't name a driver.
- **LCFYW** +52.5% : no catalyst found in the feed at all.
- **USDE** +31.2% : no ticker-specific headline, only generic sector-mover listicles.
- **TP** +30.9% : "Ticketplus Q2 EPS $0.21 Up From $0.10 YoY, Sales $12.611M Up From $6.975M YoY"
- **NEOV** +27.0% : "NeoVolta's NeoVolta Power Subsidiary Signs Five-Year Partnership With SK On For 9 Gigawatt-Hours Of Locally Produced Lithium Iron Phosphate Battery Cells To NeoVolta Power From 2027 To 2031"
- **DAIC** -25.0% : no ticker-specific headline, only generic sector-mover listicles.
- **EIX** -23.1% : "QUICK SPARK: Edison Stock Craters 24% In Worst Day Since 2001"
- **YDES** -22.7% : "YD Bio Publishes Review Article Titled Beyond Bone Health: Exploring The 'Heart-Brain-Bone' Axis Modulated By Lipid-Soluble Nutrients"
- **DPRO** +21.4% : "White House Says President Trump Signed Proclamation Imposing Tariffs On Drones And Their Parts And Components; Proclamation Imposes A 100% Ad Valorem Tariff On Drones Of A Certain Size Or With Certain Capabilities That Are Particularly Sensitive For National Security Purposes; Proclamation Imposes A 25% Ad Valorem Tariff On Certain Drones That Are Smaller In Size And Lack Certain Capabilities That Particularly Implicate National Security"
- **CPIX** -20.9% : "Cumberland Q2 Adj. EPS $(0.20) Down From $(0.13) YoY, Sales $166.458K Down From $380.797K YoY"
- **CCUP** +20.3% : no fresh ticker-specific headline, just older generic pieces about the leveraged ETF itself.
- **PCG** -20.1% : "PG&E Stock Slides After Analysts Flag Unresolved California Wildfire Liability Risks"
- **CRCA** +19.5% : no fresh ticker-specific headline, just a stale February reverse-split announcement.
- **CRCG** +19.3% : "Trading Halt: Halt status updated at 8:55:00 AM ET: Quotation Resumption: News and Resumption Times"
- **CRE** -19.2% : no ticker-specific headline, only generic sector-mover listicles.
- **EMAT** +18.2% : "Evolution Metals Secures Plans For Nearly 6x Power Expansion To 750 MW And ~$20.7M Korean Grant; Essential Infrastructure For EM&T To Scale From 1,000 Tons To 10,000 Tons Of Rare Earth Magnet Production By End 2026"
- **BMNR** +6.7% : "Bitmine Buys 53,501 ETH: What Does It Mean for BMNR?"
- **PURR** +5.6% : "Hyperliquid Strategies Beat EPS by 690% - Here's the New Price Target Chardan Set"
- **TSLA** +5.5% : no single TSLA-specific catalyst in the feed, closest is chatter like "Ross Gerber Says TSLA's Robotaxi 'Can Only Grow From Here,' But Warns of 'Bad News'"
- **IREN** +4.9% : "'Blue Owl Leads $2.4 Billion Iren Debt Deal to Buy Nvidia's Chips' - Bloomberg"

## Day Trading Watchlist

**Rule:** every name here needs `day_eligible: true`, which encodes the "Trend Join Long" setup: gap over 3%, price over $3, market cap over $1B, premarket RVOL over 1.5, and price already breaking above yesterday's high.

No names cleared the day-trading bar today. All 20 gappers came back `day_eligible: false`. On top of that, premarket high, VWAP, HOD, and LOD are all null this run, so there wouldn't be levels to build a plan around even for a marginal name.

## Swing Watchlist

**Rule:** every name here needs `swing_eligible: true`, which encodes: gap of 8% or more, price over $3, open above yesterday's high, open above the 200-day SMA, market cap of $800M or more, and a real catalyst.

No names cleared the swing bar either. All 20 gappers came back `swing_eligible: false`. The biggest up-movers by gap size (AEHL, LCFYW, USDE, TP, NEOV) all had prices sitting below their own prior-day high in the packet, so the "open above yesterday's high" leg was never in play for them regardless of catalyst quality. Nothing to watch and build a plan around today.

## Market Trends of the Day

California utility liability risk is the sharpest single-sector story in the feed today. EIX cratered 23% ("worst day since 2001") and PCG is down 20%, both tied directly to a wildfire liability bill, and a Benzinga piece frames it as "California Utilities Crater" alongside the Iran oil headline. That's a real, fresh, negative catalyst hitting a specific sector hard, not a broad market move.

The macro backdrop underneath that is still risk-off-leaning: MarketWatch has global oil prices extending a move over $90 after a report of two tankers struck in the Strait of Hormuz, bond yields "jumping from the U.K. to Japan" while U.S. bonds tumble too, and a separate piece saying Wall Street is "getting a bit nervous" about potential turbulence. A Yahoo Finance headline ties it together on the index level: Dow, S&P 500, and Nasdaq futures falling on inflation and Fed rate-hike fears.

AI infrastructure financing is still a live thread in the gapper list itself: IREN's move is tied to a Bloomberg-reported $2.4 billion debt deal (Blue Owl) to fund Nvidia chip purchases, and Evolution Metals (EMAT) is up on a real expansion and grant announcement tied to rare-earth magnet production. On the company-news side, Nvidia's headline is framed as "a new kind of bet" tied to its record quarter, Dell is tipped to gain from developments at both Nvidia and SpaceX, and Salesforce is described as betting its next chapter on "an unlikely AI marriage."

Crypto is a smaller but present thread: BMNR (Bitmine) is up on buying more ETH, and PURR (Hyperliquid Strategies) is up on both a large EPS beat and talk of a US market entry via Kraken's parent company.

## Technical Signals for Today

S&P 500, Dow, Nasdaq, and Russell 2000 proxies (SPY, DIA, QQQ, IWM) are mixed and mostly small moves: S&P -0.31%, Dow -0.69%, Nasdaq +0.03%, Russell 2000 -0.63%. Nothing dramatic on the index level despite the sharp single-sector move in utilities.

VIX, the 10-year yield, the 3-month yield, WTI crude, and the dollar index all came back null (yfinance failed on every one of them this run, and there's no Alpaca proxy set up for those). No breadth or volatility read available beyond the four index proxies above.

## Economic Data, Rates and the Fed

One high-impact USD release on deck today: ISM Manufacturing PMI at 10:00 AM ET, forecast 55.2 versus a previous reading of 55.6. A small step down expected, worth watching against the bond-yield-jump headlines in the news feed above. Nothing on the calendar for tomorrow, September 2.

## Coming Up

- **Tomorrow's events:** None in the calendar for Wednesday, September 2.
- **Earnings:** No `next_earnings_date` on file for any of today's 20 gappers, it's null across the board in the packet. TP (Ticketplus) just reported Q2 results as today's catalyst itself, but that's a report already out, not a coming date.

## Skips and Traps

- **LCFYW +52.5%:** `catalyst_found: false`. No catalyst behind the move at all. Skip, no story here.
- **AEHL +83.3%, USDE +31.2%, DAIC -25.0%, CCUP +20.3%, CRCA +19.5%, CRE -19.2%:** `catalyst_found` came back true, but every headline attached to these is either a generic sector-mover listicle that doesn't name the company or, for CCUP/CRCA, stale news from months ago about the leveraged ETF itself. There's no real story to hang a trade on. Treat these as noise, not setups, whichever direction they're moving.
- **CRCG +19.3%:** The only headline is a trading halt and resumption notice with no news attached ("Halt News Pending" followed by a resumption). A halt/reopen with no substance behind it is a coinflip on the reopen print, not a tradeable catalyst. Skip until real news shows up.
- **EIX -23.1% and PCG -20.1%:** Real, fresh, bad news (wildfire liability risk), and both are down big on it, so this isn't an "up on bad news" trap, it's a legitimate sector selloff. Still not a long setup: catching a falling knife on unresolved legal liability headlines is its own kind of trap. Both fail the gap-direction requirement for either watchlist anyway.
- **Missing market cap:** USDE, TP, CCUP, CRCA, CRCG, and CRE all came back with `market_cap: null` even after the SEC EDGAR fallback, per the packet's `gaps_to_fill` note (likely a missing CIK or an issuer that doesn't file the concept the fallback looks for). None of these can be properly sized against the market-cap filter, so treat them with extra caution even if a real catalyst shows up later.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
