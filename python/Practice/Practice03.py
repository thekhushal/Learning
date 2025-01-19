"""
2
3
5
7
11
13
17
19
"""

i = int(input("Enter till where you want Prime no. : "))

prime = []

for x in range(2, i+1) :
    bool = True        
    for y in range(2, int(x/2+1)) :
        if x % y == 0 :
            bool = False
            break
    
    if bool == True :
        prime.append(x)

print(prime)