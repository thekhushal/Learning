d = int(input("How long do you want it to be : "))

if d%2 == 0 :
    d = int((d/2) + 1)
else :
    d = int((d+1)/2)
    
for x in range(d) :
    if x == 0 :continue
    for y in range(x) :
        print("*", end = "")
    print()

for x in range(d) :
    for y in range(d-x) :
        print("*", end = "")
    print()
"""
*****FOR LOOP*****
"""