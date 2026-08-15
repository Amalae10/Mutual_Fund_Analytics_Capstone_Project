"""Clean and preprocess mutual fund NAV data."""

import pandas as pd
df=pd.read_csv("data/raw/02_nav_history.csv")


df["date"]=pd.to_datetime(df["date"])   #converting date into datetime

df=df.sort_values(["amfi_code","date"])  #sort by amfi code and date

df["nav"] = df.groupby("amfi_code")["nav"].ffill() # to fill missing NAV values using ffill

df=df.drop_duplicates()  # remove duplicates rows

df=df[df["nav"]>0] # NAV cannot be zero or negative,so NAV should be greater than zero

df.to_csv("data/processed/clean_nav.csv",index=False) # save the cleaned file.

