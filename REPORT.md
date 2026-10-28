# Premarket Report: 2026-10-28

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** Index ETF proxies are green premarket: SPY +0.58%, QQQ +1.28%, IWM +1.17%, DIA +0.03%. Headlines say Nasdaq futures are up on SK Hynix while CNBC has futures mixed ahead of the Fed. VIX, yields, oil and the dollar all came back null this scan.
- **The catch we're watching:** The Fed decision at 2:00 PM ET (forecast hold at 4.00%) and the 2:30 PM ET press conference, with Microsoft and Alphabet earnings and AI cash flow worries in the headlines.
- **Two-brain verdict:** Single-brain run, second brain not wired in yet.

**Data quality note:** Yahoo rate-limited 110 requests this scan. Index rows are Alpaca ETF proxies (SPY/DIA/QQQ/IWM), not the real index levels. Premarket RVOL, VWAP, HOD, LOD and premarket high are null for every gapper, and `next_earnings_date` is null for every gapper. Market cap is null for MSGR, BRAI, CRMX, AIOK, USAX and TEUP, so their eligibility flags are false by design.

## Pre-Market Gappers

All 20 names in the packet:

- **MSGR** +1176.83%: "MSG Rangers Completes Spinoff From MSG Knickerbockers, Become Standalone Public Entity On NYSE Under MSGR Ticker"
- **NUWE** +74.69%: "Nuwellis Accepts Multicenter Pediatric Aquadex Study In Pediatric Nephrology"
- **BRAI** +56.13%: "Braiin (BRAI) Stock Jumps 56% After Hours: What’s Behind the Move"
- **CRMX** +55.10%: "Trump, Greenland Deal Sparks CRML Trading Frenzy: These ETFs Rocket 75%"
- **AIOK** +46.51%: "AI OKTO Declares $3.50 Per Share As One-Time Special Dividend"
- **LCFYW** -41.01%: no catalyst found
- **FVNNU** +38.39%: "Trading Halt: Halt status updated at 10:35:00 AM ET: Quotation Resumption: IPO Security - Released for Quotation"
- **AEYE** +36.66%: "AudioEye Reports Third Quarter 2026 Financial Results and Announces Share Repurchase Program"
- **USAX** +34.38%: "Rare-Earth ETF Frenzy Breaks: Leveraged 2X Funds Slide After Trump Deal Rally"
- **TEUP** +33.91%: no catalyst found
- **MBRX** +30.77%: "Moleculin Biotech Completes Patient Enrollment In Part A Of Its Pivotal Phase 2/3 MIRACLE Study Of Annamycin In Combination With Cytarabine To Treat Adults With Relapsed Or Refractory Acute Myeloid Leukemia"
- **ARTV** -30.68%: "Artiva Biotherapeutics Plunges Into Crisis Over Patient Deaths and Possible Liquidation"
- **CRML** +27.43%: "Critical Metals Corp. Secures Court Approval and Finalizes Acquisition of European Lithium Limited"
- **INOD** -25.32%: "Why Is Innodata Stock Sinking Tuesday?"
- **SOFI** +13.45%: "Keefe, Bruyette & Woods Maintains Underperform on SoFi Technologies, Raises Price Target to $16"
- **BA** -10.67%: "Morgan Stanley Maintains Equal-Weight on Boeing, Lowers Price Target to $195"
- **CIFR** +10.01%: "Why Is Cipher Digital Stock Surging on Tuesday?"
- **IREN** +7.86%: "Why Is IREN Stock Surging Tuesday?"
- **ONDS** +7.70%: "Palantir Says Ondas Is Launching Regna AI, Built On Palantir’s AIP Platform And Nvidia Nemotron Models"
- **TSLA** +4.04%: "Tesla Plans Robotaxi Service Expansion to Florida Beaches"

## Day Trading Watchlist

**Rule behind the flag:** Trend Join Long. Gap > 3%, price > $3, market cap > $1B, premarket RVOL > 1.5, and price breaking above yesterday's high.

No names cleared the day-trading bar today. Every gapper came back `day_eligible: false`. Premarket RVOL is null for most names, and the ones with an RVOL figure (SOFI, CIFR, IREN, ONDS, TSLA, BA, BRAI) are all still sitting below their prior day high in the packet (SOFI 16.405 vs 16.75, TSLA 407.51 vs 408.45, CIFR 8.465 vs 8.53, IREN 27.435 vs 27.64, ONDS 6.64 vs 6.68).

## Swing Watchlist

**Rule behind the flag:** Gap >= 8%, price > $3, open above yesterday's high, open above the 200-day SMA, market cap >= $800M, and a real catalyst (earnings on the gap day, or news with no earnings). Before 9:30 AM ET the current gap price stands in for the open.

No names cleared the swing bar today. Every gapper came back `swing_eligible: false`. Swing management isn't built yet anyway, so this would be watch-and-build-a-plan only.

## Market Trends of the Day

AI is the whole story, and it cuts both ways.

- **Chips and memory are bid.** "Nasdaq futures rise as SK Hynix boosts chips before Fed decision, earnings" (Reuters). "SK Hynix Plans $75 Billion in Shareholder Returns After Blockbuster Earnings" (WSJ). QQQ is +1.28% in the proxy data.
- **AI infrastructure names are moving.** CIFR +10.01% and IREN +7.86% are in the gapper list, and "Vertiv Stock Jumps 14% as Earnings Show Another Way to Play the AI Boom" (Barron's). "CoreWeave and other AI stocks rise as Anthropic restores the market’s faith in sustained spending" (MarketWatch).
- **But the bubble worry is loud.** "China rushes to shore up markets as AI trade sours" (Financial Times). "Microsoft and Alphabet Earnings Put Focus on AI Cash Flow Drain" (Bloomberg.com). "A leading Silicon Valley cheerleader just showed all the reasons to be worried about the AI bubble" (MarketWatch). One IREN headline quotes Ed Yardeni: AI bubble "deflating without bursting" with funding scrutiny on CRWV and NBIS.
- **Small caps are firm.** IWM +1.17%.
- **Boeing is the big loser.** BA -10.67% on a gap down, with a Morgan Stanley target cut to $195.
- **Inflation chatter:** "Four reasons to start worrying about inflation — including the end of tariff refunds" (MarketWatch).

## Technical Signals for Today

Thin, because VIX and the real index levels didn't load.

- SPY 769.7 vs 765.23 prior close (+0.58%).
- QQQ 721.22 vs 712.11 (+1.28%).
- IWM 280.18 vs 276.95 (+1.17%).
- DIA 523.22 vs 523.05 (+0.03%).
- These are ETF proxies, not the index levels.
- VIX, US 10Y, US 3M, WTI and DXY: null. No read.
- Per-name levels: nothing from the packet on VWAP, HOD, LOD or premarket high, so no intraday trigger map today.
- Names under their 200-day SMA per the packet: SOFI (16.405 vs 17.93), CIFR (8.465 vs 17.9), IREN (27.435 vs 44.74), ONDS (6.64 vs 9.14), BA (168.06 vs 218.06), CRML (8.13 vs 9.4), INOD (44.74 vs 61.65). TSLA is above its (407.51 vs 385.91).

## Economic Data, Rates and the Fed

Today, 2026-10-28 (high-impact USD):

- **2:00 PM ET:** Federal Funds Rate. Forecast 4.00%, previous 4.00%. A hold is expected.
- **2:00 PM ET:** FOMC Statement. No forecast listed.
- **2:30 PM ET:** FOMC Press Conference. No forecast listed.

The packet has no actual figures yet. Expect the tape to chop into 2:00 PM and get its real direction from the press conference.

## Coming Up

- **Tomorrow's events (2026-10-29):** 8:30 AM ET Advance GDP q/q (forecast 3.2%, previous 1.5%). 8:30 AM ET Core PCE Price Index m/m (forecast 0.3%, previous 0.2%).
- **Earnings:** `next_earnings_date` is null for every gapper, so no gapper earnings dates to list. Headlines only: "Microsoft to report Q1 earnings with Wall Street looking for further Azure growth" (Yahoo Finance via Google News). "Cipher Digital Announces Date of Third Quarter 2026 Business Update and Financial Results" (fiscal.ai), but the packet doesn't give the date. The packet has no full market earnings calendar.

## Skips and Traps

Nothing made either watchlist, so here is what's worth knowing and why none of it is a trade.

**No catalyst found, skip:**
- **LCFYW** -41.01%, no catalyst found.
- **TEUP** +33.91%, no catalyst found.

**Gap math is junk or the instrument is odd:**
- **MSGR** +1176.83%. The headline is a spinoff listing under a new ticker, so the prior close of 13.91 versus 177.61 probably isn't a real gap. Market cap null.
- **FVNNU** +38.39%. The only catalyst is an IPO-security quotation resumption halt update. Not a story, and an acquisition-corp unit.
- **USAX** +34.38% and **CRMX** +55.10%. Both are tied to leveraged rare-earth ETF headlines. USAX's own headline says the 2X funds "Slide After Trump Deal Rally". Market cap null on both.

**Up on thin or suspect news, trap territory:**
- **BRAI** +56.13%. After-hours pop, sitting at 3.31 against a 200-day SMA of 11.65 and a prior day high of 4.16. Market cap null.
- **NUWE** +74.69%. Market cap is $19.7M and the headlines are a study acceptance and conference participation, nothing that explains 75%.
- **AIOK** +46.51%. Headlines include a halt on the upside, a CEO Form 4 buy, and a $3.50 per share one-time special dividend. Prior day high is 17.57 and price is 13.42, so this is a dividend-adjusted, halt-driven mess. Market cap null.
- **MBRX** +30.77%. Market cap $180M. One of the headlines is a 1-for-20 reverse stock split, effective October 20.
- **AEYE** +36.66%. Market cap $128.6M, under the $1B day bar and $800M swing bar. Real earnings plus a buyback and guidance narrowing, but it is a small cap.

**Down on bad news, not a long:**
- **ARTV** -30.68%: "Artiva Biotherapeutics Plunges Into Crisis Over Patient Deaths and Possible Liquidation", plus Needham and Wedbush downgrades.
- **INOD** -25.32%: "Why Is Innodata Stock Sinking Tuesday?" and a layoff headline.
- **BA** -10.67%: the gap is down.

**Up but didn't clear the bar:**
- **CRML** +27.43%, market cap $1.195B, headline is the European Lithium acquisition approval. Price 8.13 is under the prior day high 8.29 and the 200-day SMA 9.4. Both flags false.
- **SOFI** +13.45%. The headline is a KBW Underperform, maintained with a raised target to $16, so the "news" isn't a clean bullish catalyst. Price 16.405 is under the prior day high 16.75 and the 200-day SMA 17.93.
- **CIFR** +10.01%, **IREN** +7.86%, **ONDS** +7.70%. All below the 200-day SMA and the prior day high. CIFR's headlines include "Cipher Digital Stock Sinks To 52-Week Low - Here's Why".
- **TSLA** +4.04%. Clears the gap and cap thresholds on paper, but price 407.51 is under the prior day high of 408.45, so the break hasn't happened.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
