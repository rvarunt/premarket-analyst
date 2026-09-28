# Premarket Report: September 28, 2026

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** All four index proxies are green: S&P 500 (SPY proxy) +0.53%, Dow (DIA proxy) +0.93%, Nasdaq (QQQ proxy) +0.45%, Russell 2000 (IWM proxy) +0.10%. Broad-based grind higher, Dow out front, nothing close to risk-off.
- **The catch we're watching:** Same stale `prev_close` problem as recent sessions. Comparing `price` against the packet's own `prior_close` field instead of the headline `gap_pct`, 13 of today's 20 "gappers" show a real move under 1%, and the biggest printed gap on the list (MSGY at +309.6%) is actually down 0.98% versus `prior_close`. Only seven names are genuinely moving: IPEXU (-73.2%), VACI.U (-20.7%), LONA (-6.6%), IPEX (-3.7%), SLMT (+4.1%), SUIL (+3.3%), and AIFU (+3.3%), and most of those have no catalyst, a micro-cap price tag too small to trade, or a mechanical explanation (a SPAC unit conversion) rather than a real story.
- **Two-brain verdict:** Single brain, no second opinion to compare.

## Pre-Market Gappers

- **MSGY** +309.6%: "Why Webuy Global Shares Are Trading Higher By Around 15%; Here Are 20 Stocks Moving Premarket"
- **INLF** +72.9%: "INLIF Stock Surges Friday: What's Driving the Action?"
- **TDIC** +60.4%: "Why Webuy Global Shares Are Trading Higher By Around 15%; Here Are 20 Stocks Moving Premarket"
- **IPEX** -57.8%: "GOWell Technology Completes Business Combination with Inflection Point Acquisition Corp. V, To Trade Under NASDAQ Ticker "GOW""
- **WYY** -50.6%: "WidePoint Says GAO Sustained TurningPoint Global Solutions' Protest Of Its DHS Cellular Wireless Managed Services Contract Award, Says Outcome Could Include Corrective Action Or Re-Evaluation; Findings Under Seal"
- **USDEW** +50.4%: no catalyst headline in the packet
- **IPEXU** -47.9%: no catalyst headline in the packet
- **APUS** +47.4%: "Meta, Everpure, Akamai Technologies, Apimeds Pharmaceuticals and Costco: Why These 5 Stocks Are on Investors' Radars Today"
- **WHLR** +39.0%: "Wheeler Real Estate Investment Trust Announces 1-For-9 Reverse Stock Split Effective September 21, 2026"
- **LONA** -34.9%: "LeonaBio Q2 EPS $(0.80) Beats $(1.36) Estimate"
- **AIFU** +32.1%: "AIFU Announces About $135M Private Placement Of 45 Million Shares At $3.00/Share Plus Warrants For Up To 90 Million Shares"
- **WZRD** +27.3%: no catalyst headline in the packet
- **SLMT** +27.1%: "Solmate Infrastructure Announces Launch Of Public Treasury Dashboard, Says SOL Holdings Stood At Approximately $94.5M As Of August 10"
- **SUIL** +24.3%: no catalyst headline in the packet
- **HOST** -23.3%: "Host Digital Inks 12-Year Take-Or-Pay Least Agreement With Its Sponsor For Right To Acquire Second Data Center Site In Oklahoma"
- **TXXS** +23.0%: "Sui Token Gets Wall Street Debut With 21Shares' Leveraged ETF"
- **IPST** +21.6%: "IP Strategy Shares Halted On Circuit Breaker To The Upside, Stock Now Up 73.85%"
- **VACI.U** -21.4%: no catalyst headline in the packet
- **IREN** -4.4%: "Transcript: IREN Q4 2026 Earnings Conference Call"
- **SMCI** +4.2%: "Super Micro Computer Begins Shipments Of Nvidia Vera Rubin NVL72 Racks Integrated With Its Data Center Building Block Solutions And Direct Liquid Cooling Stack"

## Day Trading Watchlist

No names cleared the day-trading bar today. That flag encodes gap over 3%, price over $3, market cap over $1B, premarket RVOL over 1.5, and price already breaking above yesterday's high.

SMCI is the closest thing to a candidate on paper: market cap $28.4B clears the floor easily, and it's one of only three tickers today where premarket RVOL actually came through instead of null (31.57, well above the 1.5 bar). But its price ($43.255) is still sitting about half a percent under yesterday's high ($43.76), so it hasn't broken out yet, and its real move versus `prior_close` is flat (-0.01%). No actual gap here, just elevated volume in a stock sitting right at yesterday's close.

This scan ran premarket (7:28am ET), before the real open prints.

## Swing Watchlist

No names cleared the swing bar either. That flag encodes gap of 8% or more, price over $3, open above yesterday's high, open above the 200-day SMA, market cap of $800M or more, and a real catalyst.

AIFU looks closest on paper: market cap $13.6B clears the $800M floor by a mile, it has a real catalyst (a $135M private placement), and its effective open ($12.02) sits above yesterday's high ($11.75). But that same open sits below its 200-day SMA ($12.58), so it fails that leg. Even setting the SMA aside, AIFU's real move versus `prior_close` is only +3.26%, nowhere near the 8% bar despite the packet's `gap_pct` reading +32.09% (see the stale-`prev_close` note in Skips and Traps). And the catalyst itself is a dilutive offering, not the kind of news the swing backtest is built around. No other name comes within reach of a real 8% move today.

## Market Trends of the Day

The tape is quietly green across the board, but the news feed is more cautious than the price action. Nvidia's $150 billion buyback announcement is the one clean bullish mega-cap headline in the mix, the kind of number that can carry the broader AI trade on its own for a session. Set against that, multiple strategist pieces in today's feed are flagging risk: a "bad-breadth signal" retrospective, a note that "a pullback is brewing" from strategists who've studied every drawdown since 1956, and a piece on how AI agents like Muse could spark a bank run. There's also a currency thread: Japan's currency diplomat Mimura is reportedly warning markets to heed a "very clear" signal on the yen. On the gapper list, the AI/data-center infrastructure theme shows up again in SMCI (new Nvidia Vera Rubin rack shipments) and IREN (a fresh Q4 earnings transcript), both cap-qualified large caps riding the same buildout narrative as the Nvidia buyback headline. Separately, a court ruling that prediction markets can be regulated like gambling (the Kalshi case) is relevant background for SLMT, which is leaning on a Solana-treasury/crypto-adjacent story of its own.

## Technical Signals for Today

Index proxies via Alpaca ETF data: S&P 500 (SPY) +0.53%, Dow (DIA) +0.93%, Nasdaq (QQQ) +0.45%, Russell 2000 (IWM) +0.10%. All four green, no breadth divergence between large caps and small caps today, small caps just lagging a bit.

VIX, the 10-year yield, the 3-month yield, WTI crude, and the dollar index all came back null, yfinance rate limited every one of them even after retries. No direct read on volatility, rates, or the dollar this morning from the snapshot data itself.

## Economic Data, Rates and the Fed

The econ calendar came back empty for both today and tomorrow, and the packet's own note field is blank (no error message logged), so this looks like a legitimately quiet high-impact-USD calendar day rather than a failed fetch. No scheduled catalysts from the calendar to trade around this morning.

## Coming Up

- **Tomorrow's events:** None in the econ calendar (empty, no note given by the packet).
- **Earnings:** No gapper's `next_earnings_date` came back populated, every one is null (the packet's own gaps-to-fill note flags earnings coverage as partial). LONA already reported its Q2 print (EPS beat per the headline above), that's what's driving today's move there, not an upcoming date.

## Skips and Traps

**Most of today's headline gap sizes are stale, not real, same issue as recent sessions.** Every gapper carries two different "yesterday" reference prices: `prev_close` (used to compute the `gap_pct` shown on the gapper list above) and `prior_close` (from the daily bars feed, the same source behind `prior_day_high`). For 13 of 20 names, the two disagree badly and the real move is under 1%: TDIC (+60.4% headline vs +0.32% real), USDEW (+50.4% vs -0.08%), APUS (+47.4% vs +0.42%), WZRD (+27.3% vs +0.84%), HOST (-23.3% vs -0.49%), TXXS (+23.0% vs +0.32%), IPST (+21.6% vs -0.27%), IREN (-4.4% vs 0.0%), and SMCI (+4.2% vs -0.01%) are all essentially flat versus `prior_close`. MSGY (+309.6% headline vs -0.98% real) and INLF (+72.9% vs +0.39%) are the most extreme cases of this, two of the biggest headline numbers on the list and neither one is actually moving today. WHLR (+39.0% vs -1.52%) and WYY (-50.6% vs +0.92%) also show the same shape. Treat `gap_pct` with real skepticism today, and lean on `prior_close` for anything you actually check.

**IPEXU and VACI.U are the two names with a real move and no catalyst, skip both outright.** IPEXU is down 73.24% versus `prior_close` (the packet's own biggest real mover today) with `catalyst_found: false`, no market cap, and `avg_volume_20d` of 0. VACI.U is down 20.67% real, also `catalyst_found: false`, also no market cap, with `avg_volume_20d` of just 16. Both carry the U-suffix SPAC-unit naming pattern and effectively no trading history in the data, structural moves, not stories. No catalyst means no trade regardless of how big the real move is.

**LONA has a real catalyst but is too small and too thin to trade.** It's down 6.61% versus `prior_close`, and the packet's headlines explain why: a Q2 EPS beat ($(0.80) vs a $(1.36) estimate) that two analyst firms met by lowering price targets anyway (Mizuho to $15, Citizens to $17). That's a legitimate "beat but sell it" reaction. But market cap is $30.6M and `avg_volume_20d` is only 480 shares, this is a real story on a name too illiquid for either watchlist's size floor.

**AIFU's market cap looks like a data-quality flag, and its catalyst is a trap, not a tailwind.** SEC EDGAR backfill puts AIFU's market cap at $13.6B, which would imply roughly 1.1 billion shares outstanding on a $12 stock doing a $135M private placement, worth treating with the same skepticism as a stale data point rather than taking at face value. Separately, its real catalyst is dilutive: a $135M private placement of 45 million shares plus warrants for up to 90 million more. The only other headline ("AIFU Stock Rises 16% After Hours On Robinhood: Why Is It Moving?") doesn't actually explain the move. Up on a dilutive offering with no real explanation for the pop is exactly the setup to be skeptical of, size down or skip.

**HOST's catalyst list is internally contradictory.** One headline sounds like a growth story ("Host Digital Inks 12-Year Take-Or-Pay Least Agreement With Its Sponsor For Right To Acquire Second Data Center Site In Oklahoma"), but the stock is actually down (real move -0.49%, headline gap -23.3%). The other headline in the packet, "Host Hotels & Resorts Upgraded On Improving Growth Prospects," is about Host Hotels & Resorts, a different company (real ticker HST) than the "Host Digital Inc." this packet has under ticker HOST. That's a catalyst mismatch sitting right in the data, don't trust this name's news feed today.

**IPST pairs a real bad-news headline with an unexplained upside halt.** "IP Strategy Gets Nasdaq Warning After Missing Quarterly Filing Deadline" is a genuine compliance problem. The other specific headline just confirms a circuit-breaker halt to the upside happened, without explaining why. A stock popping on a listing-deficiency headline with no positive catalyst behind the halt is the up-on-bad-news pattern the rules call out, skip it.

**MSGY and TDIC have no ticker-specific catalyst at all, and their RVOL numbers look like a data-quality issue on top of that.** Every headline the packet has for each is a generic sector or market roundup, none name the company or explain a move dated to today. MSGY shows `rvol` of 3,399.65x and TDIC shows 6,690.6x on sub-$150M market caps, numbers at that scale on names this small usually mean thin/illiquid trading or a bad data point, not a tradeable signal either way.

**IPEX is a mechanical SPAC-conversion move, not a dip to buy.** The catalyst headlines explain it clearly: GOWell Technology just completed its business combination with Inflection Point Acquisition Corp. V and now trades under the new ticker "GOW". IPEX's -57.75% headline drop (real move -3.66%) is the old SPAC ticker being wound down as the combined company migrates tickers, not a name reacting to news on its own merits. No market cap available either.

**TXXS looks like a new-issue ETP listing, not a stock gap.** The headlines point to a 21Shares Sui-linked leveraged ETF making its Wall Street debut, with a trading halt tagged "Quotation Resumption: New Issue Available." That's listing-day volatility for a new fund product, not the kind of single-name catalyst gap this scanner is built to trade.

**Wide data blackout again this run.** The per-ticker enrichment log shows yfinance returning "Too Many Requests" on nearly every ticker's intraday, news, and earnings pull, and the packet's own gaps-to-fill note counts 86 failed requests even after retries. That's why VWAP, high/low of day, and premarket high are null for every single gapper today, and why RVOL only came through for three names (MSGY, INLF, TDIC among the micro caps, plus IREN and SMCI among the cap-qualified names). VIX, the 10-year, the 3-month, oil, and the dollar are all null for the same reason. Market cap is unavailable even after the SEC EDGAR fallback for eight names: IPEX, USDEW, IPEXU, WZRD, SLMT, SUIL, TXXS, and VACI.U.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
