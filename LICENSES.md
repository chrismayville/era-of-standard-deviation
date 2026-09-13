# Data sources and redistribution

| Series | Provider | Access used | Redistributed here? | Basis |
|---|---|---|---|---|
| US Economic Policy Uncertainty | Baker, Bloom & Davis — policyuncertainty.com | free download | No — pull with `pull_inputs.sh`; registered hash in manifests | Free for use with citation; provider file not mirrored |
| Trade Policy Uncertainty | Caldara, Iacoviello et al. — matteoiacoviello.com | free download | No — pull script | Same |
| Geopolitical Risk | Caldara & Iacoviello — matteoiacoviello.com | free download | No — pull script | Same |
| VIX daily history | Cboe (cdn.cboe.com) | free download | No — pull script | Cboe data terms; not mirrored |
| MOVE | ICE BofA via Yahoo Finance | free chart endpoint | No | Control series; input not archived; manifest dates carried |
| Baltic Dry Index | Baltic Exchange (accessed via investing.com, free account) | login (personal, non-employer) | **No raw levels.** Derived 36-month realised volatility and annual volatility series only | Proprietary index; derived statistics published, source levels not |
| UCDP/PRIO Armed Conflict Dataset v25.1 | Uppsala Conflict Data Program | free flat file | Processed annual counts (`ucdp_annual_statebased_counts.csv`) | CC BY 4.0 |
| Billion-dollar disasters | Climate Central (continuation of NOAA/NCEI) | registered CSV export (2026-09-13; see `cc-reacquisition-addendum-2026-09-13.md`) | Annual counts (`bdd_annual_counts_1980_2026.csv`), with attribution | Non-commercial reproduction with attribution permitted under Climate Central terms of use; export file itself not mirrored |
| BEA Fixed Assets Table 1.2 | US Bureau of Economic Analysis | free | Yes (`bea_fa_t12.csv`) | US government work, public domain |
| World GDP, current USD | World Bank API | free | Yes (`worldbank_global_gdp_current_usd.csv`) | CC BY 4.0 |
| Federal Register counts; OFAC action counts | federalregister.gov API; treasury.gov | free | Yes (counts only) | US government work, public domain |
| IMF PortWatch chokepoint transits | IMF / Oxford PortWatch | free public endpoint | Yes (`portwatch_chokepoints_daily_2019_2026.csv`) | IMF open data terms |

All z-scores, rolling volatilities, rate ratios, tail censuses and break dates in this repository are the author's computations on the sources above; they are not products of, and are not endorsed by, any provider.

Retired and absent by ruling: Swiss Re Institute sigma and Munich Re NatCatSERVICE. No value from either appears in this repository. See `ruling-source-retirement-2026-08-28.md`.

## What the author licenses, and what he cannot

The author holds rights only in what he made: the documents, manifests, results tables, figures, scripts, and the computations (z-scores, rolling volatilities, rate ratios, tail censuses, break dates). Those are released as follows:

- The Python and shell scripts: MIT License.
- The author's documents, tables and figures: CC BY 4.0.

The author does not and cannot license the underlying data. Every series in the table above remains under its provider's terms, and a reuser of any file derived from provider data must satisfy those terms as well as the author's. Two cases to note: the Climate Central counts (`bdd_annual_counts_1980_2026.csv`, and every figure or table that uses them) are reusable for **non-commercial purposes only**, with attribution to Climate Central; and the Baltic Dry Index volatility series are the author's computation on a proprietary index whose levels are not published here and whose reuse is governed by the Baltic Exchange.
