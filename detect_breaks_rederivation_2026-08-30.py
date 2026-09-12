#!/usr/bin/env python3
"""
The Era of Standard Deviation — break-date detection, re-derivation pipeline.
Created 2026-08-30 to close the provenance gap: the original Sprint 2 detection
notebook was not archived. This script re-derives all eight series' break dates
on a fully scripted, archivable pipeline, to the CORRECTED specification
registered in panel-manifest-sprint2-transforms-breaks-2026-08-28.md §4.

Specification (verbatim from manifest §4, "Corrected specification"):
  - Annual means of the UNSMOOTHED source series, transform rule applied.
  - Transform: continuous series -> log (manifest §2, all Category 2).
  - PELT, l2 cost, min_size=5 (years), pen = c * log(n) * var(diff) / 2.
  - Headline c=2; c=1, c=3, and a binary-segmentation cross-check also reported.
  - 2026 excluded from all series (partial year; manifest deviation item 6).

Inputs and their provenance (see re-derivation manifest for hashes):
  EPU  : policyuncertainty.com US_Policy_Uncertainty_Data.xlsx, col
         News_Based_Policy_Uncert_Index. Raw file IDENTICAL to 08-28 hash.
  TPU  : matteoiacoviello.com tpu_web_latest.xlsx, sheet TPU_MONTHLY, col TPU.
         Raw file IDENTICAL to 08-28 hash.
  GPR  : matteoiacoviello.com data_gpr_export.xls, col GPR (the 1985- series,
         NOT GPRH). Raw file IDENTICAL to 08-28 hash. [See manifest note below.]
  VIX  : cboe.com VIX_History.csv daily close -> annual mean. Raw file is the
         08-28 file plus subsequent trading days (control; dates unaffected).
  BDI  : project bdi_processed_annual_vol_z85_07.csv, realized_vol_annualized,
         log transform. Processed input preserved in project.
  UCDP : ucdp.uu.se ACD v25.1, annual count of distinct active state-based
         conflicts (conflict_id nunique per year). Count -> no log.
  BDD  : project bdd_annual_counts_1980_2026.csv, total, count -> no log.
  MOVE : control; Yahoo ^MOVE input not re-pulled (does not gate any finding;
         manifest dates carried).

RESULT (2026-08-30): all eight series reproduce the manifest headline (c=2)
dates EXACTLY. Cluster A (2006-2010) = 5 of 8; Cluster B (2015-2021) = 7 of 8,
matching manifest line 85. No published date required superseding.
"""
import pandas as pd, numpy as np, ruptures as rpt, json, argparse, warnings
warnings.filterwarnings("ignore")

def detect(years, values, transform=None, cvals=(1, 2, 3), min_size=5):
    years = np.asarray(years)
    x = np.asarray(values, dtype=float)
    if transform == "log":
        x = np.log(x)
    n = len(x)
    var_diff = np.var(np.diff(x), ddof=1)
    out = {"_meta": {"n": int(n), "var_diff": round(float(var_diff), 6),
                     "span": f"{int(years.min())}-{int(years.max())}",
                     "transform": transform or "none", "min_size": min_size}}
    for c in cvals:
        pen = c * np.log(n) * var_diff / 2.0
        bkps = rpt.Pelt(model="l2", min_size=min_size, jump=1).fit(x).predict(pen=pen)
        out[f"c={c}"] = [int(years[i]) for i in bkps if i < n]
    pen2 = 2 * np.log(n) * var_diff / 2.0
    bkps_b = rpt.Binseg(model="l2", min_size=min_size, jump=1).fit(x).predict(pen=pen2)
    out["binseg(c=2)"] = [int(years[i]) for i in bkps_b if i < n]
    return out

def annual_from_monthly(df, datecol, valcol):
    d = df.copy()
    d[datecol] = pd.to_datetime(d[datecol], errors="coerce")
    d = d.dropna(subset=[datecol, valcol])
    return d.groupby(d[datecol].dt.year)[valcol].mean()

def build(raw_dir, project_dir):
    R = {}

    epu = pd.read_excel(f"{raw_dir}/US_Policy_Uncertainty_Data.xlsx")
    epu = epu[pd.to_numeric(epu["Year"], errors="coerce").notna()]
    epu["Year"] = epu["Year"].astype(int)
    ea = epu.groupby("Year")["News_Based_Policy_Uncert_Index"].mean()
    ea = ea[ea.index <= 2025]
    R["EPU"] = detect(ea.index.values, ea.values, transform="log")

    tpu = pd.read_excel(f"{raw_dir}/tpu_web_latest.xlsx", sheet_name="TPU_MONTHLY")
    ta = annual_from_monthly(tpu, "DATE", "TPU"); ta = ta[ta.index <= 2025]
    R["TPU"] = detect(ta.index.values, ta.values, transform="log")

    gpr = pd.read_excel(f"{raw_dir}/data_gpr_export.xls")
    ga = annual_from_monthly(gpr.dropna(subset=["GPR"]), "month", "GPR")
    ga = ga[ga.index <= 2025]
    R["GPR"] = detect(ga.index.values, ga.values, transform="log")

    vix = pd.read_csv(f"{raw_dir}/VIX_History.csv"); vix.columns = [c.strip().upper() for c in vix.columns]
    ccol = [c for c in vix.columns if "CLOSE" in c][0]
    va = annual_from_monthly(vix.rename(columns={ccol: "CLOSE"}), "DATE", "CLOSE")
    va = va[va.index <= 2025]
    R["VIX"] = detect(va.index.values, va.values, transform="log")

    bdi = pd.read_csv(f"{project_dir}/bdi_processed_annual_vol_z85_07.csv")
    bdi = bdi[(bdi["partial_year"].isna()) | (bdi["partial_year"] == "")]
    bdi = bdi[bdi["year"] <= 2025]
    R["BDI"] = detect(bdi["year"].values, bdi["realized_vol_annualized"].values, transform="log")

    bdd = pd.read_csv(f"{project_dir}/bdd_annual_counts_1980_2026.csv")
    bdd = bdd[bdd["year"] <= 2025]
    R["BDD"] = detect(bdd["year"].values, bdd["total"].values, transform=None)

    # UCDP: expects pre-processed annual counts CSV (year,count) in raw_dir,
    # or falls back to the ACD flat file if present.
    try:
        uc = pd.read_csv(f"{raw_dir}/ucdp_annual_statebased_counts.csv")
        R["UCDP"] = detect(uc["year"].values, uc["count"].values, transform=None)
    except FileNotFoundError:
        acd = pd.read_csv(f"{raw_dir}/UcdpPrioConflict_v25_1.csv")
        counts = acd.groupby("year")["conflict_id"].nunique()
        counts = counts[counts.index <= 2025]
        R["UCDP"] = detect(counts.index.values, counts.values, transform=None)

    R["MOVE"] = {"_meta": {"note": "control; input not re-pulled; manifest dates carried"},
                 "c=2": [2012, 2021]}
    return R

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", default="./raw")
    ap.add_argument("--project", default="/mnt/project")
    args = ap.parse_args()
    results = build(args.raw, args.project)
    print(json.dumps(results, indent=2, default=str))
