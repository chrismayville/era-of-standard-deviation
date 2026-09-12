#!/bin/sh
# Re-pull the four public continuous-series inputs. Provider files are not
# redistributed here (see LICENSES.md); reproduce by pulling them yourself.
mkdir -p raw && cd raw
curl -sSL -o US_Policy_Uncertainty_Data.xlsx "https://www.policyuncertainty.com/media/US_Policy_Uncertainty_Data.xlsx"
curl -sSL -o tpu_web_latest.xlsx "https://www.matteoiacoviello.com/tpu_files/tpu_web_latest.xlsx"
curl -sSL -o data_gpr_export.xls "https://www.matteoiacoviello.com/gpr_files/data_gpr_export.xls"
curl -sSL -o VIX_History.csv "https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv"
cp ../ucdp_annual_statebased_counts.csv .
sha256sum *
