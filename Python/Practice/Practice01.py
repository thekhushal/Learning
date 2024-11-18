#Asking no.
i = int(input("Give a no. : "))

#Sorting Even & Odd No.
if i % 2 == 0 : #If given no. is even, diamond will be odd numbered long for obvaus reasons
    i = int((i/2))
else :
    i = int((i-1)/2)

t = i
x = 1
rev = 1
while i >= 0 :
    for y in range(i) :
        print(" ", end = "")
    print("*", end = "")
    for y in range(1, x) :
        print("**", end = "")
    print()

    if rev <= t :
        x += 1
        i -= 1
        rev += 1
    else :
        x -= 1
        i += 1
        if i == t+1 :
            break


"""
for x in range(i+1) : 
    for y in range(i-x) :
        print(" ", end = "")
    print("*", end = "")
    for y in range(1, x+1) :
        print("**", end = "")
    print()
"""