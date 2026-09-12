# The Era of Standard Deviation — data appendix

[Author's front page. One or two paragraphs in the author's words: what this is, what it supports, and the one-sentence statement that the panel was specified and its rules hashed before any series was pulled.]

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

[Author to add: essay citation once published; repository release tag.]
