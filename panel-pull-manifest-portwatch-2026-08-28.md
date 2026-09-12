<!-- PUBLIC COPY. Original registered file SHA-256 75dccab4dcd0c228126f6527ca04cdd8dcc854be2a6c43bd081e865554c6c664. 1 redaction(s) applied for release; each is listed in appendix-assembly-manifest-2026-09-12.md. No registered value, rule, or date was changed. -->

---
title: Panel pull manifest — IMF PortWatch chokepoint transits (E1)
created: 2026-08-28
tags: [scrm, essay, manifest, portwatch, E1]
status: pull executed, E1 built (headline + appendix)
companions: [era-of-standard-deviation-data-panel-spec, era-of-standard-deviation-essay-outline, era-of-standard-deviation-master-draft-rev3]
---

# PortWatch chokepoint transits — pull, processing, and E1

## 1. Provenance

- **Registered query** (data panel spec, Domain B): "Chokepoint transits: Suez, Bab el-Mandeb, Panama, Hormuz, Malacca — IMF PortWatch (portwatch.imf.org) — free download — Daily — 2019–." Registration unchanged; this is a re-pull, not a new specification.
- **Access path of record.** The public HTML download is an ArcGIS Hub wrapper. Data taken from the underlying feature service, which is the same product: ArcGIS Online item `3da2b9ca97684916b75c4013f95d18ab`, owner `IMF-portwatch_imf_dataviz`, service `Daily_Chokepoints_Data/FeatureServer/0`. Paginated at the service's 1,000-record limit.
- **Raw artifact:** `portwatch_chokepoints_raw.json` — SHA-256 `100cd224a677f7c30ed94d7941f31f129946009e7ab7b15b5de29eaa3bcdb1d1`
- **Retrieved:** 2026-08-28. **Vintage:** data through 2026-08-23.
- **Coverage:** 16,752 rows. Six chokepoints × 2,792 daily observations, 2019-01-01 → 2026-08-23, **zero gaps**.
- **Series pulled:** the five registered chokepoints (Suez, Bab el-Mandeb, Panama, Hormuz, Malacca) plus **Cape of Good Hope**, added at pull time as the diversion counterpart to Suez. The addition is disclosed rather than silent; it is presentation, not a panel series, and enters no test.
- **Firewall:** clean. Public IMF endpoint, no login, no employer path.
- **Prior pull superseded.** An earlier PortWatch pull was executed in a previous session and its raw file is not recoverable. Nothing from it is carried forward; every figure below comes from this vintage. Any prior finding stated from memory (including a "% of 2022 baseline" framing) is **not** treated as on the record.

## 2. Panel status

PortWatch is a short-history series under design principle 2. It **illustrates the current regime, powers E1, and enters no break test, no tail census, and no baseline standardization.** Nothing here touches §5 or the falsification ledger.

## 3. Processing

- Field used: `n_total` (daily transit calls, all vessel classes).
- 7-day and 30-day trailing means computed; E1 plots the 30-day.
- **Indexing to each chokepoint's own 2019 calendar-year mean.** This is a **post-registration presentation choice**, made after the data was visible, and it is labelled as such on the exhibit. It is not a registered transform and no claim rests on it: the unindexed counts are published alongside in the appendix exhibit and in `portwatch_chokepoints_daily_2019_2026.csv`. 2019 is used because it is the only full pre-Covid year in the series, not because of anything observed in it.

**Files:**
- `portwatch_chokepoints_raw.json` — raw service response
- `portwatch_chokepoints_daily_2019_2026.csv` — daily transit calls, wide
- `portwatch_chokepoints_7dma.csv`, `e1_index2019_30dma.csv` — smoothed and indexed
- `e1_period_means.csv` — period means table
- `e1_chokepoints_headline.png`, `e1_chokepoints_appendix_raw.png`

## 4. Data-quality findings, disclosed

- **Panama, 26 Jan – 2 Feb 2020: an AIS artifact.** Daily calls run 65, 102, 82, 95, 75, 126, 93, 70 against a 2019 mean of 32 and a physical lock capacity around 36–38. These values are not achievable and are a source defect. **Left uncorrected in the data and annotated on the exhibit.** It sits outside every annotation window and affects no claim.
- **Cape of Good Hope** shows 50 days above 2.5× its 2019 mean, all post-2023. These are consistent with the rerouting and are not treated as artifacts.
- **Hormuz records twelve zero-transit days**, all after 2026-03-04. Real, not missing data.

## 5. Findings

Mean daily transit calls, as a share of each chokepoint's own 2019 average:

| | 2019 | 2022 | 2024 | 2025 | 2026 YTD | last 30 days |
|---|---|---|---|---|---|---|
| Suez Canal | 100 | 128 | 75 | 73 | 78 | 78 |
| Bab el-Mandeb | 100 | 125 | 61 | 63 | 65 | **53** |
| Panama Canal | 100 | 104 | 83 | 97 | 101 | 91 |
| Strait of Hormuz | 100 | 135 | 132 | 124 | 32 | **7** |
| Malacca Strait | 100 | 122 | 131 | 138 | 133 | 127 |
| Cape of Good Hope | 100 | 91 | 181 | 186 | **190** | 187 |

1. **The Hormuz closure is datable to the day.** 26 Feb: 89 transits. 27 Feb: 64. 28 Feb: 57. 1 Mar: 20. 2 Mar: 4. 4 Mar: zero. A four-day collapse. Current run-rate is **4.9 transits a day against a 2025 average of 85.5** — about 6 percent.
2. **Suez has not recovered for 31 consecutive months.** Every month from February 2024 through August 2026 sits below 85 percent of its 2019 average, in a 66–81 percent band. There is no trend back toward the line.
3. **Bab el-Mandeb is at its series minimum right now** — 53 percent of 2019, lower than anything in the 2024 collapse.
4. **The rerouting is directly measured.** Cape of Good Hope transits run at 190 percent of 2019 and have not come down.
5. **Malacca is the control and it is fine** — 133 percent of 2019. The impairment is specific, not a global maritime slowdown.
6. **Panama recovered fully and is bending again.** 2026 to date is 101 percent of 2019, against a January 2024 trough of 59 percent. The last 30 days are at 91 percent, consistent with the renewed draft and slot restrictions §9 describes.

## 6. Reconciliation against the draft — three items

**(a) §9's causal sequence is wrong. Correction required.**

§9 reads: *"When the attacks paused in late 2025, the ships crept back… Then a war in the Gulf closed Hormuz, the campaign around Bab el-Mandeb resumed, and the first recovery did not get a year."* This implies the Gulf war ended the Red Sea recovery. It did not.

What the series shows: Bab el-Mandeb bottoms at **56 percent on 16 July 2025**, recovers to a peak of **71 percent on 26 November 2025**, falls back to 61 percent by end-December — **two months before the 28 February strike** — then **holds in the high 60s straight through the Gulf war**, and only collapses to its 53 percent series low from **late July 2026**, when the embargo campaign reached the strait.

So: the creep-back was real, partial (it never exceeded 71 percent of 2019), and lasted about four months. It reversed before the war, recovered again during the war, and was killed five months after the war began by a separate campaign. The Gulf war closed Hormuz and left Bab el-Mandeb roughly where it found it.

This is worse for the reader's tidy narrative and **better for the hysteresis argument**: the recovery was shallow and short, and the thing that ended it was a new shock rather than the continuation of an old one. Recorded as a correction that ran against the drafted text.

**(b) §9's Hormuz figure needs updating.** "3 transits vs ~85/day normal" was close. The accurate current statement is about **five a day against a 2025 average of eighty-five**. The 85 checks out exactly.

**(c) §1's simultaneity claim survives, with a precision note.** Panama was already degrading through the autumn — 84 percent of 2019 by end-October 2023, 71 percent by end-November — while Bab el-Mandeb was still running at 141 percent. Bab el-Mandeb crosses below its 2019 level in **the last week of December 2023**. So the two were not impaired on the same date; they became concurrently impaired in the last weeks of December. §1's *"In the last weeks of 2023, two of the four great shortcuts… failed at the same time"* is defensible as written, because the last weeks of 2023 is exactly when the overlap begins. Worth one word of care at the citation pass so it cannot be read as claiming a coincident failure date.

**(d) §1's Cape sentence can now carry a number.** *"Ships that had planned on Suez went around the Cape"* — Cape of Good Hope transits are at 190 percent of 2019 and have stayed there for two and a half years.

## 7. Open

- E1 caption to be written against final venue style.
- The appendix exhibit includes Malacca and Cape of Good Hope; whether both survive to publication is an exhibit-count decision deferred to the comprehensive edit.
- WOTR cut allows two exhibits (E2, E3 headline). E1 is a master-only exhibit unless that ruling changes.
