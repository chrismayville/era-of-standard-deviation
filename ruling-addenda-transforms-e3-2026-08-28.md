# Addenda to the standing ruling — panel transforms and the E3 metric

**Cut 2026-08-28 from the Rev3.1 session record. Ratified by author 2026-08-28.**

**Parent:** `ruling-transforms-e3-2026-08-28.md`, SHA-256 `ca96963eb56562445da0…`, hashed before the Sprint-2 transform notebook ran. **The parent file is not modified** — its hash is the pre-registration claim and stands. This file supplements it and carries its own hash. The Sprint-2 manifest (`panel-manifest-sprint2-transforms-breaks-2026-08-28.md`, §3 and §8 item 1) recorded that ratification was required; this is that ratification.

---

## The gap

Parent ruling condition 3 fixed the skew test's **threshold** (sample skewness > 1.0, computed on the 1985–2007 baseline window only) but not the **object** the test runs on. Two candidates disagree for the two series the test exists to classify:

| Series | Skew, 12m rolling mean (analysis-ready) | Skew, unsmoothed monthly level | Implied category |
|---|---|---|---|
| EPU | 0.62 | 1.60 | disagree — raw z vs. log |
| TPU | 0.64 | 1.57 | disagree — raw z vs. log |
| GPR | 1.20 | 3.92 | agree — log |

The choice decides the headline census: EPU's 2020s share beyond ±3σ is 56% under log and 77% under raw z; TPU's is 54% and 62%.

## The provisional fill (analyst, pre-outcome)

Recorded in the Sprint-2 manifest §3 **before any exceedance was counted**: the less favourable resolution (unsmoothed level → EPU, TPU, GPR all log) taken as headline; the more favourable (raw z) reported as specification sensitivity. Mirrors the adverse-selection discipline of the BDD registration. The manifest stated in terms: *"This is a gap-fill by the analyst, not a ruling by the author. It requires ratification."*

## Addendum A1 — proposed default: adverse selection as standing rule

**Status: REJECTED by author.** Rationale for rejection: adverse selection is the correct rule only where no direction-independent argument exists. Where one exists, "I picked the number I liked least" is weaker epistemology than "I picked the correct measurement and printed both." A standing adverse-selection default would also let a future analyst substitute conservatism for analysis.

## Addendum A3′ — ruled: merits first, bracket where merits are exhausted

1. **Test object = the unsmoothed monthly level.** Grounds, all direction-independent:
   - The transform decision selects a **measurement scale** (identity vs. log), which is a property of the underlying quantity, not of the smoother. EPU and TPU are nonnegative ratio-scale indices; a 12-month mean of a nonnegative series is still nonnegative, so smoothing sheds skew mechanically (0.62 vs. 1.60) without changing the support. The smoothed object passing a symmetry test is the mask, not the answer.
   - Raw z returns **TPU +41.2σ** as a live reading. Under the Gaussian reference that raw z asserts, that is a ~1-in-10³⁶⁸ event; the correct inference from observing one is **model failure, not rarity**. A broken measurement, not a large one. This argument selects log regardless of which side log favours.
2. **Where merits are exhausted, publish the bracket.** The 41σ argument is dispositive in the far tail and does not reach the ±3σ threshold, where both reference models are rough but defensible. The threshold counts therefore publish as ranges, adverse end first: EPU 3–8% (2010s) and 56–77% (2020s); TPU 29–31% and 54–62%. The interval is the finding, not whichever end the author would prefer to quote.
3. **Prose prefers transform-invariant expression.** The §5 E2 walk states ratios to the series' own baseline mean (9.0×, 3.2×, …), which no standardisation choice can move. Sigma stays where it does statistical work: the exhibits and the census.

**Timing disclosure, load-bearing.** This ratification postdates the computed results. It **left the pre-outcome fill's headline unchanged** (log, the adverse end) and changed only the presentation of the threshold counts — from headline-plus-buried-sensitivity to an explicit range in the body, which is additional disclosure. At no point did a headline number move toward the thesis, and both the fill and the ratification are in the record.

## Addendum C — E2 publishes in transform-rule units

Parent ruling scope excluded E2: *"baseline-z small multiples remain as specified; **revisit only if a series' shape makes the panel misleading**."* The condition is met on the ruling's own terms:

- Under the ruled assignments, a raw-z E2 would display the +41σ reading the parent ruling's rationale classifies as a broken measurement.
- A raw-z E2 beside a log-unit E3 would have the two headline artifacts disagreeing about which months sit beyond 3σ (e.g., GPR's 2000s), which is the definition of a misleading panel; and parent condition 4 already forbids the prose from bridging them.

E2 therefore publishes in transform-rule units, labelled on the exhibit. The pre-registered raw-z E2 prints **in full** in the appendix (`e2_small_multiples_appendix_rawz.png`), mirroring E3's treatment under parent condition 1.

## Addendum D — E4 to the appendix, composition published, post-hoc element disclosed

Ledger row 5 registered: *"If not [elevated]: cut E4, do not force it."* The result came back weak: decade means 0.33 (full-sample percentile) / 0.45 (expanding); peak months 2002–03; the index never exceeds 0.60; and the available-series count rises from 3 to 6 across the record, so cross-decade comparison is composition-confounded.

Row 5's "cut" conflicts with the ledger's own global rule — *non-cooperating results get reported, not dropped*. **Ruled:** the global rule governs. E4 moves to the appendix rather than being cut, with per-panel series composition published, and it carries no claim in the essay body.

**Post-hoc disclosure, required:** the registered demotion trigger was the weak result. The construct-validity framing (composition confound) was articulated **after** the data was seen. It is true, and it is post-hoc, and it is disclosed as both — otherwise the stated reason would pretend the demotion was not outcome-triggered.

## Conditions

- This file is hashed at creation; the hash is recorded in the batch manifest of the session that lands it.
- The parent ruling file remains byte-identical to its pre-notebook hash.
- One pointer line is added to `panel-manifest-sprint2-transforms-breaks-2026-08-28.md` (§3 and §8) referencing this file; that edit lands in the same batch as the source-retirement reconciliation paragraph so the manifest is touched once.
- Nothing in the Rev4 draft changes as a result of this file: it records the decisions the draft already implements.
