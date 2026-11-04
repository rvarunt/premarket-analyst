# Premarket Report: 2026-11-04

*Single-brain run. Claude only.*

> Rules pick the watchlist. The AI judges the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** Risk-on lean in the ETF proxies: SPY +0.31%, QQQ +0.6%, IWM +0.23%, DIA -0.44% (last vs prior close, ETF stand-ins for the indices). VIX, 10Y, 3M, oil and DXY came back null (Yahoo failed). Headline: "Stocks, Bonds Rally After US Vote as Dollar Falls: Markets Wrap - Bloomberg.com".
- **The catch we're watching:** Midterm fallout for AI and data centres. Reuters: "Morning Bid: Markets fret blue wave will drown data centres". MarketWatch: "The AI trade has been 'sold to death' but Goldman strategist highlights silver lining from Democratic sweep".
- **Two-brain verdict:** Single-brain run, no second opinion.
- **Bottom line:** No name is eligible for either watchlist today. Both lists are empty.

## Pre-Market Gappers

20 gappers in the packet. Intraday levels (VWAP, HOD, LOD, premarket high) are unavailable for all of them, and no open has printed yet. Headline shown is the first catalyst headline in the packet for each name.

- **RDAC** +121.6% "Rising Dragon Acquisition Corp. Mutually Terminates Merger Agreement with HZJL Cayman Limited"
- **RDACU** +89.5% "Trading Halt: Halt status updated at 12:15:00 PM ET: Quotation Resumption: IPO Security - Released for Quotation"
- **AEHG** +52.8% "Aehr Test Systems Gets New 2X Leveraged ETF Amid AI Semiconductor Rally"
- **RIOX** +37.1% "Textbook Lesson: This Leveraged ETF Plunged 73% Since Inception – A Warning For Crypto Investors?"
- **SUPN** -32.9% "Cantor Fitzgerald Maintains Overweight on Supernus, Raises Price Target to $87" (packet also lists "Supernus Pharmaceuticals Reports Third Quarter 2026 Financial Results", "Supernus Secures $650 Million Senior Secured Term Loan", "Supernus Pharmaceuticals Completes Merger with Indivior Pharmaceuticals")
- **RZAI** -32.8% "12 Information Technology Stocks Moving In Tuesday's Intraday Session" (also: "Roze AI and BKB Energy Sign MOA to Evaluate AI Fire Forecasting System for AI Data Centers")
- **FNG** +32.0% "A FANG ETF That Doesn't Hold Many of Those Stocks Scoops Up Beyond Meat Shares"
- **HUTG** +31.0% "Rare Earths, Energy And Crypto: Themes ETFs Expands Leveraged Lineup With Six New Funds"
- **CORZW** +30.6% "Trading Halt: Halted at 4:00:00 a.m. ET - Quotation Resumption: New Issue Available"
- **VCIG** -30.3% "US Stocks Mixed; Apple Shares Slide After Q4 Results" (also: "VCI Global Announces 1-for-18 Reverse Stock Split, Effective November 2, 2026")
- **GLX** +30.2% "Corgi's ETF Pack Grows Yet Again with 24 New Leveraged and Buffer Launches"
- **WULX** +29.8% No catalyst headline in the packet
- **STVN** -28.6% "Nasdaq Surges 1%; Pfizer Posts Upbeat Q3 Earnings" (also: "Stevanato Group Reports Q3 2026 Financial Results")
- **AEHR** +26.5% "Nasdaq Jumps Over 200 Points as Chip Stocks Gain: Fear & Greed Index Remains in 'Extreme Fear' Zone" (also: "Lake Street Maintains Buy on Aehr Test System, Lowers Price Target to $90", "Jefferies Maintains Buy on Aehr Test System, Lowers Price Target to $140")
- **CIFR** +18.6% "JP Morgan Maintains Overweight on Cipher Digital, Lowers Price Target to $18"
- **RIOT** +18.5% "RIOT, COIN, MSTR Jump up to 16%: What Is Going On With Crypto Stocks?" (also: "Riot Platforms Stock Flies Ahead of Earnings: What's Going On?")
- **WULF** +14.7% "Keefe Bruyette Adjusts Price Targets for Bitcoin Miners in Sector-Wide Reset"
- **IREN** +11.1% "Jim Cramer Sees These 'Non-Magnificent' Tech Stocks Emerging as Market Leaders While Nvidia, Microsoft Struggle: 'It's Just Not The Tech That's Led Us'"
- **ORCL** +6.0% "Jim Cramer Sees These 'Non-Magnificent' Tech Stocks Emerging as Market Leaders While Nvidia, Microsoft Struggle: 'It's Just Not The Tech That's Led Us'" (also: "'Oracle Cancels $7bn Tencent AI Deal Under Trump Pressure' - FT")
- **STLA** -5.5% "Stellantis Appoints Sandeep Bhambra as Director of Design for Citroën and DS Automobiles"

## Day Trading Watchlist

Rule (Trend Join Long): gap > 3%, price > $3, market cap > $1B, premarket RVOL > 1.5, and price already breaking above yesterday's high.

No names cleared the day-trading bar today. `day_eligible` is false for all 20. Note that intraday levels were unavailable and premarket RVOL is null for the micro-cap pool, so the rules engine had little to work with. I'm not overriding the flags.

## Swing Watchlist

Rule: gap >= 8%, price > $3, open > yesterday's high, open > the 200-day SMA, market cap >= $800M, and a real catalyst.

No names cleared the swing bar today. `swing_eligible` is false for all 20. No open has printed yet, so the scanner used the current gap price as a stand-in. Every one of the big-cap upside gappers (AEHR, CIFR, RIOT, WULF, IREN, ORCL) is trading below its 200-day SMA in the packet, which is the reason they fail.

## Market Trends of the Day

- **Bitcoin miners and AI hosting bounce.** CIFR, RIOT, WULF and IREN are all up 11% to 19% on huge volume (RVOL 16.7 to 35.8 per the packet). Headline: "RIOT, COIN, MSTR Jump up to 16%: What Is Going On With Crypto Stocks?" Analyst price target cuts are all over the group: Keefe Bruyette "Trims Price Targets for Bitcoin Miners Including Riot Platforms", JP Morgan, Wells Fargo and Needham all "Lower Price Target" on Cipher. So this is a bounce into target cuts, not a re-rating.
- **Chips.** "Nasdaq Jumps Over 200 Points as Chip Stocks Gain: Fear & Greed Index Remains in 'Extreme Fear' Zone". AEHR is +26.5%.
- **AI trade tone.** MarketWatch says it "has been 'sold to death'". Also "Here's why AMD's stock is rising" and "Super Micro's stock pops as earnings show booming demand for AI servers".
- **Politics.** "Democrats win the House and Senate. Here's what it means for your finances." Asia had "Midterm Whiplash as Selloff Gives Way to Relief Rally" per WSJ.
- **Earnings reactions:** Novo Nordisk lifted guidance on its Wegovy pill. Apple fell on gross margin outlook. Shopify "missed revenue expectations".

## Technical Signals for Today

- ETF proxies, last vs prior close: SPY 754.38 vs 752.04 (+0.31%), QQQ 685.32 vs 681.22 (+0.6%), IWM 279.83 vs 279.2 (+0.23%), DIA 517.02 vs 519.29 (-0.44%). These are ETF prices, not index levels.
- VIX: null. Breadth: not in the packet.
- Sentiment: "Fear & Greed Index Remains in 'Extreme Fear' Zone" per Benzinga.

## Economic Data, Rates and the Fed

No high-impact USD releases in the packet for today (2026-11-04). 10Y and 3M yields are null, so I can't comment on rates.

## Coming Up

- **Tomorrow's events (2026-11-05):** No high-impact USD events in the packet.
- **Earnings:** `next_earnings_date` is null for every gapper. Headlines say "Riot Platforms Stock Flies Ahead of Earnings" and Google News carries "Uber Q3 earnings preview", but the packet gives no date or timing, so I'm not stating one.

## Skips and Traps

- **Micro-cap and SPAC spikes: RDAC, RDACU, CORZW.** RDAC (+121.6%, market cap $38.8M) and RDACU (+89.5%, $37.1M) are tiny Rising Dragon acquisition-corp lines. RDAC's headline is a terminated merger, not a catalyst to chase. RDACU's headlines are an old IPO and halt notice from 2024. CORZW is a warrant line (market cap $2.41B in the packet) whose only headline is a 2024 halt notice. All skips.
- **Leveraged ETF names with stale or off-topic news: AEHG, RIOX, FNG, HUTG, GLX.** Market cap is null for all of them and the "catalysts" are ETF launch stories, some dated 2025. Not real catalysts.
- **WULX:** `catalyst_found: false`. No catalyst, skip.
- **Gap downs: SUPN -32.9%, STVN -28.6%, RZAI -32.8%, VCIG -30.3%.** Long-only rules, nothing to buy. SUPN (market cap $1.64B) has an overweight and an $87 target from Cantor against a $28.15 price, and the packet shows a merger with Indivior and a $650M term loan, so I'm not reading more into it. STVN reported Q3 and says it "continues to expect revenue in the range of €1.260 billion to €1.280 billion". VCIG did a 1-for-18 reverse split effective Nov 2.
- **The big-cap upside names (AEHR, CIFR, RIOT, WULF, IREN).** All trade below the 200-day SMA and the move leans on analyst target cuts or sympathy. Chasing is a trap until levels print. AEHR's analyst headlines are both target cuts ($90 and $140).
- **ORCL +6.0%:** "'Oracle Cancels $7bn Tencent AI Deal Under Trump Pressure' - FT" is a bad-news headline sitting on a gap up. Price is below the 200-day SMA ($126.22 vs $156.29). Treat the pop as suspect.
- **STLA -5.5%:** headline is a design director appointment. No real story.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
