"""Fetch mutual fund NAV data from the MFAPI service."""

import requests
import pandas as pd

url="https://api.mfapi.in/mf/125497"

response = requests.get(url)

data = response.json()

df = pd.DataFrame(data["data"])

df.to_csv("data/raw/HDFC_TOP100_NAV.csv", index=False)

print("Saved Successfully")

# ------------------------------------------------------------
# fetch NAV for 5 schemes

import requests
import pandas as pd

codes = [119551,
         120503,
         118632,
         119092,
         120841]

for code in codes:
    url=f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)
    data = response.json()

    df = pd.DataFrame(data["data"])

    df.to_csv(f"data/raw/{code}.csv", index=False)

    print(code,"Done")