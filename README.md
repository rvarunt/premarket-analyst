# premarket-analyst

Two daily tools for US and global equities, built to run with Claude before the US market opens.
**Want your own copy? Follow [SETUP.md](SETUP.md)** (about 15 minutes, free data sources).

| Part | What it does | Data | Output |
|---|---|---|---|
| [`gapper/`](gapper/) | Premarket gapper scan: today's gappers, market caps, news, econ calendar, checked against watchlist rules | Alpaca (free account), SEC EDGAR | `gapper/REPORT.md` (Claude writes the analysis) |
| [`valuation-dashboard/`](valuation-dashboard/) | Fair value vs price for your company list, using DCF, dividend, residual-income, PEG and peer-multiple models | Yahoo Finance (free) or TradingView | Terminal table / CSV, or a live Claude dashboard |

## Quick start

```bash
pip install -r requirements.txt
python valuation-dashboard/build_data.py --de10y 2.7     # fetch data for companies.csv
node valuation-dashboard/tools/check_models.js           # see the valuations
```

For the gapper scan, add your Alpaca keys (`.env.example`) and say "run the morning pipeline"
in Claude Code. Details in [SETUP.md](SETUP.md).

## Layout

```
premarket-analyst/
├── SETUP.md                  set it up for yourself
├── CLAUDE.md                 how Claude runs the morning pipeline
├── requirements.txt, .env.example, LICENSE
├── gapper/
│   ├── scan.py               data gatherer → packet.json
│   ├── prompt_claude.md      analysis instructions
│   ├── REPORT_TEMPLATE.md    report layout
│   ├── WATCHLIST_CRITERIA.md eligibility rules used by scan.py
│   ├── render_report.py      REPORT.md → HTML
│   └── REPORT.md             latest report
└── valuation-dashboard/
    ├── companies.csv         your company list
    ├── build_data.py         Yahoo Finance → data/*.json
    ├── page/index.html       dashboard page + valuation models
    ├── data/                 assumptions, examples (real data is git-ignored)
    ├── refresh_prompt.md     daily TradingView refresh via Claude
    └── tools/                model checker, tests
```

MIT licensed. Research aids, not investment advice.
