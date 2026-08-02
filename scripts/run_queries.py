import sqlite3
import pandas as pd

conn = sqlite3.connect("bluestock_mf.db")

query = """
SELECT *
FROM fact_nav
LIMIT 10;
"""

result = pd.read_sql_query(query, conn)

print(result)

conn.close()