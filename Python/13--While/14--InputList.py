students = []
cont = "y"
while cont.lower() == "y":
    s = input("Enter student name: ")
    students.append(s)
    cont = input("Do you wish to continue? (Y/y): ")

l = len(students)
i = 0
while i < l:
    print("Welcome {}".format(students[i])) 
    i += 1