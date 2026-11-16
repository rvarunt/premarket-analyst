# Set it up for yourself

About 15 minutes. You get your own copy of both tools, running on your own accounts.

## What you need

| For | You need | Cost |
|---|---|---|
| Both | A GitHub account, and this repo forked (the **Fork** button on GitHub) | Free |
| Both | Python 3.10+ on your computer (`python3 --version`) | Free |
| Gapper scan | An [Alpaca](https://alpaca.markets) account (paper trading is enough) and its API key | Free |
| Valuation dashboard | Node.js 18+ to run the model checker (`node --version`) | Free |
| Automatic daily runs, AI-written reports, live dashboard | A Claude plan with Claude Code (Pro or higher) | Your Claude plan |

## 1. Get the code

```bash
git clone https://github.com/<your-username>/premarket-analyst.git
cd premarket-analyst
python3 -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 2. Valuation dashboard

**Choose your companies.** Edit `valuation-dashboard/companies.csv` (any spreadsheet app works):

| Column | Example | Notes |
|---|---|---|
| `symbol` | `NASDAQ:NVDA` | TradingView-style `EXCHANGE:TICKER`, used as the row id |
| `yahoo` | `NVDA`, `ASML.AS`, `AZN.L` | Yahoo Finance symbol (search it on finance.yahoo.com) |
| `name` | `NVIDIA` | Shown on the dashboard |
| `group` | `AI chips & semis` | Decides which valuation models are used, see below |

Groups the models know: `Software`, `AI chips & semis`, `Platforms & neocloud`, `Physical AI`,
`Pharma & biotech`, `Banks`, `Digital banking`, `Brokerage`. Any other group gets DCF + peer EV/EBITDA.

**Get the data** (free, from Yahoo Finance; takes a minute or two):

```bash
python valuation-dashboard/build_data.py --de10y 2.7      # German 10-year yield in %, check it on any finance site
```

This writes `valuation-dashboard/data/companies.json` and `markets.json` on your computer.
They are git-ignored on purpose: market data is for your own use, don't commit it.

**See the valuations:**

```bash
node valuation-dashboard/tools/check_models.js                  # table in the terminal
node valuation-dashboard/tools/check_models.js --csv values.csv # also as a spreadsheet
```

No data yet? It falls back to `data/example/` (invented companies) so you can try it right away.

**Get the live dashboard page (Claude).** In Claude, attach `valuation-dashboard/page/index.html`
and the three files in `valuation-dashboard/data/` and ask: *"Publish this as a Data dashboard
artifact, with these three files as its datasets."* Claude gives you the dashboard link.

**Keep it fresh every day.** Two ways:

- **On your computer, no Claude:** schedule `build_data.py`, e.g. weekdays at 13:50 your local time with
  macOS/Linux `crontab -e`: `50 13 * * 1-5 cd ~/premarket-analyst && .venv/bin/python valuation-dashboard/build_data.py`,
  then run `check_models.js` when you want the table.
- **With Claude, from TradingView:** fill in the two placeholders in
  `valuation-dashboard/refresh_prompt.md` and ask Claude to create a weekday scheduled task with it.
  This uses your TradingView login in the Claude desktop app, so the app must be open at run time.

## 3. Gapper scan

1. Copy `.env.example` to `gapper/.env` and put in your Alpaca key and secret.
2. Run it by hand:
   ```bash
   cd gapper
   python scan.py            # writes packet.json
   ```
3. Turn the data into a report with Claude Code: open the repo in Claude Code (claude.ai/code or
   the desktop app) and say **"run the morning pipeline"**. It follows `CLAUDE.md`: scan, write
   `gapper/REPORT.md`, show it, commit it.
4. To run it every weekday, create a Claude Code routine on your fork with the prompt
   *"Run the morning pipeline per CLAUDE.md."*, scheduled weekdays 8:00 New York time, and add
   `ALPACA_API_KEY_ID` / `ALPACA_API_SECRET_KEY` to that environment's variables (not just to `.env`,
   which isn't there in a fresh cloud session).

## Changing things

| I want to… | Do this |
|---|---|
| Add or remove companies | Edit `companies.csv`, run `build_data.py` again |
| Change risk premium, growth caps, bands | Edit `valuation-dashboard/data/assumptions.json` |
| Change a valuation model | Edit the `dash.calc('valuation', …)` block in `page/index.html`; check with `check_models.js` |
| Change gapper rules | `gapper/WATCHLIST_CRITERIA.md` and `gapper/prompt_claude.md` |

## Tests

```bash
python -m unittest valuation-dashboard/tools/test_build_data.py   # data builder, offline
node valuation-dashboard/tools/check_models.js --data valuation-dashboard/data/example
```

Not investment advice. See `LICENSE`.
