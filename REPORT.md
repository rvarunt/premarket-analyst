# Premarket Report: August 24, 2026

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** All four index proxies are green this morning: S&P 500 proxy SPY +0.4%, Dow proxy DIA +0.89%, Nasdaq proxy QQQ +0.35%, Russell 2000 proxy IWM +0.76%. Dow's leading, broad mild risk-on tone.
- **The catch we're watching:** Total intraday blackout again, every one of today's 20 gappers has `intraday_data_source: unavailable`, so premarket high, VWAP, HOD and LOD are null across the board and the Day Trading Watchlist is empty outright. The Swing Watchlist is also empty, everyone comes back `swing_eligible: false`. The closest miss is NCTY, which ties its own 200-day SMA exactly (today's stand-in price $5.78 against a $5.78 SMA) instead of clearing it, and NCTY's $26.4B market cap looks like a bad SEC EDGAR fallback number for a company this size, the same kind of data-quality issue flagged in recent reports (GDXD/GDXU, STKH/SVRE). VIX, the 10-year, the 3-month, oil and the dollar all came back null too (107 failed requests even after retries this scan), and every gapper's `next_earnings_date` is null.
- **Two-brain verdict:** Single-brain run today, no second opinion to compare against.

## Pre-Market Gappers

- **RFAIU** +369.27% - "Trading Halt: Halt status updated at 7:30:00 AM ET: Quotation Resumption: News and Resumption Times" (no headline in the packet actually states the halt news; ties to the RF Acquisition Corp II / Nanyang Biologics deal, see NCTY below)
- **RFAI** +355.62% - "RF Acquisition Corp. Stock Skyrockets Following Key SEC Filings"
- **USDE** +85.25% - "12 Information Technology Stocks Moving In Friday's After-Market Session" (no ticker-specific headline in the packet)
- **MI** -58.51% - "NFT Prices $2M Registered Offering Of 437,957 Units At $4.60 Per Unit"
- **SDOT** +56.16% - "Sadot Group Shares Surge on Debt Restructuring and AI Trading Strategy"
- **AIAI** +46.14% - "AIAI Holdings's MediGuide Launches Longevity Intelligence Service, Latest Advancement In Its Expanding Precision Healthcare Platform"
- **CRMX** +45.79% - "Tradr Fires Up High-Octane 2x ETFs Targeting Rare Earths, AI, Defense" (only headline in the packet, not obviously CRMX-specific)
- **AMCI** +32.65% - "AMC Robotics Q2 EPS $(0.01), Same YoY, Sales $937.177K Down From $1.397M YoY"
- **NCTY** +32.57% - "The9 Says RF Acquisition Corp II Shareholders Approved Business Combination With Nanyang Biologics On August 19; Expects To Hold About 15% To 16% Of Combined Nasdaq-Listed Company"
- **PFSA** -27.87% - "Profusa Q2 EPS $(151.80) Up From $(9.10 thousand) YoY"
- **JUNS** +27.84% - "Jupiter Neurosciences Shares Halted On Circuit Breaker To The Downside, Stock Now Up 43.52%" (the packet also has "Jupiter Neurosciences Commences ~$2M Offering Of 307,692 Common Shares" the same day)
- **GENVR** +25.33% - "12 Information Technology Stocks Moving In Friday's Intraday Session" (no ticker-specific headline in the packet)
- **DNN** +11.8% - "Denison Mines Begins Full-Scale Construction At Its Phoenix In-Situ Recovery Uranium Project"
- **MRNA** +8.91% - "MRNA, SPCX, MSTR and More: 5 Stocks Investors Couldn't Stop Buzzing About This Week" (vague, doesn't name a specific catalyst for today's move)
- **CIFR** -8.53% - "Why Is Cipher Digital Stock Falling on Friday?" (the headline doesn't answer its own question)
- **IBIT** +6.0% - "Bitcoin's Rally Is Shifting From Short Squeeze to ETF Demand as Inflows Hit $1.6 Billion"
- **BMNR** +5.87% - "Tom Lee's BitMine Stock Surges as Ethereum DCA Strategy Finally Pays Off"
- **SOFI** +5.59% - "SoFi Stock Offers an 'Attractive Entry Point': Analyst"
- **TSLA** +5.12% - "Elon Musk's Tesla Has 'Massive Advantage' Before Selling Optimus in the Market, Says This Analyst" (a narrative piece, not a hard news catalyst for today's specific move)
- **WULF** -4.98% - "TeraWulf Stock Falls as Inflation Fears Squeeze Growth Stocks"

## Day Trading Watchlist

The "Trend Join Long" rule: gap over 3%, price over $3, market cap over $1B, premarket RVOL over 1.5, and price already breaking above yesterday's high.

No names cleared the day-trading bar today. This is a total intraday blackout, every one of today's 20 gappers has `intraday_data_source: unavailable`, so there's no premarket high, VWAP, HOD or LOD to check a breakout against, and no RVOL to confirm volume for anyone. Even setting the blackout aside, only one of the 10 cap-qualified, gap-qualified names (NCTY, GENVR, DNN, MRNA, CIFR, IBIT, BMNR, SOFI, TSLA, WULF) is currently sitting above yesterday's high using the pre-open stand-in price: NCTY at $5.78 vs. a `prior_day_high` of $5.69. Everyone else is still under yesterday's high: GENVR ($3.76 vs. $3.86), DNN ($3.505 vs. $3.54), IBIT ($43.64 vs. $44.12), BMNR ($22.815 vs. $23.34), SOFI ($18.905 vs. $19.16), TSLA ($362.78 vs. $366.5), MRNA ($145.1 vs. $159.41) and, since they're gapping down not up, CIFR ($15.765 vs. $18.21) and WULF ($15.63 vs. $17.48) are well below too.

## Swing Watchlist

The swing rule: gap of 8% or more, price over $3, open above yesterday's high, open above the 200-day SMA, market cap of $800M or more, and a real catalyst.

No names cleared the swing bar today, everyone in the packet comes back `swing_eligible: false`. The closest miss is **NCTY**: its stand-in open of $5.78 clears yesterday's high of $5.69, its gap of 32.57% clears the 8% floor, its market cap of $26.4B clears $800M easily, and it has a real, named catalyst (the RF Acquisition Corp II / Nanyang Biologics business combination). It fails on exactly one line: open above the 200-day SMA. The packet's `sma_200` for NCTY is $5.78, the same number as the stand-in open, a tie, not a clear. That's enough to keep `swing_eligible` false.

Worth flagging separately: NCTY's $26.4B market cap (`market_cap_source: sec_edgar`) looks wrong for a company this size, The9 Ltd is a small Chinese gaming name, not a $26B one. This has the same shape as the bad SEC EDGAR fallback matches called out in recent reports (GDXD/GDXU on 8/20, STKH/SVRE on 8/17), likely a shares-outstanding mismatch on the fallback calc. Since NCTY didn't clear the swing bar anyway, the CLAUDE.md market-cap override doesn't trigger here, but the number itself shouldn't be trusted, and it's also what's putting NCTY in the cap-qualified pool for the day-trading discussion above.

## Market Trends of the Day

The RF Acquisition Corp II / Nanyang Biologics deal is the standout story of the morning across three tickers. NCTY's own headline says it plainly: "The9 Says RF Acquisition Corp II Shareholders Approved Business Combination With Nanyang Biologics On August 19; Expects To Hold About 15% To 16% Of Combined Nasdaq-Listed Company," and a follow-up headline adds that Nanyang got SEC effectiveness on its Form F-4 "Ahead Of Nasdaq Listing At $1.5B Pre-Transaction Valuation." That corporate action is almost certainly what's behind RFAIU (+369.27%) and RFAI (+355.62%) too, both are RF Acquisition Corp II tickers with halt/resumption headlines in the packet but no headline that spells out the halt reason directly. Real, connected multi-ticker story, but two of the three names (RFAIU, RFAI) are far too small and halt-prone to trade off what's here.

Crypto-adjacent names are moving together on real news. IBIT (+6.0%) and BMNR (+5.87%) both have on-point headlines: "Bitcoin's Rally Is Shifting From Short Squeeze to ETF Demand as Inflows Hit $1.6 Billion" and "Tom Lee's BitMine Stock Surges as Ethereum DCA Strategy Finally Pays Off." Neither clears a watchlist bar (IBIT's 6% gap misses the 8% swing floor and both are below yesterday's high on day-trading terms), but it's a genuine sector move, not noise.

Uranium has one clean single-name story: DNN (+11.8%) has a real catalyst, "Denison Mines Begins Full-Scale Construction At Its Phoenix In-Situ Recovery Uranium Project," though the same packet also has a Q2 miss on both EPS and sales for Denison. DNN's stand-in open sits a few cents under yesterday's high ($3.505 vs. $3.54), so it doesn't clear day-trading either.

The broader tape has an AI-capex-skepticism undercurrent running into a big week. The news feed flags "Alibaba shares tumble as investors question whether AI spending splurge is justified" and "Samsung Electronics stock had its worst day in three weeks, and the other memory stocks are lower as well," both AI-adjacent hardware/capex worries, right alongside "Here are two trades to make ahead of a critical week for markets as Nvidia results and Jackson Hole loom." Nvidia earnings and the Jackson Hole Fed symposium are the two things the market is bracing for this week, per that headline, even though neither is a scheduled item in today's econ calendar.

## Technical Signals for Today

Only the four major index proxies came through this run, and all four are green: S&P 500 proxy SPY 765.64 (+0.4%), Dow proxy DIA 532.19 (+0.89%), Nasdaq proxy QQQ 713.41 (+0.35%), Russell 2000 proxy IWM 299.94 (+0.76%). Dow leading and Russell outpacing the Nasdaq is a mild broadening-out signal, not just a tech-led pop. VIX, the 10-year yield, the 3-month yield, WTI crude and the dollar index all came back null, the same yfinance rate limit that hit gapper enrichment, so there's no vol or rates read to lean on today.

## Economic Data, Rates and the Fed

The high-impact USD calendar is empty for both today and tomorrow, `econ_calendar.today` and `econ_calendar.tomorrow` both came back as empty lists in the packet. That's not the same as nothing happening this week: the news feed independently flags Jackson Hole and Nvidia earnings as the week's focal points, but neither is a scheduled high-impact USD release, so nothing to trade around from the calendar itself today or tomorrow.

## Coming Up

- **Tomorrow's events:** None on the high-impact USD calendar for August 25.
- **Earnings:** No gapper-level next earnings dates to report, every one of today's 20 gappers came back with `next_earnings_date: null` in the packet.

## Skips and Traps

**RFAIU** (+369.27%) and **RFAI** (+355.62%): both RF Acquisition Corp II tickers caught up in the Nanyang Biologics business combination story (see NCTY above and Market Trends), but market caps of $181.8M and $203.7M are both well under either watchlist floor, and the packet's own headlines are trading-halt status notices, not an explanation of the news itself. Halt-prone, illiquid, skip regardless of the gap size.

**USDE** (+85.25%): zero ticker-specific catalyst headlines in the packet, only generic sector-mover-list mentions, and market cap is unavailable (`sec_unavailable_no_concept`). Thin story, not tradeable off what's here.

**MI** (-58.51%): down hard on "NFT Prices $2M Registered Offering Of 437,957 Units At $4.60 Per Unit," a real dilutive offering. A down move that's actually explained, not a bad-news-pop trap since it isn't gapping up, just doesn't clear either bar (market cap $43M).

**SDOT** (+56.16%): real catalyst, "Sadot Group Shares Surge on Debt Restructuring and AI Trading Strategy," but market cap is $17.4M, far under any floor. The packet's own earnings headline quotes a "$71.53" EPS figure that looks like a data artifact (likely a reverse-split adjustment), not a number to lean on.

**AIAI** (+46.14%): real ticker-specific catalyst, "AIAI Holdings's MediGuide Launches Longevity Intelligence Service," but market cap is $467.8M, under both the day ($1B) and swing ($800M) floors.

**CRMX** (+45.79%): market cap unavailable (`sec_unavailable_no_cik`), only one headline in the packet and it isn't clearly CRMX-specific. Skip on thin data.

**AMCI** (+32.65%): market cap is $146.9M, way under threshold. Real story attached, a Q2 miss on both lines ("Sales $937.177K Down From $1.397M YoY") plus "Two Undisclosed Investors Agreed To Exercise Certain Warrants For $1M" the same day, a small, dilutive combination, not a name to chase.

**PFSA** (-27.87%): real earnings miss, "Q2 EPS $(151.80) Up From $(9.10 thousand) YoY," but market cap is $3.3M, nowhere near either floor.

**JUNS** (+27.84%): market cap is $4.8M. The packet shows a circuit-breaker halt to the downside the same day the stock is up 43.52% off its own base, and separately "Jupiter Neurosciences Commences ~$2M Offering Of 307,692 Common Shares." A dilutive offering landing the same day as a volatile halt-and-pop is a trap pattern, not a name to chase even before the market cap rules it out.

**GENVR** (+25.33%): market cap of $2.25B actually clears both watchlist floors, but there's no ticker-specific catalyst headline in the packet at all, only generic "stocks moving" sector-list mentions, and the stand-in open sits a dime under yesterday's high ($3.76 vs. $3.86). No story to trade and it misses the trend check anyway.

**CIFR** (-8.53%): down move whose own headline, "Why Is Cipher Digital Stock Falling on Friday?", doesn't answer its own question. Down not up, so not a bad-news-pop trap, just no watchlist bar cleared.

**MRNA** (+8.91%), **SOFI** (+5.59%), **TSLA** (+5.12%): all three have vague or narrative-style headlines rather than a hard, dated catalyst for today's specific move ("Stocks Investors Couldn't Stop Buzzing About," an analyst "attractive entry point" call, and a Musk/Optimus narrative piece respectively). MRNA's gap clears the 8% swing floor but its stand-in open is $14.31 under yesterday's high. None clear either bar.

**WULF** (-4.98%): a real, explained down move, "TeraWulf Stock Falls as Inflation Fears Squeeze Growth Stocks," just doesn't clear either bar and isn't gapping up, so not a trap.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
