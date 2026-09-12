# Reconstruction of record — lost amendments to governing files (2026-09-12, r2)

**Status:** dated addendum; correction of record. **Supersedes the same-day r1 draft**, which was delivered but not ratified and is withdrawn. r1 stated that the registered ordering's text and timing were unrecoverable; an archive recovered later the same day shows that both survive. **Requires author ratification.**

## 1. Finding

The 2026-08-28 close batch recorded delivery of amended copies of four governing files (spec, Sprint 2 manifest, brief, outline). The copies in the project store, and the copies the author first located, hash to earlier versions and contain none of the described amendments. The amended 08-28 copies remain unrecovered.

| File | Amended hash recorded 08-28 | Project-store copy | 
|---|---|---|
| `panel-manifest-sprint2-transforms-breaks-2026-08-28.md` | `d2bc65f5ad51…` | `1b2eb1feeac7…` (pre-amendment) |
| `era-of-standard-deviation-data-panel-spec.md` | `a07b83f5eb94…` | `d7234dd110eb…` (08-20 original) |
| `era-of-standard-deviation-project-brief.md` | `0433e494df3e…` | `6439aea8cf9a…` (08-25 original) |
| `era-of-standard-deviation-essay-outline.md` | `462d4b55e497…` | `89203805b107…` (08-25 original) |

## 2. Recovery, same day

An archive of 2026-08-25 session deliverables (`SDEV2.zip`, nine files) was located by the author after r1 was drafted. Hashes:

| File | SHA-256 | What it is |
|---|---|---|
| `era-of-standard-deviation-data-panel-spec.md` | `a88332e92f9d46e695727776cf9a020ccf7022f994816aaf85b8e06643656da0` | Spec **updated 2026-08-25** — carries design principle 6 (the registered damper-decay ordering) and the firewall reconciliation |
| `era-of-standard-deviation-essay-outline.md` | `abfb8b922d4355c93c5836ac8434fe67678cce61868f7b1ccac740ba84e1a869` | Outline **updated 2026-08-25** — carries ledger row 6 and the 08-25 ledger status |
| `esd-domainE-controls.png` | `f5ba57959c6a2f38c82af0d720fe7317af4fd1381bd8b358f5837d19a88a4824` | Domain E figure, 08-25 |
| `esd-manifest.json` | `c847b21ed2738ae9c0678a6e90aaa7b7c1962df94cf082c30cfc81c40c180ce7` | 08-25 pull manifest: EPU/TPU/GPR/PortWatch/VIX/MOVE hashes, pull timestamps, **registration timestamp** |
| `esd-panel-monthly-domainE.csv` | `59bc0618cde962d43e64877b1bbbb41e98f8f2514c4df2849a9176fd56e15e80` | Domain E monthly panel (VIX, MOVE) as built 08-25 |
| `esd_domainE_controls.py` | `b1ac28d0fd2a655d795997c14a8e560c61320d9569097886ad942b593b3b458e` | Domain E controls script, 08-25 |
| `move_yahoo.json` | `20b02dc3ebf8fba3a9839c8c23d8e7c6fe13c31c6dff853c6c798378a7daa6d3` | MOVE raw, monthly 2002-12–2026-08 (the input the 08-30 manifest lists as not archived) |
| `move_yahoo_daily2y.json` | `c45ac6123551e93dfde485b983f3d6d07b207168298a89378b1cc72c528ae06b` | MOVE raw, daily last two years |
| `vix_cboe.csv` | `c8534f6e3362140d2169e4e674aac0069e26bd300bc2efffaa1d0944df1cdda5` | Cboe VIX daily history as pulled 08-25 (matches the 08-25 manifest hash) |

The EPU, TPU and GPR hashes in the 08-25 manifest (`6a9cd3f2…`, `49fe0f8a…`, `6126ac68…`) are identical to those the 08-28 manifest registered and the 08-30 re-derivation confirmed. The raw inputs are the same bytes from the first pull through the re-derivations.

## 3. What was lost, what is recovered, what remains lost

| Item (per 08-28 batch) | Status after recovery |
|---|---|
| Spec design principle 6 "restored with provenance" | **Recovered verbatim** in the 08-25 spec. The 08-28 batch's "restored" implies the principle had dropped out of a later working copy and was put back; the 08-25 text is the original registration. |
| Spec Objection 2 ordering sentence | **Recovered** — the 08-25 spec's Objection 2 carries the added sentence generalising the VIX conversion to the decay ordering. |
| Spec retirement annotations, storage note struck, Amendments section | Retirement substance in `ruling-source-retirement-2026-08-28.md`; storage note struck in the public copy by logged redaction; Amendments section text **not recovered**. |
| Manifest ledger row 6 (registered ordering) | **Recovered verbatim** — it lives in the 08-25 outline's falsification ledger (below). The 08-28 manifest cited it; it did not originate it. |
| Manifest retirement paragraph; addenda ratification pointer | Substance preserved in the standalone ruling and addenda files (hashes match). |
| Manifest deviation 8; change log | **Not recovered.** |
| Brief: deliverable 4 struck; references to a defunct entity removed; Amendments | Substance known from the 08-28 batch; text **not recovered**. Brief is internal and not part of the release. |
| Outline: target-length amendment; Rev5-governs note | Substance known; text **not recovered**. Outline is internal and not part of the release. |

## 4. The registered ordering — text and timing

**Ledger row 6, 08-25 outline, verbatim:**

| 6 | Break dates respect the pre-registered decay ordering (TPU/EPU first; maritime 2023–24, persisting rather than V-recovering; GPR gradual; VIX unbroken, MOVE before VIX if finance cracks). COVID-window (2020–21) breaks excluded as common shock. | If violated — e.g., GPR breaks before TPU, or chokepoints V-recover fast, or VIX breaks while MOVE doesn't — report it plainly; the mechanism claim weakens even if aggregate variance rises. Retreat from "staggered damper failure" to "variance rising, sequence unclear." |

**Design principle 6** is printed in full in `era-of-standard-deviation-data-panel-spec.md` (public copy of the 08-25 spec).

**Timing, from `esd-pull-manifest-2026-08-25.json`:**

| Event | UTC timestamp |
|---|---|
| Pulls 1–3 (EPU, TPU, GPR) | 2026-08-25 22:34:47 |
| Ordering registered (spec principle 6 + outline ledger row 6) | **2026-08-25 22:51:15** |
| Pull 4 (PortWatch chokepoints) | 2026-08-25 22:52:42 |
| Pulls 5–6 (VIX, MOVE) | 2026-08-25 23:04:35 |

The 08-25 manifest's own note: *"registered after pulls 1-3, before this PortWatch pull."* The registration's honesty note (in principle 6) states that legs (a)–(b) were dated from public events already known and that the policy series were already in hand; what registration added was the series-to-damper mapping, the recovery-shape claim for the maritime leg, the flat-series and COVID rules, and the financial-domain sequence. The essay's §5 says the same.

r1's stated boundary — that surviving files could not establish the intra-day sequence — is withdrawn. The sequence is timestamped by the pull manifest written at the time.

**08-25 ledger status, verbatim (records the MOVE-persistence miss on the day it was observed):**

**Ledger status (2026-08-25, after pulls 1–5 of ~10):** Rows 1 & 3 — partial previews from Tier 1 (EPU/TPU emphatic; GPR zero 3σ months in any decade but at a 24-year high and climbing — reported, not dropped). Row 4 — **resolved: VIX flat.** The only 3σ episode in 36 years is the GFC; during the Hormuz closure it peaked at 31, spent two days above 30, and was back under 20 in thirteen trading days; it now sits below its 36-year mean. Keep the sleeping-VIX conversion. Row 6 — maritime leg: persistence confirmed and escalated out-of-sample (Hormuz closed Mar 2026, BeM making new lows in Aug 2026; Panama recovered to ~97% — the conflict/climate asymmetry gets reported). Financial leg: VIX-unbroken confirmed under maximal live fire; the registered MOVE-stays-elevated sub-claim **failed** (MOVE normalized to 2010s levels; spiked +57% with the war, round-tripped in five days) — the essay reports the miss. Rows 2 & 5 — open pending break tests and the full panel.

## 5. Disposition for the release package

1. The public spec is now the **08-25 version** (four logged redactions: internal tag, internal tool name ×2, cancelled deliverable note). The 08-20 original is superseded for release.
2. The 08-25 pull manifest, Domain E script, panel and figure are added to the package. MOVE and Cboe raw files are **not** redistributed; their hashes are recorded here and in the 08-25 manifest.
3. The Sprint 2 manifest remains the pre-amendment public copy, with this record beside it. Deviation 8 and the change log stay marked not recovered.
4. Going forward: close batches land in the project store in the same turn, and the store is the copy of record.

## 6. Author ratification

[ ] Ratified as a correction of record — Chris Mayville, date: ________

Open question for the author, if memory serves: the subject of deviation 8.
