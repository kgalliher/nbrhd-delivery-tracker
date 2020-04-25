import pandas as pd
import sqlite3

df = pd.read_excel("deliveries.xlsx")
print(df)

# Clean up column names
df = df.rename(columns={'My House?': 'MyHouse'})
clean_df = df[["Date", "Company", "MyHouse"]]

conn = sqlite3.connect("deliveries.sqlite")

# move df to db
clean_df.to_sql("deliveries", conn, if_exists="append")
