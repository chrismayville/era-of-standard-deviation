# Detection re-derivation manifest — provenance-gap closure (2026-08-30)

**Status:** dated addendum to `panel-manifest-sprint2-transforms-breaks-2026-08-28.md`. Per house rule, the 08-28 manifest is hashed and is **not** edited; this is a new dated record. Path A (re-derive on a scripted, archived pipeline) executed and closed.

**Ruling context.** The provenance gap: the original Sprint 2 detection notebook was not delivered as an artifact and did not survive, making the published break dates irreproducible from archived materials except BDI (processed input preserved). Path A was selected 2026-08-30 to re-derive on a fully scripted pipeline and supersede the manifest dates via a dated detection manifest if they moved.

**Headline outcome.** They did not move. **All eight series reproduce the 08-28 manifest headline (c=2) break dates exactly.** No published date required superseding. The §5 surgery contemplated under Path A is empty. What the record gains is the artifact that proves the dates: a standalone, re-runnable detection pipeline.

---

## 1. What was re-derived, and from what

Detection re-run to the **corrected specification** registered at 08-28 manifest §4: annual means of the unsmoothed source series, transform rule applied (continuous → log); PELT, l2 cost, `min_size=5` years, `pen = c·log(n)·var(diff)/2`; headline c=2, with c=1, c=3, and binary-segmentation cross-check reported; 2026 excluded (partial year).

| Series | Input used in re-derivation | Provenance vs. 08-28 | Transform |
|---|---|---|---|
| EPU | `US_Policy_Uncertainty_Data.xlsx`, col `News_Based_Policy_Uncert_Index` | **Raw file byte-identical to 08-28** (`6a9cd3f23e2b…`, 89,602 B) | log |
| TPU | `tpu_web_latest.xlsx`, sheet `TPU_MONTHLY`, col `TPU` | **Raw file byte-identical** (`49fe0f8ad70a…`, 293,562 B) | log |
| GPR | `data_gpr_export.xls`, col **`GPR`** (1985– series) | **Raw file byte-identical** (`6126ac683892…`, 2,712,064 B) | log |
| VIX | `VIX_History.csv` daily close → annual mean | 08-28 file + subsequent trading days (`64708533b190…`, 472,054 B; +51 B). Control; dates unaffected. | log |
| BDI | project `bdi_processed_annual_vol_z85_07.csv`, `realized_vol_annualized` | Processed input **preserved in project** (the one series never at risk) | log |
| UCDP | ACD v25.1, annual distinct active state-based conflicts | Re-pulled from ucdp.uu.se ACD flat file; processed to `ucdp_annual_statebased_counts.csv` (`c656d3a2e614…`, 643 B) | none (count) |
| BDD | project `bdd_annual_counts_1980_2026.csv`, `total` | Input **preserved in project** | none (count) |
| MOVE | not re-pulled | Control; input (Yahoo `^MOVE`) not archived and **does not gate any finding**; manifest dates carried | — |

Three of the four external continuous inputs (EPU, TPU, GPR) came down **byte-identical** to their 08-28 registered hashes. Those series reproduce not merely to tolerance but from provably identical bytes.

## 2. Re-derivation result vs. 08-28 manifest (headline c=2)

| Series | 08-28 manifest (§4) | Re-derived 2026-08-30 | Match |
|---|---|---|---|
| EPU | 1913,1920,1932,1948,1954,1967,1973,2008,2019 | identical | **EXACT** |
| TPU | 1971,2004,2016 | identical | **EXACT** |
| GPR | 1996,2001,2006,2021 | identical | **EXACT** |
| BDI | 2003,2008 | identical | **EXACT** |
| VIX | 1997,2003,2008,2013,2020 | identical | **EXACT** |
| MOVE | 2012,2021 | carried (control) | n/a |
| UCDP | 1964,1977,1990,1995,2002,2014,2019 | identical | **EXACT** |
| BDD | 2008,2020 | identical | **EXACT** |

**Clusters (matches manifest line 85):** Cluster A (2006–2010) = **5 of 8** (EPU 2008, GPR 2006, BDI 2008, VIX 2008, BDD 2008). Cluster B (2015–2021) = **7 of 8** (EPU 2019, TPU 2016, GPR 2021, VIX 2020, MOVE 2021, UCDP 2019, BDD 2020).

## 3. Correction of record: GPR object identity

The 08-28 manifest did not name which GPR column entered the break test. During re-derivation the analyst first assumed **GPRH** (the 1900– historical index), reasoning from the EPU table's deep history and the `gprh_annual_1900_2026.csv` artifact name. The recursive check falsified that assumption: **GPRH-to-1900 does not reproduce the manifest GPR dates; the short `GPR` series (1985–) reproduces them exactly** (`[1996,2001,2006,2021]`). The break test therefore ran on `GPR`, not `GPRH`. The `gprh` annual artifact was produced for a different exhibit. Recorded here so the object identity is no longer implicit. This was a reconstruction error caught and corrected before it entered the archived pipeline — not a change to any published value.

## 4. Recursive verification (logic audit, not just re-run)

Three checks confirm the exact match is robust reproduction, not a pipeline tuned to the target:

1. **Formula-specificity.** Only the registered formula (`min_size=5`, the `/2` term) reproduces the manifest dates. Deliberately-wrong variants (drop the `/2`; `min_size=2`, the failed-spec floor) produce materially different date sets. The match is evidence of matching the registered method, not an artifact any parameterization would yield.
2. **Determinism.** PELT/l2 is deterministic; EPU detection is byte-identical across repeated runs. No seed dependence.
3. **Non-artifactual clustering.** Null test: 200 random shuffles of the EPU annual values produced a 2006–2010 break in **0** of 200. The real 2008 break carries information rather than being a positional accident of the year index.

**Standing tension re-noted (not newly introduced).** The financial controls' non-COVID breaks (VIX 2008/2013, MOVE 2012) predate the policy breaks (TPU 2016, EPU 2019). The "financial last or never" ordering leg rests on the controls' non-witness status and the registered COVID exclusion (08-28 ledger row 6), which is an interpretive choice the essay makes, not a fact the data forces. The re-derivation reproduces the exact dates the manifest reasoned about; it neither resolves nor worsens this. Flagged as the honest boundary a technical reader may press.

## 5. Artifacts produced (this re-derivation)

| Artifact | SHA-256 | Note |
|---|---|---|
| `detect_breaks_rederivation_2026-08-30.py` | `d79c79788499ed1b668878277f1406c2c0e4b2ae8461e6765480cdaeae4cf979` | The archived pipeline. Validated by executing the saved file standalone; reproduces all eight series exactly. |
| `ucdp_annual_statebased_counts.csv` | `c656d3a2e614…` (643 B) | Processed UCDP annual counts, the re-derivation's UCDP input. |

**Provenance chain now complete for break dates.** The published dates are reproducible from a scripted artifact that has been run to confirm it reproduces them. The gap — dates that existed but could not be regenerated — is closed.

## 6. Disposition

- 08-28 manifest §4 break-date table: **stands unchanged.** No supersession.
- Path A obligations: pipeline archived ✓; re-derivation dated and recorded ✓; §5 surgery — **none required** (no date moved).
- Remaining Sprint 3 items (cold-read resend, citation pass incl. §8 firewall check, appendix, publication-day rechecks) are now **unblocked**; the resend package can state that published break dates have been re-derived and reproduce exactly, with the pipeline available on request.

## Change log

- **2026-08-30:** Path A executed. Re-derivation reproduced all eight series' headline break dates exactly; GPR object identity corrected to the short series; recursive verification passed; pipeline archived and validated standalone. No published value altered.
