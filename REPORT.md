# Premarket Report: August 20, 2026

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** Index proxies are mixed and barely moving: S&P 500 proxy SPY +0.22%, Dow proxy DIA +0.24%, Russell 2000 proxy IWM +0.49%, Nasdaq proxy QQQ -0.24% is the lone laggard. Nothing dramatic in the index tape itself this morning.
- **The catch we're watching:** Total intraday blackout again, third session in a row for this scanner. All 20 gappers today have `intraday_data_source: unavailable`, so premarket high, VWAP, HOD and LOD are null across the board and both watchlists come back empty. The packet also flags 120 failed requests even after retries this scan, and VIX, the 10-year, the 3-month, oil and the dollar all came back null too (same yfinance rate limit). No high-impact USD econ events today or tomorrow, so the calendar itself isn't the catalyst. Watch Moderna: it's reportedly doubled (per a sister ETF's own headline, "FDA Decision Nears"), but nothing in Moderna's own catalyst list in the packet actually names what decision or when.
- **Two-brain verdict:** Single-brain run today, no second opinion to compare against.

## Pre-Market Gappers

- **FIXX** +1413.65% - "Trading Halt: Halted at 7:50:00 p.m. ET - Trading Halt: Halt News Pending" (the only other headlines attached are a stale Nasdaq minimum-bid-price deficiency notice and generic mover-list mentions, nothing that explains a gap this size)
- **MRNX** +352.09% - "Bulls Pile Into Moderna As FDA Decision Nears, Ignites 60% Surge In This ETF" (MRNX is a 2x leveraged single-stock ETF tracking Moderna, not Moderna itself)
- **MRNA** +176.97% - "Morgan Stanley Maintains Equal-Weight on Moderna, Raises Price Target to $89" (this is the top headline in the packet for MRNA itself, but it's a routine PT raise, nothing in Moderna's own catalyst list explains a move this size; the FDA-decision framing above comes from MRNX's headline, not Moderna's)
- **ZSTK** +169.55% - "ZeroStack (ZSTK) Stock Skyrockets Wednesday: What's Driving the Action?" (headline doesn't actually answer its own question)
- **MRNY** +169.23% - "ETFs Shine As S&P 500 Hits Record High: Top 5 ETFs With Best Gains From Last Week" (a generic ETF roundup, not a story specific to this move)
- **YJ** +144.25% - "Yunji H1 Adj. EPS $(2.16) Up From $(4.00) YoY, Sales $14.192M Down From $22.102M YoY" (a narrower loss, but sales fell about 36% year over year)
- **TNON** +109.36% - "Tenon Medical Stock Surges on Key Patent News: What Investors Need to Know"
- **PUR** +61.31% - no catalyst headline in the packet at all
- **PFSA** -50.62% - "Mercury Systems Posts Mixed Q4 Results, Joins WhiteFiber And Other Big Stocks Moving Lower In Wednesday's Pre-Market Session"
- **PURR** +30.42% - "Stan Druckenmiller Reveals $23 Million PURR Bet as Hyperliquid Takes On Polymarket"
- **GDXD** -27.95% - "New ETNs Bring Leverage, Spice To Gold Miners" (packet's company match for this ticker is "BANK OF MONTREAL /CAN/", see data quality note below)
- **GDXU** +27.75% - "This ETF Has Surged An Eye-Watering 470% - And It's Not Even Tech" (same Bank of Montreal company-match issue as GDXD)
- **WYFI** -21.02% - "WhiteFiber Stock Sinks After Raising $270 Million via Convertible Unsecured Debt" (a dilutive financing event, explains the drop)
- **HL** +14.38% - "Aramco and Maaden Move Ahead With Saudi Copper Mining Venture" (not really about Hecla; the more relevant headline in its list is "Gold Miners Eye Best Month Since April 2020: 5 Stocks Are Already Up 30% In August")
- **CDE** +12.99% - "Aramco and Maaden Move Ahead With Saudi Copper Mining Venture" (same generic top headline as HL, same gold-miner sector story underneath)
- **BMNR** +10.73% - "BTC Digital Stock Soars Over 111% After-Hours, BitMine Shares Trending as Bitcoin and Ethereum Regain Their Mojo"
- **ETHA** +9.99% - "Jane Street's Q2 Filing Reveals Nearly $1 Billion Bet on These Bitcoin ETFs - and a Major Stake in Michael Saylor's MSTR"
- **MRVL** +9.87% - "Broadcom Rival Marvell Surges After Google Strikes AI Chip Deal, Gets Option to Buy $12.2B Stake"
- **MARA** +7.70% - "Bitcoin ETFs See $486M Inflows in 2 Days: Could This Be the Best Week Since January?"
- **IBIT** +6.00% - "Bitcoin Surges Above $71,000 as Raoul Pal Says It's The 'Bessent Put' and 'The Signal Is Enormous'"

## Day Trading Watchlist

The "Trend Join Long" rule: gap over 3%, price over $3, market cap over $1B, premarket RVOL over 1.5, and price already breaking above yesterday's high.

No names cleared the day-trading bar today. This is a total intraday blackout: every one of today's 20 gappers has `intraday_data_source: unavailable`, so there's no premarket high, VWAP, HOD or LOD to check a break against, and no RVOL to confirm volume for anyone. Even setting the blackout aside, only one of today's ten cap-qualified, gap-qualified names (MRNA, PURR, GDXU, HL, CDE, BMNR, ETHA, MRVL, MARA, IBIT) is actually sitting above yesterday's high: GDXU at 158.63 vs. a `prior_day_high` of 158.18. But GDXU's market cap in the packet ($112.45B) is the SEC filer match for "BANK OF MONTREAL /CAN/", not a real market cap for this leveraged gold-miner ETN, so that cap-qualified read is itself suspect (see the data quality note in Skips and Traps). Everything else is still running into resistance from below: MRNA ($174.38 vs. $176.59), CDE ($20.92 vs. $21.31), BMNR ($20.23 vs. $20.89), MRVL ($237.35 vs. $245.35), IBIT ($38.78 vs. $39.47), HL ($20.52 vs. $20.56), MARA ($9.65 vs. $9.88) and ETHA ($15.86 vs. $15.96) are all a few cents to a few dollars short of yesterday's high, and PURR ($9.39 vs. $9.44) is close but not through.

## Swing Watchlist

The swing rule: gap of 8% or more, price over $3, open above yesterday's high, open above the 200-day SMA, market cap of $800M or more, and a real catalyst.

No names cleared the swing bar. The closest call is MRNX: it clears the 8% gap floor (+352.09%), sits above both yesterday's high ($141.64 vs. $136.85) and the 200-day SMA ($141.64 vs. $29.95), and has a catalyst in the packet, but `market_cap` came back null (`sec_unavailable_no_cik`), so there's no way to confirm it clears the $800M floor and it can't be waved through. MRNY has the same story: above yesterday's high, above the 200-day SMA, catalyst present, but market cap null. GDXU clears yesterday's high but sits well below its 200-day SMA ($158.63 vs. $209.05), so it fails that leg outright even setting the bad market-cap-source issue aside. Everything else with a confirmed market cap over $800M (MRNA, PURR, HL, CDE, BMNR, ETHA, MRVL) is still trading under yesterday's high, and the smaller names that clear the 8% gap (FIXX, ZSTK, TNON) either have no market cap on file or fall well short of $800M.

## Market Trends of the Day

Crypto and bitcoin-adjacent names are the clear group move this morning. BMNR (+10.73%), ETHA (+9.99%), MARA (+7.70%) and IBIT (+6.00%) are all green together, and the news backing it up is consistent: "Bitcoin Surges Above $71,000 as Raoul Pal Says It's The 'Bessent Put' and 'The Signal Is Enormous'," "Bitcoin ETFs See $486M Inflows in 2 Days," and BitMine's own headline calling out bitcoin and ethereum "regaining their mojo." PURR (Hyperliquid Strategies) rides the same wave with Druckenmiller's reported $23M bet.

Gold and precious metals have a real macro tailwind. HL and CDE both carry "Gold Miners Eye Best Month Since April 2020: 5 Stocks Are Already Up 30% In August" in their catalyst lists, and the market news feed backs it up directly: "Why Bessent's Treasury operations have breathed life back into the gold trade." Worth noting GDXD/GDXU (the leveraged gold-miner ETNs) moved in opposite directions as expected for a 2x/-2x pair, but their market cap data in the packet is unreliable, see Skips and Traps.

Rates and the dollar are the macro backdrop even without hard numbers today (VIX, 10-year, 3-month, oil and dollar index all failed to load). The news feed flags "Treasury's bond buyback blitz may end up driving yields higher, warns JPMorgan" and a separate Yahoo Finance piece from the past two days notes the 30-year yield touching a 19-year high as US debt approaches $40 trillion. Oil is also in the mix: "Oil prices jump after Trump declares economic war on Iran," a fresh geopolitical headline as of this morning.

AI capex financing is a live worry, not a straightforward bull story. "AMD is betting on dirt-cheap AI chips, but financing them is a major question mark" raises exactly the kind of funding-risk question that's been dogging the AI trade, even as MRVL's own catalyst is bullish on its face: "Broadcom Rival Marvell Surges After Google Strikes AI Chip Deal, Gets Option to Buy $12.2B Stake."

## Technical Signals for Today

Only the four major index proxies came through this run, and they're mixed: S&P 500 proxy SPY 769.09 (+0.22%), Dow proxy DIA 534.24 (+0.24%), Russell 2000 proxy IWM 301.72 (+0.49%), Nasdaq proxy QQQ 716.03 (-0.24%). Nasdaq is the lone red one, but the move is small either way. VIX, the 10-year yield, the 3-month yield, WTI crude and the dollar index all came back null, same yfinance rate limit that hit the gapper enrichment.

## Economic Data, Rates and the Fed

The high-impact USD calendar is empty for both today and tomorrow, `econ_calendar.today` and `econ_calendar.tomorrow` both came back as empty lists in the packet. That's not the same as "nothing happening": the news feed independently flags a JPMorgan warning that Treasury's bond buyback program could push yields higher, and (per Yahoo Finance coverage from the past two days) the 30-year yield already sitting at a 19-year high with US debt near $40 trillion. None of that is on today's or tomorrow's scheduled-release calendar, it's ongoing market commentary, not a print to trade around.

## Coming Up

- **Tomorrow's events:** None on the high-impact USD calendar for August 21.
- **Earnings:** No gapper-level next earnings dates to report, every one of today's 20 gappers came back with `next_earnings_date: null` in the packet.

## Skips and Traps

**FIXX** (+1413.65%): the only headline that's actually current is a trading halt with "Halt News Pending," meaning no news has actually been released yet to explain the halt. The other headline attached is a stale Nasdaq minimum-bid-price deficiency notice, which is bad news, not good. No market cap on file. A gap this large with no real explanation and no size data is not tradeable, it's noise or a data artifact.

**PUR** (+61.31%): no catalyst headline in the packet at all. Per the rules, no catalyst means no story, skip regardless of what the gap or eligibility flags say.

**ZSTK** (+169.55%) and **MRNY** (+169.23%): both have headlines that don't actually explain the move ("Stock Skyrockets: What's Driving the Action?" and a generic ETF roundup, respectively). ZSTK's market cap is $86.7M, well under any watchlist floor. MRNY's market cap is unavailable entirely.

**YJ** (+144.25%): the headline quotes the actual numbers, adjusted EPS loss narrowed to $(2.16) from $(4.00) year over year, but sales fell from $22.102M to $14.192M, about 36% down. A smaller loss on shrinking sales isn't a clean beat-and-raise story, and market cap isn't available in the packet to size the move against.

**TNON** (+109.36%): real-sounding catalyst (patent news), but market cap is $7.6M. Even if it cleared every other bar, this is a microcap that would get the automatic red-flag treatment under this repo's data integrity rules for being well under $2B.

**GDXD** (-27.95%) and **GDXU** (+27.75%): these are leveraged gold-miner ETNs, but the packet's SEC EDGAR company match for both is "BANK OF MONTREAL /CAN/," the ETN issuer, not the ETN itself. That means the market cap figures attached to these two ($13.03B for GDXD, $112.45B for GDXU) are Bank of Montreal's own market cap, not any measure of the ETNs' actual tradeable size. Don't use those cap numbers for anything, including the near-miss read on GDXU in the Day Trading section above.

**WYFI** (-21.02%): down on real bad news, a $270M convertible unsecured debt raise. Dilutive financing event, not a dip to buy.

**PFSA** (-50.62%): down alongside other names on a mixed Mercury Systems earnings reaction, no ticker-specific bullish story here, just moving with a sour tape for its peer group.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
