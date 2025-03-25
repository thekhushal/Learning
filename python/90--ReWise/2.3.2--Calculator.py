Continue = "yes"
change = "yes"
while Continue.lower() == "yes" :
    if change == "yes" :
        fno = int(input('Input First no. please : '))
        sno = int(input("Input Second no. please : "))
    operation = input("What operatin would you like to perform \(+, -, *, /, ^, %\) :")

    if operation == "+" :
        print(f"The sum of {fno} and {sno} is ", fno + sno)
    elif operation == "-" :
        print(f"The subtraction of {fno} and {sno} is ", fno - sno)
    elif operation == "*" :
        print(f"The multiplication of {fno} and {sno} is ", fno * sno)
    elif operation == "/" :
        print(f"The division of {fno} and {sno} is ", fno / sno)
    elif operation == "^" :
        print(f"{sno} rais to {fno} is ", fno ** sno)
    elif operation == "%" : #error HERE IS SOME ISSUE IT DONT WORK
        print(f"The reminder of {fno} is {fno % sno} when divided by {sno}")
    else :
        print("You gave an invalid input")
    input()

    Continue = input("Do you wish to continue ( Yes | NO )")
    if Continue == "Yes" :
        change = input("Do you wish to change no. : \(yes|no\)")