# CLAUDE.md

Guidance for Claude Code working in this repo.

The repo has two parts:

- `gapper/` — the premarket gapper pipeline (scan → packet.json → REPORT.md). All of its
  files live in that folder and all of its paths are relative to it.
- `valuation-dashboard/` — the Daily Valuation Dashboard (see its README). Not part of the
  morning pipeline; never touch it while running the pipeline.

## Morning pipeline

When the user says "run the morning pipeline" (or a clear equivalent), do these steps in
order, without stopping to ask for confirmation between them. **Run every step from inside
`gapper/`** (`cd gapper` first): `scan.py`, `render_report.py`, `packet.json`, `.env`,
`.venv` and `REPORT.md` all live there.

1. **Run the scan.** `cd gapper && /home/user/.venv/bin/python3 scan.py`. That venv
   already has `requests`, `feedparser`, `yfinance`, `pandas`, and `markdown` installed. If
   that path doesn't exist in this session, create a local one first (inside `gapper/`):
   `python3 -m venv .venv && .venv/bin/pip install requests feedparser yfinance pandas markdown`,
   then use `.venv/bin/python3 scan.py`. This writes a fresh `gapper/packet.json`.
2. **Write the report.** Read the `gapper/packet.json` that was just written (not a stale copy
   from earlier in the conversation) and follow `gapper/prompt_claude.md` against it exactly,
   section by section, per `gapper/REPORT_TEMPLATE.md`. Title the report with today's actual
   calendar date, not necessarily `packet.json`'s `generated_at` date if the scan is reflecting
   an earlier session's close. Overwrite `gapper/REPORT.md` with the result. Apply the data
   integrity rules below on top of `prompt_claude.md`'s own judgment rules (catalyst check,
   bad-news-pop check), not instead of them. To render HTML, run `render_report.py` from
   inside `gapper/` too.
3. **Show the report.** Paste the full contents of the freshly written `gapper/REPORT.md` into
   the chat. Not a summary, not an excerpt, the whole thing.
4. **Commit and push.** Same as any other change in this repo: commit what actually changed
   (`packet.json` is gitignored, so this is normally just `gapper/REPORT.md`, plus
   `gapper/scan.py` if it was also touched) and push to the current branch.

Don't skip step 3. Don't stop after committing without having shown the report in the chat.

## Data integrity rules

These apply to every report this repo produces, not just the morning pipeline.

- Never invent, estimate, or "fill in" any number, headline, catalyst, or econ figure that
  isn't literally present in `packet.json`. If a field is null or missing, say so in the
  report instead of guessing a plausible-sounding value.
- Any name on the Swing Watchlist (`swing_eligible: true`, after the catalyst and
  bad-news-pop checks from `prompt_claude.md` have already been applied) gets flagged as
  suspect with a 🔴 conviction, overriding whatever the normal confluence scoring would
  otherwise produce, if either of these is true:
  - `market_cap` is under $2,000,000,000, or
  - a `catalyst_headlines` title in the packet itself quotes revenue/sales that's near-zero
    relative to the market cap (for example, a headline citing sales in the thousands or low
    tens of thousands against a market cap in the hundreds of millions or billions). Only use
    a revenue figure that's actually quoted in a catalyst headline in the packet. Don't look
    one up elsewhere and don't estimate one.
  State plainly which trigger fired and cite the actual numbers from the packet (market cap,
  and the revenue figure and its source headline if that's the trigger), rather than tagging
  the name red with no explanation.
