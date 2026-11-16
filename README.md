# premarket-analyst

Two daily market tools, both run by Claude on weekdays before the US open.

| Part | What it does | Runs | Output |
|---|---|---|---|
| [`gapper/`](gapper/) | Premarket gapper scan: finds today's gappers (Alpaca data, SEC market caps, news), checks them against the watchlist criteria and writes a report | Claude Code routine **premarket-analyst**, weekdays (target 08:00 New York) | `gapper/REPORT.md`, pushed to `main` |
| [`valuation-dashboard/`](valuation-dashboard/) | Fair value vs price for ~57 listed companies in 8 groups, using DCF, DDM, residual income, PEG and peer multiples | Claude scheduled task **Daily Valuation Dashboard refresh**, weekdays 07:50 New York | Live Claude dashboard (link in its README) |

## Layout

```
premarket-analyst/
├── CLAUDE.md                 how Claude runs the morning pipeline
├── gapper/
│   ├── scan.py               data gatherer → packet.json
│   ├── prompt_claude.md      analysis instructions
│   ├── REPORT_TEMPLATE.md    report layout
│   ├── WATCHLIST_CRITERIA.md eligibility rules used by scan.py
│   ├── render_report.py      REPORT.md → HTML
│   └── REPORT.md             latest report
└── valuation-dashboard/
    ├── page/index.html       dashboard page + valuation models
    ├── data/                 company list, rates/FX, assumptions
    ├── refresh_prompt.md     daily refresh instructions
    └── tools/check_models.js test the models on the saved data
```

## Running by hand

- **Gapper:** in Claude Code, say "run the morning pipeline".
- **Valuation dashboard:** ask Claude to refresh the Daily Valuation Dashboard, or run
  `node valuation-dashboard/tools/check_models.js` to see today's model output from the saved data.

Research aids, not investment advice.
