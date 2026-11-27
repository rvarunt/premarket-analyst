# Premarket Report: November 27, 2026

*Single-brain pass: Claude only. Second brain not wired in yet.*

> Rules pick the watchlist. The AI judges the quality of the setups. This is not financial advice.

**Read this first: Black Friday, and the gap data is stale.** The packet says "Scan run 2026-11-27 07:13 EST (premarket)." But Thursday was Thanksgiving, so the latest daily bar is still Wednesday's. Every gapper row is identical to yesterday's packet: same `price`, `prev_close` and `gap_pct` for all 15 names, and for the cap-qualified names `price` equals `prior_close` (MU 600.4 vs 600.4, SNDK 73.56 vs 73.56, STLA 3.655 vs 3.65, AMBA 35.68 vs 35.66). So these gaps are Wednesday's close vs Tuesday's close, not this morning's premarket. The ETF proxies are also unchanged from yesterday (SPY 716.74 vs 718.91 prev). There are no futures numbers in the packet, only headlines.

The packet has a MarketWatch headline "Is the stock market open on Black Friday?" with the summary "Here's how the day after Thanksgiving will affect trading on Wall Street," but it doesn't give the hours. If today is a shortened session, the 10:00am to 3:30pm window and the 3:51pm flat rule may not fit. Check the exchange schedule before planning anything.

**Data gaps.** Yahoo rate-limited the scan again: 61 requests failed even after retries. Intraday data is `unavailable` for all 15 gappers, so VWAP, HOD, LOD, premarket high and premarket volume are null across the board. `today_open` and `next_earnings_date` are null for all 15. VIX, 10Y, 3M, WTI and the dollar are null. Index levels are ETF proxies (SPY, DIA, QQQ, IWM). Market cap is null for MUU, NVDL, NVD, RKT and NU. `rvol` is null for the seven rows sourced from Alpaca's movers list (WLDSW, EUDA, FCUV, RIBBU, PW, PHAR, AMBA).

## Summary

- **The tape in one line:** Headlines point to a bounce attempt into a heavy tape. MarketWatch: "Stocks are poised for a Friday jump," and CNBC: "The S&P 500 is in a correction. Bear markets and recessions don't always follow." No futures numbers in the packet to confirm the size of it.
- **The catch we're watching:** Goldman says the Friday jump runs "right into a $100 billion wave of automated selling," with the summary noting "one big bout of selling is left for stocks this year by some trend-following trend funds." That's the thing that can flip a holiday pop into a fade.
- **Two-brain verdict:** Single-brain run, no second opinion.

## Pre-Market Gappers

All 15 gappers in the packet. Gap % is `price` vs `prev_close`, which reflects Wednesday's session (see the warning above). Market cap in parentheses. The headline is the first one the packet lists for each ticker.

- **WLDSW** +134.68% ($277.4M, SEC-derived): no headline in the packet (`catalyst_found: false`)
- **EUDA** -53.67% ($7.9M): "EUDA Health Subsidiary Melana International Wins Golden Bull Award 2026 Singapore"
- **FCUV** +53.12% ($5.5M): "Focus Universal Inc. (FCUV) Experiences Significant Stock Price Movement"
- **RIBBU** +52.5% ($475.9M, SEC-derived): no headline in the packet (`catalyst_found: false`)
- **PW** -32.97% ($1.3M): "Power REIT Reports Third Quarter 2026 Financial Results"
- **PHAR** -23.98% ($7.05B, SEC-derived): "Form 8.5 (EPT/RI) Disclosure Regarding Pharos Energy Plc"
- **AMBA** -19.77% ($1.57B): "Analyst Downgrades and Price Target Adjustments for Ambarella"
- **MUU** -8.95% (cap null): no headline in the packet (`catalyst_found: false`)
- **NVDL** -8.01% (cap null): no headline in the packet (`catalyst_found: false`)
- **NVD** +7.94% (cap null): no headline in the packet (`catalyst_found: false`)
- **RKT** +7.34% (cap null): "New York Regulators Fine Rocket Mortgage and Mr. Cooper $6.75 Million for Cybersecurity Violations"
- **STLA** +5.94% ($10.59B): "Stellantis in Advanced Negotiations with Struggling Supplier"
- **SNDK** -5.58% ($10.47B): "Tradr ETFs Announces Launch of Triple Threat Series Including Memory ETF Featuring SanDisk"
- **MU** -4.71% ($679.31B): "Micron Reports High Bandwidth Memory (HBM) Capacity Largely Booked for Upcoming Year"
- **NU** +4.21% (cap null): "Sandy & Junior Announce Residency at Nubank Parque"

## Day Trading Watchlist

The bar is Trend Join Long: gap > 3%, price > $3, market cap > $1B, premarket RVOL > 1.5, and price already breaking above yesterday's high.

No names cleared the day-trading bar today. Every gapper is `day_eligible: false`. STLA is again the closest: gap +5.94%, price 3.655, $10.59B cap, RVOL 34.7, but it sits under its prior-day high of 3.69. RKT (+7.34%) and NU (+4.21%) are also under their prior-day highs (15.28 vs 15.39, 12.365 vs 12.53) and have null market caps. And with intraday levels null across the board, there's no premarket high, HOD or VWAP to build a plan from even if something had cleared.

## Swing Watchlist

The bar is: gap >= 8%, price > $3, open above yesterday's high, open above the 200-day SMA, market cap >= $800M, and a real catalyst (earnings on the gap day, or news with no earnings).

No names made the swing list today. Every gapper is `swing_eligible: false`. The only up-gappers over 8% are WLDSW, FCUV and RIBBU, all sub-$800M caps with junk volume. See Skips and Traps.

## Market Trends of the Day

The story this week is the AI unwind and whether it's done. Today's headlines split right down the middle.

The bear side: "Nvidia's stock has tumbled 27% over one chaotic month. The next big test lies in the week ahead," with Jensen Huang facing "tough questions from Congress this week." Bloomberg: "Watch Nvidia, AI Fears Jolt Markets." Strategist Darius Dale is "100% in cash" and says buying the Nasdaq dip is "like catching a falling knife," citing "an overheating economy, too-hot inflation and upward pressure on interest rates." CNBC confirms "The S&P 500 is in a correction."

The bull side: "The AI stock crash is mostly over, JPMorgan says," though the same piece warns "a worse phase could be coming in 2027." MarketWatch notes "Analysts raised their profit forecasts for S&P 500 companies during the selloff," framed as "Stocks look like a Black Friday bargain. Read the fine print."

Tech labor is still getting cut: "SAP reportedly to cut 10,000 jobs," between 9% and 10% of its workforce, "to transition to the artificial-intelligence era."

Overseas, China is propping things up. Reuters: "China cabinet calls for greater role by 'national team' investors to steady sinking markets." Meituan posted an "Earnings Beat as Price War Cools" (WSJ). South African retailer SPAR "flags up to 50% drop in annual earnings" (Reuters).

In the gapper list, memory is still the weak spot. MU -4.71% (RVOL 58.24) has "BNP Paribas Downgrades Micron Technology to Neutral" in its headlines next to "HBM Capacity Largely Booked for Upcoming Year." SNDK -5.58% (RVOL 142.86) carries "SanDisk Shares Decline Amid Weak NAND Flash Price Outlook." AMBA -19.77% after earnings, with BofA cutting its target to $30 from $70 and Morgan Stanley to $70 from $96 (both per the packet's links).

## Technical Signals for Today

ETF proxy levels from the scan vs each one's `prev_close`. These are Wednesday's session, unchanged from yesterday's packet, not this morning's futures:

- SPY 716.74 (prev 718.91), -0.3%
- DIA 501.29 (prev 499.78), +0.3%
- QQQ 633.92 (prev 638.12), -0.66%
- IWM 268.84 (prev 267.2), +0.61%

Tech lagged into the holiday while small caps and the Dow held green. VIX, 10Y, 3M, WTI and DXY are all null, so there's no volatility, rate, oil or dollar read.

Cap-qualified names vs prior-day high and the 200-day SMA (no VWAP or HOD, intraday data was unavailable):

- MU 600.4: under its prior-day high of 604.78 and the 200-day SMA of 776.38.
- SNDK 73.56: just under its prior-day high of 73.77. The 200-day SMA of 1275.57 doesn't fit the price. Bad data, ignore it.
- STLA 3.655: just under its prior-day high of 3.69, well under the 200-day SMA of 6.08.
- AMBA 35.68: under its prior-day high of 36.54, about half the 200-day SMA of 66.69.
- PHAR 10.05: under its prior-day high of 10.89 and the 200-day SMA of 13.34.

Not one cap-qualified name is above its 200-day SMA.

On volume: daily bars are Alpaca IEX, a subset of the tape, and the RVOL figures look like a full Wednesday session against a 20-day average. Don't read those multiples literally.

## Economic Data, Rates and the Fed

From `econ_calendar` (USD, high impact only):

- **Today (Friday, November 27):** nothing high-impact listed.
- **Tomorrow (Saturday, November 28):** nothing high-impact listed.

The calendar's `note` field is empty, so no fetch problem flagged. With no 10Y or 3M reading there's no rates read from the packet. The only Fed-adjacent items are Dale's worry about "upward pressure on interest rates" and a BNP Paribas Asset Management piece titled "Has central bank communication become counterproductive?"

## Coming Up

- **Tomorrow's events:** nothing on the USD high-impact calendar, and tomorrow is Saturday. Next week's flagged event in the packet is Jensen Huang facing "tough questions from Congress this week" (MarketWatch), no date given.
- **Earnings:** `next_earnings_date` is null for all 15 gappers, and the packet has no market-wide earnings calendar.

## Skips and Traps

- **The whole list, as a premise:** these are Wednesday's moves replayed, not today's gaps. Nothing here tells you what's gapping this morning.
- **STLA** +5.94%: closest thing to a day setup, but under its prior-day high (3.655 vs 3.69) and way under its 200-day (6.08). The headline set is mostly bad news: "Stellantis Scales Back French Plant Operations," "Stellantis Files Lawsuit Against Unifor Over Brampton Plant Access," and "Canadian Officials and Union Demand Carbon Tax Exemption to Save Stellantis Brampton Plant." The new lead, "Stellantis in Advanced Negotiations with Struggling Supplier," is not a clear positive. Up on a bad-news set. Trap.
- **RKT** +7.34%: null market cap, and the catalyst match is broken. Three of its five headlines are about Reckitt ("Reckitt Enters 10-Year Renewable Power Purchase Agreement" and others), a different company. The Rocket ones are a $6.75M regulatory fine and a Las Vegas Grand Prix sponsorship. Neither explains the move, and the fine is bad news. Skip.
- **NU** +4.21%: null market cap, under its prior-day high (12.365 vs 12.53). Lead headline is a concert residency at Nubank Parque, the rest are older items (bank recognition, Q3 results). No story for the move. Skip.
- **AMBA** -19.77%: earnings gap-down with two big target cuts. Not a long setup for either list.
- **PHAR** -23.98%: real bad news, "Pharming Temporarily Pauses RUCONEST® Manufacturing Following Media Fill Failure," with the link adding it notified the FDA of a likely supply interruption. The $7.05B SEC-derived cap next to a 20-day average volume of 182 doesn't hang together, and the lead headline is about Pharos Energy, a different company. Skip.
- **MU** and **SNDK**: gap-downs on memory weakness, both under their prior-day highs. MU has a downgrade in the mix, SNDK has a weak NAND outlook and an insider sale ("SanDisk Chief Accounting Officer Discloses Stock Sale in SEC Filing"). Skip.
- **WLDSW** +134.68% and **RIBBU** +52.5%: warrant- and unit-style tickers (W and U suffixes, and RIBBU's name is Ribbon Acquisition Corp.), no catalyst, 20-day average volume of 0 and 20. `prev_close` doesn't match `prior_close` for either (41.0 vs 23.7, 62.0 vs 39.0), so the gap math itself is shaky. Skip.
- **FCUV** +53.12%: $5.5M cap. The lead headline just says the stock moved, and the next one is "Focus Universal Inc. Announces Exercise of Warrants for Approximately $3.7 Million in Gross Proceeds." More shares. Skip.
- **EUDA** -53.67% and **PW** -32.97%: $7.9M and $1.3M caps, both with reverse splits in their headlines ("1-for-20" and "One-for-Ten"). Skip.
- **MUU**, **NVDL**, **NVD**: ticker-only rows, no name, no cap, no catalyst. The scanner's note says names like this are often ETFs, warrants or foreign issuers SEC doesn't cover. Skip.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
