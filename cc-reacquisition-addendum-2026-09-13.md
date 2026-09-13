# Climate Central counts — re-acquisition addendum (2026-09-13)

**Status:** dated addendum to `panel-pull-manifest-2026-08-27.md` §3 (Climate Central billion-dollar disasters). Correction of provenance, not of data.

## Why

The 08-27 pull took the annual event counts from the public time-series page's embedded chart data by session fetch, because the CSV export was registration-gated. Climate Central's terms of use permit non-commercial reproduction with attribution, but treat automated extraction from the site as screen scraping and prohibit it. The access path, not the data, was the problem.

## What was done

The author registered for the export on the billion-dollar-disasters time-series page and downloaded the CSV through the sanctioned route on 2026-09-13.

| Item | Value |
|---|---|
| File | `time-series.csv` (Climate Central export) |
| SHA-256 | `69296fb6d88c7e6c62b3…` |
| Rows | 47 (1980–2026, 2026 partial) |
| Columns used | `count_drought` … `count_winter-storm` (7 categories) |
| Columns not used | `Total Cost (Billions)`, `rolling5yrAvgCostMillions`, `combinedCostPerEventMillions` — cost fields; the panel uses counts only |

## Result

Year-by-year, category-by-category comparison against `bdd_annual_counts_1980_2026.csv` (the panel file built from the 08-27 pull): **no differences** across 47 years × 8 columns (seven categories plus total). 2026 partial-year total is 12 in both.

## Disposition

- The panel counts file stands unchanged; its provenance is now the registered export, and the 08-27 page-payload pull is superseded as the source of record.
- The export file itself is not redistributed; the counts are, with attribution and a link to the source page, under Climate Central's non-commercial terms.
- The `LICENSES.md` row for Climate Central is cleared of its "status to confirm" flag.
- No result, exhibit, or essay figure changes.

Attribution: Billion-Dollar Weather and Climate Disasters, Climate Central (continuation of the NOAA NCEI database), https://www.climatecentral.org/climate-services/billion-dollar-disasters. Accessed via registered export, 2026-09-13.
