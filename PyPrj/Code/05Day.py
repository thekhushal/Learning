"""
Part 2

Create the table and use python to automate loading of the following file into SQLite:
Public_Chauffeurs_Short_hw3.csv

Find (using SQL)
a) how many records are in the Chauffeurs table and
b) how many of the records are missing the “Original Issue Date” entry.

It contains comma-separated data, with two changes: NULL may now be represented by NULL string or an empty string (e.g., either ,NULL, or ,,) and some of the names have the following form “Last, First” instead of “First Last”, which is problematic because when you split the string on a comma, you end up with too many values to insert.

You can use csvreader to automatically load the data for you:

import csv
fd = open('Public_Chauffeurs_Short_hw3.csv', 'r')
reader = csv.reader(fd)
for row in reader:
print(row)
fd.close()
"""

import csv
import sqlite3

conn = sqlite3.connect("/home/theta/CODE/Learning/PyPrj/DB/Public_Chauffeurs.db")
cur = conn.cursor()

# cur.execute()
count = 0

loc_csv = '/home/theta/CODE/Learning/PyPrj/Document/Public_Chauffeurs_Short_hw3.csv'
fd = open(loc_csv, 'r')
reader = csv.reader(fd)

for row in reader: 
    if count == 0:
        cur.execute(f"""
            {row}
        """)
        
        count = 1
        break
    

    
fd.close()