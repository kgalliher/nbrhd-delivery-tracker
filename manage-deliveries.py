import sqlite3
import sys
import datetime
import pandas as pd

conn = sqlite3.connect(
    r"C:\Users\kgall\OneDrive\Documents\covid-deliveries\deliveries.sqlite")


def get_delivery_df(sql=""):
    if sql == "":
        sql = "SELECT id as cnt, Company, MyHouse FROM deliveries"
    return pd.read_sql(sql, conn)


if len(sys.argv) == 1:
    sys.exit()
if sys.argv[1] == "help":
    print("View or Insert deliveries:")
    print("Flags:")
    print("\t'add': Add a new delivery to the table")
    print("\t'view': View all existing deliveries")
    print("\t'count': Get a count of deliveries grouped by company")
    print("")
if sys.argv[1] == "count":
    df = get_delivery_df("SELECT id as count, Company FROM deliveries")
    print(df.groupby("Company").count())
    print("Total: ", df.shape[0])
elif sys.argv[1] == "view":
    df = get_delivery_df()
    print(df)
elif sys.argv[1] == "add":
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
            curse = conn.cursor()
            curse.execute("INSERT INTO deliveries (Date, Company, MyHouse) VALUES (?, ?, ?)", [
                _date, _company, my_house])
            conn.commit()

            df = get_delivery_df()
            print(df.groupby(["Company"]).count())

        else:
            print("Exiting")
else:
    print("What are you trying to do?  Use flag 'add', 'view' or 'count'")
