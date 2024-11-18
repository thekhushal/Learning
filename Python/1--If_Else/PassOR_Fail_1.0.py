M = bool(input("Pass OR Fail"))
E = bool(input("Pass OR Fail"))
S = bool(input("Pass OR Fail"))

#First Method : 7 Steps

if  M == True :
    if E == True :
        if S == True :
            print("Student Pass")
        else :
            print("Oh..., You've gotta Suplimentary")
    else : 
        if S == True :
            print("Oh..., You've gotta Suplimentary")        
        else : 
            print("Ahh..., You've Failed")
else :
    if E == True :
        if S == True :
            print("Oh... You've gotta Supplimentary")
        else :
            print("Ahh..., You've Failed")
    else :
        print("Ahh..., You've Failed")


#Second Method (Part 1) : 5 Steps + 2 extra 

if M == True and E == True :
    if S == True :
        print("Passed")
    else : 
        print( "Suplimentary")
elif M == True and S == True :
    if E == False :     # Useless
        print("Suplimentary")
elif E == True and S == True :
    if M == False :     # NoNeed
        print("Spupplimentary")
else : 
    print("Failed")


#Second Method (Part 2) : 5 Steps (More Compact)

if M == True and E == True :
    if S == True :
        print("Passed")
    else : 
        print( "Suplimentary")
elif M == True and S == True :
    print("Suplimentary")
elif E == True and S == True :
    print("Spupplimentary")
else : 
    print("Failed")

