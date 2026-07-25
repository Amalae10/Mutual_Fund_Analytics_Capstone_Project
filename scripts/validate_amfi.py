import pandas as pd

fund_master=pd.read_csv("data/raw/01_fund_master.csv")
nav_history=pd.read_csv("data/raw/02_nav_history.csv")

# find missing AMFI codes
missing_codes=fund_master[
        ~fund_master["amfi_code"].isin(nav_history["amfi_code"])
]

# display the result
if missing_codes.empty:
    print("AMFI codes are present in nav_history")
else:
    print("Missing AMFI codes:")
    print(missing_codes[["amfi_codes","scheme_name"]])