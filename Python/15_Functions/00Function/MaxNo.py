s = []

def append() :
    i = int(input("Enter the no. : "))
    s.append(i)

ask = "y"
while True :
    
    if ask.lower() == "y" :
        append()
        ask = input("Do you wanna continue : ")
    else :
        break

big = s[0]
l = len(s)
for x in range(1, l) :

    if big < s[x] :
        big = s[x]

print(big)

"""
15 6 51
5
"""