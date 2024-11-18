"""
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""
d = int(input("How long would you like Diamond to be :"))

if d % 2 == 0 : 
    d = int((d/2)+1)
else :
    d = int((d+1)/2)

#Method one 1st and 2nd for loop
for x in range(d) :
    if x == 0 :
        continue
    for y in range(d-x) :
        print(" ", end = "")
    print("*", end = "")
    for z in range(2, x+1) :
        print("**", end = "")
    print()

for x in range(d+1) :
    if x == 0 :
        continue
    for y in range(2, x+1) :
        print(" ", end = "")
    print("*", end = "")
    for y in range(d-x) :
        print("**", end = "")
    print()

"""
#Method two under while loop
x = 1
rev = 1
while i >= 0 :
    for y in range(i) :
        print(" ", end = "")
    print("*", end = "")
    for y in range(1, x) :
        print("**", end = "")
    print()

    if rev < 4 :
        x += 1
        i -= 1
        rev += 1
    else :
        x -= 1
        i += 1
        if i == 4 :
            break
"""

"""
12345*
1234***
123*****
12*******
1*********
***********
1*********
12*******
123*****
1234***
12345*
"""