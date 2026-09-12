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
| Billion-dollar disasters | Climate Central (continuation of NOAA/NCEI) | display data on public page | Annual counts (`bdd_annual_counts_1980_2026.csv`) | Public page; CSV export is registration-gated and was not used; **status to confirm before release** |
| BEA Fixed Assets Table 1.2 | US Bureau of Economic Analysis | free | Yes (`bea_fa_t12.csv`) | US government work, public domain |
| World GDP, current USD | World Bank API | free | Yes (`worldbank_global_gdp_current_usd.csv`) | CC BY 4.0 |
| Federal Register counts; OFAC action counts | federalregister.gov API; treasury.gov | free | Yes (counts only) | US government work, public domain |
| IMF PortWatch chokepoint transits | IMF / Oxford PortWatch | free public endpoint | Yes (`portwatch_chokepoints_daily_2019_2026.csv`) | IMF open data terms |

All z-scores, rolling volatilities, rate ratios, tail censuses and break dates in this repository are the author's computations on the sources above; they are not products of, and are not endorsed by, any provider.

Retired and absent by ruling: Swiss Re Institute sigma and Munich Re NatCatSERVICE. No value from either appears in this repository. See `ruling-source-retirement-2026-08-28.md`.

Code in `` is released under the MIT License. Documents, tables and figures are released under CC BY 4.0. [Author to confirm both.]
