# Premarket Report: August 26, 2026

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** All four index proxies are green and clustered tight this morning: S&P 500 proxy SPY +0.31%, Dow proxy DIA +0.29%, Nasdaq proxy QQQ +0.61%, Russell 2000 proxy IWM +0.43%. Nasdaq's leading by a little, otherwise a broad, mild risk-on tone with no single index running away from the pack.
- **The catch we're watching:** Total intraday blackout again, all 20 of today's gappers came back `intraday_data_source: unavailable`, so premarket high, VWAP, HOD and LOD are null across the board and the Day Trading Watchlist is empty outright. The Swing Watchlist is also empty, every ticker comes back `swing_eligible: false`. The closest miss is MRNA: it clears the gap, price, market cap and 200-SMA lines but its stand-in open ($158.815) sits about $2.48 under yesterday's high ($161.29). Separately, NCTY's $19.96B market cap looks like a bad SEC EDGAR fallback number for a company this size, the same kind of data-quality issue flagged in recent reports (GDXD/GDXU, STKH/SVRE, and NCTY itself on 8/24). VIX, the 10-year, the 3-month, oil and the dollar all came back null too (93 failed requests even after retries this scan), and every gapper's `next_earnings_date` is null.
- **Two-brain verdict:** Single-brain run today, no second opinion to compare against.

## Pre-Market Gappers

- **BTA** +153.57% - "Stocks That Hit 52-Week Lows On Monday" (all five headlines the packet has for BTA are stale 2021-2022 sector listicles, none explain today's 153% move)
- **DAIC** +124.28% - "Why Cadeler Shares Are Trading Higher By 6%; Here Are 20 Stocks Moving Premarket" (none of DAIC's five headlines actually name DAIC or CID Holdco, just generic mover-list mentions)
- **PMI** +86.16% - "Why Is Picard Medical Stock Gaining Monday?" (names the company but the headline never answers its own question, no stated reason in the packet)
- **JEM** +77.88% - "707 Cayman Holdings Signs Term Sheet To Acquire Pharmaceutical Botanicals Firm Crucial Innovation ; Backed By $10.25M Committed Financing Led By GeoNova Holdings Together With Its Co-Investors"
- **FVN** -52.47% - "Future Vision II Acquisition Receives Merger Termination Notification From VIWO Technology"
- **CRMX** +42.39% - "Tradr Fires Up High-Octane 2x ETFs Targeting Rare Earths, AI, Defense" (the packet's only CRMX headline, not clearly CRMX-specific)
- **EXYN** +40% - "Exyn Technologies Says Nexys Handheld LiDAR Scanner Selected By Unnamed US Government Research Organization After Competitive Benchmark Against Rival Commercial Systems; Terms Not Disclosed"
- **PSNYW** +37.07% - "Trading Halt: Halt status updated at 9:00:00 AM ET: Quotation Resumption: News and Resumption Times" (a Polestar-linked warrant, halted then resumed, no headline in the packet spells out the underlying news)
- **LHSW** +36.1% - "Lianhe Sowell Intl FY EPS $(1.74) Down From $1.00 YoY, Sales $43.270M Up From $36.540M YoY"
- **AMIX** +33.89% - "Reported Earlier, Autonomix Medical To Issue New Series E-1 And E-2 Warrants For 535,913 Shares Each At $6.25 Per Share In Exchange For Immediate Cash Exercise Of Existing Warrants"
- **BRNX** +33.01% - "12 Industrials Stocks Moving In Tuesday's Intraday Session" (no BRENX-specific headline anywhere in the packet's five entries)
- **DKS** -30.68% - "Dick's Sporting Goods Stock Sinks To 52-Week Low - Here's Why" (tied to "US Stocks Higher; Dick's Sporting Goods Shares Tumble After Weak Q2 Results" elsewhere in the packet)
- **SHMD** -29.48% - "Schmid Group Lowers FY26 Adjusted EBITDA Margin Guidance to 6%-9%; Reaffirms Revenue Guidance Above €100M"
- **SDOT** -29.4% - "Sadot CFO Resigns for 'Personal Reasons,' Stock Falls" (also a same-day dilutive resale prospectus in the packet, see Skips and Traps)
- **NCTY** -21.54% - "The9 Says RF Acquisition Corp II Shareholders Approved Business Combination With Nanyang Biologics On August 19; Expects To Hold About 15% To 16% Of Combined Nasdaq-Listed Company"
- **MRNA** +14.4% - "Wolfe Research Upgrades Moderna to Peer Perform"
- **SMCI** +9.43% - "Cisco Expands Rack-Scale AI Computing With Nvidia, Supermicro"
- **MARA** +5.86% - "Why Is MARA Stock Surging Friday?" (headline is stale, dated Friday's session, not today's)
- **DNN** +4.8% - "Denison Mines Begins Full-Scale Construction At Its Phoenix In-Situ Recovery Uranium Project"
- **SOFI** +4.31% - "Sofi Stock Is Trending: A Key Level Just Came Into Play" (a technical framing, not a fundamental catalyst)

## Day Trading Watchlist

The "Trend Join Long" rule: gap over 3%, price over $3, market cap over $1B, premarket RVOL over 1.5, and price already breaking above yesterday's high.

No names cleared the day-trading bar today. This is a total intraday blackout, all 20 of today's gappers have `intraday_data_source: unavailable`, so there's no premarket high, VWAP, HOD or LOD to check a breakout against, and no RVOL to confirm volume for anyone. Even setting the blackout aside, none of the cap-qualified, positive-gap names (MRNA, SMCI, MARA, DNN, SOFI, all over $1B market cap and gapping up more than 3%) are sitting above yesterday's high using the pre-open stand-in price: MRNA ($158.815 vs. a `prior_day_high` of $161.29), SMCI ($38.465 vs. $38.6), MARA ($11.835 vs. $12.15), DNN ($3.71 vs. $3.83) and SOFI ($19.01 vs. $19.02, essentially a penny short). DKS would otherwise be in this cap-qualified group but its market cap came back null (`sec_unavailable_no_concept`), a clear data gap for a name this size and liquid, so it can't be confirmed cap-qualified off the packet alone, and it's gapping down anyway.

## Swing Watchlist

The swing rule: gap of 8% or more, price over $3, open above yesterday's high, open above the 200-day SMA, market cap of $800M or more, and a real catalyst.

No names cleared the swing bar today, everyone in the packet comes back `swing_eligible: false`. The closest miss is **MRNA**: its gap of 14.4% clears the 8% floor, its price ($158.815) and market cap ($63.4B) clear easily, its stand-in open sits way above its 200-day SMA ($158.815 vs. $49.98), and it has real, named catalysts (a Wolfe Research upgrade to Peer Perform plus a headline flagging "a key trading signal"). It fails on exactly one line: open above yesterday's high. The stand-in open of $158.815 is about $2.48 under the `prior_day_high` of $161.29. No other gapper with a positive 8%+ gap has a market cap anywhere close to the $800M floor (the next closest, JEM at $179M, is still off by more than 4x).

## Market Trends of the Day

The RF Acquisition Corp II tie-up with Nanyang Biologics is still working its way through the tape. NCTY's own headline spells it out: "The9 Says RF Acquisition Corp II Shareholders Approved Business Combination With Nanyang Biologics On August 19; Expects To Hold About 15% To 16% Of Combined Nasdaq-Listed Company." NCTY is gapping down 21.54% today, not up, so this looks like the news getting digested rather than chased further, and it's a leftover story from the same deal flagged in the 8/24 report.

SPAC and shell-company churn is a bigger theme than any single sector today. DAIC, PMI, JEM, FVN, CRMX, PSNYW and LHSW are all sub-$200M names (or market cap unavailable) making triple-digit or near-triple-digit percentage moves, and several of them (DAIC, PMI, BRNX) don't even have a ticker-specific headline in the packet, just generic "stocks moving" listicle mentions that happened to sweep them up. FVN's move is explained (a terminated SPAC merger), but the rest of this cluster reads as thin, illiquid churn rather than a coherent story.

AI infrastructure buildout has one clean thread: SMCI's gap ties directly to "Cisco Expands Rack-Scale AI Computing With Nvidia, Supermicro," which names Supermicro specifically, alongside a separate Nvidia liquid-cooling headline in the same packet. Crypto-adjacent names (MARA, and DNN via the uranium/nuclear angle) are also green, but MARA's own headline is stale (dated Friday) and DNN pairs its uranium-project news with a same-packet Q2 miss on both EPS and sales.

Retail earnings reactions cut both ways in the packet: DKS is down sharply on what the news feed calls "Weak Q2 Results," while MRNA is up on an analyst upgrade rather than a fundamental print. No broader single macro narrative ties the whole gapper list together today beyond "small/micro caps swinging hard, mega caps barely moving."

## Technical Signals for Today

Only the four major index proxies came through this run, and all four are green: S&P 500 proxy SPY 765.79 (+0.31%), Dow proxy DIA 535.15 (+0.29%), Nasdaq proxy QQQ 710.66 (+0.61%), Russell 2000 proxy IWM 299.25 (+0.43%). Nasdaq leading by a bit but nothing close to a tech blowout, the four are within half a point of each other. VIX, the 10-year yield, the 3-month yield, WTI crude and the dollar index all came back null, the same rate-limit issue that hit gapper enrichment, so there's no vol or rates read to lean on today.

## Economic Data, Rates and the Fed

Two high-impact USD releases today per the packet's calendar: Core PCE Price Index m/m at 8:30am ET (forecast 0.2%, previous 0.1%) and Prelim GDP q/q at 8:30am ET (forecast 1.5%, previous 1.5%). Both land right at the open, so any repricing on an inflation or growth surprise will hit before or right as the bell rings. Tomorrow's calendar is empty in the packet.

## Coming Up

- **Tomorrow's events:** None on the high-impact USD calendar for August 27.
- **Earnings:** No gapper-level next earnings dates to report, every one of today's 20 gappers came back with `next_earnings_date: null` in the packet.

## Skips and Traps

**BTA** (+153.57%): market cap unavailable (`sec_unavailable_no_cik`) and every headline in the packet is a stale 2021-2022 "52-week high/low" listicle mention. No real catalyst tied to today's 153% move, skip on thin, stale data.

**DAIC** (+124.28%): market cap is $117.4M, well under either floor, and none of its five packet headlines actually name DAIC or CID Holdco, just generic "stocks moving" sector-list mentions. No real story to trade.

**PMI** (+86.16%): market cap is $22.3M. The one company-specific headline, "Why Is Picard Medical Stock Gaining Monday?", never answers its own question. Thin data, thin story.

**JEM** (+77.88%): a real, specific catalyst (a term sheet to acquire Crucial Innovation backed by $10.25M in financing), but market cap is $179M, far under the $800M swing floor.

**FVN** (-52.47%): down hard on a real, explained catalyst, "Future Vision II Acquisition Receives Merger Termination Notification From VIWO Technology." A down move that's actually explained, not a bad-news-pop trap since it isn't gapping up, just doesn't clear either bar (market cap $71.1M).

**CRMX** (+42.39%): market cap unavailable (`sec_unavailable_no_cik`), and its one packet headline about Tradr's new leveraged ETFs isn't clearly CRMX-specific. Skip on thin data.

**EXYN** (+40%): a real catalyst, a government research org selecting its Nexys LiDAR scanner, plus a Q2 print with an EPS miss but a sales beat. Market cap is $25.6M, nowhere near either floor.

**PSNYW** (+37.07%): a Polestar-linked warrant that was halted and resumed, but no headline in the packet actually states the halt reason. Market cap is unavailable (`sec_unavailable_no_concept`). Skip on an unexplained halt-and-pop.

**LHSW** (+36.1%): real earnings headline, but EPS swung from $1.00 to $(1.74) YoY even as sales rose, a mixed print. Market cap is $196M, under both floors.

**AMIX** (+33.89%): the catalyst is a warrant exercise for cash, not a growth story, and it adds shares rather than removing overhang. Market cap is $6.98M, deep micro-cap. Not a name to chase on a warrant-exercise headline.

**BRNX** (+33.01%): market cap is $3.98M and none of its five packet headlines name BRENX specifically, just generic industrials sector-list mentions. No real story, skip.

**DKS** (-30.68%): a real, explained down move, "Dick's Sporting Goods Stock Sinks To 52-Week Low" tied to a weak Q2 print, but market cap came back null (`sec_unavailable_no_concept`) despite this being a well-known, liquid large-cap retailer, a clear data gap worth flagging on its own. Down not up, so not a bad-news-pop trap, just can't be watchlist-qualified off what's in the packet.

**SHMD** (-29.48%): down on a real, explained catalyst, a guidance cut on FY26 EBITDA margin. Not a trap since it's gapping down, just doesn't clear either bar (market cap $147.3M).

**SDOT** (-29.4%): two real, explained bad-news catalysts the same day, a CFO resignation and a dilutive resale prospectus for over 4.25M shares. Down not up, so not a bad-news-pop trap, just doesn't clear either bar (market cap $21.6M).

**NCTY** (-21.54%): real catalyst (the RF Acquisition Corp II / Nanyang Biologics business combination), but it's gapping down, not up, so it misses the swing bar's gap-direction requirement outright. Worth flagging separately: NCTY's $19.96B market cap (`market_cap_source: sec_edgar`) looks wrong for a company this size, The9 Ltd is a small Chinese gaming name, and the same packet's own earnings headline quotes Q2 sales of just $712K against that supposed $19.96B cap, a massive mismatch. This is the same bad-SEC-EDGAR-fallback pattern called out for NCTY on 8/24 and for GDXD/GDXU and STKH/SVRE in earlier reports.

**MRNA** (+14.4%): the closest miss on the Swing Watchlist (see above), misses only on open vs. yesterday's high. Its catalyst, an analyst upgrade rather than a fundamental beat, would only support a middling conviction score even if it had cleared.

**SMCI** (+9.43%), **MARA** (+5.86%), **DNN** (+4.8%), **SOFI** (+4.31%): all four clear the day-trading market-cap floor but none clear yesterday's high on the pre-open stand-in price, and the day-trading bar is moot anyway with intraday data fully unavailable. MARA's own headline is stale (dated Friday), and SOFI's is a vague technical call rather than a hard catalyst.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
