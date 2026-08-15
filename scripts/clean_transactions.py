"""Clean and preprocess investor transaction data."""

import pandas as pd
df=pd.read_csv("data/raw/08_investor_transactions.csv")

df["transaction_date"].str.strip().str.title() #strip=remove extra spaces,title= capitalize  the first letter of each word.

print(df["kyc_status"].unique())  #check KYC status

df["transaction_date"]=pd.to_datetime(df["transaction_date"]) #converting date into datetime

df=df.drop_duplicates()  #remove duplicates rows

df.to_csv("data/processed/clean_transations.csv",index=False)  #save the cleaned file.