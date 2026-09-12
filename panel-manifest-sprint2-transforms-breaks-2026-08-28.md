# Panel manifest — Sprint 2 transform notebook, E2/E3, break tests (2026-08-28)

Run by Claude session, 2026-08-28. All sources public, no logins. Governing ruling hashed **before** the notebook ran, per its own condition 3.

---

## 1. Provenance

| Artifact | Source | SHA-256 (first 20) | Bytes |
|---|---|---|---|
| `ruling-transforms-e3-2026-08-28.md` | governing ruling, hashed pre-run | `ca96963eb56562445da0` | 4,286 |
| `prereg-bdd-normalization-2026-08-28.md` | prior registration (hash matches 08-28 manifest) | `da2227e665cf40f9958b` | 6,438 |
| `US_Policy_Uncertainty_Data.xlsx` | policyuncertainty.com | `6a9cd3f23e2be5a6b03d` | 89,602 |
| `data_gpr_export.xls` | matteoiacoviello.com/gpr | `6126ac6838929a4fd2e4` | 2,712,064 |
| `tpu_web_latest.xlsx` | matteoiacoviello.com/tpu | `49fe0f8ad70ad930eb92` | 293,562 |
| `VIX_History.csv` | cdn.cboe.com daily VIX history, 1990– | `be8fc7180260c05c955a` | 472,003 |
| `move_yahoo.json` | Yahoo `^MOVE` chart endpoint, 2002– | `40d7db16d599a74ba20d` | 577,172 |
| `UcdpPrioConflict_v25_1.csv` | ucdp.uu.se flat-file download, ACD v25.1 | `a7a2ff6caf6c854f4faf` | 506,186 |
| `bdi_monthly_1985_2026.csv` | project file, prior pull | `44f03508763c44667689` | 14,047 |
| `bdd_annual_counts_1980_2026.csv` | project file, prior pull | `e6fba2a99b6f331459f4` | 1,149 |

**Access note.** EPU, TPU, GPR, VIX, MOVE and UCDP were re-pulled this session rather than reused; the prior-session files were not on the working volume. The UCDP API now returns `401 API token required`; the ACD flat-file download at `ucdp.uu.se/downloads/ucdpprio/` remains open and was used instead. Substantively identical data, different access path, recorded here so the change is not silent.

## 2. Panel as run

Eight series, four domains plus two controls. Monthly grain for continuous series (12-month rolling mean for Tier 1; 36-month rolling σ of monthly log changes for BDI). Annual for counts.

| Series | Domain | Baseline window | n | Category |
|---|---|---|---|---|
| EPU | A policy | 1985-01 – 2007-12 | 276 | 2 (log) — see §3 |
| TPU | A policy | 1985-01 – 2007-12 | 276 | 2 (log) — see §3 |
| GPR | D geopolitical | 1985-12 – 2007-12 | 265 | 2 (log) |
| BDI realised vol | B maritime | 1988-02 – 2007-12 | 239 | 2 (log) |
| VIX [control] | E financial | 1990-12 – 2007-12 | 205 | 2 (log) |
| MOVE [control] | E financial | 2003-10 – 2007-12 | 51 ⚠ | 2 (log) |
| UCDP state-based conflicts | D geopolitical | 1985 – 2007 | 23 yr | 1 (rate ratio) |
| Billion-dollar disasters | C physical | 1985 – 2007 | 23 yr | 1 (rate ratio) |

⚠ MOVE's pre-2008 stretch is 51 months. It is retained under the spec's "longest pre-2008 stretch" clause and flagged everywhere it appears; it is not treated as a regime-change witness.

Domain F counts (Entity List, tariff presidential documents, OFAC) run 2010–2025 only. **No Great Moderation baseline exists for them, so they cannot enter E2, E3 or the break tests.** They remain §4 level evidence, as specified.

## 3. Skew test — the ruling's gap, and how it was filled

The ruling fixed the threshold (skew > 1.0 on the 1985–2007 window) but not **the object the test runs on**. The two candidates disagree:

| Series | Skew, 12m rolling mean (analysis-ready) | Skew, unsmoothed monthly level | Implied category |
|---|---|---|---|
| EPU | 0.62 | 1.60 | **disagree** — raw z vs. log |
| TPU | 0.64 | 1.57 | **disagree** — raw z vs. log |
| GPR | 1.20 | 3.92 | agree — log |

Rolling means shed skew mechanically; the smoothed object is not obviously the right test target and neither is obviously wrong. Category 3 (raw z) produces the **larger** magnitudes, so the ambiguity resolves in the thesis's favour.

**Fill applied, recorded before any exceedance was counted:** the less favourable resolution is the headline (test the unsmoothed level; EPU, TPU and GPR all → log), the more favourable is reported as specification sensitivity. This mirrors the adverse-selection discipline of the BDD registration. Effect on the headline numbers:

| | Headline (log) | Sensitivity (raw z) |
|---|---|---|
| EPU, % of 2020s beyond ±3σ | **56** | 77 |
| TPU, % of 2020s beyond ±3σ | **54** | 62 |

**This is a gap-fill by the analyst, not a ruling by the author.** It requires ratification into `ruling-transforms-e3-2026-08-28.md`; the addendum is drafted and attached separately.

## 4. Break tests — first specification failed, replaced, both reported

**Failed specification (reported, not deleted).** PELT with l2 cost on the 12-month-smoothed series, penalty `c·log(n)·var(diff)/2`, returned a break every 36 months back to 1905 — the `min_size` floor. Cause: the smoothed series have lag-1 autocorrelation of 0.988–0.998 and their first differences remain autocorrelated (ρ 0.16–0.85), so the white-noise variance estimate understates residual variance by two to three orders of magnitude (EPU: 0.011 against a series variance of 4.36). The output is an artifact of the smoother.

**Corrected specification.** Annual means of the **unsmoothed** source series, transform rule applied; l2 cost, `min_size` 5 years, `pen = c·log(n)·var(diff)/2`; headline c = 2, with c = 1 and c = 3 and a binary-segmentation cross-check all reported. Variance-to-noise ratios of 2.1–25.1 and near-zero differenced autocorrelation confirm the estimator is now behaving.

**All headline dates (PELT, c = 2), every one reported:**

| Series | Break years |
|---|---|
| EPU | 1913, 1920, 1932, 1948, 1954, 1967, 1973, **2008**, **2019** |
| TPU | 1971, 2004, **2016** |
| GPR | 1996, 2001, **2006**, **2021** |
| BDI realised vol | 2003 ⚠, **2008** |
| VIX | 1997, 2003, **2008**, 2013, **2020** |
| MOVE | 2012, **2021** |
| UCDP | 1964, 1977, 1990, 1995, 2002, 2014, **2019** |
| BDD | **2008**, **2020** |

- **2006–2010: 5 of 8 series.** **2015–2021: 7 of 8 series.** Ledger row 2's registered clustering prediction holds in both windows.
- **EPU's 1973 → 2008 gap is 35 years**, the longest in a record running to 1900 (next longest: 16). The damped era registers as an absence of breaks.
- **VIX break dates are specification-unstable:** c = 3 returns none at all, and binary segmentation returns only 1997 and 2004. Reported as unstable; §6 does not rest on them.
- ⚠ **BDI's 2003 break falls inside its own baseline window.** See §5.

## 5. BDI baseline contamination — disclosed, correction declined

A break is detected at 2003, inside the 1985–2007 baseline. The window is therefore not a clean damped-era reference for this series.

| Baseline | log-μ | log-σ | 2020s mean z |
|---|---|---|---|
| 1985–2007 (as specified, **headline**) | −1.0810 | 0.2606 | **+4.58** |
| 1985–2002 (break-clean, sensitivity) | −1.2076 | 0.1069 | +12.34 |

The correction **raises** every post-2008 magnitude. It is therefore reported and not adopted: the contaminated, wider baseline stays as headline precisely because fixing it would move the numbers toward the thesis.

**Separate honesty note for §5:** BDI realised volatility sits beyond +3σ for 88% of the 2010s and 100% of the 2020s. At full saturation the metric has stopped measuring tails and is measuring a level shift. Stated as such in the prose.

## 6. E3 results

**Continuous series — % of decade beyond ±3σ (headline units):**

| Series | 1980s | 1990s | 2000s | 2010s | 2020s |
|---|---|---|---|---|---|
| EPU | 0 | 0 | 0 | 3 | **56** |
| TPU | 0 | 0 | 0 | 29 | **54** |
| GPR | 0 | 0 | **0** | **0** | **0** |
| BDI vol | 0 | 0 | 12 | 88 | **100** |
| VIX [control] | — | 0 | 0 | 0 | **0** |
| MOVE [control] | — | — | 4 | 0 | **0** |

All 2020s exceedances are upper-tail; zero lower-tail observations in any series.

**Count series — × the 1985–2007 baseline annual rate:**

| Series | 1980s | 1990s | 2000s | 2010s | 2020s |
|---|---|---|---|---|---|
| UCDP conflicts | 1.03 | 1.10 | 0.87 | 1.12 | **1.41** |
| Billion-dollar disasters | 0.63 | 1.09 | 1.28 | 2.51 | **4.41** |

Appendix (pre-registered raw-z metric, printed in full per ruling condition 1): EPU 0/0/0/8/77; TPU 0/0/0/31/62; GPR 0/0/2/0/0; BDI vol 0/0/12/100/100; VIX —/0/8/0/0; MOVE —/—/19/0/0. Counts as |z|>3 years per decade: UCDP 0/0/0/0/1; BDD 0/0/0/5/6. **Every headline magnitude is smaller than its pre-registered counterpart**, as the caption asserts.

## 7. Ledger reconciliation

| # | Registered claim | Verdict |
|---|---|---|
| 1 | Rolling variance rises post-~2016 in a majority of long series | **Cooperates.** 4 of 6 continuous series rise 2016–2026 vs 2008–2015 (EPU +1.67, TPU +6.76, GPR +0.69, BDI +0.04); the two that fall are VIX (−0.51) and MOVE (−0.88), both controls. Both count series rise. |
| 2 | Break dates cluster ~2008 and ~2016–2020 | **Cooperates.** 5 of 8 in 2006–2010; 7 of 8 in 2015–2021. |
| 3 | >3σ counts rise by decade | **Partial — one named miss.** Rises in EPU, TPU, BDI vol and both count series. **GPR registers zero in every decade, including the 2020s.** Reported as a miss; GPR carries no census weight. |
| 4 | VIX flat over the long run | **Confirmed flat.** 2026 z = +0.06; zero exceedances in any decade. §6 conversion stands. |
| 5 | Simultaneity index elevated in the 2020s | **Weak — do not force.** Decade means 0.03 / 0.15 / 0.15 / **0.33** (full-sample percentile) and 0.13 / 0.29 / 0.21 / **0.45** (expanding). But peak months are 2002–03, the index never exceeds 0.60, and available-series count rises from 3 to 6 across the record, so cross-decade comparison is not clean. **Recommendation: E4 to appendix, not capstone.** |

**Published misses now number three:** MOVE persistence (2026-08-27), BDD exposure normalisation at RR = 1.96 (2026-08-28), and GPR's empty tail census (this run).

## 8. Deviations and limitations, disclosed regardless of direction

1. **Skew-test object was unspecified.** Filled adversely; see §3. Requires ratification.
2. **First break specification failed** and is reported rather than deleted; see §4.
3. **BDI baseline contains a break**; correction declined because it favours the thesis; see §5.
4. **MOVE baseline is 51 months.** Any MOVE z-score is a weak measurement and is used only to report a failed claim.
5. **News-index substrate is shared.** EPU, TPU and GPR are all newspaper-text indices. Their co-movement is not four independent instruments agreeing; it is at most two. No test registered, no essay claim built on their mutual confirmation. Open thread, carried forward from the 08-28 manifest.
6. **2026 is partial** (through July for index series, mid-year for counts). Excluded from all count rate computations and from E2's count panels to avoid endpoint anchoring. The GPR postwar-high claim in §6 is explicitly stated as a partial-year reading.
7. **No R `strucchange` cross-check** was run; the spec listed it as optional. Cross-checking was done with binary segmentation inside the same library, which is a weaker independence claim than a second implementation would be.

## 9. Artifacts produced

`panel_monthly_analysis_ready.csv`, `panel_annual_counts.csv`, `panel_annual_z.csv`, `panel_z_corrected.csv`, `panel_z_rawz.csv`, `panel_z_sensitivity.csv`, `transform_assignment.json`, `e3_census_headline.csv`, `e3_census_rawz.csv`, `e3_census_sensitivity.csv`, `e3_count_rate_ratios.csv`, `break_dates.json` (failed spec), `break_dates_annual.json`, `e4_simultaneity.csv`, `gprh_annual_1900_2026.csv`, `hashes.json`, and four figures: `e2_small_multiples_headline.png`, `e2_small_multiples_appendix_rawz.png`, `e3_tail_census_headline.png`, `e3_tail_census_appendix_rawz.png`.
