x = int(input("Enter a number: "))

match x:
    case 0:
        print("x is zero")
    case 10: # a condition can also be added here
        print("x is 10")
    case _ if x != 20: #Default case with condition
        print("x is not 20")
    case _: # Default case
        print("default case, _ represents default case if no other case runs and _ is present it will run")
    
