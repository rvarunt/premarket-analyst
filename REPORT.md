# Premarket Report: September 25, 2026

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** Index proxies are basically dead flat: S&P 500 (SPY proxy) -0.08%, Nasdaq (QQQ proxy) -0.01%, Russell 2000 (IWM proxy) -0.12%, Dow (DIA proxy) -0.34%. No risk-on or risk-off lean here, this is a quiet morning by any of the four.
- **The catch we're watching:** Same data problem as the last few sessions. The packet's `gap_pct` field is computed off a stale `prev_close`, not last session's real close. Comparing `price` against the packet's own `prior_close` field instead, 19 of today's 20 gappers show a real move under 3.4%, nowhere close to a gap. Only IPEXU is genuinely moving (-48.6% versus `prior_close`), and it has zero catalyst headlines in the packet. That's the real reason both watchlists came back empty, most of today's list isn't actually gapping at all.
- **Two-brain verdict:** Single brain, no second opinion to compare.

## Pre-Market Gappers

- **APUS** +114.9%: "Apimeds Pharmaceuticals Stock Skyrockets Thursday: What's Happening?"
- **SRZN** +108.4%: "Surrozen Gains Momentum as FDA Submission Opens Path for Lead Therapy"
- **GLND** +83.9%: "Greenland Energy Enters Farm-Out Agreement With 80 Mile And March GL On The Jameson Land Basin, With The Company Assuming March GL's Rights And Obligations"
- **PFSA** +47.8%: "Profusa Says It Received Positive Quality System Certification Decision From EU Certifier GMED; Lumee CE Mark Still Pending"
- **YDES** +47.7%: "YD Bio Publishes Review Article Titled Beyond Bone Health: Exploring The 'Heart-Brain-Bone' Axis Modulated By Lipid-Soluble Nutrients"
- **TRT** -36.6%: "CORRECTION: Trio-Tech Intl Q4 EPS $(0.02) Down From $0.02 YoY, Sales $14.931M Up From $10.671M YoY"
- **SPHL** +35.7%: "12 Consumer Discretionary Stocks Moving In Thursday's Intraday Session"
- **GRML** +33.1%: "Greenland Mines Fully Funds 2027 Milestones With $42M Raise At $12.00 Per Share, Wraps Sarfartoq NdPr Field Program"
- **AVX** +32.9%: "AVAX One Technology Authorizes $40M Buyback"
- **IPEXU** -32.0%: no catalyst headline in the packet
- **WHLR** -31.3%: "Wheeler Real Estate Investment Trust Announces 1-For-9 Reverse Stock Split Effective September 21, 2026"
- **SVRN** +29.7%: "12 Industrials Stocks Moving In Thursday's After-Market Session"
- **ARTL** -29.3%: "12 Health Care Stocks Moving In Thursday's Intraday Session"
- **VBIO** +27.5%: "Valion Bio Appoints Dean Zikria Interim CEO, Thomas Jensen As Board Chair"
- **ZSQR** +25.3%: "Z Squared Announces Closing Of All-Stock Acquisition Of Paradox Data From Paradox Infrastructure, Adding El Dorado, Arkansas Union County Campus With About 8.0 MW Energized Service; No Cash Paid, No Debt Incurred"
- **ALP** +23.6%: "Alpha Compute Executes Definitive Real Estate And Operating Oil and Gas Asset Purchase Agreements in Pennsylvania"
- **IPDN** -23.1%: "12 Industrials Stocks Moving In Thursday's After-Market Session"
- **JAGX** -20.8%: "Jaguar Health Files Supplement To Offer Up To ~$9.82M Of Common Stock Under At-The-Market Offering Program"
- **EOSE** -9.2%: "Eos Energy Announces Receipt Of $87M First Advance Under Second Tranche Of DOE Loan Agreement, Bringing Total Drawn To About $178M Since 2024"
- **IONQ** +5.7%: "IonQ Removes Major Quantum Barrier, Driving Investor Debate Over Commercial Timelines"

## Day Trading Watchlist

No names cleared the day-trading bar today. That flag encodes gap over 3%, price over $3, market cap over $1B, premarket RVOL over 1.5, and price already breaking above yesterday's high.

IONQ is the closest thing to a candidate on paper: market cap $17.1B clears the floor easily, and it's one of the only tickers today where premarket RVOL actually came through (67.46, well above the 1.5 bar) instead of null. But its real move versus `prior_close` is flat at 0.0%, and its current price ($44.99) sits just under its prior day high ($45.65). There's no actual gap to trade here, just above-average volume in a stock sitting at yesterday's close.

This scan ran premarket (7:23am ET), before the real open prints.

## Swing Watchlist

No names cleared the swing bar either. That flag encodes gap of 8% or more, price over $3, open above yesterday's high, open above the 200-day SMA, market cap of $800M or more, and a real catalyst.

GRML looks closest on the surface: market cap $2.37B clears the $800M floor and it has a genuine catalyst (a $42M raise at $12/share funding 2027 rare-earth milestones). But its real move versus `prior_close` is flat (0.0%), and its price ($14.89) sits below yesterday's high ($15.96), so it fails that leg outright. It's not a near miss so much as a name that isn't actually gapping today. Worth flagging separately: GRML's `sma_200` field reads $0.97 against a $14.89 stock, that gap is wide enough to look like a stale or bad data point rather than a real 200-day average, so don't lean on it either way. No other name comes within reach of a real 8% move today.

## Market Trends of the Day

Nothing distinctive at the index level, all four proxies are within a third of a point of flat. The real color today is in the news feed rather than the tape. Rates anxiety is still the background hum: "Why the alternative to the 'clear and present' danger from bond yields is this AI-fueled market that's quietly outperformed" and "'We were wrong.' Why Morgan Stanley changed its tune on the U.S. dollar" both point at rising yields and Fed-hike expectations reshaping positioning. Against that, there's a real AI-infrastructure thread running through both the news feed and today's gapper list: Akamai's stock is surging on a reported $12 billion cloud deal with Anthropic, and separately ZSQR (an all-stock data center acquisition) and ALP (a natural-gas-powered data center campus deal in Pennsylvania) are both leaning on the same buildout theme, alongside IONQ's quantum-computing headlines. On the earnings side, Costco beat expectations but the stock is reportedly down anyway, a "beat but sell it" reaction worth watching for a read on how forgiving this tape is toward good numbers.

## Technical Signals for Today

Index proxies via Alpaca ETF data: S&P 500 (SPY) -0.08%, Dow (DIA) -0.34%, Nasdaq (QQQ) -0.01%, Russell 2000 (IWM) -0.12%. All four are essentially flat, no breadth divergence between large caps and small caps today.

VIX, the 10-year yield, the 3-month yield, WTI crude, and the dollar index all came back null, yfinance rate limited every one of them even after retries. No direct read on volatility, rates, or the dollar this morning from the snapshot data itself.

## Economic Data, Rates and the Fed

The econ calendar came back empty for both today and tomorrow, and the packet's own note field is blank this time (no error message logged), so this looks like a legitimately quiet high-impact-USD calendar today rather than a failed fetch. No scheduled catalysts from the calendar to trade around this morning.

## Coming Up

- **Tomorrow's events:** None in the econ calendar (empty, no note given by the packet).
- **Earnings:** No gapper's `next_earnings_date` came back populated, every one is null (the packet's own gaps-to-fill note flags earnings coverage as partial). Separately, the market news feed mentions Micron reporting "next week" and ICF Announcing timing for its Q3 release, neither is a gapper on today's list, just loose color from the news feed, not the earnings calendar.

## Skips and Traps

**Most of today's headline gap sizes are stale, not real, same issue as recent sessions.** Every gapper carries two different "yesterday" reference prices: `prev_close` (used to compute the `gap_pct` shown on the gapper list above) and `prior_close` (from the daily bars feed, the same source behind `prior_day_high`). For 19 of 20 names, the two disagree badly. APUS shows `gap_pct` +114.9% but is actually down 3.34% versus `prior_close`. SRZN (+108.4% vs -0.27% real), GLND (+83.9% vs +0.38%), PFSA (+47.8% vs +2.36%), YDES (+47.7% vs +0.63%), TRT (-36.6% vs +0.14%), SPHL (+35.7% vs -0.95%), GRML (+33.1% vs 0.0%), AVX (+32.9% vs -0.18%), WHLR (-31.3% vs -0.27%), SVRN (+29.7% vs -1.22%), ARTL (-29.3% vs +1.97%), VBIO (+27.5% vs -1.14%), ZSQR (+25.3% vs -0.54%), ALP (+23.6% vs -0.18%), IPDN (-23.1% vs +0.24%), JAGX (-20.8% vs +2.17%), EOSE (-9.2% vs -0.15%), and IONQ (+5.7% vs 0.0%) all show the same shape, real move near flat, headline percentage nowhere close. Treat the `gap_pct` column with real skepticism today, and lean on `prior_close` for anything you actually check.

**IPEXU has no catalyst and no market cap, skip outright.** `catalyst_found` is false, there isn't a single headline in the packet for it. It's also the one name with a real move today (-48.6% versus `prior_close`), `avg_volume_20d` of 0, and `market_cap_source: sec_unavailable_no_concept`. The U-suffix ticker and complete lack of trading history data point at a SPAC-unit-style structure, not an operating company with a story behind it. No catalyst means no trade, per the ground rules, regardless of how big the real move is.

**JAGX's real news is dilution, not a headline number.** Its catalyst headlines show a fresh share issuance to retire ~$5.05M of a promissory note and a new ATM supplement to offer up to ~$9.82M more common stock. That's a dilution overhang independent of whatever the packet's -20.8% `gap_pct` implies (JAGX's real move versus `prior_close` is actually +2.17%, essentially flat). Either way, this is a name being diluted right now, not a dip to buy.

**TRT's own headline is a mixed earnings print, not a clean beat or miss.** The corrected release shows Q4 EPS of $(0.02), down from $0.02 a year ago, even as sales grew to $14.931M from $10.671M. Real move versus `prior_close` is flat (+0.14%), so nothing has actually reacted to this yet either way.

**WHLR's only ticker-specific headline is four days old.** The 1-for-9 reverse split it references was effective September 21, this isn't fresh news explaining today's list entry, it's a stale corporate-action headline resurfacing in the scanner's catalyst match.

**SPHL, SVRN, ARTL, and IPDN have no ticker-specific catalyst at all.** Every headline the packet has for each of these four is a generic sector "stocks moving" roundup, none of them mention the company by name or explain what's actually happening there. `catalyst_found` reads true because a headline exists, not because there's a real story. Skip these on catalyst quality alone.

**AVX, VBIO, and YDES are running on stale company news.** AVX's headlines (a $40M buyback authorization, a CFO departure, an August earnings transcript) predate today by weeks. VBIO's newest headline is a CEO/board appointment from earlier in September, alongside a NASDAQ compliance note and a reverse split effective back on Aug. 31. YD Bio's only ticker-specific headline is a review-article publication from late August. None of these explain a move specifically dated to today.

**ALP is a mixed bag, not a clean story either way.** It's carrying a real growth pitch (a $55M natural-gas-powered data center campus deal in Pennsylvania, seller financing the remaining $47M via a note) alongside a same-week Nasdaq minimum bid price compliance extension and a trading halt with news pending. Growth story and financial-distress signal both showing up in the same ticker's headline list, size any interest here accordingly.

**APUS and PFSA are both sub-$10M market caps with extreme reported RVOL.** APUS shows a $7.4M market cap with `rvol` of 5,201.9x, PFSA shows $1.8M with `rvol` of 4,801.2x. Even with real moves close to flat today, numbers like that at this size usually mean either genuinely illiquid trading or a data quality issue, size down or skip entirely.

**Wide data blackout again this run.** The per-ticker enrichment log shows yfinance returning "Too Many Requests" on nearly every ticker's intraday, news, and earnings pull, and the packet's own gaps-to-fill note counts 89 failed requests even after retries. That's why VWAP, high/low of day, and premarket high are null for every single gapper today, and why RVOL only came through for five names (APUS, GLND, PFSA, EOSE, IONQ). VIX, the 10-year, the 3-month, oil, and the dollar are all null for the same reason. Market cap is unavailable even after the SEC EDGAR fallback for IPEXU specifically.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
