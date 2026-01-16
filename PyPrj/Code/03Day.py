# """
# a) Write python code that is going to export a table from a SQLite database into a CSV file. You can use the attached SQLite_LoadAnimalTable.py to create and populate the table before you start.
# Once you have created the database using attached code, your python code solution should query the rows from the Animal table in SQLite database and write the data into a new animal.txt file that is contains the comma-separated rows from the Animal table, e.g.,:
# 1, Galapagos Penguin, exotic, 0.6
# 2, Emperor Penguin, rare, 0.75
# …

# b) Write python code that is going to load the comma-separated animal.txt file you have created in part-a into the Animal table in SQLite database. Your code must read the animal.txt file and use executemany() to load the data in python (i.e., your solution has to be different from the sample code from part 2-a to load the data). You can either drop the table from 2-a or create a different database for this part of the assignment.
# At the end of your code, you should verify how many rows were loaded by printing the output of
# SELECT COUNT(*) FROM Animal;
# """
import sqlite3
import csv

# conn = sqlite3.connect("dsc450.db")

# cursor = conn.cursor()

# cursor.execute("select * from animal")

# rows = cursor.fetchall()

# with open("animal.txt", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerows(rows)

# conn.close()



# import sqlite3

# 1. connect to sqlite database (creates file if it doesn't exist)
conn = sqlite3.connect("animals.db")
cur = conn.cursor()

# 2. drop table if it already exists
cur.execute("drop table if exists animal2")

# 3. create animal table
cur.execute("""
    create table animal2 (
        animal_id integer,
        name text,
        species text,
        age integer
    )
""")

# 4. read data from animal.txt
# data = []

with open("animal.txt", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        cur.execute("insert into animal2 values (?,?,?,?)", 
                    (row[0], row[1], row[2], row[3]))
        # data.append((row[0], row[1], row[2], row[3]))

# 5. insert data using executemany()
# cur.executemany(
#     "insert into animal2 values (?, ?, ?, ?)",
#     data
# )

conn.commit()

# # 6. verify number of rows loaded
# cur.execute("select count(*) from animal")
# row_count = cur.fetchone()[0]

# print("Rows loaded:", row_count)

# # 7. close connection
# conn.close()
