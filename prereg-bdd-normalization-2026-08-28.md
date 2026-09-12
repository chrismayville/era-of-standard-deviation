<!-- PUBLIC COPY. Original registered file SHA-256 da2227e665cf40f9958bc7c6118babd8d4fc8d8ab8e98cd65e412c82c3344864. 1 redaction(s) applied for release; each is listed in appendix-assembly-manifest-2026-09-12.md. No registered value, rule, or date was changed. -->

# Pre-registration — BDD constant-relative-significance threshold test

**Registered:** 2026-08-28, before retrieval of event-level Climate Central data and before retrieval of any denominator series.
**Registrant:** Chris Mayville. Public sources only.
**Status at registration:** no event-level costs computed; no denominator series in hand.

---

## 1. Problem being tested

The Climate Central BDD count series uses a threshold of $1B CPI-adjusted to 2026 dollars. CPI adjustment removes currency debasement but **not exposure growth**. A fixed real-dollar threshold applied against a growing real capital stock mechanically raises event counts at constant physical hazard. Swiss Re's own decomposition (sigma 1/2026) attributes >80% of the long-term rise in global weather-related insured losses (1970–2025) to exposure growth.

This test asks whether the rise in event frequency survives holding the threshold at **constant relative significance** to the size of the exposed economy.

## 2. Threshold definition

For year *t* and anchor year *a*:

```
T(t) = $1.0B (2026 dollars) x  D(t) / D(a)
```

where `D` is a real denominator series (below). An event in year *t* is counted if its CPI-adjusted cost (2026 dollars, as published) is greater than or equal to `T(t)`.

`T(a) = $1.0B` by construction. Because `D` grows, `T(t)` rises in real terms after the anchor year.

## 3. Denominators — both run, adverse result headlined

- **D1 (concept-preferred):** BEA real net stock of fixed assets, private + government, chained dollars (BEA Fixed Assets Table 1.2 or equivalent). Disasters destroy capital stock, not annual output.
- **D2 (accessible proxy):** US real GDP, annual, chained dollars (FRED `GDPCA`).

**Adverse-selection rule, binding:** if D1 and D2 produce different verdicts under Section 6, **the less favorable result is reported as the headline** and the more favorable one appears as the sensitivity. This rule is registered before either series is retrieved.

## 4. Anchor years and censoring

Anchors run at **1980, 1985, 1990**. Primary is **1985**, for consistency with the panel's Great Moderation baseline discipline.

**Censoring, stated in advance:** for any year *t* earlier than the anchor, `T(t) < $1.0B`, and the required sub-billion events are absent from the source dataset. Those years are therefore **censored and excluded from all counts and charts**, not reported as low counts.

- Anchor 1980: no censoring; full 1980–2025 record usable.
- Anchor 1985: 1980–1984 censored. Does not affect the 1985–2007 baseline or the 2016–2025 comparison window.
- Anchor 1990: 1980–1989 censored.

## 5. Comparison windows

- Baseline: **1985–2007** (Great Moderation), mean annual count under `T(t)`.
- Comparison: **2016–2025**, mean annual count under `T(t)`.
- Rate ratio `RR` = comparison mean / baseline mean.
- **2026 excluded** from all rate computations (partial year). Reported separately as partial, never annualized.

## 6. Success / failure conditions — fixed before the pull

Under the primary specification (D1, anchor 1985):

| Outcome | Condition | Disposition |
|---|---|---|
| **Survives** | RR >= 2.0 | Exposure objection substantially answered on the source's own data. §5 may use the normalized series. |
| **Indeterminate** | 1.5 <= RR < 2.0 | Reported as indeterminate. No directional claim either way. BDD demoted to corroborating role only. |
| **Fails** | RR < 1.5 | Recorded as a **miss** in the falsification ledger and reported in the essay alongside the MOVE persistence miss. BDD drops out of E3 entirely. |

The indeterminate band is registered deliberately so that a middling result cannot be graded on a curve after the fact.

## 7. Reporting rules

- **Full grid published:** 2 denominators x 3 anchors = 6 cells, all six printed regardless of outcome, with censoring noted per cell.
- **No post-hoc category filtering.** Severe storm and hail events are the types most inflated by exposure growth and will not be dropped. Breakdown by hazard type is reported as a diagnostic only.
- Raw event-level artifact hashed (SHA-256) at retrieval; denominator series hashed at retrieval; query and retrieval date recorded verbatim in the data appendix.

## 8. Known biases, disclosed regardless of outcome

1. **Loss-estimation methodology improved over the record.** The 2012 NCEI expert review (Smith and Katz, 2013) corrected an underestimation bias in earlier assessments. Older events may be systematically under-costed, therefore under-counted, therefore the measured rise is somewhat exaggerated. This bias runs **toward** the thesis and is not correctable here.
2. **National normalization understates the problem.** Exposure grew fastest where hazards land — coasts and the wildland-urban interface — not uniformly across the national capital stock. This bias runs **against** the thesis.
3. **CPI is the wrong deflator for replacement cost.** Construction costs have generally outpaced CPI. A construction-cost re-deflation is a separate robustness pass, not performed here; it would cut **against** the thesis.

## 9. Ceiling on the claim

Even a surviving result licenses only: *the frequency of loss events of constant relative significance has risen.* It does **not** license a claim about rising physical hazard variance. BDD remains an exposure-inclusive, institutional measure of how often a loss large enough to matter occurs. Registered here so the framing cannot be widened after a favorable number.

Regardless of outcome, BDD is **not load-bearing** in E3. The series carrying the tail-census argument are those with no exposure denominator beneath them: GPR, EPU, TPU, BDI realized volatility, UCDP.

## 10. Contamination disclosure

During a 2026-08-28 feasibility check of the Climate Central events page, rendered event costs for approximately 2018–2026 were visible in the fetched page text before truncation. No values were recorded, transcribed, or computed, and no pre-2018 events were seen. The 1980–2017 record — which is where this test binds — was not observed prior to this registration. Disclosed for completeness.

## 11. Open and NOT covered by this registration

The panel-wide transform question (Gaussian z-scores on count and volatility series; log and rate-ratio alternatives) remains **unruled**. This registration governs the BDD normalization test only and does not settle E3's metric definition.
