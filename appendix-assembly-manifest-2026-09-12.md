# Appendix assembly manifest — GitHub release package (2026-09-12, r2)

**r2 supersedes the same-day r1** (not ratified, withdrawn): the redaction table now describes removals by class and location rather than printing removed text; the spec public copy is the recovered 08-25 version; recovered 08-25 artifacts added. See `reconstruction-of-record-2026-09-12.md`.

**Status:** dated addendum to `detection-rederivation-manifest-2026-08-30.md`. Registered files are not edited; this is a new dated record.

**Context.** The author ruled 2026-09-12 that the panel numbers in the War on the Rocks submission will link to a self-hosted public data appendix rather than to series providers. Sprint 2 output artifacts (`panel_z_corrected.csv`, `e3_census_*.csv`, `break_dates_annual.json`, `hashes.json`) and the raw provider files were removed from the project store to control its size and were not recoverable. This session re-pulled the public inputs, re-ran the archived pipeline, added a scripted record for the ratio-to-baseline figures, and assembled the release package.

## 1. Re-pull of public inputs, 2026-09-12

Provider files have moved on since the registered vintage (August 2026 observations added). None matches its registered hash; this is expected and is the reason the break test excludes the partial year.

| File | Registered SHA-256 (first 20) | 2026-09-12 SHA-256 (first 20) | Bytes | Latest observation |
|---|---|---|---|---|
| `US_Policy_Uncertainty_Data.xlsx` | `6a9cd3f23e2be5a6b03d` | `4f167dc2ed6b26081b0e` | 70,734 | 2026-08 |
| `tpu_web_latest.xlsx` | `49fe0f8ad70ad930eb92` | `f9d7c924f000fce4b03a` | 294,459 | 2026-08 |
| `data_gpr_export.xls` | `6126ac6838929a4fd2e4` | `6ff388db4aa34eb66433` | 2,714,112 | 2026-08 |
| `VIX_History.csv` | `be8fc7180260c05c955a` | `cb3515efe5577d39df5c` | 472,564 | 2026-09-11 |

UCDP annual counts: project file `ucdp_annual_statebased_counts.csv` (`c656d3a2e614…`), unchanged. BDI and BDD: project processed files, unchanged. MOVE: control, not re-pulled, manifest dates carried.

## 2. Break-date reproduction, third run

Archived pipeline `detect_breaks_rederivation_2026-08-30.py` (SHA-256 `d79c79788499ed1b668878277f1406c2c0e4b2ae8461e6765480cdaeae4cf979`, unchanged) run against the 2026-09-12 vintage. **All eight series reproduce the 08-28 manifest headline (c = 2) dates exactly.** Output archived as `break_dates_rederivation_2026-09-12.json`. This is the first reproduction on a *different* raw vintage, which rules out the possibility that the 08-30 match depended on byte-identical inputs.

## 3. Ratio-to-baseline figures — scripted record (new)

The essay's §5 figures (TPU 9.0, EPU 3.2, BDI vol 2.6, GPR 1.65, VIX 0.96) were computed in the Sprint 2 notebook and stated in the Rev6 drafting notes, but had no standalone artifact. `compute_ratios_2026-09-12.py` implements the stated definition (latest 12-month mean of the level as a multiple of the baseline-window mean; BDI on the 36-month rolling σ) and reproduces every published value at the registered endpoint:

| Series | Published (through 2026-07) | Reproduced, --end 2026-07 | Current vintage (through 2026-08) |
|---|---|---|---|
| TPU | 9.0 | 9.04 | **8.2** |
| EPU | 3.2 | 3.22 | 3.09 |
| BDI realised vol | 2.6 | 2.60 | 2.60 |
| GPR | 1.65 | 1.66 | 1.64 |
| VIX | 0.96 | 0.96 | 0.96 (through partial 2026-09) |

**Finding for the author.** TPU's twelve-month reading has moved from 9.0× to 8.2× with one added month. The essay's "9 times" is correct at the registered vintage and will drift monthly. Disposition (prose, author's): state the vintage in §5, or refresh on publication day. The appendix `results.md` carries both columns.

## 4. Public copies of registered documents — redactions

Registered files are never edited in place. Redacted public copies carry a header with the original file's SHA-256. Removals, by class and location (the exact-string log is held by the author, internal):

| File | Location | Class |
|---|---|---|
| `era-of-standard-deviation-data-panel-spec.md` (08-25 version) | front-matter tags | internal project tag |
| same | Domain F heading; build-order item 5 | internal tool name (×2) |
| same | Tooling/Storage line | cancelled internal database deliverable; note replaced with a pointer to the retirement ruling |
| `prereg-bdd-normalization-2026-08-28.md` | Registrant line | defunct entity name replaced with the author's name |
| `ruling-source-retirement-2026-08-28.md` | §2 item 2 | defunct entity name removed from a clause about a cancelled deliverable |
| `panel-pull-manifest-2026-08-27.md` | §2, two bullets | extracted values and a quoted finding from a source retired under its terms of use |
| `panel-pull-manifest-portwatch-2026-08-28.md` | front-matter tags | internal project tag |

No registered value, rule, date, verdict, or limitation was altered. Files with no redaction are byte-identical to the registered originals.

| Group | File | Original SHA-256 | Public copy SHA-256 | Redactions |
|---|---|---|---|---|
| spec | `era-of-standard-deviation-data-panel-spec.md (08-25)` | `a88332e92f9d46e69572…` | `89c379f49ad3fc8ac056…` | 4 |
| spec | `ruling-transforms-e3-2026-08-28.md` | `ca96963eb56562445da0…` | `ca96963eb56562445da0…` | 0 |
| spec | `ruling-addenda-transforms-e3-2026-08-28.md` | `de195648fa95c4930af0…` | `de195648fa95c4930af0…` | 0 |
| spec | `prereg-bdd-normalization-2026-08-28.md` | `da2227e665cf40f9958b…` | `fa364adfda5e08bb8ad9…` | 1 |
| spec | `ruling-source-retirement-2026-08-28.md` | `b898b12f55d2c794a032…` | `9c4dcd48bd36199a4b2c…` | 1 |
| manifests | `panel-pull-manifest-2026-08-27.md` | `21db4f59438557978dec…` | `cbe41e6040bc1af6436d…` | 2 |
| manifests | `panel-pull-manifest-portwatch-2026-08-28.md` | `75dccab4dcd0c228126f…` | `f0809ff638ceb727af66…` | 1 |
| manifests | `panel-manifest-sprint2-transforms-breaks-2026-08-28.md` | `1b2eb1feeac7e56792e9…` | `1b2eb1feeac7e56792e9…` | 0 |
| manifests | `detection-rederivation-manifest-2026-08-30.md` | `9cb5c86a052f275e5d30…` | `9cb5c86a052f275e5d30…` | 0 |

## 5. Recovered 2026-08-25 artifacts added to the package

`esd-pull-manifest-2026-08-25.json`, `esd_domainE_controls_2026-08-25.py`, `esd-panel-monthly-domainE_2026-08-25.csv`, `esd-domainE-controls_2026-08-25.png`. Hashes of all nine recovered files, including the MOVE and Cboe raw inputs that are *not* redistributed, are in the reconstruction record.

## 6. Excluded from the package, by rule

Project brief, essay outline, master drafts, reader copy, publication-readiness review, cold-read log, beat sheet, review addenda, strategy and method documents (reader names, an affiliation ruled internal-use only, employer context, drafting material). The redaction script and exact-string log (internal). Raw BDI monthly levels (proprietary). Climate Central raw payload (annual counts only are released, pending the sanctioned re-acquisition). Provider raw files (pull script and hashes instead). `E2draftsmallmultiples.png` (draft).

## 7. Open items before release (author)

1. Re-acquire Climate Central counts through the registered CSV export; hash and diff against `bdd_annual_counts_1980_2026.csv`.
2. Confirm licence choice: MIT for code (attached at repo creation), CC BY 4.0 for documents and figures (`LICENSES.md`).
3. Write the README front page and citation block.
4. Rule on the TPU vintage wording for §5 (§3 above).
5. Ratify the reconstruction record (r2).
6. Outside-activity disclosure filed before the repository is made public.
7. Tag the first release `v1.0`; essay links point at the tag.

## 8. Package layout and hashes

Flat layout, all files at the repository root (folder structure dropped 2026-09-12 for upload simplicity; nothing else changed).

| File | SHA-256 (first 20) | Bytes |
|---|---|---|
| `LICENSES.md` | `45c0d0fdc7cf81384719` | 2,612 |
| `README.md` | `593d8a62a81c7fa71cac` | 2,869 |
| `bdd_annual_counts_1980_2026.csv` | `e6fba2a99b6f331459f4` | 1,149 |
| `bdd_processed_z85_07.csv` | `951adc4d8e6401b3d307` | 739 |
| `bdi_processed_annual_vol_z85_07.csv` | `82984deca77e5b50fea6` | 868 |
| `bdi_rolling36m_vol_z85_07.csv` | `798c241d78d4df8a0eac` | 11,663 |
| `bea_fa_t12.csv` | `0f74c40e6047972f646b` | 18,265 |
| `break_dates_rederivation_2026-09-12.json` | `e31b28a4ac7aac2bab9e` | 3,213 |
| `compute_ratios_2026-09-12.py` | `0e7a1ebb58abb4f1f553` | 3,220 |
| `detect_breaks_rederivation_2026-08-30.py` | `d79c79788499ed1b6688` | 6,120 |
| `detection-rederivation-manifest-2026-08-30.md` | `9cb5c86a052f275e5d30` | 7,506 |
| `e1_chokepoints_headline.png` | `28acfee96a75f4d13610` | 108,737 |
| `e2_small_multiples_appendix_rawz.png` | `18f7cd06161f7bdf2c07` | 122,524 |
| `e2_small_multiples_headline.png` | `4254f85dacc52454368d` | 121,096 |
| `e3_tail_census_appendix_rawz.png` | `efe3b6fe83afedd5a523` | 79,526 |
| `e3_tail_census_headline.png` | `5311f5e5f387d20985d1` | 84,214 |
| `e4_simultaneity_appendix.png` | `7453b992a4e01d86bc3f` | 113,589 |
| `era-of-standard-deviation-data-panel-spec.md` | `89c379f49ad3fc8ac056` | 17,804 |
| `esd-domainE-controls_2026-08-25.png` | `f5ba57959c6a2f38c82a` | 308,409 |
| `esd-panel-monthly-domainE_2026-08-25.csv` | `59bc0618cde962d43e64` | 50,159 |
| `esd-pull-manifest-2026-08-25.json` | `c847b21ed2738ae9c067` | 4,059 |
| `esd_domainE_controls_2026-08-25.py` | `b1ac28d0fd2a655d7959` | 7,719 |
| `fedreg_entity_list_counts_by_year.csv` | `8d0b69445e94d34a692b` | 318 |
| `fedreg_tariff_presdoc_counts_by_year.csv` | `accf7396e9a1ee4e504b` | 157 |
| `ofac_action_counts_2010_2025.csv` | `5538baa77846906c07ac` | 225 |
| `panel-manifest-sprint2-transforms-breaks-2026-08-28.md` | `1b2eb1feeac7e56792e9` | 11,634 |
| `panel-pull-manifest-2026-08-27.md` | `cbe41e6040bc1af6436d` | 6,320 |
| `panel-pull-manifest-portwatch-2026-08-28.md` | `f0809ff638ceb727af66` | 8,653 |
| `portwatch_chokepoints_daily_2019_2026.csv` | `34591e455b41727a36c7` | 84,546 |
| `prereg-bdd-normalization-2026-08-28.md` | `fa364adfda5e08bb8ad9` | 6,702 |
| `pull_inputs.sh` | `530a61e77d83ebfc6112` | 656 |
| `reconstruction-of-record-2026-09-12.md` | `94ee5941633b48c711ab` | 8,500 |
| `results.md` | `1381d9ef3b4c667e4614` | 4,997 |
| `ruling-addenda-transforms-e3-2026-08-28.md` | `de195648fa95c4930af0` | 6,708 |
| `ruling-source-retirement-2026-08-28.md` | `9c4dcd48bd36199a4b2c` | 3,611 |
| `ruling-transforms-e3-2026-08-28.md` | `ca96963eb56562445da0` | 4,286 |
| `ucdp_annual_statebased_counts.csv` | `c656d3a2e614cf6f02e9` | 643 |
| `worldbank_global_gdp_current_usd.csv` | `a14dd8e284c705c87aaf` | 1,193 |
