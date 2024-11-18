length = int(input("What should be the length : "))

if length % 2 == 0 :
    length = (length) / 2
else :
    length = (length + 1) / 2

starno = 1
fixed = "yes" 
while 0 < starno <= length :

    x = 0
    while x < starno : 

        print("*", end = "")
        x += 1
    
    print()

    if fixed == "yes" :
        starno += 1
        if starno == length :
            fixed = "Hell No"
    else : 
        starno -= 1

print(length)