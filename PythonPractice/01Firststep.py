a = int(input("Enter your first number : "))
b =  int(input("Enter your second number : "))

stdName = []
while True :
    stdName, conti = int(input("Enter name of the student : ")), input("do you wish to continue (y/n) : ")

    if conti == "n" :
        break

for x in range(len(stdName)) :
    print(stdName[x])
