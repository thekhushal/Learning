fno = int(input('Input First no. please : '))
sno = int(input("Input Second no. please : "))

Continue = "yes"
while Continue.lower() == "yes" :

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
"""Aim  
Step 1. First User Input 2 no. in system 
Step 2. Then he is asked the operation he wanna perform on the entered no.'s
Step 3. User gets the result 
Step 4. User is asked if he wishes to continue 
        If NO Code ends with a beautiful note
        If YES he is asked which operation will he like to perform on no.'s
    NOTE - No.'s don't change if user wishes to continue 'Operation' obvausly is again asked
"""
