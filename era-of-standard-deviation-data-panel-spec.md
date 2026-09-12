<!-- PUBLIC COPY of the spec as updated 2026-08-25 (design principle 6 registered). Original SHA-256 a88332e92f9d46e695727776cf9a020ccf7022f994816aaf85b8e06643656da0. 4 redaction(s) applied for release, listed in manifests/appendix-assembly-manifest-2026-09-12.md and the reconstruction record. No registered value, rule, or date was changed. -->

---
title: Era of Standard Deviation — Data Panel Spec
created: 2026-08-20
updated: 2026-08-25 (firewall reconciliation; damper-decay ordering registered as design principle 6)
tags: [scrm, essay, data-spec, variance]
status: draft
---

# Era of Standard Deviation — Data Panel Spec

## Purpose and claim

The essay's testable proposition: **institutions are variance dampers, and institutional decay shows up in the second moment before the first.** Averages hold while tails widen. The evidence standard is *simultaneity* — rolling variance rising at the same time across domains with no common mechanism (policy, maritime, climate, conflict). Any single series can be argued with; the panel cannot.

Baseline: the **Great Moderation, 1985–2007** — an era economists literally named for its low variance. The claim is not "unprecedented chaos"; it is **exit from a damped regime**.

## Design principles

1. **Measure the second moment, not levels.** Rolling σ, coefficient of variation, tail counts — never raw levels as the headline.
2. **Baseline σ comes from the damped era only.** If you compute σ over the full sample, recent volatility inflates the denominator and mechanically hides tail growth. All z-scores and 3σ thresholds use 1985–2007 statistics (or the series' longest pre-2008 stretch).
3. **Two tiers of series, two treatments.**
   - **Tier 1 — direct uncertainty gauges** (EPU, TPU, GPR, WUI): these already measure dispersion of expectations. Use levels, smoothed.
   - **Tier 2 — outcome series** (freight rates, transits, losses, conflict counts): compute rolling σ or CV yourself.
4. **Include an adversarial control and publish it.** The VIX will probably *not* show a secular rise. That is not a problem — it is the sharpest point in the essay (see Objections).
5. **Simultaneity is the thesis.** The capstone metric is "how many sensors are red at once," not any single series.
6. **Pre-registered damper-decay ordering** *(registered 2026-08-25 — after pulls 1–3 (EPU/TPU/GPR), before pulls 4–10)*. Dampers do not decay in unison, so variance should escape in a sequence matching which institutions failed first. Registered ordering, dated by public institutional events: **(a) trade/policy first** — §232/§301 actions from 2018, WTO Appellate Body paralysis Dec 2019 → TPU/EPU break first and hardest. Already visible in pulls 1–3, so this leg is postdiction at the level of levels; its testable content is formal break dates (transform 4) aligning with the Domain F event dating. **(b) Maritime commons 2023–24** — Red Sea campaign from Dec 2023, Gatún drought restrictions 2023–24, no fast institutional restoration → forward claim for the PortWatch pull: chokepoint throughput enters a depressed/volatile regime that *persists* rather than V-recovers; freight-rate variance is noisy corroboration only (demand shocks confound it). **(c) Broad geopolitical, gradual** — GPR elevated and climbing without wartime tails. **(d) Financial last or never** — VIX flat (principle 4); within finance, MOVE moves first as the fiscal/monetary-doubt gauge. **Flat-series rule:** a flat series counts *for* the thesis only where Domains F/G independently show its damper functioning (capitalized, legitimate, active); otherwise it counts against. **COVID rule:** 2020–21 breaks are a common exogenous shock hitting every domain at once — report them, label them, exclude them from the ordering test (they demonstrate simultaneity, not staggered decay). Honesty note: legs (a)–(b) are dated from public events already known; what registration adds is the series→damper mapping, the recovery-shape claim, the flat-series and COVID rules, and the financial-domain sequence.

---

## The panel

### Domain A — Policy & institutional (Tier 1)

| Series | Provider / access | Freq | Span | Notes & caveats |
|---|---|---|---|---|
| US Economic Policy Uncertainty (Baker–Bloom–Davis) | policyuncertainty.com — free Excel/CSV | Monthly | 1985– (news-based historical to 1900) | The workhorse. Media-volume normalization handled by authors. |
| Global EPU (GDP-weighted) | policyuncertainty.com | Monthly | 1997– | Shorter; use as corroboration. |
| Trade Policy Uncertainty (Caldara–Iacoviello, Fed Board) | matteoiacoviello.com/tpu.htm — free | Monthly | 1960– | Newspaper-based. Directly on-thesis for trade. |
| World Uncertainty Index (Ahir–Bloom–Furceri) | worlduncertaintyindex.com — free | Quarterly | ~1990– | Different text corpus (EIU reports) → robustness check on EPU. Optional. |
| Global Trade Alert — new harmful interventions/yr | globaltradealert.org — free w/ registration | Annual | 2009– | Starts 2009, early reporting lag. Cannot show pre-2008 baseline — use as level evidence of rules erosion, not in the variance panel. |

### Domain B — Maritime & trade (Tier 2)

| Series | Provider / access | Freq | Span | Notes & caveats |
|---|---|---|---|---|
| Chokepoint transits: Suez, Bab el-Mandeb, Panama, Hormuz, Malacca | IMF PortWatch (portwatch.imf.org) — free download | Daily | 2019– | AIS-based, short history. Powers Exhibit 1, not long-run variance claims. |
| Drewry World Container Index (composite) | drewry.co.uk — composite is public | Weekly | 2011– | Compute 52-wk rolling CV (level trends, so CV not σ). |
| Freightos Baltic Index (FBX) | freightos.com — charts free, download may need account | Daily | ~2017– | Backup/corroboration for WCI. |
| Baltic Dry Index | Official feed paywalled; via TradingView / investing.com free tier (personal account) | Daily | 1985– | **The one freight series spanning the Great Moderation** — worth the access hassle. Annual realized vol of daily log changes; monthly averages are an acceptable fallback for 36-month rolling σ. |
| Marine war-risk premia | No clean public series. Proxy: Joint War Committee Listed Areas revision count/yr (Lloyd's/LMA circulars) + reported point quotes from trade press | — | — | Narrative garnish, not a chart. The insurance market's *priced* estimate of variance. |

### Domain C — Physical & climate (Tier 2)

| Series | Provider / access | Freq | Span | Notes & caveats |
|---|---|---|---|---|
| Insured natural-catastrophe losses (inflation-adj.) | Swiss Re Institute sigma — free reports, extract the long table | Annual | 1970– | Primary loss series (economically verified). Also compute losses as % of global GDP (World Bank) to kill the exposure-growth objection. |
| Billion-Dollar Disasters | **Climate Central** (climatecentral.org / climate.us) — continuation of the retired NOAA database, same methodology, led by the former NOAA program lead | Annual | 1980– | NOAA retired it May 2025; Climate Central revived it months later. The hand-off itself is a narrative beat: variance-damping *and sensing* capacity migrating out of government. CPI-adjusted, not exposure-adjusted — say so. |
| EM-DAT global disasters | CRED / UCLouvain — free for non-commercial, registration | Annual | 1900– | Severe reporting bias pre-1980. Restrict to 1980+, and prefer insured losses as primary. |
| Panama: Gatún levels + transit slots | ACP publications; PortWatch for daily transits | Daily/Monthly | varies | Your existing Gatún tracking slots directly in. |

### Domain D — Geopolitical & conflict

| Series | Provider / access | Freq | Span | Notes & caveats |
|---|---|---|---|---|
| Geopolitical Risk Index (Caldara–Iacoviello) | matteoiacoviello.com/gpr.htm — free | Monthly (daily recent) | 1900– | Tier 1. **This is the series that answers "the 1970s felt the same"** — plot the 70s and show them. |
| UCDP/PRIO armed conflicts (state-based) | ucdp.uu.se — free | Annual | 1946– | Recent years at post-WWII highs. Count series → decade comparison. |
| ACLED political violence events | acleddata.com — free w/ access agreement | Event-level | Global coverage mature only ~2018– | Coverage expansion inflates trends. Use within-region post-coverage windows only, or skip for the essay. |

### Domain E — Adversarial controls (financial)

| Series | Provider / access | Freq | Span | Notes & caveats |
|---|---|---|---|---|
| VIX | FRED (VIXCLS) or CBOE VIX_History.csv direct — free | Daily | 1990– | Expect flat long-run. Publish it anyway — see Objections §2. Resolved 2026-08-25: flat confirmed — the only 3σ episode in 36 years is the GFC; peaked 31 during the Hormuz closure and round-tripped in 13 trading days. |
| MOVE (bond vol) | Yahoo (^MOVE) | Monthly 2002-12– free (daily for recent windows) | 2002-12– (free) | Was elevated 2022–23 (~119 vs ~71 in the 2010s); normalized to 2010s levels by 2025–26 — the persistent contrast with VIX did not survive the data. Baseline 2002-12–2007 is thin (61 obs); flag wherever z is shown. Publish as control alongside VIX. |

### Domain F — Own sensors (Federal Register plumbing)

| Series | Source | Notes |
|---|---|---|
| BIS Entity List additions/yr | Federal Register API (federalregister.gov/api) — count EAR final rules + entities added | Institutional *output* frequency — the mechanism series linking "institutional change" to "trade variance." |
| OFAC SDN additions/yr | OFAC change logs / archived lists | Same. |
| FCC Covered List additions | Published list w/ dates | Small n, pure step function. The July 2026 inverter expansion is your live regime-shift example. |
| §232/§301 + tariff proclamations/yr | Federal Register + USTR | Policy variance you can literally count. |

### Domain G — Damper legitimacy (mechanism series, not variance series)

The testable core of "crisis era" claims: is the dampers' legitimacy declining? These are **level** series measuring the *input* to damping capacity (legitimacy → compliance → capacity). Keep them out of the variance panel and break tests; use them as the causal link in the essay — Domains F/G show damping capacity falling, Domains A–D show variance escaping, Domain E shows where the dampers still hold.

| Series | Provider / access | Freq | Span | Notes & caveats |
|---|---|---|---|---|
| Pew: Public Trust in Government | pewresearch.org — free, aggregated from multiple polls | Periodic | 1958– | US federal; high-70s% mid-1960s → low-20s% now. The single most famous damper-legitimacy series. |
| Gallup: Confidence in Institutions | news.gallup.com — free | Annual | 1973– | 15+ institutions (Congress, presidency, courts, press, military). Broad decline; military the partial outlier. US-centric. |
| V-Dem institutional indices | v-dem.net — free download | Annual | 1789– | Expert-coded institutional quality, cross-country, very long history. Methodological debates over expert coding — use aggregate indices, note the caveat. |
| OECD Trust Survey | oecd.org — free | ~Biennial | 2021– (older *Government at a Glance* series to ~2006) | Cross-country corroboration that this isn't purely a US story. Short history. |

---

## Transforms

1. **Ingest & align.** Common grain: monthly. Daily series → within-month realized volatility (std of daily log changes). Weekly → 52-week rolling window, sampled monthly. Annual series (Swiss Re, UCDP, GTA) stay annual and feed Exhibit 3 / decade tables, not the monthly panel.
2. **Tier treatment.** Tier 1: 12-month rolling mean of the index level. Tier 2: 36-month rolling σ, or rolling CV (σ ÷ mean over same window) where the level trends — freight, loss series.
3. **Baseline standardization.** Per series: compute mean and σ over 1985–2007 (or longest pre-2008 stretch). Z-score the whole series against that baseline. Flag any series whose entire history is post-2008 (PortWatch, WCI, FBX, GTA) — they illustrate the current regime but **cannot testify to regime change**; keep them out of the break tests.
4. **Break detection.** PELT changepoint detection on each transformed series (`ruptures`, Python); robustness cross-check with Bai–Perron (`strucchange`, R). Report every detected date, including ones that don't fit the story — expect clustering around ~2008 and ~2016–2020.
5. **Tail census.** Count |z| > 3 observations per decade per series, σ from baseline era only. Annualize the partial 2020s.
6. **Simultaneity index.** Monthly share of panel series above their own 90th percentile of the transformed measure. Document the percentile choice: full-sample (simpler, mild lookahead — fine for an essay, footnote it) vs expanding-window (cleaner, noisier early).
7. **Optional — variance co-movement.** Average pairwise correlation of the variance series, 5-year rolling window. Rising co-movement = variance turning systemic, not idiosyncratic.

## Exhibits

**E1 — The hook.** Suez/Bab el-Mandeb and Panama daily transits overlaid, 2019–present (PortWatch). Annotate: Houthi campaign begins Dec 2023; Gatún drought slot restrictions 2023–24; recovery paths. Caption angle: two of the world's four great maritime shortcuts impaired at once — one by conflict, one by climate — and no institution restored either quickly.

**E2 — The evidence.** Small multiples: 6–8 long series (US EPU, TPU, GPR, BDI realized vol, Swiss Re losses/%GDP, billion-dollar disaster count, UCDP conflicts, MOVE), each z-scored to its Great Moderation baseline, GM window shaded. Caption angle: none of these measures the same thing; all of them bend the same direction.

**E3 — The takeaway.** Grouped bar chart: >3σ events per decade across the panel, 1980s → 2020s (annualized). The general-reader chart — one glance, no statistics required.

**E4 (optional capstone).** Simultaneity index line, 1990–present: "how many sensors are red at once." This is the chart that operationalizes *institutional decay = correlated variance*.

## Objections & controls (write these into the essay, don't wait for comments)

1. **"The 1970s were worse."** GPR runs from 1900 — show the 70s explicitly. Frame: we are *re-entering an undamped regime* after an anomalously damped one. More defensible and more interesting than "unprecedented."
2. **"If volatility is rising, why is the VIX asleep?"** Publish the VIX as a control. Interpretation: equities sit inside the one domain whose variance damper is intact and well-capitalized (central banks, deep option markets). Institutions damp variance where they still function — the flat VIX is *evidence for* the damper theory, not against the thesis. The variance is entering through the physical and policy layers, where the dampers are failing. The decay ordering (design principle 6) generalizes this conversion: dampers fail in sequence, the flat VIX is the predicted last domino, and within finance MOVE cracks first.
3. **Reporting/coverage bias.** EM-DAT pre-1980 and ACLED expansion inflate naive trends. Restrict windows; prefer economically verified series (insured losses).
4. **Exposure growth.** More stuff in harm's way raises losses at constant hazard. Normalize by global GDP; note that the disaster databases CPI-adjust but do not exposure-adjust.
5. **Endpoint bias.** The 2021 container spike is a tail event inside a long series, not a trendline anchor. Always show full history.
6. **σ vs regime shift.** State plainly that several series show step-changes (Covered List additions, tariff proclamations, FEOC designations), not just fatter dispersion — that's the distinction that breaks buffer math and motivates sensing over stockpiling.

## Build order

1. **Afternoon one:** EPU + TPU + GPR — three free downloads, one notebook, first small-multiples draft. Momentum matters.
2. PortWatch chokepoints → E1 draft.
3. Freight: WCI (+ FBX); chase BDI long history via TradingView / investing.com free tier; monthly averages fallback.
4. Physical: Swiss Re sigma table (manual extract), Climate Central BDD, EM-DAT pull.
5. Institutional counts: UCDP, GTA, Federal Register API (Entity List / OFAC / tariff actions).
6. Controls: VIX (FRED), MOVE (Yahoo). *(Pulled 2026-08-25, ahead of order — live-fire test of ordering leg (d) after the Hormuz closure.)*
7. Transforms + breaks + exhibits notebook.

**Tooling:** Python (pandas, matplotlib, `ruptures`); optional R `strucchange` cross-check. **Storage:** [struck — the database deliverable was cancelled 2026-08-28; see `ruling-source-retirement-2026-08-28.md`]

## Essay packaging notes

- Working titles: *The Era of Standard Deviation*; *After the Great Moderation, Everywhere*; *The End of the Average World*.
- Hamant is the frame, not the crutch: open with the biology, land on the design shift (robustness over performance), close on what a practitioner does differently. The data panel is the spine between.
- The NOAA → Climate Central hand-off earns one paragraph: the sensor was decommissioned as the variance rose, and civil society picked it up — observability degrading exactly when it matters, which is one of your own scores.
- **Strauss–Howe ruling:** the Fourth Turning mood gets at most one clause as zeitgeist, never a citation as evidence — unfalsifiable, historians reject it, and the Bannon association is byline risk in serious venues. The citable lineage for "stability erodes the capacity to handle instability" is Minsky (financial instability hypothesis), Olson (*Rise and Decline of Nations*), and Turchin (structural-demographic theory) — plus Domain G, which converts the crisis-era intuition into measurable damper legitimacy.
