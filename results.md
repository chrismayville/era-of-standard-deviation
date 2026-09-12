# Results table

Headline values as published. Registered vintage: index series through 2026-07, counts through 2025. Baseline window is 1985–2007 (or each series' longest pre-2008 stretch, as recorded in `panel-manifest-sprint2-transforms-breaks-2026-08-28.md` §2). Every value below traces to a manifest in this repository; the scripts in `` reproduce the break dates and the ratios from public inputs.

## Latest reading as a multiple of the series' Great Moderation average

| Series | Domain | Baseline window | Registered vintage (2026-07) | Recheck 2026-09-12 (through 2026-08) | Registered prediction | Outcome |
|---|---|---|---|---|---|---|
| Trade policy uncertainty (TPU) | Policy | 1985-01 – 2007-12 | **9.0** | 8.2 | Rises; leads maritime | Holds |
| US economic policy uncertainty (EPU) | Policy | 1985-01 – 2007-12 | **3.2** | 3.1 | Rises | Holds |
| Baltic Dry realised volatility (36-month σ) | Maritime | 1988-02 – 2007-12 | **2.6** | 2.6 | Rises; follows policy | Holds — and saturates (see tail census) |
| Geopolitical risk (GPR) | Geopolitical | 1985-12 – 2007-12 | 1.65 | 1.64 | Rises gradually | Level rises; **tail census empty in every decade** (published miss) |
| VIX (control) | Financial | 1990-12 – 2007-12 | **0.96** | 0.96 | Flat over the long run | Holds — registered as a possible falsification, came back flat |
| MOVE (control) | Financial | 2003-10 – 2007-12 (51 months ⚠) | 0.85 | not rechecked | Elevated and persistent post-2021 | **Miss:** rose after 2021, then subsided |

## Count series — decade rate as a multiple of the 1985–2007 annual rate

| Series | Domain | 2010s | 2020s | Registered prediction | Outcome |
|---|---|---|---|---|---|
| UCDP active state-based conflicts | Geopolitical | 1.12 | **1.41** | Rises gradually | Holds; 2024 = 61, series maximum since 1946 |
| Billion-dollar US disasters (Climate Central, CPI-adjusted threshold) | Physical | 2.51 | **4.41** | Rises | Under the price-level threshold, rises. Under the registered exposure-normalised test the rate ratio is **1.96 against a pre-registered bar of 2.0: indeterminate** (published miss; see `prereg-bdd-normalization-2026-08-28.md`) |

## Share of each decade beyond ±3σ of the baseline (headline units)

| Series | 1980s | 1990s | 2000s | 2010s | 2020s |
|---|---|---|---|---|---|
| EPU | 0 | 0 | 0 | 3 | **56** |
| TPU | 0 | 0 | 0 | 29 | **54** |
| GPR | 0 | 0 | 0 | 0 | **0** |
| BDI realised vol | 0 | 0 | 12 | 88 | **100** |
| VIX (control) | — | 0 | 0 | 0 | **0** |
| MOVE (control) | — | — | 4 | 0 | **0** |

All 2020s exceedances are upper-tail. The pre-registered raw-z metric (larger in every cell) is printed in the 08-28 manifest §6 and in `e3_tail_census_appendix_rawz.png`.

## Structural break dates (PELT, l2, min_size 5 years, c = 2; annual means of unsmoothed series; 2026 excluded)

| Series | Break years |
|---|---|
| EPU | 1913, 1920, 1932, 1948, 1954, 1967, 1973, **2008**, **2019** |
| TPU | 1971, 2004, **2016** |
| GPR | 1996, 2001, **2006**, **2021** |
| BDI realised vol | 2003 ⚠ (inside baseline; disclosed, correction declined because it would favour the thesis), **2008** |
| VIX (control) | 1997, 2003, **2008**, 2013, **2020** (specification-unstable; no claim rests on them) |
| MOVE (control) | 2012, **2021** |
| UCDP | 1964, 1977, 1990, 1995, 2002, 2014, **2019** |
| Billion-dollar disasters | **2008**, **2020** |

Clusters: 2006–2010, 5 of 8 series; 2015–2021, 7 of 8. Registered prediction holds. EPU's 1973→2008 gap (35 years) is the longest in a record running to 1900.

Reproduced exactly three times: 2026-08-28 (original run), 2026-08-30 (archived pipeline, byte-identical raw inputs), 2026-09-12 (archived pipeline, current provider vintage — see `appendix-assembly-manifest-2026-09-12.md`).

## Ordering registration

The per-leg ordering (policy first, maritime as recovery shape, geopolitical gradual, financial last or never with the 2020–21 pandemic breaks excluded) was recorded as ledger row 6 of the 08-28 manifest. The amended copy holding that row was lost; its content is reconstructed from surviving files and its timing boundary is stated plainly in `reconstruction-of-record-2026-09-12.md`.

## Published misses

1. MOVE persistence (registered 2026-08-27): rose after 2021, then subsided.
2. Billion-dollar disasters under exposure normalisation (registered 2026-08-28): RR 1.96 against a bar of 2.0. Indeterminate, not confirmed.
3. GPR tail census (2026-08-28): zero months beyond ±3σ in every decade including the 2020s.

## Registered limitations

Recorded in the 08-28 manifest §8 and carried here: the skew-test object was filled adversely by the analyst and ratified by addendum; the first break specification failed and is reported, not deleted; EPU, TPU and GPR share a newspaper-text substrate and are at most two independent instruments, not three; MOVE's baseline is 51 months; 2026 is a partial year and is excluded from all count computations.
