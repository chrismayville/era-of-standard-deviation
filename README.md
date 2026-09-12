# The Era of Standard Deviation — data appendix

This repository holds the data, rules, and code behind The Era of Standard Deviation, an essay arguing that institutions damp variance and that their decay shows in the spread before the average. The essay claims that eight series across policy, maritime, physical, geopolitical, and financial domains left their Great Moderation range in a registered order; this is where a reader can check that claim.

The panel was specified, and its transforms and predictions written down and hashed, before any series was pulled. Every detected break date is reported, including the ones that cut against the thesis, and three registered predictions that failed are published here with the same weight as the ones that held. results.md is the place to start; the manifests carry the hashes and the pull timestamps; the scripts reproduce the headline numbers from public inputs.

## What is here

All files sit at the top level. By name:

- `results.md` — every number the essay quotes, with its registered prediction and outcome, including the three published misses.
- `era-of-standard-deviation-data-panel-spec.md`, `ruling-*.md`, `prereg-*.md` — the panel specification and the pre-registration rulings.
- `panel-pull-manifest-*.md`, `esd-pull-manifest-2026-08-25.json`, `panel-manifest-sprint2-*.md`, `detection-rederivation-manifest-*.md`, `appendix-assembly-manifest-*.md`, `reconstruction-of-record-*.md` — provenance, hashes, break tests, re-derivations, and the correction of record.
- `detect_breaks_rederivation_2026-08-30.py`, `compute_ratios_2026-09-12.py`, `esd_domainE_controls_2026-08-25.py`, `pull_inputs.sh` — the archived pipeline, the ratio computation, the Domain E controls script, and a pull script for the public inputs.
- `*.csv`, `break_dates_rederivation_2026-09-12.json` — processed series and detection output. Provider files are not mirrored; see `LICENSES.md`.
- `e1_*.png` … `e4_*.png`, `esd-domainE-controls_2026-08-25.png` — the figures at headline and appendix resolution.

## How to reproduce the headline numbers

```
sh pull_inputs.sh
python3 detect_breaks_rederivation_2026-08-30.py --raw raw --project .
python3 compute_ratios_2026-09-12.py --raw raw --project . --end 2026-07
```

The first command prints the hashes of what you pulled; compare them with the registered hashes in the manifests. Providers add months, so current files will not match byte-for-byte after August 2026; the break dates (2026 excluded) reproduce regardless, and the ratios reproduce at the registered endpoint.

## Public copies of registered documents

Registered documents are hashed and never edited in place. Five of the registered documents carry a header line stating that the copy here differs from the registered original: a small number of internal references (an access path listed as an option but never used, a cancelled internal deliverable, and values from a data source retired under its terms of use) were removed for release. Each removal is listed with the original hash in `appendix-assembly-manifest-2026-09-12.md`. No registered value, rule, date, or verdict was altered.

## A correction of record

Two governing documents exist here in a version that predates amendments recorded on 2026-08-28; the amended copies were lost. `reconstruction-of-record-2026-09-12.md` lists what was added, what survives elsewhere, and what cannot be recovered.

## Citation

Mayville, C. (2026). The Era of Standard Deviation — data appendix, v1.0. https://github.com/chrismayville/era-of-standard-deviation
