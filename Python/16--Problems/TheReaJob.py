"""
    -1  -1      2
    -1  0       0
    -1  1       1
    -1  2       2    
    -1  3       3

    0   -1      0
    0   1       1
    0   2       2
    0   3       3

    1   -1      1
    1   0       1
    1   1       1
    1   2       1
    1   3       1

    2   -1      2
    2   0       2
    2   1       1
    2   2       2
    2   3       2

    3   -1      3
    3   0       3
    3   1       1
    3   2       2
    3   3       3

myFunc(a, b) :
    return y

myFuncTest() :
    for a in range(-1, 4):
        for b in range(-1, 4):
            c = myFunbc(a,b)
            Assert.IsEqual(c, exp)

"""
# Thisone will print each posiblity by itself
x = 4
y = 4
for a in range(-1, x) :
    print("for", a, ":")
    for b in range(-1, y) :
        # if a == b :
        #     if a == -1 :
        #         c = 2
        #     else :
        #         c = a

        # elif a == -1 or b == -1 or a == 0 or b == 0 :
        #     if a == -1 or a == 0 :
        #         if a == 0 and b == -1 :
        #             c = a
        #         else :
        #             c = b
        #     else :
        #         c = a
                
        # # elif a == 0 or b == 0 :
        # #     if a == 0 :
        # #         c = b
        # #     else :
        # #         c = a

        # else : 
        #     if a<b :
        #         c = a
        #     else :
        #         c = b
        if a >= 1 and b >= 1 :
            c = min(a,b)
        else :
            c = max(a,b)
            if c == -1 :
                c = 2
        print("{} \t {} \t\t {}".format(a,b,c))
    print()

"""
#In thisone you will have to give input again 'n again 
a = int(input("Enter : "))
b = int(input("Enter : "))

if a == b :
    if a == -1 :
        c = 2
    else :
        c = a

elif a == -1 or b == -1 :
    if a == -1 :
        c = b
    else :
        c = a
        
elif a == 0 or b == 0 :
    if a == 0 :
        c = b
    else :
        c = a

else : 
    if a<b :
        c = a
    else :
        c = b
print(c)
"""