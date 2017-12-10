# Takes Kaggle coinbase (historical bitcoin prices) CSV file and constructs a sqlite3 database

import sqlite3
import csv

db = sqlite3.connect('mydb.db')
exc = db.cursor()

exc.execute(''' CREATE TABLE data
            (   timestamp time, open real, high real, low real, close real,
                volume_btc real, volume_curr real, weighted_price real)''')

with open("coinbaseUSD_1-min_data_2014-12-01_to_2017-10-20.csv.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if row[0].isdecimal():
            exc.execute("INSERT into data VALUES (?, ?, ?, ?, ?, ?, ?, ?)", row[0:8])

db.commit()

db.close()
