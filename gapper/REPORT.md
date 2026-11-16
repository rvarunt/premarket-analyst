# Premarket Report: November 16, 2026

*Single-brain pass: Claude only. Second brain not wired in yet.*

> Rules pick the watchlist. The AI judges the quality of the setups. This is not financial advice.

**Data warning: read this first.** This is not a premarket scan. The packet says "Scan run 2026-11-16 11:40 EST (regular session)." So every gap below is today's live move vs Friday's close, and the levels (VWAP, HOD, LOD) are from the first two hours of the session. It replaces the 06:09 ET version of today's report.

Yahoo rate-limited the scan hard: 85 requests failed even after retries. VIX, 10Y, 3M, WTI and the dollar are null. Market cap is null for 8 names (HZN, GDHG, PSNYW, AVAZ, CRMX, CRDX, SLON, SOLT), so their flags are false by default. `next_earnings_date` is null for all 20. `premarket_high` is null for 13 of 20, and intraday data is missing entirely for MTEX, CRDX and TPEI. Index levels are ETF proxies (SPY, DIA, QQQ, IWM), not the indices themselves.

## Summary

- **The tape in one line:** broad risk-off, tech leading down. SPY -1.1%, QQQ -1.75%, IWM -1.02%, DIA -0.66%. The headlines: "Nasdaq falls 1% at open as Nvidia woes weigh on sentiment ahead of earnings" and "Stocks Fall Before Nvidia Earnings, Anthropic IPO: Markets Wrap".
- **The catch we're watching:** Nvidia's earnings call ("Jensen Huang's sudden departure has made Tuesday's earnings call 'the most important in the company's history'"). Closer in: Fed Chair Warsh speaks at 12:00 PM ET today, about 20 minutes after this scan ran.
- **Two-brain verdict:** Single-brain run, no second opinion.

## Pre-Market Gappers

All 20 gappers in the packet. Gap % is today's price vs Friday's `prev_close`. Market cap in parentheses. Headline is the first one the packet lists for each ticker, which often isn't the real story (see Skips and Traps for the ones that are).

- **HZN** +4872.73% (cap null) : "Black Hills And NorthWestern Energy Complete Merger; To Trade On NYSE As Bright Horizon Energy Under The Ticker Symbol 'HZN' Starting Today"
- **GDHG** +806.34% (cap null) : "12 Consumer Discretionary Stocks Moving In Thursday's Pre-Market Session"
- **PSNYW** +57.8% (cap null) : "What's Going On With Polestar Shares On Monday?"
- **FCUV** -39.55% ($4.2M) : "Nasdaq Down Over 1%; Tyson Foods Earnings Top Views"
- **MTEX** -34.6% ($8.0M) : "Mannatech, Incorporated Announces Third Quarter 2026 Financial Results"
- **AVAZ** -29.44% (cap null) : no headline in the packet (`catalyst_found: false`)
- **CLRO** +26.26% ($11.4M) : "12 Information Technology Stocks Moving In Monday's Pre-Market Session"
- **IEP** -24.66% ($2.70B) : "12 Industrials Stocks Moving In Monday's Pre-Market Session"
- **CRMX** -24.18% (cap null) : "Trump, Greenland Deal Sparks CRML Trading Frenzy: These ETFs Rocket 75%"
- **CRDX** -22.36% (cap null) : "Cannabis Movers & Shakers: MindMed & Trulieve Management Shake-Ups, Credex Corp & CapStone Bolster Leadership Teams"
- **SLON** -22.31% (cap null) : "Shares of crypto-linked stocks are trading higher amid a rise in the price of Bitcoin."
- **SOLT** -22.29% (cap null) : "Soltech Energy Divests Large-Scale Solar Development Portfolio to Alight"
- **TPEI** +20.09% ($41.8B, see below) : "BMO, REX Launch 3X Brazil, Taiwan, Japan ETNs as Emerging-Market Inflows Hit a 6th Week"
- **TU** +10.78% ($14.6B) : "H World Group Posts Upbeat Q3 Earnings, Joins CG Oncology, TELUS And Other Big Stocks Moving Higher On Monday"
- **IREN** -9.52% ($5.87B) : "IREN Stock Is Falling Monday: What's Going On?"
- **ONDS** -6.8% ($2.74B) : "Stifel Maintains Buy on Ondas, Lowers Price Target to $15"
- **IBIT** -6.15% ($52.4B) : "Bitcoin ETFs Face $1B Exodus As Ethereum, Solana Funds Bleed: Is Institutional Crypto Demand Cracking?"
- **INTC** -6.13% ($297.6B) : "Intel Reports Share Stake Of 1.3M Ordinary Shares In Iren Limited"
- **VALE** -5.17% ($34.7B) : "Samarco Orders Yokogawa Control Systems for Mining and Pelletizing Operations"
- **CIFR** -4.89% ($2.98B) : "Why Is Cipher Digital Stock Surging on Wednesday?"

## Day Trading Watchlist

The bar is Trend Join Long: gap > 3%, price > $3, market cap > $1B, premarket RVOL > 1.5, and price already breaking above yesterday's high.

No names cleared the day-trading bar today. Every gapper is `day_eligible: false`. Only two up-movers have a known cap over $1B. TU is above its prior-day high (9.455 vs 8.63) but its RVOL is 0.01. TPEI has null RVOL and no intraday data at all. Nobody else up more than 3% has a known cap over $1B.

## Swing Watchlist

The bar is: gap >= 8%, price > $3, open above yesterday's high, open above the 200-day SMA, market cap >= $800M, and a real catalyst (earnings on the gap day, or news with no earnings).

Swing management isn't built yet. Anything here is a "watch and build a plan" name, not a trade.

| Ticker | Catalyst | Trend context | Idea | Second-brain check | Conviction |
|---|---|---|---|---|---|
| TPEI | "BMO, REX Launch 3X Brazil, Taiwan, Japan ETNs as Emerging-Market Inflows Hit a 6th Week" (news, no earnings date in the packet). Theme: leveraged emerging-market ETN. | Open is null, so the scanner used price 58.93 as the stand-in. That's above the prior-day high of 44.99 and the 200-day SMA of 44.99. | Watch only. No entry until the data is confirmed. | Not wired in. | 🔴 |

Why TPEI is red, and why I wouldn't touch it on this data:

- **The catalyst is stale.** The only headline is an August launch article (the link is dated 26/08). Nothing in the packet explains a 20% move today.
- **The market cap isn't TPEI's.** The packet names it "BANK OF MONTREAL /CAN/" and the $41.8B came from the SEC fallback. That's the issuer's cap, not the cap of a single exchange-traded note.
- **The daily bars look broken.** Prior-day high, prior close and the 200-day SMA are all exactly 44.99, and 20-day average volume is 0. Meanwhile `prev_close` is 49.07, which doesn't match the 44.99 prior close. The trend checks that made it eligible ran against one thin bar.
- **No live levels.** VWAP, HOD, LOD, premarket high and RVOL are all null.

It cleared the rules on a technicality. Treat it as a data-quality question, not a setup.

## Market Trends of the Day

The AI trade is still unwinding into Nvidia's print. "NVIDIA Falls 4% Ahead of Earnings as Elon Musk Joins Calls to Reinstate Jensen Huang; AMD Drops 6%, Taiwan Semiconductor Slides 5%." Then later in the morning: "Nvidia's stock extends declines following harsh words from the U.S. government." There's a policy piece behind that in the INTC feed: "U.S. Department Of Commerce's Bureau of Industry and Security Interim Final Rule To Address Remote Access To Advanced Super Intelligence Chips And Servers."

The AI-infra and crypto-miner names are getting hit together. IREN -9.52%, CIFR -4.89%, INTC -6.13%, and IBIT -6.15% on "Bitcoin ETFs Face $1B Exodus". INTC has its own problem too: "Intel Stock Falls as Shareholders Sue Over PC Slump Behind 29% One-Day Drop."

The week has two big AI tests: "Nvidia Earnings, Anthropic IPO Ahead in New Test for AI Economy" (WSJ). The selloff isn't just tech, though. IWM -1.02% and DIA -0.66% are red too. The only clean up-story with size is a takeover bid (TU). A couple of single-name earnings headlines are in the feed (Tyson "Stock Surges After Earnings") but no theme.

## Technical Signals for Today

ETF proxy levels at the 11:40 ET scan:

- SPY 745.97 (prev 754.27), -1.1%
- QQQ 668.09 (prev 680.01), -1.75%
- IWM 274.71 (prev 277.55), -1.02%
- DIA 519.64 (prev 523.1), -0.66%

QQQ is the weak spot again. VIX, 10Y, 3M, WTI and DXY are all null, so there's no volatility, rate, oil or dollar read.

Big names vs VWAP and the 200-day SMA:

- INTC 56 vs VWAP 56.07, HOD 57.2, LOD 55.36. Way under the 200-day SMA of 87.39.
- IREN 16.435 vs VWAP 16.44, sitting right on it. HOD 17.05, LOD 16.02. 200-day SMA is 42.59.
- IBIT 36.545 vs VWAP 36.65, just under. 200-day SMA is 41.05.
- TU 9.455 vs VWAP 9.52, under. It hit 10.45 (HOD and premarket high) and has faded about 9.5% off that. Still under its 200-day SMA of 11.1.

The pattern is the same everywhere: the losers are pinned near VWAP and the low end of the range. No bounce yet.

Volume figures: CIFR shows RVOL 7.35 and GDHG 40565.9, but daily bars are Alpaca IEX, a subset of the tape. Several big names show RVOL 0.0 or 0.01 because it's a premarket RVOL and the IEX premarket print was tiny. Don't read either extreme literally.

## Economic Data, Rates and the Fed

From `econ_calendar` (USD, high impact only):

- **Today, 12:00 PM ET:** Fed Chairman Warsh Speaks. No forecast or previous, it's a speech.
- **Tomorrow, 8:30 AM ET:** Core Retail Sales m/m, forecast 0.4%, previous 0.9%.
- **Tomorrow, 8:30 AM ET:** Retail Sales m/m, forecast 0.2%, previous 0.8%.

Both retail numbers are expected to cool a lot from last month. A hot print leans hawkish, a soft one helps the rate-cut case. The packet has no 10Y or 3M reading, so there's no live read on yields going into Warsh at noon. His remarks are the only scheduled event left in today's session.

## Coming Up

- **Tomorrow's events:** Retail Sales m/m (forecast 0.2%, previous 0.8%) and Core Retail Sales m/m (forecast 0.4%, previous 0.9%), both at 8:30 AM ET.
- **Earnings:** `next_earnings_date` is null for all 20 gappers, and the packet has no market-wide earnings calendar. The news feed puts Nvidia's call on Tuesday ("has made Tuesday's earnings call 'the most important in the company's history'"). The Anthropic IPO is in the headlines but the packet gives no date.

## Skips and Traps

- **TU** +10.78%: the real catalyst is "Telus Confirms Board Of Directors Has Received An Unsolicited, Non-Binding, And Conditional Acquisition Proposal From Québecor". Real news, $14.6B cap, and it's above the prior-day high. Not eligible: RVOL 0.01 kills the day bar, and the stand-in open of 9.57 is under the 200-day SMA of 11.1 for swing. It's also faded from 10.45 to 9.455, under VWAP 9.52. A non-binding bid is binary. Skip.
- **HZN** +4872.73%: not a real gap. The ticker got reused. Black Hills and NorthWestern merged and started trading as Bright Horizon Energy under "HZN" today. The 1.76 prev close belongs to the old Horizon Global (the other headlines are from 2023). Ignore the number.
- **GDHG** +806.34%: no cap, $0.83 prev close, 20-day average volume 1,227, and the only company news is a September amusement-park acquisition. HOD 7.48 vs VWAP 3.27. Pure microcap mania. Skip.
- **PSNYW** +57.8%: a Polestar warrant, not the stock. No cap, and the headlines are a July article and old halts. Skip.
- **CLRO** +26.26%: $11.4M cap, RVOL 0.1, and the only "catalysts" are generic movers roundups. Skip.
- **TPEI** +20.09%: on the swing list on a technicality, see the Swing section. Watch only.
- **AVAZ** -29.44%: `catalyst_found: false`, no headline, no cap. Skip.
- **FCUV** -39.55% and **MTEX** -34.6%: sub-$10M caps. MTEX's own headline has sales falling ("Sales $24.872M Down From $29.161M YoY"). FCUV's headlines are roundups. No long setups.
- **IEP** -24.66%: $2.70B but down hard, and the earnings line is a miss ("Icahn Enterprises Q3 EPS $(0.31) Misses $0.09 Estimate"). Far under the 200-day SMA of 7.28. No long setup.
- **CRMX, CRDX, SLON, SOLT** (-22% to -24%): no cap, and the headlines are old or unrelated (CRDX's only headline is from 2021). Some look like leveraged ETFs. Skip.
- **IREN, CIFR, INTC, IBIT, ONDS, VALE** (-4.9% to -9.5%): down with the AI and crypto unwind, or on target cuts (ONDS: Stifel to $15, Lake Street to $14, Needham $19 to $14). Neither setup is a short or a dip-buy, and they're all well under their 200-day SMAs. INTC also has a shareholder suit. Skip.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
