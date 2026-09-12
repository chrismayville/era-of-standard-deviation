# Standing ruling — panel transforms and the E3 metric

**Ruled 2026-08-28 by author. Registered before the Sprint-2 transform notebook runs.**

## Problem

The spec's transform 5 (tail census) counts `|z| > 3` observations per decade with σ from the 1985–2007 baseline, applied uniformly. Gaussian z-scores presume an approximately symmetric reference distribution. Several panel series are not:

- **Count series** (BDD, UCDP, Entity List additions, tariff presidential documents, OFAC actions) are Poisson-like — variance ≈ mean, bounded below at zero. BDD baseline: μ=5.22, σ=2.33, √5.22=2.28. A z of +9.8 implies ~1-in-10²² under a normal distribution but ~1-in-10¹² under Poisson — a rarity claim borrowed from a distribution the data does not follow, and zero sits only 2.24σ below the mean, so sigma units are not symmetric.
- **Volatility series** (BDI realized vol, VIX, MOVE) are bounded at zero and right-skewed. BDI baseline μ≈0.3475, σ≈0.103 puts absolute zero at −3.4σ: a floor 3.4 sigmas down against an unbounded ceiling. Untransformed z of +10.8 (2008) becomes ≈ +5.1 in logs.

## Ruling

**1. E3 primary metric = transform-appropriate.** The corrected metric is the published exhibit. The pre-registered raw-z version moves to the data appendix, **printed in full, not summarized**.

**2. Transform rule — fixed by series property, no per-series discretion.**

| Series property | Transform | Applies to |
|---|---|---|
| Count / event-frequency | **Rate ratio** vs. 1985–2007 baseline rate ("×baseline") | BDD, UCDP, Entity List, tariff presdocs, OFAC |
| Continuous, bounded at zero, right-skewed | **Natural log**, then z vs. baseline log-mean/log-σ | BDI realized vol, VIX, MOVE |
| Continuous, approximately symmetric | **Raw z** unchanged | (per skew test below) |

**3. Skew test — pre-specified, not eyeballed.** Series not obviously in category 1 or 2 (notably EPU, TPU, GPR) are assigned by testing the **1985–2007 baseline window only**: if sample skewness > 1.0, treat as category 2 (log). Otherwise category 3 (raw z). The test runs on the baseline window so the assignment cannot be influenced by the post-2008 data the essay is arguing about. Assignment is recorded for every series before results are read.

**4. §5 prose uses corrected units only.** "×baseline rate" for counts; log-sigma for volatility. **No raw sigma appears in the essay body.** Mixed units in prose re-opens the ruling by the back door.

**5. Caption carries the disclosure.** E3 travels — it will be screenshotted and lifted into decks detached from the appendix. The correction must travel with the artifact. Caption template:

> Counts are stated as multiples of the 1985–2007 baseline rate; volatility series in log units. The pre-registered raw z-score version, and why it was replaced, appear in the appendix. **The correction reduces every magnitude shown.**

The final clause is load-bearing: it tells a skeptical reader the direction of the change before they can wonder about it.

## Rationale

Both available options survive a hostile read. Option A (raw z primary, robustness secondary) protects the process claim marginally better but costs E3 its job — it is the one-glance general-reader exhibit, and two panels in competing units is not that. Option B was chosen because **every correction moves the numbers away from the thesis** (9.8σ → 5.4× baseline; 11.8σ → ≈5σ). A metric change that halves the author's own effect size, prints the original alongside it, and states the direction on the exhibit is close to unfalsifiable as evidence of good faith.

## Conditions that make this a rule rather than a preference

- The appendix must be **complete** — the raw-z E3 in full. The caption only functions if what it points to exists.
- The skew test is **pre-specified above** and runs on the baseline window only.
- This file is hashed **before** the transform notebook runs.

## Scope

Governs E3, the tail census, and §5 prose units. Does **not** govern E2 small multiples (baseline-z small multiples remain as specified; revisit only if a series' shape makes the panel misleading), break detection (PELT/Bai–Perron operate on the transformed series per the rule above), or the simultaneity index.
