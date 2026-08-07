# Premarket Report: August 7, 2026

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** Mildly risk-off ahead of the jobs report. All four Alpaca ETF proxies are red premarket: SPY (S&P 500) -0.15%, DIA (Dow) -0.82%, QQQ (Nasdaq) -0.33%, IWM (Russell 2000) -0.51%. VIX, rates, oil, and the dollar all came back null again, yfinance rate-limited every one of those legs.
- **The catch we're watching:** It's jobs day. Non-Farm Employment Change, the Unemployment Rate, and Average Hourly Earnings m/m all drop at 8:30am ET, and that print is the real catalyst for where the tape goes today. Underneath it, 20 gappers came through the screener but every single one still reads `day_eligible: false` and `swing_eligible: false`, yfinance's intraday enrichment (premarket RVOL, HOD/LOD, VWAP, premarket high) got rate-limited across the board again, so most of these setups can't be graded against the rules yet.
- **Two-brain verdict:** Single brain today, no GPT cross-check to compare against.

## Pre-Market Gappers

- **WYHG** +194.3%: "Wing Yip Food Holdings Group Shares Halted On Circuit Breaker To The Upside, Stock Now Up 609.17%"
- **CLRO** +166.3%: "ClearOne (CLRO) Stock Soars Over 98% After Hours: Here's What You Need To Know"
- **AMEM** +116.2%: "Trading Halt: Halt status updated at 9:30:00 AM ET: Quotation Resumption: IPO security released for quotation"
- **YXT** -66.1%: "YXT Prices Offering Of 150K ADSs At An Offering Price Of $7 Per ADS"
- **TDUP** -50.5%: "Telsey Advisory Group Maintains Outperform on ThredUp, Lowers Price Target to $6"
- **ZTG** +47.8%: "12 Industrials Stocks Moving In Tuesday's After-Market Session" (a sector roundup mentioning ZTG, not a dedicated story)
- **WLDS** +46.7%: "Wearable Devices Prices ~$3.3M Offering Of 1M Shares At $3.285 Per Share"
- **IOVA** +43.1%: "Iovance (IOVA) Stock Soars After Better-Than-Expected Q2 Results"
- **HNST** +40.8%: "B. Riley Securities Maintains Buy on Honest Co, Raises Price Target to $5"
- **UTI** -34.2%: "Universal Technical Q3 EPS $0.04, Inline, Sales $218.907M Miss $219.891M Estimate"
- **INSM** +33.9%: "Motorola Solutions Posts Upbeat Q2 Earnings, Joins Insmed, Diodes, Parker-Hannifin And Other Big Stocks Moving Higher On Thursday" (INSM gets a passing mention, not a dedicated story)
- **KRO** +32.5%: "Kronos Worldwide Shares Surge on Q2 Earnings Beat"
- **LZ** -30.1%: "William Blair Downgrades LegalZoom.com to Market Perform"
- **AEVA** +28.8%: "Aeva Technologies Q2 Adj. EPS $(0.41) Beats $(0.43) Estimate, Sales $6.136M Beat $5.920M Estimate"
- **SITM** +26.6%: "UBS Maintains Buy on SiTime, Raises Price Target to $840"
- **ATS** -26.6%: "ATS Q1 Adj. EPS $0.25 Misses $0.29 Estimate, Sales $504.423M Miss $526.470M Estimate"
- **WPP** +25.9%: "WPP H1 EPS $0.02 Down From $0.27 YoY, Sales $8.570B Beat $3.260B Estimate"
- **TRIP** -25.5%: "TripAdvisor Q2 Adj. EPS $0.35 Misses $0.37 Estimate, Sales $441.900M Miss $503.851M Estimate"
- **CDE** -10.4%: "Coeur Mining Q2 Adj. EPS $0.12 Misses $0.32 Estimate, Sales $1.086B Miss $1.286B Estimate"
- **JOBY** +6.0%: "Joby Aviation Beats Q2 Revenue Estimates, Raises FY Guidance"

## Day Trading Watchlist

Rule: gap over 3%, price over $3, market cap over $1B, premarket RVOL over 1.5, and price already breaking above yesterday's high. This is the Trend Join Long setup.

No names cleared the day-trading bar today. All 20 gappers came back `day_eligible: false`. For most of them that's a data gap: `premarket_high`, `hod`, `lod`, and `vwap` are null and `intraday_data_source` reads `unavailable`, yfinance got rate-limited on the intraday leg again this run. But two names would still fail the rule even with RVOL data present: **IOVA** (rvol 81.1, price $6.21) and **JOBY** (rvol 46.91, price $8.26) both clear the RVOL bar easily, but neither has broken above yesterday's high yet ($6.38 for IOVA, $8.59 for JOBY), missing by 17 cents and 33 cents respectively. Worth a premarket watch if that gap closes, not a trade yet.

## Swing Watchlist

Rule: gap of 8% or more, price over $3, open above yesterday's high, open above the 200-day SMA, market cap of $800M or more, and a real catalyst. Entry and exit management for swing names isn't built yet either way, these would be watch-and-build-a-plan names, not full trade plans.

No names cleared the swing bar today either. Every gapper came back `swing_eligible: false`. `today_open` hasn't printed yet (premarket), so the packet uses each ticker's current gap price as a stand-in, and most of the 8%+ gappers are sitting just under yesterday's high on that stand-in: KRO ($8.23 vs $8.71 prior high), AEVA ($25.26 vs $28.34), SITM ($687.50 vs $692.37), and WPP ($25.95 vs $26.61) all miss by a small margin. CLRO and WYHG clear the gap percentage easily but fail the $800M market cap floor outright ($26.2M and $494.8M). Nothing here is a clean miss, most names are sitting just below the trigger with the real open still to print.

## Market Trends of the Day

Earnings season is still the dominant force, split cleanly between beats and misses. On the beat-and-raise side: Iovance (IOVA) soared on a better-than-expected Q2 and affirmed FY2026 sales guidance of $350M-$370M against a $362M estimate, Kronos Worldwide (KRO) beat on both EPS and sales, Aeva Technologies (AEVA) beat estimates and got a Canaccord Genuity price target raise to $26, and Joby Aviation (JOBY) beat Q2 revenue estimates and raised full-year guidance. On the miss-and-cut side: Universal Technical (UTI) came in inline on EPS but missed on sales and lowered FY2026 sales guidance, ATS missed on both EPS and sales, TripAdvisor (TRIP) missed on both lines, and Coeur Mining (CDE) missed on both EPS and sales too.

WPP is the name worth a second look: EPS came in at $0.02, down from $0.27 a year ago, while the packet's own headline says sales beat estimate ($8.570B vs $3.260B). That's a lopsided-looking "beat" against an EPS collapse, and the stock is up 25.9% anyway. Take the headline at face value since that's all the packet has, but don't assume a clean beat-and-raise story here the way IOVA or KRO read.

The rest of today's gap list leans toward low-liquidity, catalyst-thin names. WYHG and CLRO are both up on circuit-breaker halt chains rather than a fresh dedicated story (CLRO's real driver looks like merger shareholder approval, buried in an after-hours headline), AMEM is a fresh IPO print (gap percentage is a pricing artifact, not a signal), and ZTG and INSM both carry `catalyst_found: true` on nothing but sector-roundup mentions, no dedicated story behind either move. WLDS is up 46.7% on a stale dilutive offering headline from late July, nothing fresh in the packet explains today's pop. YXT is worth flagging for continuity: it spiked over 800% on circuit-breaker halts in the prior session and is down 66.1% today on a real catalyst, a $7-per-ADS offering pricing, a sharp round trip in two days.

## Technical Signals for Today

Only the four index ETF proxies are usable this run. Alpaca has SPY (S&P 500 proxy) at 768.64, down 0.15% from a 769.79 prior close. DIA (Dow proxy) is at 538.31, down 0.82% from 542.77. QQQ (Nasdaq proxy) is at 714.70, down 0.33% from 717.10. IWM (Russell 2000 proxy) is at 298.25, down 0.51% from 299.77. VIX, US 10-year yield, US 3-month yield, WTI crude, and the dollar index all came back null, yfinance rate-limited every one of those legs and there's no Alpaca proxy wired in for them. No breadth or rates read beyond the four levels above.

## Economic Data, Rates and the Fed

Jobs day. Three high-impact USD releases hit at 8:30am ET this morning: Average Hourly Earnings m/m (forecast 0.3%, previous 0.3%), Non-Farm Employment Change (forecast 85K, previous 57K), and the Unemployment Rate (forecast 4.2%, previous 4.2%). The payrolls forecast would be a solid step up from last month's 57K print if it hits, while the unemployment rate is expected to hold flat at 4.2%. This print is the whole rates story for today, everything else on the tape is downstream of how it lands against forecast.

## Coming Up

- **Tomorrow's events:** Nothing on the high-impact USD calendar for Saturday, August 8, per the packet.
- **Earnings:** `next_earnings_date` came back null for all 20 gappers in this packet, nothing scheduled to report from today's list.

## Skips and Traps

**WYHG** is up 194.3% purely on a chain of circuit-breaker halt headlines, no dedicated fundamental story behind the move in the packet. Market cap ($494.8M) also fails both watchlist floors outright. Treat the halt chain as evidence of a violent, thin-liquidity move, not a tradeable catalyst.

**CLRO** is up 166.3% with a real driver buried in the headlines (merger shareholder approval), but the market cap is $26.2M, this is a micro-cap with a 69M-share volume print on a stock that trades under 13K shares a day on average. Automatically fails both watchlist cap floors and isn't something to chase off this packet.

**AMEM** is up 116.2%, but this is a Day 1 IPO print (the only headline is an IPO quotation-resumption halt notice), not a real premarket gap. Market cap came back null (SEC has no CIK on file). Treat the gap percentage as a pricing artifact, not a signal.

**ZTG** and **INSM** both carry `catalyst_found: true` but every headline attached to either is a sector roundup ("12 Industrials Stocks Moving...", "...Joins Insmed...") that mentions the ticker in passing, not a dedicated story. The flags are technically true, the actual story confirmation is thin, especially for INSM given its $28.9B market cap and 33.9% gap.

**WLDS** is up 46.7% on a dilutive offering headline dated back in late July, nothing in the packet is a fresh catalyst for today's specific move. Direction and timing don't line up cleanly here.

**WPP** is up 25.9% despite EPS down 92% year over year ($0.02 vs $0.27), with the packet's own sales figure ($8.570B) beating an estimate that looks small by comparison ($3.260B). Worth reading the "beat" with some skepticism rather than assuming a clean beat-and-raise story.

**HNST** is up 40.8% on two analyst price-target raises to just $5 apiece, no earnings or news headline in the packet backs a move of that size. The catalyst is real but the magnitude looks out of proportion to what's actually in the packet.

Beyond those, **IOVA** and **JOBY** are the two names closest to clearing the day-trading bar: both have real RVOL and a real catalyst (earnings beats), but neither has broken above yesterday's high yet, IOVA is 17 cents short, JOBY is 33 cents short. Worth a premarket watch, not a trade yet. On the swing side, KRO, AEVA, SITM, and WPP all clear the 8% gap and catalyst legs but are still trading a few percent under yesterday's high on the pre-open stand-in price, none of them are gradeable as a real miss until the actual open prints.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
