# Valuation dashboard

Fair value vs price for a list of listed companies (US, Europe, Asia), using two or three
valuation models chosen for each company's group. Setup for your own copy: see [`../SETUP.md`](../SETUP.md).

## Files

| Path | What it is |
|---|---|
| `companies.csv` | **The company list.** symbol, Yahoo symbol, name, group. Edit this to change what is valued. |
| `build_data.py` | Pulls prices and fundamentals from Yahoo Finance (free, no account) into `data/companies.json` and `data/markets.json`. |
| `data/assumptions.json` | Model assumptions: equity risk premium, terminal growth, beta and growth limits, signal bands. |
| `data/example/` | Invented sample data so everything works before you fetch real data. |
| `data/companies.json`, `data/markets.json` | Real market data, built on your computer. **Git-ignored** (personal use only). |
| `page/index.html` | The dashboard page for a Claude Data artifact. Holds all model logic, the chart, tables and notes. |
| `refresh_prompt.md` | Prompt for a Claude scheduled task that refreshes the dashboard daily from TradingView instead of Yahoo. |
| `tools/check_models.js` | Runs the page's model code on a data folder; prints the table or writes a CSV. |
| `tools/test_build_data.py` | Offline tests for `build_data.py`. |

## How the valuation works

Cost of equity `ke = 10Y yield + beta × equity risk premium` (German 10Y for European stocks,
US 10Y otherwise). Growth = average of next-year EPS growth (ignored if it jumps more than 50%)
and revenue growth, within limits. Fair value = median of the models for the company's group:

| Group | Models |
|---|---|
| Software, AI chips & semis, Platforms & neocloud, Pharma & biotech | DCF, PEG = 1, peer EV/EBITDA |
| Physical AI | Market-wide P/S, PEG = 1, DCF |
| Banks | Residual income, peer P/B, Gordon DDM |
| Digital banking | Residual income, peer P/B, PEG = 1 |
| Brokerage | PEG = 1, peer P/E, residual income |
| Any other group | DCF, peer EV/EBITDA |

Signal: **Cheap** if upside > 15%, **Rich** if below −15%, **Fair** in between, **Low data** if
only one model applies (left out of the counts). Full method notes are at the bottom of the page.

## Data sources

| Source | Account | Notes |
|---|---|---|
| Yahoo Finance (`build_data.py`) | None | Free. Gaps for some Asian listings; Yahoo limits request speed. German 10Y entered by hand (`--de10y`). |
| TradingView (`refresh_prompt.md`) | TradingView account, Claude desktop app | Richer fundamentals; runs through your browser session. |

Both write the same file format, so the page and `check_models.js` work with either.
Research aid, not investment advice.
