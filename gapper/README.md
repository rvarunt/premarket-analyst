# Gapper — premarket scan

Finds US premarket gappers and writes a report with a swing watchlist.

1. `scan.py` gathers raw data (Alpaca movers and bars, SEC EDGAR market caps, news, econ calendar) into `packet.json`. No analysis.
2. Claude reads `packet.json` and follows `prompt_claude.md` + `REPORT_TEMPLATE.md` to write `REPORT.md`, applying the data integrity rules in the repo's `CLAUDE.md`.
3. `render_report.py` turns `REPORT.md` into a standalone HTML page in `reports/`.

Run everything from inside this folder (`cd gapper`): all paths (`.env`, `.venv`, `packet.json`, caches, `reports/`) are relative to it.

Secrets: `ALPACA_API_KEY_ID` / `ALPACA_API_SECRET_KEY` come from the Claude Code environment's variables (or a gitignored `gapper/.env`).
