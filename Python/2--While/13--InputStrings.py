cont = "y"
students = ""
while cont.lower() == "y":
    student = input("Enter student name: ")
    if len(students) != 0:
        students += ","
    students += student
    cont = input("Do you want to continue?: ")

print()
print(students)
