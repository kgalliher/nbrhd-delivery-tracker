import sqlite3

conn = sqlite3.connect("deliveries.sqlite")
print("Opened db")

ct = '''
CREATE TABLE deliveries
(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    delivery_date DATE,
    company VARCHAR(20),
    my_house BOOLEAN
)
'''

conn.execute(ct)
print("Created table")
