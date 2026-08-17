# Premarket Report: August 17, 2026

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** Red across the majors again, small caps the lone bright spot: SPY proxy for the S&P is -0.2%, DIA/Dow is -0.2%, QQQ/Nasdaq is -0.15%, IWM/Russell 2000 is the only one green at +0.53%. Today's news feed backs it up: "U.S. stock futures little changed as investors ponder the Fed's next move."
- **The catch we're watching:** Total intraday blackout, every one of today's 20 gappers has `intraday_data_source: unavailable`, so premarket high, VWAP, HOD and LOD are null across the board and both watchlists come back empty on missing data, not weak setups. On top of that, 108 requests failed even after retries this scan (per the packet's own note), which forced every market cap in this packet through the SEC EDGAR fallback instead of yfinance, and two of those fallback numbers look badly wrong: STKH shows a $19.58B market cap on a $3.60 stock that trades an average of 29,200 shares a day, and SVRE shows $90.18B on a $3.01 stock trading 1,068 shares a day. Don't trust either figure.
- **Two-brain verdict:** Single-brain run today, no second opinion to compare against.

## Pre-Market Gappers

- **WETO** +127.7% - no ticker-specific headline in the packet, only generic "Industrials Stocks Moving" mover-list mentions
- **CAPR** +57.96% - "Capricor Therapeutics Remains Optimistic about Deramiocel FDA Approval"
- **BANL** +55.92% - "CBL International Regains Nasdaq Compliance"
- **HHS** +53.02% - "Star Equity Holdings To Acquire Harte Hanks At $5 Per Share Comprising Cash And STRRP Pref Shares At EV Of $38.4M"
- **UMAL** +50.93% - no catalyst headline in the packet
- **ETON** +44.26% - "Canaccord Genuity Maintains Buy on Eton Pharmaceuticals, Raises Price Target to $68"
- **DAAQ** +43.53% - "Digital Asset Acquisition Corp & Old Glory Terminate Business Combination Agreement As Of Aug 13, 2026; Termination Agreement Imposes No Further Liability On Parties; All Ancillary Documents Terminated"
- **SPAI** +37.72% - "Safe Pro Group Q2 EPS $(0.15) Misses $(0.12) Estimate, Sales $1.332M Beat $1.220M Estimate"
- **AEYE** +37.52% - "AudioEye FY2026 Adj EPS expected to be more than $0.98 vs $0.94 Est; Narrows FY2026 Sales Guidance from $43.250M-$44.250M to $43.500M-$44.000M vs $43.881M Est"
- **YXT** -36.81% - "YXT.com Announces $1.5M Registered Direct Offering Of 500,000 ADSs Priced At $3.00 Per ADS, Expected To Close August 17"
- **HTFL** +35.7% - "HeartFlow Shares Soar Following Strong Q2 Results and Upgraded Guidance"
- **APLM** +34.72% - "Apollomics Announces $10M Private Placement Of Up To 700,001 Class A Ordinary Shares At $15 Per Share, Including $2M Note Conversion By CEO Howard Chen"
- **EMAT** +34.07% - "Evolution Metals & Techs Q2 EPS $(0.02) Beats $(0.03) Estimate, Sales $1.636M Miss $2.100M Estimate"
- **VALN** +26.19% - "European Regulator Validates Pfizer and Valneva's Lyme Disease Vaccine Application"
- **UMAC** +25.04% - "Tariffs, Pentagon Task Force Signal Major Shift In US Drone Warfare and Industrial Policy"
- **STKH** +25% - no ticker-specific headline in the packet, only generic "stocks moving / market summary" mover-list mentions
- **SVRE** -19.73% - no ticker-specific headline in the packet, only generic "Information Technology Stocks Moving" mover-list mentions
- **CIFR** +7.43% - "Tiger Global Management Takes New Stake In Cipher Digital Inc With 927,000 Shares"
- **KEEL** +6.04% - "Keel Infrastructure Form4 Filing Shows CEO Benjamin Gagnon Purchases 58,888 Shares At An Average Price Of $3.33, Raising Direct Holdings To 1.35M Shares"
- **ACHR** -5.1% - "Why Is Archer Aviation Stock Falling on Wednesday?"

## Day Trading Watchlist

The "Trend Join Long" rule: gap over 3%, price over $3, market cap over $1B, premarket RVOL over 1.5, and price already breaking above yesterday's high.

No names cleared the day-trading bar today. This is a total intraday blackout: every one of today's 20 gappers has `intraday_data_source: unavailable`, so premarket high, VWAP, HOD and LOD are null for all of them, there's no real premarket level to check the "breaking above yesterday's high" leg against for anyone. Market cap isn't the universal blocker, ETON ($1.68B), HTFL ($3.66B), EMAT ($1.88B), VALN ($1.24B), UMAC ($1.7B), CIFR ($7.41B), KEEL ($2.17B) and ACHR ($5.09B) all clear the $1B floor. Where the packet does carry an `rvol` number at all (WETO 335.73, CAPR 312.77, CIFR 19.27, KEEL 30.22, ACHR 25.08), `premarket_volume` is null for every one of them too, so that ratio is full-day volume against the 20-day average, not the premarket-specific read this rule actually calls for. Missing data is why this list is empty, not the setups themselves.

## Swing Watchlist

The swing rule: gap of 8% or more, price over $3, open above yesterday's high, open above the 200-day SMA, market cap of $800M or more, and a real catalyst.

No names cleared the swing bar either. Every cap-qualified name with a real catalyst fails the "open above yesterday's high" leg, and it's close in every case: ETON's `today_open_effective` ($58.86) sits $0.64 under its `prior_day_high` ($59.50), HTFL ($42.08) is $0.90 under ($42.98), EMAT ($3.03) is $0.47 under ($3.50), VALN ($7.13) is $0.10 under ($7.23), and UMAC ($34.06) is $0.76 under ($34.82). Worth remembering the packet's own caveat here: before 9:30am ET the real open hasn't printed, so `today_open_effective` is standing in for the actual open and this could flip either way once the bell rings. Everything else that clears the 8% gap and catalyst bars fails on market cap instead: CAPR ($386.6M), BANL ($300.6M), HHS ($32.1M), SPAI ($125.6M), AEYE ($100.4M) and APLM ($51.4M) are all under the $800M floor, and UMAL and DAAQ don't have a market cap in the packet at all (SEC EDGAR fallback came back empty for both, no CIK for UMAL and no shares-outstanding concept filed for DAAQ).

## Market Trends of the Day

Healthcare is the biggest single cluster again: CAPR, ETON, HTFL, APLM and VALN all carry Benzinga's own "Health Care Stocks Moving" tag, five of today's twenty gappers. Story quality is mixed inside that cluster though. CAPR and VALN have real regulatory news (FDA-approval optimism, an EU regulator validating a Pfizer/Valneva vaccine application), HTFL and ETON are riding a genuine earnings beat plus stacked sell-side price-target raises, but APLM's gap is a $10M dilutive private placement, that's a story to be skeptical of, not one to chase. Tech-tagged names (AEYE, YXT, UMAC, SVRE, KEEL) split cleanly too: AEYE is up on a real earnings and guidance raise, UMAC is up on the drone-tariff policy story, KEEL is up modestly on insider buying against a same-week earnings miss, while YXT and SVRE are both down, YXT on its own dilutive offering headline, SVRE with no ticker-specific news behind the drop at all. The drone-tariff theme (SPAI, UMAC, ACHR) is the other cross-cutting thread: the White House's tariffs on drones (100% on larger/sensitive units, 25% on smaller ones) is a real policy catalyst, but it's still not one-directional days later, UMAC is up 25.04% on it while ACHR, an eVTOL air-taxi maker that's tariff-adjacent but not really a drone maker, is down 5.1% on the same headline, the same split that showed up in this packet earlier this week. Underneath both threads the broader tape is soft: only the Russell 2000 proxy is green, and today's news feed carries a dovish-leaning Fed read (Goldman: no September hike, per "Why Goldman Sachs thinks the Fed won't be hiking interest rates in September") plus a dollar-index headline citing rate-hike bets fading, even with the high-impact econ calendar empty both today and tomorrow.

## Technical Signals for Today

Index proxies (via Alpaca ETF fallback since the direct index pulls failed): SPY proxy -0.2%, DIA proxy -0.2%, QQQ proxy -0.15%, IWM proxy +0.53%. Small caps are the only green line.

Everything else needed a straight yfinance pull and every one of those calls failed today too: VIX, US 10Y, US 3M, WTI Oil and the Dollar Index all came back null (`data_source: yfinance_failed`). No breadth data is in the packet either. Same story as the intraday blackout above, this is a data-availability problem, not a "nothing's moving" read, there's no vol read, no rates read, and no dollar read to hand you this morning.

## Economic Data, Rates and the Fed

The high-impact USD calendar came back empty for both today and tomorrow under the packet's filter, nothing scheduled either day. The news feed fills in some of the color the calendar doesn't capture: "Why Goldman Sachs thinks the Fed won't be hiking interest rates in September" (Goldman expects the Fed to stand pat "barring any dramatic data"), and a separate headline notes the dollar has "slipped to lowest since early June as rate hike bets fade." A third headline frames the open itself around the Fed: "U.S. stock futures little changed as investors ponder the Fed's next move."

## Coming Up

- **Tomorrow's events:** Nothing listed. The econ calendar's "tomorrow" (August 18) came back empty under the high-impact USD filter.
- **Earnings:** `next_earnings_date` is null for every gapper in this packet, so there's nothing confirmed to report here. The news feed does flag a general retail-earnings backdrop this week ("Stock market today: Dow, S&P 500, Nasdaq futures waver ahead of retail earnings"), but no specific tickers or dates for that are in the packet.

## Skips and Traps

- **WETO**: +127.7% with no ticker-specific catalyst in the packet, only generic "Industrials Stocks Moving" roundups. Market cap ($180.8M) comes from the SEC EDGAR fallback, not yfinance, treat it as approximate. Skip.
- **CAPR**: a real catalyst (FDA-approval optimism plus an analyst upgrade), but market cap is $386.6M, well under the $800M swing floor, so it can't qualify regardless of trend.
- **BANL**: "CBL International Regains Nasdaq Compliance" is a real headline, but 20-day average volume is just 1,698 shares, and the packet's own history on this ticker includes an April headline whose URL literally reads "low-float-speculative-trading-no-clear-catalyst" for an earlier surge. Thin, speculative name.
- **HHS**: a real M&A catalyst ("Star Equity Holdings To Acquire Harte Hanks At $5 Per Share... EV Of $38.4M"), but market cap is $32.1M and 20-day average volume is 1,152 shares. Too small and thin to be a rules-qualified trade regardless of the story being genuine.
- **UMAL**: `catalyst_found: false`. No catalyst, no story, skip regardless of the 50.93% gap. Market cap is also unavailable (SEC EDGAR has no CIK for it).
- **ETON**: strong catalyst cluster (Canaccord and B. Riley both raising price targets), market cap $1.68B clears both watchlist floors, but `today_open_effective` ($58.86) sits $0.64 under `prior_day_high` ($59.50), missing the swing "open above yesterday's high" check narrowly. Worth a manual look if it clears $59.50.
- **DAAQ**: up double digits after its SPAC target (Old Glory Bank) terminated the merger agreement. Reads as a mechanical move toward trust/redemption value, not a fundamental catalyst, and market cap is unavailable (SEC EDGAR has no shares-outstanding concept on file for it). Skip as a story-driven trade.
- **SPAI**: mixed Q2 print (EPS missed, sales beat) plus generic drone-tariff sympathy headlines attached; market cap $125.6M fails the $800M swing floor and $1B day floor regardless of the setup.
- **AEYE**: a real earnings and guidance-raise catalyst, but market cap $100.4M is too small for either watchlist regardless of trend.
- **YXT**: -36.81% on its own dilutive news, a $1.5M registered direct offering priced at $3.00/ADS. Down on bad news is expected here, not a trap, just don't fade it into strength. Worth noting the packet also shows a decent H1 print for this name (EPS improved YoY, sales up YoY), it's the dilution headline driving today's move, not the fundamentals.
- **HTFL**: a genuine earnings beat plus upgraded guidance, market cap $3.66B clears both floors, but `today_open_effective` ($42.08) sits $0.90 under `prior_day_high` ($42.98), missing the swing check narrowly. Worth a manual look if it clears $42.98.
- **APLM**: +34.72% on a $10M private placement, including a $2M note conversion by the CEO. A dilutive financing announcement driving a gap up is the "up on bad news" pattern the trap rule calls out directly, treat as a trap, not a buy. Also essentially no liquidity, 20-day average volume is 78 shares.
- **EMAT**: a genuine earnings beat plus a real supply-chain catalyst (NdPr metals delivery), market cap $1.88B clears both floors, but `today_open_effective` ($3.03) sits $0.47 under `prior_day_high` ($3.50), missing the swing check.
- **VALN**: a genuine positive catalyst (EU regulator validates the Pfizer/Valneva Lyme disease vaccine application) and market cap ($1.24B) clears the swing floor, but `today_open_effective` ($7.13) is just $0.10 under `prior_day_high` ($7.23), missing swing eligibility by a hair. Worth a manual look if it clears $7.23.
- **UMAC**: a real sector-wide tariff catalyst, market cap $1.7B clears both floors, but `today_open_effective` ($34.06) sits $0.76 under `prior_day_high` ($34.82), missing the swing check.
- **STKH**: no ticker-specific headline in the packet, only generic "stocks moving" or "market summary" roundups, nothing is actually about Steakholder Foods. Also worth flagging hard: the packet reports STKH's market cap as $19.58B, which is wildly out of line with a $3.60 stock trading an average of 29,200 shares a day. That figure is the SEC EDGAR fallback (the primary yfinance source failed), cite it as-is but don't trust it, and don't trust the size of this name either way. Skip.
- **SVRE**: same pattern as STKH, only generic "Information Technology Stocks Moving" roundups behind a -19.73% move, no ticker-specific news at all. The market cap figure here is even more extreme: $90.18B on a $3.01 stock trading 1,068 shares a day on average. Clearly bad fallback data, don't trust it. Skip.
- **CIFR**: real institutional-stake news (Tiger Global) and a data-center-compliance story, but the gap is only 7.43%, below the swing floor, and this ticker came from the most-actives pool (`candidate_data_source: alpaca_most_actives`), not the gap screener. Intraday blackout means no premarket RVOL confirmation either way.
- **KEEL**: a real insider-buying story (CEO Form 4 purchase) alongside a genuine same-week earnings miss, but the gap is only 6.04%, below both watchlists' floors, and it's also a most-actives entry, not a gap-screener pick.
- **ACHR**: -5.1% on the same tariff headline driving UMAC higher, the losing side of the same policy story, an eVTOL air-taxi maker rather than a domestic drone beneficiary. Nothing actionable beyond the divergence given the gap size and the total intraday blackout.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
