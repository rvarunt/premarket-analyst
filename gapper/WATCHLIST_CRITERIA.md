# Watchlist Criteria

Source of truth for the scanner. These are the two validated setups. If the scanner's output doesn't match these rules exactly, the scanner is wrong, not the rules.

## Day Trading Watchlist: "Trend Join Long"

Backtest: 54.6% win rate, profit factor 1.59, 280 trades.

### Premarket selection (all required)

- Gap % vs prev close > 3%
- Price > $3
- Market cap > $1B
- Premarket relative volume (RVOL) > 1.5
- Price breaking above yesterday's high

### Intraday plan

- **Window:** 10:00am to 3:30pm ET
- **Trigger:** price > premarket high AND > prior high-of-day
- **Stop (1R):** 1% below premarket high, or the LOD, whichever is lower
- **Scale out:** 1/3 at +1R, 1/3 at +2R, trail the last 1/3 on the 21-EMA
- **Flat by:** 3:51pm, no exceptions

## Swing Watchlist

Backtest: 57.6% win rate / PF 5.34 on news catalysts, 44.7% / PF 2.57 on earnings catalysts.

### Premarket selection (all required)

- Gap % >= 8%
- Price > $3
- Open > yesterday's high
- Open > 200-day SMA
- Market cap >= $800M
- A real catalyst: earnings on the gap day, or news with no earnings

### Entry and exit management

Not built yet. Swing picks are starter ideas only. Do not attach stops or targets to them until this is built out for real.
