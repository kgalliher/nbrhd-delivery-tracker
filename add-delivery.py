import sqlite3
import sys
import datetime
import pandas as pd


while True:
    _date = input("Enter the date ('x' for current time, 'q' to exit):  ")
    if _date == "x":
        _date = datetime.datetime.now()
    if _date == "q":
        break

    _company = input("Enter delivery company name:  ")
    my_house = input("Is the delivery for you?  ")

    print(_date, _company, my_house)
    confirm = input("Is this correct?")

    if confirm.upper() == "YES" or confirm.upper() == "Y":
        conn = sqlite3.connect(
            r"C:\Users\kgall\OneDrive\Documents\covid-deliveries\deliveries.sqlite")
        curse = conn.cursor()
        curse.execute("INSERT INTO deliveries (Date, Company, MyHouse) VALUES (?, ?, ?)", [
            _date, _company, my_house])
        conn.commit()

        df = pd.read_sql("SELECT id, Company FROM deliveries", conn)
        print(df.groupby(["Company"]).count())
    else:
        print("Exiting")
