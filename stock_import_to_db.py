import pandas as pd
import sqlite3

print("--Create a pandas DataFrame from csv file---------------------------")
df1 = pd.read_csv("python_0620_stock_import_to_db.csv")

print("--Insert dataFrame data into database ------------------------------")
conn = sqlite3.connect("../program6/python_0490_database.db")
df1.to_sql("stock", conn, if_exists="replace")


