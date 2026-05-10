# Part 1
# B) Repeat the following queries using python (i.e., by reading data from animal.txt, without using a database or SQL language). The idea is to replicate what a database does when the query executes.


# 1. Find the animal names and categories for animals related to a bear

# with open('/home/theta/CODE/Learning/PyPrj/TXT/04animal.txt', 'r') as f:
#     data = [lines.strip().split(',') for lines in f]

# print(*(i for i in data), sep="\n")

# for i in data:
    # if 'bear' in i[1]:
    #     print(i[1], i[2])
    
        
# 2. Find the names of the animals that are not related to the tiger and are common

# with open("/home/theta/CODE/Learning/PyPrj/TXT/04animal.txt", 'r') as f:
#     for line in f:
#         i = line.strip().split(',')
#         if 'tiger' not in i[1] and i[2] == 'common':
#             print(i[1])

# Part 2

# A) You are given a following schema in 1NF:
# (First, Last, Address, Job, Salary, Assistant) and the following set of functional dependencies:

# First, Last -> Address
# Job -> Salary, Assistant

# Decompose the schema to make sure it is in Third Normal Form (3NF).
"""
Employee(First, Last, Address)

JobInfo(Job, Salary, Assistant)

EmployeeJob(First, Last, Job)
"""

# B) Write the necessary SQL DDL statements (CREATE TABLE) to define these the tables you 
# created
# def clean(value):
#     if value is None:
#         return None
#     v = value.strip()
#     if v == "" or v.upper() == "NULL":
#         return None
#     return v


# import sqlite3
# conn = sqlite3.connect("/home/theta/CODE/Learning/PyPrj/DB/random.db")
# cur  = conn.cursor()

# cur.execute("""
# CREATE TABLE IF NOT EXISTS Employee (
#     first      VARCHAR(50) NOT NULL,
#     last       VARCHAR(50) NOT NULL,
#     address    VARCHAR(250),
#     PRIMARY KEY (first, last)
# );
# """)

# cur.executescript("""
# CREATE TABLE JobInfo (
#     job        VARCHAR(100) NOT NULL,
#     salary     DECIMAL(10,2),
#     assistant  VARCHAR(100),
#     PRIMARY KEY (job)
# );

# CREATE TABLE EmployeeJob (
#     first      VARCHAR(50) NOT NULL,
#     last       VARCHAR(50) NOT NULL,
#     job        VARCHAR(100) NOT NULL,
#     PRIMARY KEY (first, last),
#     FOREIGN KEY (first, last) REFERENCES Employee(first, last),
#     FOREIGN KEY (job) REFERENCES JobInfo(job)
# );
# """)


# C) Write a python script that is going to create your tables and populate them with data automatically from data_module4_part2.txt (file attached). You do not have to use executemany, your python code can load data row-by-row. Make sure that you are inserting a proper NULL into the database. HINT: You can use INSERT OR IGNORE statement (instead of a regular INSERT statement) in SQLite to skip over duplicate primary key inserts without throwing an error.

# For example:
# cursor.execute("INSERT OR IGNORE INTO Animal VALUES(?,?,?,?)", [11, 'Llama', None, 3.5]);
# would automatically ignore the insert if animal with ID 11 already exists in the database and insert a NULL into the third column. If you use ‘NULL’ value instead, animal category would be set to the 4-character string ‘NULL’
# import sqlite3
# conn = sqlite3.connect("/home/theta/CODE/Learning/PyPrj/DB/random.db")
# cur  = conn.cursor()
# with open("/home/theta/CODE/Learning/PyPrj/Document/data_module4_part2.txt", 'r') as f:
#     for row in f:
#         parts = row.strip().split(', ')
#         first, last, address, job, salary, assistant = parts

#         assistant = clean(assistant)
#         salary = clean(salary)
#         salary = float(salary) if salary is not None else None
#         # print(f'{first} | {last} | {address} | {job} | {salary} | {assistant}')

#         cur.execute("""
#             INSERT OR IGNORE INTO Employee (first, last, address)
#             VALUES (?, ?, ?)
#         """, (first, last, address))

#         # Insert into JobInfo
#         cur.execute("""
#             INSERT OR IGNORE INTO JobInfo (job, salary, assistant)
#             VALUES (?, ?, ?)
#         """, (job, salary, assistant))

#         # Insert into EmployeeJob
#         cur.execute("""
#             INSERT OR IGNORE INTO EmployeeJob (first, last, job)
#             VALUES (?, ?, ?)
#         """, (first, last, job))

# conn.commit()
# conn.close()

# D) Verify that your NULLS are loaded correctly, by finding all jobs with no salary specified using Salary IS NULL condition.


import sqlite3
conn = sqlite3.connect("/home/theta/CODE/Learning/PyPrj/DB/random.db")
cur  = conn.cursor()

cur.execute("select * from jobinfo where salary is null;")

rows = cur.fetchall()
for row in rows:
    print(row[0])

