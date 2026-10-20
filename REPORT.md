# Premarket Report: October 20, 2026

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** Tech-led bid. The packet's ETF proxies show Nasdaq (QQQ) +1.2%, S&P 500 (SPY) +0.43%, Russell 2000 (IWM) +0.31%, Dow (DIA) -0.02%. Headlines say Nasdaq futures dipped on oil and earnings, so read the proxies as a snapshot, not a settled direction.
- **The catch we're watching:** AI earnings and oil. Reuters: "Shares slide again as oil stays high; AI earnings in focus". Sentiment is still in "Extreme Fear" per Benzinga even with the Nasdaq up.
- **Two-brain verdict:** Single brain, no second opinion to compare.

## Pre-Market Gappers

Scan ran 07:11 EDT with the Alpaca screener as candidate source. 20 gappers came back. Intraday levels (VWAP, HOD, LOD, premarket high) are unavailable for all of them, and 88 requests failed after retries, so many fields are null. Most "catalysts" below are generic mover roundups, not company news.

- **SLN** +125.6% "Why Is Silence Therapeutics Stock Skyrocketing Monday?"
- **XHG** +60.0% "XChange TEC.INC Intends To Gradually Reduce Its Operations In Mainland China And Plans To Invest Between $5M And $10M In US Market"
- **IRON** +38.9% "Disc Medicine Announces Proposed $350M Public Offering Of Common Stock And Pre-Funded Warrants"
- **BKHA** -33.0% "Black Hawk Acquisition Shareholders Approve Its Proposed Business Combination With Vesicor Therapeutics"
- **IAM** -31.4% "Iambic Therapeutics shares are trading lower amid post-IPO volatility."
- **XLAB** +30.2% "What's Going On With Exascale Labs Stock Monday?"
- **LCFYW** -27.4% No headline in the packet.
- **TANH** -25.1% "Tantech Holdings Shares Fall 13% After Hours After Announcing 1-for-50 Reverse Split: What You Need To Know"
- **AMRO** +24.7% "Why 3M Shares Are Trading Higher; Here Are 20 Stocks Moving Premarket"
- **SVRN** -24.4% "Short Seller Says SVRN Stock Is 'Uninvestable'"
- **MTEX** +22.7% "Mannatech Q2 EPS $0.53 Up From $(2.27) YoY, Sales $26.650M Up From $25.679M YoY"
- **PMI** +21.2% "12 Health Care Stocks Moving In Friday's Pre-Market Session"
- **AXTU** +21.1% "These AXT ETFs Turned a 30% Stock Rally Into Nearly 50% Returns"
- **AXTX** +21.1% No headline in the packet.
- **RFAIU** +21.0% "Reported Earlier, RF Acquisition Corp II Prices $100M Initial Public Offering Of 10M Units At $10/Unit"
- **AKTX** +20.9% "Akari Therapeutics Submits PCT/US2026/45955 To Expand Its IP Portfolio"
- **AXTC** +20.9% No headline in the packet.
- **CLF** +16.2% "Barclays Maintains Underweight on Cleveland-Cliffs, Raises Price Target to $11"
- **AMZN** +5.0% "Amazon Announces Plan To Invest More Than €16B ($18B) In Germany In 2027, Spanning Data Centers, AI, Satellite Internet, Logistics And Prime Video"
- **RIG** +5.0% "Transocean Receives ~$62M Firm Contract Award Alongside Formal Approval Of Previously Announced Equinor Agreement; Converts $1B Contract Value To Firm Backlog"

## Day Trading Watchlist

No names cleared the day-trading bar today. That flag encodes gap over 3%, price over $3, market cap over $1B, premarket RVOL over 1.5, and price already breaking above yesterday's high. Every gapper came back `day_eligible: false`. Premarket high and VWAP are null across the board, so no trigger levels exist to build a plan from.

## Swing Watchlist

That flag encodes gap of 8% or more, price over $3, open above yesterday's high, open above the 200-day SMA, market cap of $800M or more, and a real catalyst. One name came back `swing_eligible: true`, and it's a weak one.

| Ticker | Catalyst | Trend context | Idea | Second-brain check | Conviction |
|---|---|---|---|---|---|
| AKTX | News, no earnings: "Akari Therapeutics Submits PCT/US2026/45955 To Expand Its IP Portfolio". Theme: a patent filing. | Gap price $9.89 is above prior day high $9.17 and above the 200-day SMA $6.45. Gap +20.9%. | Watch only. Swing management isn't built yet, so this is a "watch and build a plan" name, not a trade. | None, single brain. | 🔴 |

Why 🔴: the packet lists AKTX market cap as $1,540,451,857,081 (sec_edgar). That is about $1.54 trillion for a ~$10 biotech, which is clearly bad data, so the cap-based eligibility can't be trusted. Beyond that, a patent filing is a thin catalyst for a 20% gap. It's on the list on a technicality. The under-$2B market cap trigger can't be checked reliably, and the revenue-in-headline trigger doesn't apply (no revenue figure quoted).

## Market Trends of the Day

Tech and AI are doing the pushing. Nasdaq proxy +1.2% vs Dow flat. Benzinga: "Nasdaq Jumps Over 1% As Tech Stocks Gain" and "Nasdaq 100 Rises as AI Chip Rout Reverses, SanDisk Jumps 7%". But the AI trade is shaky. MarketWatch: "South Korean IPO flop is the latest in a string of disappointments for the global AI trade" and "Strategist Tom Lee says he's buying the AI stock dip". Oil is high and weighing on futures per Reuters. Small caps lag: "Why smaller stocks face worse prospects than the S&P 500 in the coming years". Earnings season is in motion: GM beat Q3 and narrowed full-year guidance, Synchrony and Equifax reported Q3.

## Technical Signals for Today

Index data is ETF proxies only, no levels beyond last and prior close:

- S&P 500 (SPY): 766.60 vs 763.34 prior close, +0.43%
- Nasdaq (QQQ): 718.31 vs 709.82, +1.2%
- Russell 2000 (IWM): 271.30 vs 270.47, +0.31%
- Dow (DIA): 518.98 vs 519.10, -0.02%

VIX, US 10Y, US 3M, WTI oil and DXY all failed to load (null). No breadth or chart signals in the packet.

## Economic Data, Rates and the Fed

No high-impact USD releases listed for today or tomorrow in the packet's econ calendar. Nothing on rates or the Fed from the packet either, and the 10Y and 3M yields came back null, so there's no rate read today.

## Coming Up

- **Tomorrow's events:** None listed (no high-impact USD releases for 2026-10-21).
- **Earnings:** No `next_earnings_date` for any gapper. Headlines mention a "U.S. Earnings Preview: Before Market Open Oct. 20" and AI-name earnings ahead (Jim Cramer on MSFT, GOOGL, AMZN), but the packet gives no dates or tickers beyond that.

## Skips and Traps

- **IRON** +38.9%: Up on bad news. Headline is "Disc Medicine Announces Proposed $350M Public Offering Of Common Stock And Pre-Funded Warrants". A dilutive raise. The BMO price target bump doesn't change that. Trap.
- **SLN** +125.6%: Stock is up huge, but price $19.58 sits right at prior close $19.57 and prior-day high $19.61, so the "gap" looks like stale prior-day data. RVOL 401x on a 179K average volume. Headlines are roundups ("Why Is Silence Therapeutics Stock Skyrocketing Monday?") with no stated reason. Skip.
- **XHG** +60%: Packet market cap is $82.8B for a $3 stock, which is bad data. Average volume is about 8K shares. Skip.
- **XLAB, PMI, AMRO, AXTU:** Catalysts are generic mover roundups or an ETF article. No real story. Skip.
- **AXTX, AXTC, LCFYW:** No catalyst found. Skip.
- **SVRN** -24.4%: Short-seller report ("Short Seller Says SVRN Stock Is 'Uninvestable'") plus a co-CEO resignation. Down gap on a fraud-style allegation. Not a long.
- **TANH** -25.1%: 1-for-50 reverse split news and a chairman change. Avoid.
- **BKHA, IAM, RFAIU:** SPAC and fresh-IPO names with halts and thin floats. Skip.
- **MTEX** +22.7%: Market cap $16.9M, and the headlines are months old (Q1 and Q2 results). Micro-cap, no fresh catalyst. Skip.
- **CLF** +16.2%: Market cap $8.05B, RVOL 82x, but the headline is a Barclays Underweight with a $11 target, below the $14.11 price. Not a clean story, and no intraday levels. Skip.
- **AMZN** +5.0%: Real news (Germany investment plan), but day-trade flag is false and no premarket levels exist. No setup today.
- **RIG** +5.0%: Real contract news, but fails the day-trade flag and has no levels. No setup.
- **AKTX:** See the Swing Watchlist. Watch only, and the data is suspect.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
