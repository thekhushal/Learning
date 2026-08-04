j = "yes"
while True :
    if j.lower() == "yes":
        a=int(input("enter your first number :"))
        b=int(input("enter your second number :"))
    c = input("what operation you want ?")
    if c == "+" :
        print("addition of {} and {} is {}".format (a, b, a+b))
    elif c == "*":
        print("the multiplication of {} and {} is {}".format(a,b,a*b))
    elif c =="-"    :
        print("the subtraction of {} and {} is {} ".format(a,b,a-b))
    elif c =="/":
        print("the diidant of {} and {} is {} ".format(a, b, a/b))   
    i =input("do you want to continue ? (yes/no)")
    if i.lower() == "yes" :
        j = input("Do you wish to change the numbers? :")
    else : 
        break
print("done")  

 