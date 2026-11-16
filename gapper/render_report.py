#!/usr/bin/env python3
"""Renders REPORT.md into a styled, standalone HTML page."""

import re
from datetime import datetime
from pathlib import Path

import markdown

REPORT_PATH = Path("REPORT.md")
OUTPUT_DIR = Path("reports")

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<style>
  body {{
    margin: 0;
    padding: 40px 20px;
    background: #f4f5f7;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #1f2328;
    line-height: 1.6;
  }}
  .page {{
    max-width: 900px;
    margin: 0 auto;
    background: #ffffff;
    border: 1px solid #e3e5e8;
    border-radius: 8px;
    padding: 40px 48px;
  }}
  header {{
    border-bottom: 2px solid #1f2328;
    padding-bottom: 16px;
    margin-bottom: 24px;
  }}
  header h1 {{
    margin: 0 0 4px 0;
    font-size: 28px;
  }}
  header .date {{
    color: #57606a;
    font-size: 15px;
  }}
  h1, h2, h3 {{
    color: #1f2328;
  }}
  h2 {{
    margin-top: 36px;
    border-bottom: 1px solid #e3e5e8;
    padding-bottom: 6px;
    font-size: 20px;
  }}
  blockquote {{
    margin: 16px 0;
    padding: 10px 16px;
    background: #f9f9fb;
    border-left: 4px solid #c9ccd1;
    color: #444;
  }}
  table {{
    border-collapse: collapse;
    width: 100%;
    margin: 16px 0;
    font-size: 15px;
  }}
  th, td {{
    border: 1px solid #e3e5e8;
    padding: 8px 12px;
    text-align: left;
    vertical-align: top;
  }}
  th {{
    background: #f0f1f3;
    font-weight: 600;
  }}
  tbody tr:nth-child(even) {{
    background: #fafbfc;
  }}
  code {{
    background: #f0f1f3;
    padding: 2px 5px;
    border-radius: 4px;
    font-size: 0.9em;
  }}
  pre code {{
    display: block;
    padding: 12px;
    overflow-x: auto;
  }}
  hr {{
    border: none;
    border-top: 1px solid #e3e5e8;
    margin: 28px 0;
  }}
  footer {{
    margin-top: 40px;
    padding-top: 16px;
    border-top: 1px solid #e3e5e8;
    text-align: center;
    color: #8a8f98;
    font-size: 13px;
  }}
</style>
</head>
<body>
<div class="page">
<header>
  <h1>{title}</h1>
  <div class="date">{date}</div>
</header>
{body}
<footer>Educational only, not financial advice</footer>
</div>
</body>
</html>
"""


def extract_title_and_date(md_text):
    first_line = md_text.splitlines()[0]
    match = re.match(r"#\s*(.+?):\s*(.+)$", first_line)
    if match:
        return match.group(1).strip(), match.group(2).strip()
    return "Premarket Report", datetime.now().strftime("%B %d, %Y")


def date_for_filename(date_str):
    try:
        return datetime.strptime(date_str, "%B %d, %Y").strftime("%Y-%m-%d")
    except ValueError:
        return datetime.now().strftime("%Y-%m-%d")


def render():
    md_text = REPORT_PATH.read_text()
    title, date_str = extract_title_and_date(md_text)

    body_md = "\n".join(md_text.splitlines()[1:])  # header line is rendered separately
    body_html = markdown.markdown(body_md, extensions=["tables", "fenced_code", "sane_lists"])

    page = PAGE_TEMPLATE.format(title=title, date=date_str, body=body_html)

    OUTPUT_DIR.mkdir(exist_ok=True)
    out_path = OUTPUT_DIR / f"premarket_{date_for_filename(date_str)}.html"
    out_path.write_text(page)
    print(f"Wrote {out_path.resolve()}")


if __name__ == "__main__":
    render()
