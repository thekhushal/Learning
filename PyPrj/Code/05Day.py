import csv
import sqlite3

conn = sqlite3.connect("/home/theta/CODE/Learning/PyPrj/DB/Public_Chauffeurs.db")
cur = conn.cursor()

# cur.execute()


fd = open('/home/theta/CODE/Learning/PyPrj/Document/Public_Chauffeurs_Short_hw3.csv', 'r')

reader = csv.reader(fd)
count = 0

for row in reader:
    print(row)
    
    



fd.close()