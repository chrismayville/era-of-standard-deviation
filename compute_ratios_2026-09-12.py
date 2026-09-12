#!/usr/bin/env python3
"""
The Era of Standard Deviation — headline ratio-to-baseline figures.

Definition (as stated in the essay's master draft, Rev6 §5): the latest
twelve-month reading of each monthly series, stated as a multiple of that
series' own Great Moderation average.

Implementation:
  - Tier 1 index series (EPU, TPU, GPR, VIX): 12-month rolling mean of the
    monthly level. Baseline = mean of that rolling series over the registered
    window (EPU/TPU 1985-01..2007-12; GPR 1985-12..2007-12; VIX 1990-12..2007-12,
    per panel-manifest-sprint2-transforms-breaks-2026-08-28.md §2).
    Ratio = latest 12-month mean / baseline mean.
  - BDI realised volatility: the 36-month rolling sigma of monthly log changes
    (project file bdi_rolling36m_vol_z85_07.csv). Baseline = mean of that
    series over 1988-02..2007-12. Ratio = latest sigma / baseline mean.
  - VIX daily closes are averaged to monthly before the 12-month mean.

Published values (registered vintage, series through 2026-07):
  TPU 9.0, EPU 3.2, BDI vol 2.6, GPR 1.65, VIX 0.96.
Run with --end 2026-07 to reproduce; omit --end for the current vintage.
"""
import pandas as pd, argparse

def r12(s): return s.rolling(12).mean()

def ratio(s, b0, b1, end=None):
    m = r12(s)
    base = m[b0:b1].mean()
    m = m if end is None else m[:end]
    return m.iloc[-1] / base, base, m.index[-1].strftime('%Y-%m')

def main(raw, project, end):
    e = pd.read_excel(f'{raw}/US_Policy_Uncertainty_Data.xlsx')
    e = e[pd.to_numeric(e['Year'], errors='coerce').notna()]
    e['date'] = pd.to_datetime(dict(year=e.Year.astype(int), month=e.Month.astype(int), day=1))
    es = e.set_index('date')['News_Based_Policy_Uncert_Index'].sort_index()

    t = pd.read_excel(f'{raw}/tpu_web_latest.xlsx', sheet_name='TPU_MONTHLY')
    ts = t.set_index(pd.to_datetime(t.DATE))['TPU'].sort_index()

    g = pd.read_excel(f'{raw}/data_gpr_export.xls').dropna(subset=['GPR'])
    gs = g.set_index(pd.to_datetime(g.month))['GPR'].sort_index()

    v = pd.read_csv(f'{raw}/VIX_History.csv'); v['DATE'] = pd.to_datetime(v.DATE)
    vs = v.set_index('DATE')['CLOSE'].resample('MS').mean()

    out = []
    for name, s, b0, b1 in [('TPU', ts, '1985-01', '2007-12'), ('EPU', es, '1985-01', '2007-12'),
                            ('GPR', gs, '1985-12', '2007-12'), ('VIX', vs, '1990-12', '2007-12')]:
        rr, base, d = ratio(s, b0, b1, end)
        out.append((name, d, round(rr, 2), round(base, 2)))

    b = pd.read_csv(f'{project}/bdi_rolling36m_vol_z85_07.csv'); b['date'] = pd.to_datetime(b.date)
    bs = b.set_index('date')['rolling36m_sigma']
    base = bs['1988-02':'2007-12'].mean()
    bb = bs if end is None else bs[:end]
    out.append(('BDI realised vol', bb.index[-1].strftime('%Y-%m'), round(bb.iloc[-1] / base, 2), round(base, 4)))

    print('series,latest_month,ratio_to_baseline,baseline_mean')
    for r in out: print(','.join(map(str, r)))

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--raw', default='./raw'); ap.add_argument('--project', default='.')
    ap.add_argument('--end', default=None, help='last month to include, e.g. 2026-07')
    a = ap.parse_args(); main(a.raw, a.project, a.end)
