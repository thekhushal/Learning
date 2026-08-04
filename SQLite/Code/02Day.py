"""
Write a python function to validate SQL insert statements. 
The function will take a string containing a SQL insert statement and print two kinds of messages. 
1) “Invalid insert” or 
2) Inserting [list of values] into [the target] table. 
The values and the table name would be based on each particular statement. For validating the statement, you only have to check that the insert statement starts with INSERT INTO and that statements ends with a semicolon (;).


Examples:

validateInsert(”INSERT INTO Students VALUES (1, 'Jane', 'A-');”)
- Inserting (1, 'Jane', 'A-') into Students table

validateInsert(“INSERT INTO Students VALUES (1, 'Jane', 'A-')”)
- Invalid insert

validateInsert(“INSERT Students VALUES (1, 'Jane', B+);”)
- Invalid insert

validateInsert(“INSERT INTO Phones VALUES (42, '312-676-1213');”)
- Inserting (42, '312-667-1213') into Phones table
"""


def validate_insert(message):
    message = message.strip()

    if message[:11].lower() != "insert into":
        return "invalid insert"
    if message[-1] != ";":
        return "Invalid insert"

    message = message[:-1]


    before, val = message.split("VALUES", 1)
    table_name = before[11:].strip()

    return f"Inserting {val.strip()} into {table_name} table"



statement = "INSERT INTO Phones VALUES (42, '312-676-1213');"
message = validate_insert(statement)


"""
Consider a MEETING table that records information about meetings between clients and representatives in the company. Each record contains the names of the client and the representative’s name as well as the office number, floor and the building. Finally, each record contains the city that the building is in and the date of the meeting. The table is in First Normal Form and the primary key is (Client, Office).

(Date, Client, Office, Floor, Building, City, Representative)


You are given the following functional dependencies:

Building → City

Office → Floor, Building, City

Client → Representative

Client, Office → Date


a. For the functional dependency Building → City, explain the redundancy problem and possible consequences through an example (you can make up your own building names as you see fit).


b. Remove any existing partial dependencies and convert the logical schema to the Second Normal Form. Please remember that when performing schema decomposition you need to denote primary key for every new table as well as the foreign key that will allow us to reconstruct the original data.


c. Remove any existing transitive dependencies to create a set of logical schemas in Third Normal Form. Again, remember to denote primary keys and foreign keys (including which primary key those foreign keys point to).
"""


"""
1nf:
meeting(client, office, date, floor, building, city, representative)
primary key: (client, office)

2nf:

client(client pk, representative)
office(office pk, floor, building, city)
meeting(client pk, office pk, date)

foreign key: client → client(client)
foreign key: office → office(office)

3nf:

client(client pk, representative)

office(office pk, floor, building)
building(building pk, city)
foreign key: office(building) → building(building)

meeting(client pk, office pk, date)

foreign key: client → client(client)
foreign key: office → office(office)
"""

"""

"""

"""
Part 3 
Consider a table that stores information about students, student name, GPA, honors list and the credits that the student had completed so far.

(First, Last, GPA, Honor, Credits)

You are given the following functional dependencies
First, Last → GPA, Honor, Credits
GPA → Honors

a. Is this schema in Second Normal Form? If not, please state which FDs violate 2NF and decompose the schema accordingly.
b. Is this schema in Third Normal Form? If not, please state which FDs violate 3NF and decompose the schema accordingly.

a. The schema is already in 2NF as no partial dependency, no non key attribute depends on part of composit key.

b. No the schema is not in 3NF due to transitive dependencies the schema has, currently Honnor depends on GPA which itself depends on (First, Last), this is exeactly what we avoide in 3NF, it increases redundancy. Bellow is the decomposed version:
Table one: (First, Last, GPA, Credits) and its FD: (First, Last → GPA, Credits)
Table two: (GPA, Honor) and its FD: (GPA → Honors)
"""