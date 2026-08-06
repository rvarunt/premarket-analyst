# Premarket Report: August 6, 2026

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** Mixed, not a clean risk-on or risk-off open. Alpaca ETF proxies have the Nasdaq (QQQ) down 0.91% and the S&P (SPY) down 0.17%, but the Dow (DIA) is up 0.43%. VIX, rates, oil, and the dollar all came back null, Yahoo rate-limited every one of those legs again.
- **The catch we're watching:** 20 gappers came through the screener, several with real earnings beat-and-raise or miss-and-cut catalysts behind them, but every single one still reads `day_eligible: false` and `swing_eligible: false`. That's not the rules saying no, it's the intraday data (premarket RVOL, today's open, VWAP, HOD/LOD) coming back null across the board because yfinance got rate-limited on every enrichment call this run. The setups can't actually be graded yet.
- **Two-brain verdict:** Single brain, no second opinion to compare.

## Pre-Market Gappers

- **ATTO** +4544.8%: "Reported Earlier, Attovia Therapeutics Prices Upsized Initial Public Offering Of 17M Shares At $17.00 Per Share, Raising $289.0M"
- **YXT** +801.2%: "YXT.com Shares Halted On Circuit Breaker To The Upside, Stock Now Up 513.46%"
- **INLF** +97.2%: "INLIF Shares Halted On Circuit Breaker To The Upside, Stock Now Up 161.64%"
- **JLHL** +72.5%: "Why Arista Networks Shares Are Trading Higher By 13%; Here Are 20 Stocks Moving Premarket" (a sector roundup mentioning JLHL, not a dedicated story)
- **OESX** +54.4%: "Orion Energy Sys Q1 EPS $0.47 Beats $0.14 Estimate, Sales $25.743M Beat $23.890M Estimate"
- **TDCL** -48.6%: no catalyst headline in the packet
- **APPS** +38.5%: "Digital Turbine Shares Surge Following Strong Q1 Earnings Beat and Raised Outlook"
- **BLMN** +32.9%: "Outback Owner Bloomin' Brands Cooks Up Bigger Margins, Stronger Sales And A Higher Forecast"
- **MTRN** +30.8%: "Materion Raises FY2026 Adj EPS Guidance from $6.00-$6.50 to $6.80-$7.20 vs $6.43 Est"
- **SEDG** -30.5%: "'SolarEdge Says US Home Solar Market Weak Due to Financing Issues' - Bloomberg"
- **SWIM** +28.1%: "Latham Group Raises FY2026 Sales Guidance from $580.000M-$610.000M to $600.000M-$620.000M vs $590.228M Est"
- **FTK** +27.9%: "Flotek Industries Raises FY2026 Sales Guidance from $270.000M-$290.000M to $340.000M-$350.000M vs $285.250M Est"
- **TBLA** -27.5%: "Taboola.com Lowers FY2026 Sales Guidance from $2.006B-$2.062B to $1.930B-$1.956B vs $2.044B Est"
- **VPG** -27.2%: "Vishay Precision Group Q2 Adj. EPS $0.04 Misses $0.19 Estimate, Sales $83.936M Miss $84.646M Estimate"
- **LMAT** -25.3%: "Wells Fargo Maintains Equal-Weight on LeMaitre Vascular, Lowers Price Target to $94"
- **EOSE** -12.2%: "Eos Energy Enterprises Q2 EPS $(1.20) Misses $(0.18) Estimate, Sales $68.775M Miss $69.430M Estimate"
- **OPEN** -8.8%: "Opendoor Reports Q2 Results, Says 'Everything is Up, Except Costs'"
- **AMD** -8.4%: "AMD Beat Wall Street. These Bear ETFs Stole the Show"
- **CDE** +7.6%: "Coeur Mining Q2 Adj. EPS $0.12 Misses $0.32 Estimate, Sales $1.086B Miss $1.286B Estimate"
- **HL** +7.3%: "Hecla Mining Q2 EPS $0.17 Misses $0.21 Estimate, Sales $333.851M Beat $73.600M Estimate"

## Day Trading Watchlist

Rule: gap over 3%, price over $3, market cap over $1B, premarket RVOL over 1.5, and price already breaking above yesterday's high. This is the Trend Join Long setup.

No names cleared the day-trading bar today. All 20 gappers came back `day_eligible: false`. Worth being straight about why: `premarket_rvol`, `premarket_high`, `hod`, `lod`, and `vwap` are null for every single one, `intraday_data_source` reads `unavailable` across the board. Yahoo's yfinance leg (the intraday/RVOL source) got rate-limited on every one of the 20 enrichment passes this run. The RVOL and above-yesterday's-high legs of this rule literally cannot be checked without that data, so today's empty list is a data gap, not a clean "nothing qualified" read. Not overriding the flags either way, just flagging why the list looks the way it does.

## Swing Watchlist

Rule: gap of 8% or more, price over $3, open above yesterday's high, open above the 200-day SMA, market cap of $800M or more, and a real catalyst. Entry and exit management for swing names isn't built yet either way, these would be watch-and-build-a-plan names, not full trade plans.

No names cleared the swing bar today. Every gapper came back `swing_eligible: false`. `today_open` is null for all 20 (still premarket, hasn't printed), so the open-above-yesterday's-high and open-above-200-day-SMA legs can't be checked yet. A handful of names clear the 8% gap bar (ATTO, YXT, INLF, JLHL, OESX among the big movers), but even setting the missing-open problem aside: ATTO has no market cap in the packet (fails the $800M floor by default), and JLHL's catalyst headlines are all sector roundups mentioning Arista Networks, not a dedicated JLHL story, so that flag looks thinner than it reads. Nothing here is gradeable against the real rule until the open prints and RVOL/market-cap data fills in.

## Market Trends of the Day

Earnings season is running hot in both directions this morning. On the beat-and-raise side: Digital Turbine (APPS) surged on a strong Q1 beat and raised outlook, Bloomin' Brands (BLMN) posted bigger margins and a higher forecast, Materion (MTRN) beat and raised FY26 EPS guidance, Flotek Industries (FTK) beat big on both lines and raised sales guidance, Latham Group (SWIM) raised its sales guidance too, and Orion Energy (OESX) beat and affirmed guidance. On the miss-and-cut side: Taboola (TBLA) cut FY26 sales guidance and guided Q3 light, Vishay Precision Group (VPG) missed on both EPS and sales, and Eos Energy (EOSE) missed badly on EPS. SolarEdge (SEDG) is down on a Bloomberg report that US home solar demand is weak on financing issues, on top of a Goldman Sachs price target cut.

The mining and silver trade looks disconnected from the earnings themselves. Both Coeur Mining (CDE) and Hecla Mining (HL) missed on EPS this quarter but gapped up anyway, with a headline flagging silver at a "now or never" level and a fresh MOU between Hecla's Greens Creek unit and NVRO Metals in the mix. Looks like sector momentum is doing more work than the actual print here.

Chips are sending a split signal too. SoftBank's earnings beat expectations without any OpenAI boost, credited to its Intel stake paying off, per MarketWatch. Meanwhile AMD is down 8.4% premarket despite beating Wall Street estimates and getting price target raises from DA Davidson and Morgan Stanley, MarketWatch's own headline calls out "bear ETFs" stealing the show, a sell-the-news read. Sandisk slumped 9% premarket on guidance that disappointed after its own earnings, and overnight in Seoul, SK Hynix saw a 30% flash crash before recovering most of the loss, with a SocGen strategist calling the Korean chip-stock shakeout nearly done.

Opendoor (OPEN) is worth a specific flag: it beat both EPS and sales estimates, but the stock gapped down anyway on a headline reading "Everything is Up, Except Costs," margin concern trumping the top-line beat.

Outside single names, JPMorgan strategists (via MarketWatch) say hedge funds took heavy hits in the July tech selloff and may be buying meaningfully less of those names going forward, framed as leaving tech more at the mercy of retail flow. Up to 911.5 million SpaceX insider shares become saleable today, though a separate 455.8 million share tranche stays locked up given the stock's recent weakness. Fed's Schmid is on record calling for tighter policy to bring down inflation he calls "too high."

## Technical Signals for Today

Only the four index ETF proxies are usable this run. Alpaca has SPY (S&P 500 proxy) at 769.79, down 0.17% from a 771.11 prior close. DIA (Dow proxy) is at 542.77, up 0.43% from 540.43. QQQ (Nasdaq proxy) is at 717.10, down 0.91% from 723.69. IWM (Russell 2000 proxy) is at 299.77, down 0.64% from 301.71. VIX, US 10-year yield, US 3-month yield, WTI crude, and the dollar index all came back null, yfinance rate-limited every one of those and there's no Alpaca proxy wired in for them. No breadth or rates read beyond the four levels above.

## Economic Data, Rates and the Fed

Nothing high-impact on the USD calendar today. Tomorrow (Friday, August 7) is jobs day: Average Hourly Earnings m/m at 8:30am ET (forecast 0.3%, previous 0.3%), Non-Farm Employment Change at 8:30am ET (forecast 85K, previous 57K), and the Unemployment Rate at 8:30am ET (forecast 4.2%, previous 4.2%). That's the one real rates catalyst on deck this week, and the news feed's own preview piece frames it as likely showing a soft but not worsening pace of hiring. On the Fed-speak side, Schmid is already out pushing for tighter policy given inflation he's calling too high, worth weighing against a payrolls print that's forecast to come in stronger than last month's 57K.

## Coming Up

- **Tomorrow's events:** Average Hourly Earnings m/m, Non-Farm Employment Change, and the Unemployment Rate, all at 8:30am ET Friday, August 7.
- **Earnings:** `next_earnings_date` came back null for all 20 gappers in this packet, nothing scheduled to report from today's list. From the news feed, SoftBank and Sandisk already reported and moved on their prints today, that's already priced in by the time this report goes out.

## Skips and Traps

**TDCL** is down 48.6% with `catalyst_found: false`, no headline behind the move in the packet. No catalyst means no story, skip it.

**ATTO** is up over 4500%, which isn't a real tradeable gap, it's a fresh IPO (Attovia Therapeutics priced its upsized offering at $17, opened around $21). Market cap came back null in the packet too. Treat the printed gap percentage as a data artifact of Day 1 IPO pricing, not a signal.

**YXT** is up over 800% on circuit-breaker halt headlines confirming a real, violent move, but nothing in the packet is a dedicated fresh-news catalyst beyond the halt notices themselves and an unrelated SiTime roundup mention. High risk, thin story confirmation, not something to chase off this packet.

**JLHL** carries `catalyst_found: true` but every headline attached to it is a sector roundup ("12 Industrials Stocks Moving...") or a story about Arista Networks, not a dedicated JLHL headline. The flag is technically true, the actual story confirmation is thin.

Beyond those, the bigger theme today: even the clean beat-and-raise names (BLMN, FTK, MTRN, OESX, SWIM) and the clean miss-and-cut names (TBLA, VPG, EOSE) can't be traded off either rule right now, RVOL and today's open aren't in the packet yet. And a few names are worth a second look before assuming the gap direction tells the whole story: AMD is down despite beating estimates (sell-the-news), CDE and HL are up despite EPS misses (sector momentum, not the print), and OPEN is down despite a top-and-bottom-line beat (cost commentary spooked it). None of these clear the watchlist bars today regardless, but worth knowing the headline doesn't always match the tape.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
