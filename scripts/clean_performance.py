import numpy as np
import pandas as pd
df=pd.read_csv("data/raw/07_scheme_performance.csv")
print(df.columns)
print(df.head())

df["return_1yr_pct"]=pd.to_numeric(df["return_1yr_pct"],errors="coerce") # validate return values are numbers.convert return columns to numbers 
df["return_3yr_pct"]=pd.to_numeric(df["return_3yr_pct"],errors="coerce")  
df["return_5yr_pct"]=pd.to_numeric(df["return_5yr_pct"],errors="coerce")

df["negative_sharpe"]=df["sharpe_ratio"]<0  #flag means identify or mark the rows where the Sharpe Ratio is negative.

df=df[
    (df["expense_ratio_pct"]>=0.1) &  # the expected range is 0.1 to 2.5%,so keep only rows with that range
    (df["expense_ratio_pct"]<=2.5)
]

df=df.drop_duplicates()   # remove duplicates rows

df.to_csv("data/processed/clean_performance.csv",index=False)