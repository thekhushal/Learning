"""
Make two list
Input numbers in first
Check for the smallest no. in list
Add it to another list 
Remove it from first lisi
Check for the smallest in first one again
and keep popping smallest in other
"""

s = []
a = []

ask = ""
while True :
    if ask == "" :
        num = int(input("Enter the no. : "))
        s.append(num)
        #ask = input("Do you wanna continue : (enter/n) : ")
    elif ask == "n" :
        break
    # else :
    ask = input("To continue Enter, to discontinue Press n : ")

l = len(s)


# for y in range(l) : # y=0, 0 < 3 ; 
while True :
    smaller = s[0] # 

    for x in range(1, len(s)) :
        if smaller > s[x]  :
            smaller = s[x]

    a.append(smaller)
    s.remove(smaller)
    if len(s) == 0:
        break

print(a)
print(s)

"""
s = []
a = [3, 5, 15]

Bubble Sort:
5   |  1    
15  |  5    |   3
3   |  15   |   5   |   5
10  |  3    |   15  |   6   |   6
1   |  10   |   6   |   15  |   10  |   10
6   |  6    |   10  |   10  |   15  |  15   |   15
        
"""
"""
while True :

    num = input("ENter a no. : ")
    s.append(num)

    ask = input("Do you wanna continue : ")
    if ask == "y" or ask == "" or ask == "yes" :
        continue
    else :
        break

"""