# Daily Valuation Dashboard

A daily view of fair value vs price for ~57 listed companies across 8 groups
(Software, AI chips & semis, Platforms & neocloud, Physical AI, Pharma & biotech,
Banks, Digital banking, Brokerage), US, Europe and Asia.

- **Live dashboard:** https://claude.ai/artifact/Nn6Zgepqon2xiARN1zFmkL (private Claude artifact)
- **Data source:** TradingView scanner fields, via the signed-in TradingView Pro account
- **Refresh:** Claude scheduled task, weekdays 07:50 New York time (just before the 07:58–08:00 premarket gapper scan)

This folder is the versioned copy. The dashboard itself runs in Claude; changing files here
does not change the live page until they are published to the artifact again.

## Layout

| Path | What it is |
|---|---|
| `page/index.html` | The dashboard page. Holds all model logic (`dash.calc('valuation', …)`), the chart, tables and notes. |
| `data/companies.json` | Snapshot of the company list and fundamentals. **The `rows` list (id, symbol, name, bucket) is the master company list** — the daily refresh reads it from the live artifact and keeps it. |
| `data/markets.json` | Snapshot of 10Y yields, FX rates and benchmarks. |
| `data/assumptions.json` | Model assumptions (ERP, terminal growth, beta and growth limits, signal bands). Not touched by the refresh. |
| `refresh_prompt.md` | Copy of the scheduled task's prompt. |
| `tools/check_models.js` | Runs the page's model code on the `data/` snapshot and prints fair value, upside and signal per company. `node tools/check_models.js` |

## How the valuation works

Cost of equity `ke = 10Y yield + beta × ERP` (German 10Y for European stocks, US 10Y otherwise).
Growth = average of next-year EPS growth (ignored if it jumps > 50%) and revenue growth, clamped.
Fair value = median of the models for the company's group:

| Group | Models |
|---|---|
| Software, AI chips & semis, Platforms & neocloud, Pharma & biotech | DCF, PEG = 1, peer EV/EBITDA |
| Physical AI | Market-wide P/S, PEG = 1, DCF |
| Banks | Residual income, peer P/B, Gordon DDM |
| Digital banking | Residual income, peer P/B, PEG = 1 |
| Brokerage | PEG = 1, peer P/E, residual income |

Signal: Cheap if upside > 15%, Rich if < −15%, Fair in between; **Low data** if only one model applies.
Research aid, not investment advice.

## Changing things

- **Add or remove a company / change its group:** edit the live artifact's companies file (ask Claude), then copy it here.
- **Change a model or assumption:** edit `page/index.html` or `data/assumptions.json`, run `node tools/check_models.js`, then ask Claude to publish to the artifact.
- **Not valued (no listing):** Databricks, Huawei; Anthropic (ANT) is added automatically once it trades.
