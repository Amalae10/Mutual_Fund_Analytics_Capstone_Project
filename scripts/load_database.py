import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db") # creating database

nav=pd.read_csv("data/processed/clean_nav.csv")
nav.to_sql("fact_nav",engine,if_exists="replace",index=False) # load into sqlite

transactions=pd.read_csv("data/processed/clean_transactions.csv")
transactions.to_sql("fact_transactions",engine,if_exists="replace",index=False)

performance=pd.read_csv("data/processed/clean_performance.csv")
performance.to_sql("fact_performance",engine,if_exists="replace",index=False)

print("Database loaded successfully!")