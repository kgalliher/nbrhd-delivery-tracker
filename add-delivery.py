import sqlite3
import sys
import datetime
import pandas as pd
_date = input("Enter the date ('x' for current tme):  ")
if _date == "x":
    _date = datetime.datetime.now()
_company = input("Enter delivery company name:  ")
my_house = input("Is the delivery for you?  ")

print(_date, _company, my_house)
confirm = input("Is this correct?")

if confirm.upper() == "YES" or confirm.upper() == "Y":
    conn = sqlite3.connect("deliveries.sqlite")
    curse = conn.cursor()
    curse.execute("INSERT INTO deliveries (Date, Company, MyHouse) VALUES (?, ?, ?)", [
                  _date, _company, my_house])
    conn.commit()

    df = pd.read_sql("SELECT id, Company FROM deliveries", conn)
    print(df.groupby(["Company"]).count())
else:
    print("Exiting")
