x = int(input("Number till which you wanna see primr no. : "))
y = x-1
while x >= 1 :
    y = x-1
    while y > 1 :
        if x%y == 0 :
            break   
        y -= 1
    print(x)
            
    x -= 1

'''
while x >= 1 :
    if  :
        while x%y != 0 :
            y -= 1
        
    x -= 1
y = 2
while y < x :
    if x % y != 0 :
        y += 1
'''
