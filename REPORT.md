# Premarket Report: August 21, 2026

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** All four index proxies are red this morning: S&P 500 proxy SPY -0.84%, Dow proxy DIA -1.26%, Nasdaq proxy QQQ -0.71%, Russell 2000 proxy IWM -1.34%. Small caps are leading the tape lower, this reads risk-off.
- **The catch we're watching:** Total intraday blackout again, every one of today's 20 gappers has `intraday_data_source: unavailable`, so premarket high, VWAP, HOD and LOD are null across the board. That kills the Day Trading Watchlist outright. On the swing side only AIFU clears the numeric bar, but the packet doesn't actually contain a headline that explains its 20% gap, just a CFO appointment and two trading-halt status notices with no halt reason attached. VIX, the 10-year, the 3-month, oil and the dollar all came back null too (107 failed requests even after retries this scan), and market cap is unavailable for MRNX and UXRP.
- **Two-brain verdict:** Single-brain run today, no second opinion to compare against.

## Pre-Market Gappers

- **MRNX** -47.54% - "Bulls Pile Into Moderna As FDA Decision Nears, Ignites 60% Surge In This ETF" (this headline is old and about a past surge, not today's move; MRNX is a leveraged Moderna-tracking ETF and is crashing today alongside Moderna's own real drop, see MRNA below)
- **PFSA** -44.22% - "Profusa Q2 EPS $(151.80) Up From $(9.10 thousand) YoY"
- **TNON** -38.59% - "12 Health Care Stocks Moving In Thursday's After-Market Session" (no ticker-specific headline in the packet, this is the closest sector-list mention)
- **WETO** +32.59% - "12 Industrials Stocks Moving In Thursday's Intraday Session" (no ticker-specific headline in the packet)
- **ARBB** +32.17% - "Maxim Group Downgrades ARB IOT Group to Hold" (a downgrade from June, bad news and stale, doesn't explain today's pop)
- **UXRP** +31.69% - no catalyst headline in the packet at all
- **PCLA** +31.38% - "12 Information Technology Stocks Moving In Thursday's After-Market Session" (no ticker-specific headline in the packet)
- **AAP** -24.55% - "Advance Auto Parts Rebounds After 25% Plunge as $26 Million Trump Tariff Refund Boosts Q2 Margins, SKU Catalog Expands"
- **MRNA** -23.55% - "QUICK SPARK: Moderna Stock Drops 25%, Eyes Worst Day in Company's History"
- **AIFU** +20.00% - "Trading Halt: Halt status updated at 8:55:00 AM ET: Quotation Resumption: News and Resumption Times" (the packet also has "AIFU Announces Appointment Of Shanyu Chang As CFO Effective Immediately" and a prior halt notice, but no headline actually states what the halt news was)
- **EMAT** +17.54% - "Evolution Metals & Techs Q2 EPS $(0.02) Beats $(0.03) Estimate, Sales $1.636M Miss $2.100M Estimate"
- **MARA** +15.44% - "Why Is MARA Stock Surging Friday?" (headline doesn't actually answer its own question)
- **IOVA** +11.93% - "Why Iovance Biotherapeutics Stock Hit 52-Week High"
- **HIVE** +10.85% - "HIVE Digital Stock Tests $3 Resistance: Can $350M NVIDIA Deal Drive a Breakout?"
- **ETHA** +10.59% - "Ethereum's Target Is $4,000 or $10,000, Says Trader Who Predicted The Breakout"
- **WMT** -9.23% - "WMT Stock Just Got Crushed 9% - Top Analyst Says Walmart's E-Commerce, Advertising Growth Still 'Support the Bull Case'"
- **PURR** +7.56% - "HYPE Rallies 22%, PURR Skyrockets 33% as President Trump Vows to Bring Hyperliquid to US" (the 33% in the headline doesn't match today's 7.56% gap, this headline is from an earlier move)
- **BMNR** +6.52% - "Bitmine Immersion Stock Moves Higher as Ethereum and Bitcoin Rally"
- **IBIT** +6.16% - "Bitcoin Reclaims $70K: Why Falling Treasury Yields Could Supercharge Spot BTC ETFs"
- **ONDS** -5.78% - "Ondas Adds Israeli Defense Manufacturing Muscle In $33 Million Deal" (dated M&A news, doesn't explain why the stock is down today)

## Day Trading Watchlist

The "Trend Join Long" rule: gap over 3%, price over $3, market cap over $1B, premarket RVOL over 1.5, and price already breaking above yesterday's high.

No names cleared the day-trading bar today. This is a total intraday blackout, every one of today's 20 gappers has `intraday_data_source: unavailable`, so there's no premarket high, VWAP, HOD or LOD to check a breakout against, and no RVOL to confirm volume for anyone. Even setting the blackout aside, only one of the 13 cap-qualified, gap-qualified names (AAP, MRNA, AIFU, EMAT, MARA, IOVA, HIVE, ETHA, WMT, PURR, BMNR, IBIT, ONDS) is currently sitting above yesterday's high using the pre-open stand-in price: AIFU at $15.00 vs. a `prior_day_high` of $11.48. Everyone else is still under yesterday's high by a few cents to several dollars: MARA ($11.14 vs. $11.19), HIVE ($3.115 vs. $3.18), ETHA ($17.54 vs. $17.80), PURR ($10.10 vs. $10.27), BMNR ($21.55 vs. $21.80) and IBIT ($41.17 vs. $41.33) are all close but not through, while AAP ($42.39 vs. $47.23), MRNA ($133.32 vs. $155.00), EMAT ($3.35 vs. $3.55), IOVA ($8.96 vs. $9.36), WMT ($103.84 vs. $106.96) and ONDS ($8.40 vs. $8.93) have more room to make up.

## Swing Watchlist

The swing rule: gap of 8% or more, price over $3, open above yesterday's high, open above the 200-day SMA, market cap of $800M or more, and a real catalyst.

| Ticker | Catalyst | Trend context | Idea | Second-brain check | Conviction |
|---|---|---|---|---|---|
| AIFU | Halted premarket, then resumed with no halt reason quoted anywhere in the packet | Effective open $15.00 vs. 200-day SMA $11.03 (above) and vs. yesterday's high $11.48 (above) | Watch and build a plan only, no stop or target | N/A, single-brain run | 🔴 |

**AIFU** is the only name that clears the swing bar today, and it's a technicality. The catalyst headlines in the packet are "Trading Halt: Halted at 7:50:00 p.m. ET - Trading Halt: Halt News Pending" followed the next morning by "Trading Halt: Halt status updated at 8:55:00 AM ET: Quotation Resumption: News and Resumption Times," neither of which states what the actual news was. The only other recent, named headline is "AIFU Announces Appointment Of Shanyu Chang As CFO Effective Immediately," a CFO change that wouldn't typically move a $17B name 20%. Catalyst type here is news, not earnings (`next_earnings_date` is null), but it's news we can't actually read. Trend context: the pre-open stand-in price of $15.00 sits above both the 200-day SMA ($11.03) and yesterday's high ($11.48), which is exactly what pushed `swing_eligible` to true, but remember today's real open hasn't printed yet. Market cap is $17.01B, comfortably clear of the CLAUDE.md micro-cap red-flag threshold, and no catalyst headline in the packet quotes a revenue figure, so neither automatic override trigger fires here. The red conviction is a plain confluence call: we can't confirm what's actually driving the move, we can't see premarket high or VWAP to judge where price sits right now (total intraday blackout), and the broader tape is red this morning, not backing this one up. This is a watch-and-build-a-plan name, not a trade, and per `WATCHLIST_CRITERIA.md` swing management isn't built out yet, so no stop or target attached regardless.

## Market Trends of the Day

Crypto and bitcoin/ethereum-adjacent names are the clearest group move this morning. ETHA (+10.59%), MARA (+15.44%), PURR (+7.56%), BMNR (+6.52%) and IBIT (+6.16%) are all green together, and the news backs it up directly: "Bitcoin Reclaims $70K: Why Falling Treasury Yields Could Supercharge Spot BTC ETFs," "Bitcoin Hits $74,000, Ethereum, XRP, Dogecoin Also Advance After Trump-Hosted Crypto Summit," and "Ethereum's Target Is $4,000 or $10,000, Says Trader Who Predicted The Breakout." This is a real, multi-headline sector story, not a one-off.

Biotech is split, not a uniform move. IOVA is up on real good news, "Why Iovance Biotherapeutics Stock Hit 52-Week High," with two separate price-target raises (UBS to $7, Mizuho to $11) in its headline list. MRNA is down hard the same morning on "Moderna Stock Drops 25%, Eyes Worst Day in Company's History," and MRNX, a leveraged ETF tracking Moderna, is crashing right alongside it. Same sector, opposite stories.

The broader tape has a stalled-AI-trade undercurrent. The market news feed flags "Nvidia earnings could rescue a stalling stock market, if the AI chip maker breaks this trend" right alongside "Hedge funds are doubling down on Big Tech even after summer volatility triggered a massive portfolio cleanup," a real tension between "the trade needs a catalyst" and "funds are still all-in." Separately, "The U.S. government plans to crack down on its $40 trillion debt, but brace for a 'wrenching time' ahead" is circulating as a debt-load headline this morning, though nothing ties it to a scheduled data print today.

Retail earnings reactions are cutting both ways. WMT is down 9.23% on "WMT Stock Just Got Crushed 9%," even with a bullish AI-shopping-assistant angle in the same headline ("Sparky Users Spend 40% More"). AAP is down 24.55% on weak DIY demand despite a one-time tariff-refund margin boost. Neither is a story to fade as noise, both are real earnings reactions, just not ones that clear a watchlist bar today.

## Technical Signals for Today

Only the four major index proxies came through this run, and all four are red: S&P 500 proxy SPY 762.62 (-0.84%), Dow proxy DIA 527.49 (-1.26%), Nasdaq proxy QQQ 710.93 (-0.71%), Russell 2000 proxy IWM 297.68 (-1.34%). Russell leading the drop is the standout, a real small-cap-underperformance signal, not just index noise. VIX, the 10-year yield, the 3-month yield, WTI crude and the dollar index all came back null, the same yfinance rate limit that hit gapper enrichment.

## Economic Data, Rates and the Fed

The high-impact USD calendar is empty for both today and tomorrow, `econ_calendar.today` and `econ_calendar.tomorrow` both came back as empty lists in the packet. That's not the same as nothing happening: the news feed independently flags "The U.S. government plans to crack down on its $40 trillion debt, but brace for a 'wrenching time' ahead," but that's ongoing commentary, not a scheduled release to trade around.

## Coming Up

- **Tomorrow's events:** None on the high-impact USD calendar for August 22.
- **Earnings:** No gapper-level next earnings dates to report, every one of today's 20 gappers came back with `next_earnings_date: null` in the packet.

## Skips and Traps

**UXRP** (+31.69%): `catalyst_found` is false, there are zero catalyst headlines attached in the packet. Per the rules, no catalyst means no story, skip regardless of the gap size.

**MRNX** (-47.54%): a leveraged ETF tracking Moderna, crashing today alongside Moderna's own real drop (see MRNA below). Its only catalyst headlines in the packet are stale ones about a past 60% surge, nothing about today. Market cap is unavailable (`sec_unavailable_no_cik`).

**PFSA** (-44.22%) and **TNON** (-38.59%): both down small biotech/medtech names. PFSA's headline quotes a Q2 EPS loss of $(151.80), a real earnings miss. TNON has no ticker-specific headline at all in the packet, just generic sector-mover-list mentions. Neither has a market cap over $4.7M, well under any watchlist floor regardless.

**WETO** (+32.59%) and **PCLA** (+31.38%): both up over 30% with zero ticker-specific catalyst headlines in the packet, only generic "stocks moving" sector-list mentions. Thin story, not tradeable off what's here.

**ARBB** (+32.17%): the only named headline is a June downgrade to Hold, bad news and stale, not an explanation for a 32% pop today. Market cap is $9.4M.

**AAP** (-24.55%): down on weak DIY demand despite a one-time tariff-refund margin boost, a real earnings reaction, not a trap since it's down not up. Doesn't clear either watchlist.

**MRNA** (-23.55%): "worst day in company's history" per its own headline, a real negative catalyst. Down hard, not a bad-news-pop trap since it's not gapping up, just a name sitting out both watchlists.

**EMAT** (+17.54%): even the packet's own headline asks "What's Driving the Move?" after an EPS beat paired with a sales miss, a thin, unclear story for a 17.5% pop. Fails the swing bar anyway (today's effective open is below yesterday's high).

**WMT** (-9.23%): down hard on an earnings miss despite a bullish AI-shopping-assistant narrative in the same headline. A real move, not a trap, just doesn't clear any watchlist bar.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
