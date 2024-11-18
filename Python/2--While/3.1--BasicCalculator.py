a=int(input("enter first a no."))
b=int(input("enter second no."))

i = "yes"
while i.lower() == "yes" :
    O = input("What Operation you want : ")
    if O == "+" :
        print("additionn of",a,"and",b,"is",a+b)
    elif O == "*" :
        print("Poduct of {} and {} is {}".format(a, b, a*b))
    elif O == "-" :
        print("Subtraction of {} and {} is {}".format(a, b, a-b))
    elif O == "/" :
        print("Dividend of {} / {} is {}".format(a, b , a/b))
    i = input("Do you want to continue? (Yes/No) ")
print("Done")

# while True :
#     O = input("What Operation you want? (+, *, -, /, or any other key to break): ")
#     if O == "+" :
#         print("additionn of",a,"and",b,"is",a+b)
#     elif O == "*" :
#         print("Poduct of {} and {} is {}".format(a, b, a*b))
#     elif O == "-" :
#         print("Subtraction of {} and {} is {}".format(a, b, a-b))
#     elif O == "/" :
#         print("Dividend of {} / {} is {}".format(a, b , a/b))
#     else:
#         break
# print("Done")