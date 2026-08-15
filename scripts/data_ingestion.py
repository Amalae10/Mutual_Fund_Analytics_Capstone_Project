"""Load raw mutual fund datasets for the analytics project."""

import pandas as pd

df1=pd.read_csv("data/raw/01_fund_master.csv")
print(df1.head())
print(df1.shape)
print(df1.dtypes)
# -----------------------------------------------------------------------------------------
df2=pd.read_csv("data/raw/02_nav_history.csv")
print(df2.head())
print(df2.shape)
print(df2.dtypes)
# -----------------------------------------------------------------------------------------
df3=pd.read_csv("data/raw/03_aum_by_fund_house.csv")
print(df3.head())
print(df3.shape)
print(df3.dtypes)
# -----------------------------------------------------------------------------------------
df4=pd.read_csv("data/raw/04_monthly_sip_inflows.csv")
print(df4.head())
print(df4.shape)
print(df4.dtypes)
# -----------------------------------------------------------------------------------------
df5=pd.read_csv("data/raw/05_category_inflows.csv")
print(df5.head())
print(df5.shape)
print(df5.dtypes)
# -----------------------------------------------------------------------------------------
df6=pd.read_csv("data/raw/06_industry_folio_count.csv")
print(df6.head())
print(df6.shape)
print(df6.dtypes)
# -----------------------------------------------------------------------------------------
df7=pd.read_csv("data/raw/07_scheme_performance.csv")
print(df7.head())
print(df7.shape)
print(df7.dtypes)
# -----------------------------------------------------------------------------------------
df8=pd.read_csv("data/raw/08_investor_transactions.csv")
print(df8.head())
print(df8.shape)
print(df8.dtypes)
# -----------------------------------------------------------------------------------------
df9=pd.read_csv("data/raw/09_portfolio_holdings.csv")
print(df9.head())
print(df9.shape)
print(df9.dtypes)
# -----------------------------------------------------------------------------------------
df10=pd.read_csv("data/raw/10_benchmark_indices.csv")
print(df10.head())
print(df10.shape)
print(df10.dtypes)