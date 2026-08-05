# Premarket Report: August 5, 2026

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** Broad green tape. Alpaca ETF proxies have the S&P 500 up 1.77%, Dow up 1.74%, Russell 2000 up 1.88%, and Nasdaq leading hard at up 3.37%, with Q2 earnings season in full swing (Eli Lilly's revenue up 48% on GLP-1 demand, Disney topping Q3 estimates).
- **The catch we're watching:** The S&P just hit a fresh record high, and Michael Burry is out saying that setup could bring a 1987-style fall. On top of that, zero of today's 20 gappers cleared either watchlist bar, and six of those twenty aren't even single-stock movers, they're leveraged ETFs tracking Palantir. More on that below.
- **Two-brain verdict:** Single brain, no second opinion to compare.

## Pre-Market Gappers

- **AMIX** +434.3%: "Autonomix Stock Skyrockets After Obtaining Key Cancer Tech Patent"
- **PLTZ** -58.7%: "Defiance's New PLTZ ETF Lets You Double Down On A Drop in Palantir Stock"
- **PLTG** +58.1%: "Big Week For Palantir And Robinhood"
- **PLTL** +58.1%: no catalyst headline in the packet
- **PTIR** +58.0%: "What's Going On With Palantir Stock Friday?"
- **PLTA** +58.0%: no catalyst headline in the packet
- **PLTU** +57.9%: "Direxion's PLTU, PLTD ETFs Offer Two Paths Through The Great Palantir Debate"
- **AHCO** -38.0%: "AdaptHealth Lowers FY2026 Sales Guidance from $3.450B-$3.520B to $2.850B-$2.890B vs $3.488B Est"
- **REZI** -27.8%: "Resideo To Host Investor Day At NYSE, Ahead Of Planned Spin-Off Of ADI Global Distribution; Targets Revenue CAGR Of 4% To 5% From 2025 Through 2030"
- **AIQD** -23.2%: "As bank bonuses soar, PE's biggest firms play catch-up"
- **DFNS** -23.0%: "T3 Defense's Tiltan Software Engineering Subsidiary Receives Initial Purchase Order From Undisclosed Israeli Defense Contractor To Provide Hardware-In-The-Loop Simulation Of Infrared Electro-Optical System; Program May Expand Up To $2M Value"
- **BRKR** -21.8%: "Bruker Affirms FY2026 Adj EPS Guidance of $2.10-$2.15 vs $2.12 Est; Lowers FY2026 Sales Guidance from $3.570B-$3.600B to $3.540B-$3.570B vs $3.589B Est"
- **CTRI** -21.5%: "Centuri Holdings Raises FY2026 Sales Guidance from $3.150B-$3.450B to $3.590B-$3.790B vs $3.481B Est"
- **CIFR** -15.6%: "Cipher Mining Q2 EPS $(0.65) Misses $(0.22) Estimate, Sales $24.837M Miss $32.515M Estimate"
- **INTC** +10.9%: "How Intel's Earnings Turned AMD's Beat Into A Sell-Off"
- **SMCI** +10.7%: "Supermicro Announces Ten AI Data Center Rack Models, Says Manufacturing Scale Enables Up To 3,000 Racks Per Month Including 2,000 Liquid-Cooled"
- **CMG** -9.7%: "Chipotle Shares Hammered as Minnesota Salmonella Outbreak Triggers Jalapeño Removal"
- **NOK** +6.2%: "Nokia Stock Rallies Tuesday: What's Driving the Rebound?"
- **ONDS** +6.1%: "What's Going on With Ondas Stock Monday?"
- **OPEN** +5.2%: "Opendoor Technologies Q2 Adj. EPS $(0.03) Beats $(0.07) Estimate, Sales $883.000M Beat $666.540M Estimate"

## Day Trading Watchlist

Rule: gap over 3%, price over $3, market cap over $1B, premarket RVOL over 1.5, and price already breaking above yesterday's high. This is the Trend Join Long setup.

No names cleared the day-trading bar today. Every one of the 20 gappers in the packet came back `day_eligible: false`. Worth flagging: `premarket_high`, `hod`, `lod`, and `vwap` are null for every name, `intraday_data_source` reads `unavailable` across the board because both Alpaca and the yfinance fallback got rate limited on the intraday leg. The breakout-above-yesterday's-high leg of this rule can't be confirmed without that data, so today's empty list is partly a real "nothing qualified" and partly "the data needed to check couldn't be pulled." Not overriding the flags either way, just flagging why the list looks the way it does.

## Swing Watchlist

Rule: gap of 8% or more, price over $3, open above yesterday's high, open above the 200-day SMA, market cap of $800M or more, and a real catalyst. Entry and exit management for swing names isn't built yet either way, these would be watch-and-build-a-plan names, not full trade plans.

No names cleared the swing bar today. Every gapper came back `swing_eligible: false`. `today_open` is null for all 20 (premarket, not printed yet), so the scanner is using the current gap price as its documented stand-in. A handful of names have the gap size (AMIX, the six Palantir-linked leveraged ETFs) but fail elsewhere: several sit below their 200-day SMA, some have no real catalyst, and per the ground rules below, some of these aren't real single-company catalysts at all.

## Market Trends of the Day

Two threads dominate the news feed today. First, Q2 earnings season is running hot and the reactions are all over the map: Eli Lilly's revenue jumped 48% on Mounjaro and Zepbound demand, Disney topped Q3 estimates and exited its A+E Media stake, and Upstart's AI underwriting upgrades got credit for a loan-growth pickup, all reacting well. On the other side, AdaptHealth cut FY2026 sales guidance hard (from $3.45-3.52B down to $2.85-2.89B) and gapped down 38%, Bruker beat on EPS but missed on sales and trimmed its own sales guidance, and Cipher Mining missed on both lines. Zalando also trimmed its FY26 outlook despite strong Q2 revenue growth. Earnings reactions are clearly not uniform today, beats and misses are both landing hard in either direction.

Second, the AI capex and chip trade has a genuine split under the hood. A Yahoo Finance headline sums it up directly: "Dow Jones Futures Rise; SpaceX, AMD Dive As Arista, Eli Lilly Jump With S&P 500 At Highs." Intel gapped up 10.9% with the market read being that its earnings turned AMD's own beat into a sell-off for AMD, while Supermicro is up on a concrete product announcement (ten new AI data center rack models, up to 3,000 racks a month). Elon Musk separately addressed memory-chip stock concerns on the SpaceX earnings call, which MarketWatch frames as easing some AI capex sustainability worries. Yahoo also has a piece flagging healthcare stocks warming up as the tech trade shows turbulence, worth watching for a rotation story building underneath the index-level "everything's green" picture.

Sitting on top of all of it: the S&P just printed a fresh record high, and Michael Burry is publicly warning that could set up a 1987-style fall. He's not backing off his bearish tech view. That's the tension for today, a market grinding higher on earnings beats and AI enthusiasm while a well-known bear calls the top out loud.

## Technical Signals for Today

Only the index proxies are usable today. Alpaca ETF proxies have S&P 500 (SPY) at 771.11, up 1.77%; Dow (DIA) at 540.43, up 1.74%; Nasdaq (QQQ) at 723.69, up 3.37%; and Russell 2000 (IWM) at 301.71, up 1.88%. VIX, US 10-year yield, US 3-month yield, WTI crude, and the dollar index (DXY) all came back null, yfinance rate-limited every one of those requests and there's no Alpaca proxy wired in for them. No breadth or rates read to offer beyond the four index levels above.

## Economic Data, Rates and the Fed

Calendar came back clean this time, live fetch worked. Filtered to USD, high-impact only, there are zero events listed for today (August 5) and zero for tomorrow (August 6). This looks like a genuinely quiet stretch on the calendar, not a data failure, nothing to read into the rates path from today's releases.

## Coming Up

- **Tomorrow's events:** None listed. High-impact USD calendar is empty for August 6.
- **Earnings:** No dates available. `next_earnings_date` came back null for all 20 gappers in this packet.

## Skips and Traps

- **PLTZ, PLTG, PLTL, PTIR, PLTA, PLTU:** These six aren't real single-company gappers, they're leveraged and inverse single-stock ETFs (Defiance and Direxion products) that track Palantir at 2x-5x. Their moves are just leveraged PLTR price action, not an independent catalyst on the underlying company. PLTL and PLTA also came back `catalyst_found: false`, no catalyst headlines at all, so per the ground rules those two are a skip outright regardless of the gap size. The other four technically have catalyst headlines, but the headlines are just ETF-existence writeups and general Palantir chatter, not news about a specific move today. Treat the whole cluster as noise, not tradeable single-stock setups.
- **AMIX** (+434.3%): Real catalyst, a cancer-tech patent grant, but this is an extreme thin-float move. Average 20-day volume is 44,473 shares and today's volume printed at 120 million, RVOL of nearly 2,700x. A gap this explosive on a stock this thin is closer to a lottery ticket than a setup, size and liquidity risk here are severe.
- **AIQD** (-23.2%): The name attached to this ticker is "Bank of Montreal /CAN/" and its only catalyst headline, "As bank bonuses soar, PE's biggest firms play catch-up," doesn't mention AIQD or Bank of Montreal at all. This looks like a ticker/name mismatch from the SEC EDGAR fallback lookup, not a real read on what AIQD actually is or why it's down 23%. Don't trust this one, the underlying data is unreliable.
- **CTRI** (-21.5%): Centuri Holdings beat Q2 on both lines and raised FY2026 sales guidance meaningfully, yet the stock is gapping down 21.5%. That's a real beat-and-raise getting sold anyway, worth noting as a "good numbers, bad reaction" case rather than assuming the headline guidance raise explains the move.
- **DFNS** (-23.0%): This is the same T3 Defense that gapped up 122% yesterday on a short-seller report calling it "uninvestable." Today's move looks like it's giving back some of that pump rather than reacting fresh to today's purchase-order headline, which is minor (potential contract value up to $2M) relative to the size of the move.
- **NOK** (+6.2%): Catalyst headlines directly contradict each other, one says Nokia is rallying, another from the same day asks why it's falling. The packet's headline set for this one isn't coherent enough to hang a story on.
- **ONDS** (+6.1%): Catalyst headlines are all generic competitor-comparison pieces and a "what's going on with the stock" post, nothing that actually explains today's specific move. Weak story behind the gap.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
