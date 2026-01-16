""" Problem 1:
Write a python function that will accept a name of a text file containing multiple rows with comma separated numbers (for example “5, 16, 13, 65, 7”) and return the average of these numbers. Your function should compute and average all of the numbers in a file.

Note that your function should return the result of the computation (i.e., return res not print(res)).
"""

# handle non-numeric chars
# handle flaots

# def convert(list):
#     result = []
#     for num in list:
#         if isinstance(num, bool):
#             continue
#         elif isinstance(num, (int, float)):
#             result.append(num)
#         else:
#             try:
#                 t = float(num)
#                 result.append(int(t) if t.is_integer() else t)
#             except: # not sure of what exeact errors to account for so for now im leaving like this
#                 pass
#     return result

# def average(txt):
    
#     with open(txt, 'r') as f:
#         l = f.read()
#         l = l.replace(',', '').split()

#     l = convert(l)

#     avg = sum(l) / len(l)
#     return avg

# avg = average("/home/theta/CODE/Learning/PyPrj/TXT/01file.txt")
# print(avg)



''' Problem 2:
Write a python function that will accept a name of a text file containing multiple rows with comma separated numbers (same as in part-A) and will write these numbers into a new file so that there is only one number in each line. For example
1,2,8
4,5,9
Would be transformed into a new file:
1
2
8
4
5
9
'''
# VIP: Target filename be input param
# VIP: Unnecessary memory and processing usage
# def rearrange(txt, destination):
#     with open(txt, 'r') as f:
#         data = f.read()
#         data = data.replace(",", "").split()
#     data = convert(data)

#     with open(destination, 'w') as f:
#         for x in data:
#             f.write(str(x) + '\n')
            
# rearrange("TXT/01file.txt", "/home/theta/CODE/Learning/PyPrj/TXT/03ReArranged.txt")
# rearrange("TXT/02file.text")

""" Problem 3:
Write a python function that is going to generate and return a SQL INSERT statement given a table name and value list as parameters. We have not covered SQL yet, so you don’t need to run these insert statements, just get your python code to return the required string. Do not hardcode the output.

For example,
print(generateInsert('Students', ['1', 'Janine', 'B-'])) should print
INSERT INTO Students VALUES (1, Janine, B-);

All statements start from INSERT INTO, followed by the name of the table, followed by VALUES and the comma-separated list of supplied values inside parenthesis, terminated by a semi-colon
Make sure that your function returns the string rather than prints it.

If you are interested in additional challenge, modify your function to instead return (this modification is not required):
INSERT INTO Students VALUES (1, 'Janine', 'B+');
(i.e., put quotes around strings, but not around numbers).

Another example:
generateInsert('Phones', ['42', '312-556-1221']) should return
INSERT INTO Phones VALUES (42, '312-556-1221');

Both of the example calls (with different number of inserted values) should work correctly.
"""

# def generateInsert(table, values):
#     # lis = [
#     #     v if v.isdigit() else f"'{v}'"
#     #     for v in values
#     # ]
#     # for v in values:
#     #     if v.isdigit():
#     #         lis.append(v)
#     #     else:
#     #         lis.append(f"'{v}'")
#     val = ', '.join(
#         v if v.isdigit() else f"'{v}'"
#         for v in values
#     )
#     return f"INSERT INTO {table} VALUES ({val});"

# # print(generateInsert('Students', ['1', 'Janine', 'B-']))

# print(generateInsert('Phones', ['42', '312-556-1221']))


""" Problem 4:
a) Define a relational schema with underlined (primary) keys and arrows connecting foreign keys and primary keys for a database containing the following information.
1. Authors have LastName, FirstName, ID, and Birthdate (identified by ID)
2. Publishers have Name, PubNumber, Address (identified by PubNumber)
3· Books have ISBN, Title, Publisher (each book has a publisher and is identified by its ISBN).
4· Authors Write Books; since many authors can co-author a book, we need to know the relative contribution of the author to a book, signified by their position in the author list (i.e. 1, 2, 3, etc.).

Create sample data for at least 2 books, at least 1 publisher and at least 2 authors (who co-authored the same book).

Please do not forget about the author list ordering – your schema should have a column of data representing that information.
"""
# """
# Authors (ID, LastName, FirstName, Birthdate)
# Publishers (PubNumber, Name, Address)
# Books (ISBN, Title, Publisher)
# Writes (AuthorID, BookISBN, Position)
# """

"""
Author
ID, LastName, FirstName, Birthdate
1, Smith, John, 1980-01-01
2, Johnson, Emily, 1990-05-15

Publisher
PubNumber, Name, Address
1, Penguin Books, 123 Penguin Lane

Book
ISBN, Title, Publisher
1-1-1, The Great Gatsby, 1
1-1-2, To Kill a Mockingbird, 1

Writes
AuthorID, BookISBN, Position
1, 1-1-1, 1
2, 1-1-1, 2
1, 1-1-2, 1
2, 1-1-2, 2
"""

""" Problem 5:
Define a relational schema for students, student advisors, and advisor departments

1· Students have StudentID, First Name, Last Name, DOB, Telephone and a reference to their advisor
2· Advisors have ID, Name, Address, Research Area, and a reference link to their Department
3· Departments have Name, Chair, College (identified by Name)
"""

# Students (StudentID pk, FirstName, LastName, DOB, Telephone, AdvisorID fk)
# Advisors (ID pk, Name, Address, ResearchArea, DepartmentName fk)
# Departments (Name pk, Chair, College)
