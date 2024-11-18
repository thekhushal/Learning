M = bool(input("Pass OR Fail"))
E = bool(input("Pass OR Fail"))
S = bool(input("Pass OR Fail"))


a = (M == True and S == True)
b = (E == True and S == True)
if M == True and E == True :
    if S == True :
        print("Passed")
    else : 
        print( "Suplimentary")
elif a or b : 
    print("Suplimentary")
else : 
    print("Failed")

# SINCE THAT WORKED WHY TO PUT SO MANY LINES LETS MAKE IT SIMPLE

if M == True and E == True and S == True :
    print("Passed")
elif (M == True and E == True) or (M == True and S == True) or (E == True and S == True) :
    print("SUPPLIMENTRY")
else :
    print("FAILED")