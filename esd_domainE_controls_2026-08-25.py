#!/usr/bin/env python3
"""
Era of Standard Deviation -- Domain E adversarial controls (pulled ahead of build
order after Hormuz closure: live-fire test of decay-ordering leg (d)).
VIX: Yahoo ^VIX daily 1990- (FRED 503 at pull time; same CBOE index).
MOVE: Yahoo ^MOVE monthly closes 2002-12- (Yahoo caps range=max at monthly);
      daily last 2y for the war window. Baseline 2002-12..2007-12 = THIN (61 obs).
"""
import hashlib, json, datetime as dt
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

RAW, OUT = Path("raw"), Path("out")
def sha256(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

vix_d = pd.read_csv(RAW/"vix_yahoo_daily.csv", parse_dates=["date"]).set_index("date")["vix"]
mv = json.load(open(RAW/"move_yahoo.json"))["chart"]["result"][0]
move_m = pd.Series({pd.Timestamp(dt.datetime.fromtimestamp(t, dt.timezone.utc).date()): c
                    for t, c in zip(mv["timestamp"], mv["indicators"]["quote"][0]["close"]) if c is not None},
                   name="MOVE").sort_index()
move_m.index = move_m.index.to_period("M").to_timestamp()  # month start
mvd = json.load(open(RAW/"move_yahoo_daily2y.json"))["chart"]["result"][0]
move_d = pd.Series({pd.Timestamp(dt.datetime.fromtimestamp(t, dt.timezone.utc).date()): c
                    for t, c in zip(mvd["timestamp"], mvd["indicators"]["quote"][0]["close"]) if c is not None},
                   name="MOVE_daily").sort_index()

vix_m = vix_d.resample("MS").mean()
vs, ms = vix_m.rolling(12, min_periods=12).mean(), move_m.rolling(12, min_periods=12).mean()
vb = vs.loc["1990-01":"2007-12"]; vz = (vs - vb.mean())/vb.std(ddof=1)
mb = ms.loc["2002-12":"2007-12"]; mz = (ms - mb.mean())/mb.std(ddof=1)

print("=== decade means (VIX: daily-close mean | MOVE: monthly-close mean) ===")
for lab, lo, hi in [("1990s","1990","1999"),("2000s","2000","2009"),("2010s","2010","2019"),
                    ("2020s","2020","2026"),("2026 YTD","2026","2026")]:
    v = vix_d.loc[lo:hi].mean()
    m = move_m.loc[lo:hi].mean() if hi >= "2003" else float("nan")
    print(f"{lab:8s} VIX {v:5.1f}   MOVE {m:6.1f}")

print("\n=== smoothed z: max per decade, |z|>3 months per decade ===")
for name, z in [("VIX", vz), ("MOVE(thin base)", mz)]:
    for lo, hi in [("1990","1999"),("2000","2009"),("2010","2019"),("2020","2026")]:
        zz = z.loc[lo:hi].dropna()
        if len(zz): print(f"{name:16s} {lo}s: max z {zz.max():+5.2f}  |z|>3 months: {int((zz.abs()>3).sum())}")
    print(f"{name:16s} latest z: {z.dropna().iloc[-1]:+.2f}")

print("\n=== war window (pre-war close 2026-02-27) ===")
pre_v, pre_m = vix_d.loc["2026-02-27"], move_d.loc["2026-02-27"]
w_v, w_m = vix_d.loc["2026-02-27":], move_d.loc["2026-02-27":]
for nm, s, pre, hi1, hi2, back in [("VIX", w_v, pre_v, 30, 40, 20), ("MOVE", w_m, pre_m, 120, 140, 100)]:
    pk, pkd = s.max(), s.idxmax()
    after = s.loc[pkd:]; rt = after[after < back]
    rt_days = (rt.index[0]-pkd).days if len(rt) else None
    print(f"{nm}: pre-war {pre:.1f} | peak {pk:.1f} on {pkd:%Y-%m-%d} ({pk/pre-1:+.0%}) | "
          f"days>{hi1}: {int((s>hi1).sum())} | days>{hi2}: {int((s>hi2).sum())} | "
          f"back<{back} after {rt_days}d | latest {s.iloc[-1]:.1f}")
print(f"context: VIX 1990-2026 mean {vix_d.mean():.1f}; MOVE 2010s mean {move_m.loc['2010':'2019'].mean():.1f}, "
      f"2022-23 mean {move_m.loc['2022':'2023'].mean():.1f}, 2024 {move_m.loc['2024'].mean():.1f}, "
      f"2025 {move_m.loc['2025'].mean():.1f}, 2026 YTD {move_m.loc['2026'].mean():.1f}")

# ---- chart: three panels ----
fig, axes = plt.subplots(3, 1, figsize=(10.5, 11))
ax = axes[0]
ax.axvspan(pd.Timestamp("1990-01-01"), pd.Timestamp("2008-01-01"), color="#d9e8d9", alpha=0.7, zorder=0)
ax.axhline(0, color="#999", lw=0.8); ax.axhline(3, color="#bb4444", lw=0.8, ls=":"); ax.axhline(-3, color="#bb4444", lw=0.8, ls=":")
zz = vz.dropna(); ax.plot(zz.index, zz.values, lw=1.1, color="#1f3b5c")
ax.set_title("VIX, 1990– — the adversarial control (z vs 1990–2007 baseline, 12-mo smoothed)", loc="left", fontsize=10.5)
ax.set_ylabel("z"); ax.margins(x=0.01)

ax = axes[1]
ax.axvspan(pd.Timestamp("2002-12-01"), pd.Timestamp("2008-01-01"), color="#d9e8d9", alpha=0.7, zorder=0)
ax.plot(move_m.index, move_m.values, lw=1.1, color="#7a4a2e")
ax.axhline(mb.mean(), color="#999", lw=0.8, ls="--")
ax.text(pd.Timestamp("2003-06-01"), mb.mean()+4, f"pre-2008 baseline mean {mb.mean():.0f} (thin: 61 obs)", fontsize=8, color="#666")
ax.set_title("MOVE (bond volatility), monthly closes, 2002– — level", loc="left", fontsize=10.5)
ax.set_ylabel("index"); ax.margins(x=0.01)

ax = axes[2]
vi = (w_v/pre_v*100); mi = (w_m/pre_m*100)
ax.plot(vi.index, vi.values, lw=1.3, color="#1f3b5c", label="VIX")
ax.plot(mi.index, mi.values, lw=1.3, color="#7a4a2e", label="MOVE")
ax.axhline(100, color="#999", lw=0.8)
for d_, lab in [("2026-03-02","war / Hormuz closed"), ("2026-04-08","ceasefire"),
                ("2026-04-18","re-closure"), ("2026-07-26","BeM blockade")]:
    ax.axvline(pd.Timestamp(d_), color="#b0413e", lw=0.8, ls="--")
    ax.text(pd.Timestamp(d_), ax.get_ylim()[1]*0.98, " "+lab, fontsize=7.5, color="#b0413e", rotation=90, va="top")
ax.set_title("The live-fire test: VIX and MOVE indexed to Feb 27, 2026 = 100", loc="left", fontsize=10.5)
ax.set_ylabel("index (pre-war = 100)"); ax.legend(fontsize=9, frameon=False); ax.margins(x=0.01)
fig.suptitle("Domain E — financial dampers: the controls, published as promised", fontsize=12, x=0.02, ha="left")
fig.tight_layout(rect=[0,0,1,0.96])
fig.savefig(OUT/"esd-domainE-controls.png", dpi=150)

# ---- tidy + manifest ----
tidy = pd.concat([
    pd.DataFrame({"date": vix_m.index, "series": "VIX", "level": vix_m.values,
                  "smooth12": vs.reindex(vix_m.index).values, "z_vs_gm": vz.reindex(vix_m.index).values}),
    pd.DataFrame({"date": move_m.index, "series": "MOVE", "level": move_m.values,
                  "smooth12": ms.reindex(move_m.index).values, "z_vs_gm": mz.reindex(move_m.index).values}),
]).dropna(subset=["level"])
tidy.to_csv(OUT/"esd-panel-monthly-domainE.csv", index=False)

man_p = Path("/mnt/user-data/outputs/esd-manifest.json")
man = json.loads(man_p.read_text())
man["series"]["VIX"] = {"label":"CBOE VIX daily closes (Yahoo ^VIX; FRED VIXCLS 503 at pull time — same index, re-verify against FRED later)",
    "url":"https://query1.finance.yahoo.com/v8/finance/chart/%5EVIX (chunked period1/period2, interval=1d)",
    "file":"raw/vix_yahoo_daily.csv","sha256":sha256(RAW/"vix_yahoo_daily.csv"),
    "pulled_utc":dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
    "span":[f"{vix_d.index.min():%Y-%m-%d}",f"{vix_d.index.max():%Y-%m-%d}"],
    "baseline":"1990-01..2007-12 (longest pre-2008 stretch)","monthly_treatment":"mean of daily closes"}
man["series"]["MOVE"] = {"label":"ICE BofA MOVE (Yahoo ^MOVE): monthly closes 2002-12- (Yahoo caps max-range at monthly) + daily last 2y",
    "url":"https://query1.finance.yahoo.com/v8/finance/chart/%5EMOVE",
    "files":{"monthly":"raw/move_yahoo.json","daily2y":"raw/move_yahoo_daily2y.json"},
    "sha256":{"monthly":sha256(RAW/"move_yahoo.json"),"daily2y":sha256(RAW/"move_yahoo_daily2y.json")},
    "pulled_utc":dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
    "span":[f"{move_m.index.min():%Y-%m}",f"{move_m.index.max():%Y-%m}"],
    "baseline":"2002-12..2007-12 -- THIN (61 monthly obs); flag wherever z is shown",
    "monthly_treatment":"monthly closes (not daily means) -- treatment differs from VIX, note in exhibits"}
man_p.write_text(json.dumps(man, indent=2))
print("\nwrote: esd-domainE-controls.png, esd-panel-monthly-domainE.csv; manifest updated")
