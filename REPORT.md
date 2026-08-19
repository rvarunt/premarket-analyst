# Premarket Report: August 19, 2026

*Two-brain pass: Claude and GPT independently review the tape, then compare notes.*

> Rules pick the watchlist. Both AIs judge the quality of the setups. This is not financial advice.

## Summary

- **The tape in one line:** Red across every index proxy this morning (the raw index feed failed, so these are ETF proxies): S&P 500 proxy SPY -0.68%, Dow proxy DIA -0.24%, Nasdaq proxy QQQ -1.67%, Russell 2000 proxy IWM -1.25%. Nasdaq's the laggard, and the news feed backs that up: "Dow Jones Futures Fall After Sandisk, Micron, Credo Lead AI Losses."
- **The catch we're watching:** Total intraday blackout again. Every one of today's 20 gappers has `intraday_data_source: unavailable`, so premarket high, VWAP, HOD and LOD are null across the board and both watchlists come back empty. On top of that, the packet's own note says 120 requests failed even after retries this scan. FOMC Meeting Minutes drop at 2:00 PM ET today, the only high-impact event on the calendar, so whatever direction the tape takes into 2pm could flip fast.
- **Two-brain verdict:** Single-brain run today, no second opinion to compare against.

## Pre-Market Gappers

- **PFSA** +506.62% - "Profusa Stock Dips After Hours As Whopping 506% Rally Cools: Here Is Why PFSA Is Trending" (the packet's own headline says the rally is already fading after hours, classic blow-off top territory)
- **IPST** +113.26% - "Why Is IP Strategy Stock Falling Today?" (headline title contradicts today's up gap, doesn't explain the current move)
- **XOS** +112.44% - "Xos Stock Surges on US Air Force Contract Win"
- **SLE** +82.12% - "Super League Enterprise Announces Definitive Agreement For Metaplanet To Contribute 2,100 Bitcoin Valued At About $132.1M Plus $2.5M Cash For 44,859,400 Shares At $3.00/Share, Taking About 95.7% Stake; Company To Be Renamed Superplanet"
- **AMLX** +63.84% - "Amylyx Pharmaceuticals Announces $350M Common Stock Offering" (a dilutive offering, though the same packet also carries "Baird Maintains Outperform on Amylyx Pharmaceuticals, Raises Price Target to $52" and "HC Wainwright & Co. Maintains Buy on Amylyx Pharmaceuticals, Raises Price Target to $55")
- **GNLN** +51.74% - "Greenlane Hldgs Q2 EPS $(6.06) Up From $(25.46) YoY, Sales $82.000K Down From $788.000K YoY" (EPS "improved" off a smaller loss base, but sales cratered year over year)
- **FNG** -38.72% - no ticker-specific headline in the packet, the only headlines attached are about an unrelated FANG-themed ETF
- **SXTC** +36.8% - no ticker-specific headline in the packet, only generic "Health Care Stocks Moving" mover-list mentions
- **WETO** +34.2% - no ticker-specific headline in the packet, only generic "Industrials Stocks Moving" mover-list mentions
- **XTLB** +24.23% - "President Trump Say In A Social Media Post That The University Of Miami Shared Its 1994 Ibogaine Investigational New Drug Application With The Government, Which Will Help Accelerate Development As A Medical Treatment In The U.S." (the headline doesn't name XTL Biopharmaceuticals directly, link to today's move is unclear)
- **KEEL** -15.82% - "Keel Infrastructure Q2 Earnings Miss Estimates as Bitcoin Wind-Down Continues" (same week as a CEO Form 4 buy: "CEO Benjamin Gagnon Purchases 58,888 Shares At An Average Price Of $3.33")
- **CIFR** -12.97% - "Cipher Digital Stock Slides Tuesday: What's Happening?"
- **AUR** -11.82% - "Nasdaq Drops, Chip Stocks Crater As Bond Yields Bite: Stock Market Today" (also carries "Aurora Innovation Says It Expects 2026 Revenue Of $14M To $16M, Up 400% Year-Over-Year At Midpoint," a bullish guide that isn't stopping today's slide)
- **WULF** -11.42% - "TeraWulf Stock Falls as Inflation Fears Squeeze Growth Stocks"
- **MARA** -7.72% - "What's Going On With the Fall in MARA Shares?"
- **INTC** -6.55% - "What's Going On With Intel Stock Tuesday?"
- **IREN** -6.54% - "IREN Stock: Earnings Could Spark Big Move as Short Interest Reaches 26%"
- **OPEN** -5.5% - "UBS Maintains Neutral on Opendoor Technologies, Lowers Price Target to $4.5"
- **HL** -4.63% - "Hecla Mining Q2 EPS $0.17 Misses $0.21 Estimate, Sales $333.851M Beat $73.600M Estimate"
- **CDE** -4.19% - "Scotiabank Maintains Sector Outperform on Coeur Mining, Lowers Price Target to $26.5"

## Day Trading Watchlist

The "Trend Join Long" rule: gap over 3%, price over $3, market cap over $1B, premarket RVOL over 1.5, and price already breaking above yesterday's high.

No names cleared the day-trading bar today. This is a total intraday blackout: every one of today's 20 gappers has `intraday_data_source: unavailable`, so there's no premarket high, VWAP, HOD or LOD to check a break against for anyone. But even setting that aside, the packet's own numbers show none of today's 12 cap-qualified names (all clear $1B) would have cleared the "already breaking above yesterday's high" leg anyway: the two closest are AMLX ($35.11 vs a `prior_day_high` of $35.38) and XTLB ($3.23 vs a `prior_day_high` of $3.31), both still sitting under yesterday's high by a few cents. Everything else that gapped is running into resistance from well below, not through it.

## Swing Watchlist

The swing rule: gap of 8% or more, price over $3, open above yesterday's high, open above the 200-day SMA, market cap of $800M or more, and a real catalyst.

No names cleared the swing bar either. AMLX is the only cap-qualified name with an 8%+ gap (+63.84%) and a real catalyst, but it fails the same "open above yesterday's high" leg as above ($35.11 effective open vs a $35.38 prior high), so it's a watch-if-it-clears-$35.38 name, not a qualifier. Everything else either doesn't clear the 8% gap floor on the cap-qualified side, or is a micro-cap name (PFSA, IPST, XOS, SLE, GNLN, FNG, SXTC, WETO) sitting well under the $800M cap floor.

## Market Trends of the Day

No hard index data beyond the ETF proxies, but the news feed and the gapper list together paint a fairly consistent picture.

AI infrastructure and chip names are under pressure. The Dow futures headline puts it plainly: "Dow Jones Futures Fall After Sandisk, Micron, Credo Lead AI Losses; Target Earnings Beat." That's showing up in the gapper list too, Aurora's own catalyst headline reads "Nasdaq Drops, Chip Stocks Crater As Bond Yields Bite," and bitcoin/AI-infra miners are broadly red this morning: CIFR -12.97%, AUR -11.82%, WULF -11.42%, MARA -7.72%, INTC -6.55%, IREN -6.54%. Rising yields squeezing growth and AI-adjacent names is the through-line, per TeraWulf's own headline: "TeraWulf Stock Falls as Inflation Fears Squeeze Growth Stocks."

Gold miners are the counter-trend. Both HL and CDE carry the same market-wide headline in their catalyst lists: "Gold Miners Eye Best Month Since April 2020: 5 Stocks Are Already Up 30% In August." Both are only down modestly today (-4.63% and -4.19%) despite the broader risk-off tone, consistent with gold acting as a hedge while growth names sell off.

Retail earnings are diverging hard from price action. Target's earnings doubled and guidance was raised amid tariff refunds, but the stock is falling anyway ("Target Earnings Double, Guidance Raised Amid Tariff Refunds, But TGT Stock Falls"). Lowe's sent its stock lower on a cautious outlook, flagging "pressure" in DIY spending. Two different retailers, two different setups, both stocks moving against the headline number.

Trade and rates are the macro backdrop. Trump is holding off on new 50% tariffs for Canadian goods per MarketWatch, and futures "stalled" on that news rather than rallying. The dollar is described as softening while the bond market "steadies" ahead of the Fed minutes this afternoon, and a separate piece argues the bond selloff shouldn't be read as a signal of a deeper stock downturn. Outside those threads: a Chinese robotics company's stock soared over 600% on its trading debut, and Cerebras's post-IPO stock is still a bust, with its comeback hinging on a new chip per MarketWatch.

## Technical Signals for Today

Only the four major index proxies came through this run, and all four are red: S&P 500 proxy SPY 767.37 (-0.68%), Dow proxy DIA 532.96 (-0.24%), Nasdaq proxy QQQ 717.76 (-1.67%), Russell 2000 proxy IWM 300.24 (-1.25%). Nasdaq's the clear laggard, consistent with the AI/chip-loss headline above. VIX, the 10-year yield, the 3-month yield, WTI crude and the dollar index all came back null, same Yahoo rate limit that hit the gapper enrichment.

## Economic Data, Rates and the Fed

One high-impact USD event today: FOMC Meeting Minutes at 2:00 PM ET. The calendar doesn't carry a forecast or previous figure for this release. The news feed adds context even without hard numbers: the dollar is described as softening while the bond market "steadies" ahead of the minutes, so positioning looks like the market is waiting on this release rather than fighting it into the print.

## Coming Up

- **Tomorrow's events:** None on the high-impact USD calendar for August 20.
- **Earnings:** No gapper-level next earnings dates to report, every one of today's 20 gappers came back with `next_earnings_date: null`. Worth flagging from the news feed though: Target and Lowe's both already reported this morning, Target beat and raised guidance while Lowe's came in cautious on DIY spending, and both stocks fell regardless of the numbers.

## Skips and Traps

**PFSA** (+506.62%): the packet's own headline says the rally is already cooling after hours, that's a parabolic move fading in real time, not a fresh setup to chase.

**IPST** (+113.26%): the only headline in the packet ("Why Is IP Strategy Stock Falling Today?") contradicts today's up gap and doesn't explain the current move. $10.8M market cap, no volume figure in the packet. Skip.

**FNG** (-38.72%): every headline attached to this ticker is about an unrelated FANG-themed ETF, not this stock. No real catalyst behind the move as reported.

**SXTC** (+36.8%) and **WETO** (+34.2%): no ticker-specific headlines in the packet, only generic sector mover-list mentions that don't name either ticker. No story to trade.

**XTLB** (+24.23%): the one headline in its catalyst list (a Trump social media post about an Ibogaine drug application from the University of Miami) never names XTL Biopharmaceuticals directly, the connection to today's gap is unconfirmed. Also worth noting: `avg_volume_20d` is just 20 shares, this name is barely liquid.

**GNLN** (+51.74%): the EPS figure "improved" only because last year's loss was even bigger. Sales fell from $788K to $82K year over year. A shrinking business, not a turnaround story, whatever the EPS headline implies.

**AMLX** (+63.84%): real bullish catalysts here (two analyst price-target raises), but also a same-day $350M dilutive stock offering. Worth watching if it clears $35.38 (yesterday's high), but the offering is a real overhang, not a footnote.

## Where the Two Brains Landed

Single-brain run, second brain not wired in yet.

---

**Conviction key:** 🟢 high conviction &nbsp;&nbsp; 🟡 mixed signals, size down &nbsp;&nbsp; 🔴 low conviction, watch only
