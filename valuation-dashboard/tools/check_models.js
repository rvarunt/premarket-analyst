#!/usr/bin/env node
// Runs the dashboard's own valuation code (from page/index.html) on a data folder and prints
// fair value, upside and signal for every company. No browser or Claude needed.
//
//   node tools/check_models.js                 uses data/ if built, else data/example/
//   node tools/check_models.js --data DIR      any folder with companies.json, markets.json, assumptions.json
//   node tools/check_models.js --csv out.csv   also write the results as a CSV (opens in Excel)
const fs = require('fs');
const path = require('path');

const args = process.argv.slice(2);
const opt = (name) => { const i = args.indexOf(name); return i >= 0 ? args[i + 1] : null; };
const root = path.join(__dirname, '..');
let dataDir = opt('--data');
if (!dataDir) {
  dataDir = fs.existsSync(path.join(root, 'data', 'companies.json')) ? path.join(root, 'data') : path.join(root, 'data', 'example');
}
const readRows = (f) => {
  const p = fs.existsSync(path.join(dataDir, f)) ? path.join(dataDir, f) : path.join(root, 'data', f);
  return JSON.parse(fs.readFileSync(p, 'utf8')).rows;
};

// Small stand-in for the parts of d3 the model code uses.
const d3 = {
  mean: (a) => a.reduce((x, y) => x + y, 0) / a.length,
  median: (a, f) => { const v = (f ? a.map(f) : a).filter((x) => x != null).sort((p, q) => p - q); const m = Math.floor(v.length / 2); return v.length % 2 ? v[m] : (v[m - 1] + v[m]) / 2; },
  ascending: (a, b) => a - b,
  group: (a, f) => { const m = new Map(); a.forEach((x) => { const k = f(x); if (!m.has(k)) m.set(k, []); m.get(k).push(x); }); return m; },
};

const html = fs.readFileSync(path.join(root, 'page', 'index.html'), 'utf8');
const firstScript = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)][0][1];
const calcs = {};
global.d3 = d3; global.window = global; global.document = { querySelectorAll: () => [] };
global.dash = { calc: (id, o) => { calcs[id] = o; }, draw: () => {}, data: () => ({}), onData: () => {} };
eval(firstScript); // defines the 'valuation', 'summary' and 'groups' calcs exactly as the page does

const v = calcs.valuation.fn(readRows('companies.json'), readRows('markets.json'), readRows('assumptions.json'));
const s = calcs.summary.fn(v)[0];
const fmt = (x, d = 1) => (x == null || !isFinite(x) ? '-' : x.toFixed(d));

console.log(`Data: ${path.relative(process.cwd(), dataDir) || '.'}`);
console.log(`${s.valued} of ${s.total} valued with 2+ models: ${s.cheap} cheap, ${s.fair} fair, ${s.rich} rich (${s.low_data} low data)\n`);
console.log(['Ticker'.padEnd(11), 'Group'.padEnd(22), 'Price'.padStart(11), 'Fair'.padStart(11), 'Upside'.padStart(8), ' Signal'].join(' '));
v.sort((a, b) => (b.upside_pct ?? -1e9) - (a.upside_pct ?? -1e9)).forEach((r) => {
  console.log([r.ticker.padEnd(11), r.bucket.padEnd(22), fmt(r.price, 2).padStart(11), fmt(r.fair_value, 2).padStart(11),
    (r.upside_pct == null ? '-' : fmt(r.upside_pct, 0) + '%').padStart(8), ' ' + r.signal].join(' '));
});

const csvPath = opt('--csv');
if (csvPath) {
  const cols = ['ticker', 'name', 'bucket', 'region', 'currency', 'price', 'fair_value', 'upside_pct', 'signal', 'agreement', 'n_models',
    'dcf', 'ddm', 'ri', 'peg_fv', 'peer_fv', 'peer_basis', 'pe', 'peg', 'ev_ebitda', 'pb', 'ps', 'div_yield_pct', 'ke_pct', 'g_pct'];
  const esc = (x) => (x == null ? '' : /[",\n]/.test(String(x)) ? `"${String(x).replace(/"/g, '""')}"` : String(x));
  fs.writeFileSync(csvPath, [cols.join(','), ...v.map((r) => cols.map((c) => esc(r[c])).join(','))].join('\n'));
  console.log(`\nWrote ${csvPath}`);
}
