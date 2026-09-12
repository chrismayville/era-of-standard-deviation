<!-- PUBLIC COPY. Original registered file SHA-256 21db4f59438557978decce73ea0cfba811edb83449dd3f1326328267a1f40c73. 2 redaction(s) applied for release; each is listed in appendix-assembly-manifest-2026-09-12.md. No registered value, rule, or date was changed. -->

# Panel pull manifest — 2026-08-27 (Domain C physical + supports)

Retrieved 2026-08-27 by Claude session. All sources public, no logins. Raw artifacts hashed (SHA-256) at retrieval; raw files included alongside this manifest.

## 1. Climate Central — U.S. Billion-Dollar Weather and Climate Disasters (counts)

- **Source:** climatecentral.org/climate-services/billion-dollar-disasters/time-series — annual event counts by type embedded in the page payload (the CSV export button is registration-gated; the display data is not). Continuation of the retired NOAA/NCEI database, methodology unchanged, same lead scientist (Adam Smith); NOAA ceased May 2025, Climate Central relaunched Oct 2025.
- **Raw artifact:** `climatecentral_bdd_timeseries_embedded.json` — SHA-256 `9fde921497d610a2…` (full hash in pull_summary.json)
- **Coverage:** 1980–2026 (2026 partial year, through ~June; flagged in processed file)
- **Normalization label (must ride with every use):** event threshold is $1B **CPI-adjusted to 2026 dollars; NOT exposure-adjusted.** A fixed real-dollar threshold against growing built exposure mechanically raises counts over time.
- **Files:** `bdd_annual_counts_1980_2026.csv` (by type + total), `bdd_processed_z85_07.csv` (totals z-scored vs 1985–2007 baseline: μ=5.22, σ=2.33)

### Ledger reconciliation (rows 1 and 3)

- **Row 3 (>3σ counts rise by decade): cooperates emphatically.** Years with |z|>3 by decade: 1980s **0**, 1990s **0**, 2000s **0**, 2010s **5**, 2020s **6 of 6** (2020–2025 all exceed **+5σ**; 2023 = +9.8σ, 2024 = +9.3σ, 2025 = +7.6σ). Annualized per-decade: 0 → 0 → 0 → 5 → 10.
- **Row 1 (variance/regime): contributes a long series with a visible step; formal PELT/Bai–Perron at the Sprint-2 notebook.**
- **Required honesty note for §5:** the exposure confounder is real and now *stronger* than the spec assumed — see Swiss Re decomposition below. Use BDD as "frequency of billion-dollar-scale loss events" (institutional/exposure-inclusive), not as physical-hazard variance per se. The NOAA→Climate Central hand-off beat (observability migrating out of government) is unaffected and lands as planned.
- 2026 partial: 12 events through ~June (+2.9σ already at half-year). Report as partial; do not lean on naive ×2 annualization in print.

## 2. Swiss Re Institute sigma — insured nat-cat losses (PARTIAL: anchors only)

- **Raw artifact:** `sri-sigma-natcat-1-2025.pdf` (sigma 1/2025, "Natural catastrophes: insured losses on trend to USD 145 billion in 2025," 33 pp., retrieved from swissre.com/dam/…) — SHA-256 `2b9d810b257c9c64…`
- **Finding:** the full 1970– annual table is **no longer printed in the public PDFs** — Figures 1/2/7 chart the series without per-year labels, and the underlying data now sits behind the **sigma explorer client portal** (login; sigma-explorer.swissre.com is not publicly reachable). Digitizing a chart fails provenance standards; not done.
- **Anchors extracted:** [values redacted in the public copy — source retired 2026-08-28 under its terms of use; see `ruling-source-retirement-2026-08-28.md`. No value from this source was used in the panel, exhibits, or essay.]
- **Material finding for the spec:** [redacted in the public copy — retired source; the finding motivated the BDD normalization registration, which stands on its own.] The spec's "% of global GDP to kill the exposure-growth objection" framing needs a write-down: %GDP normalization removes economy-scaling but Swiss Re's decomposition substantially pre-empts the residual claim. §5 should use the loss series primarily via the *protection-gap / who-absorbs* angle and the peak-year concentration, not as evidence of rising physical variance. **This goes in the essay as a reported limitation, per ledger rule.**
- **Access decision → Chris:** (a) register for the sigma explorer client portal (joins the BDI/EM-DAT login bucket), or (b) Claude assembles the annual series from ~20 archived sigma editions' stated annual totals in a dedicated session (each year's figure in then-current prices, deflated with CPI, every step labeled). Route (b) is fully provenanced but is its own afternoon.

## 3. World Bank — global GDP, current US$ (support series)

- **Source:** api.worldbank.org, NY.GDP.MKTP.CD, country=WLD, 1970–2025 (56 rows) — raw `wb_gdp_wld.json`, SHA-256 `7ea64190a351acb2…`
- **File:** `worldbank_global_gdp_current_usd.csv`. Purpose: denominator for losses-%-GDP when the Swiss Re annual series lands.

## 4. Pre-registered for the NEXT pull — Federal Register / announcement counts (§4's "they can be counted")

Registered now, before any pull, per project discipline. Definitions to finalize in wording but fixed in intent:

1. **Entity List additions/yr:** Federal Register API, agency = Bureau of Industry and Security, document type = Rule, title contains "Entity List," action = additions (revisions counted separately), 2010–2025.
2. **Tariff/import-adjustment presidential documents/yr:** FedReg type = Presidential Document, terms "tariff" OR "duties" OR "Section 232" OR "Section 301," 2010–2025.
3. **OFAC designation actions/yr:** OFAC "Recent Actions" archive (FedReg notices undercount), SDN update actions per year, 2010–2025.

Counting rule: one document/action = one count; no severity weighting; report the raw count and the query verbatim in the essay's data appendix.

## Session status after this pull

| Item | Status |
|---|---|
| EPU, TPU, GPR, PortWatch, VIX, MOVE, UCDP | landed (prior sessions) |
| Climate Central BDD | **landed this session** |
| Swiss Re sigma | **anchors landed; full series blocked on access decision** |
| World Bank GDP support | **landed this session** |
| WCI / FBX / BDI | blocked on logins (Chris) — TradingView/investing.com route, monthly fallback sanctioned |
| EM-DAT | optional; registration (Chris); spec prefers insured losses as primary |
| FedReg counts | pre-registered above; pull next session |
| Swiss Re %GDP series | pending full annual series |
