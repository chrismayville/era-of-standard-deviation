<!-- PUBLIC COPY. Original registered file SHA-256 b898b12f55d2c794a03264e2c7e3c9cbc7afe43e79302257dd48e06622a41378. 1 redaction(s) applied for release; each is listed in appendix-assembly-manifest-2026-09-12.md. No registered value, rule, or date was changed. -->

---
title: Ruling — insured-loss sources retired (Swiss Re, Munich Re)
created: 2026-08-28
tags: [scrm, panel, ruling, provenance]
status: ruled by author; batch-landed with the Rev5 close
companions: [era-of-standard-deviation-data-panel-spec, panel-manifest-sprint2-transforms-breaks-2026-08-28, prereg-bdd-normalization-2026-08-28]
---

# Ruling — insured-loss sources retired

**Ruled by author, 2026-08-28:** no Swiss Re and no Munich Re data. Both are prohibited on their terms of use.

## Scope

No value from Swiss Re Institute sigma or from Munich Re NatCatSERVICE / as-reported releases appears in the panel, the exhibits, the database, or the essay. The prohibition covers extraction, republication, derivative computation, and ingestion, regardless of access path. It applies to the two headline figures extracted 2026-08-27 before the terms review and to the four as-reported Munich Re annual figures assembled the same week.

## Artifacts retired

- `swissre_sigma_anchors.csv` — two press-release headline figures
- `munichre_natcat_annual_asreported.csv` — 2022–2025 as-first-reported totals
- `sri-sigma-natcat-1-2025.pdf` — raw artifact

The author removes these from the project store. Their SHA-256 hashes remain in the 2026-08-27 pull manifest as the record that they existed and what they contained; the manifest itself is unedited history.

## Downstream audit (2026-08-28, clean)

Search of every project file plus manual review of the Sprint-2 notebook chain: no value from either source was consumed by the panel as run (eight series), by any exhibit (E1–E4, headline or appendix), by any notebook output, or by the Rev4/Rev5 essay body. The BDD constant-relative-significance test uses BEA fixed assets (denominator D1) and World Bank GDP (denominator D2), both open. Nothing to unwind.

## Dispositions

1. **Domain C.** The specified primary series (insured losses) is retired with **no substitute**. Domain C is carried by the Climate Central billion-dollar disaster count alone, under its registered ceiling: corroborating role only, not load-bearing in E3.
2. **EM-DAT.** Stays retired. The earlier session's stated reason — a commercial-license conflict with a database deliverable — is void now that the deliverable is struck. The standing reasons suffice on their own: the essay needs nothing from it, the spec flags its pre-1980 reporting bias, and adding a series post-registration would cut against the panel's discipline. Recording the corrected rationale here rather than silently keeping the conclusion.
3. **Prereg citation.** `prereg-bdd-normalization-2026-08-28.md` §1 cites Swiss Re's published exposure-growth decomposition as motivation. That file is hashed, registered history and stands verbatim. Forward-facing text (essay, appendix commentary) cites the independent normalization literature instead — Pielke et al., Bouwer (2011), Neumayer and Barthel (2011) — and no essay claim rests on the Swiss Re finding.
4. **World Bank GDP support file** (`worldbank_global_gdp_current_usd.csv`). Its stated purpose — denominator for a losses-as-%-of-GDP series — is orphaned. Open license; retained; currently feeds nothing.
5. **2026-08-27 manifest §2.** Stands as the historical pull record. Its open "access decision" fork is closed by this ruling: both routes are dead.
