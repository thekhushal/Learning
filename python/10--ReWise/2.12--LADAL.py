straight = input()

x = len(straight) - 1
y = 0

LADAL = True
while y-x <= 1 :
    
    if straight[y] != straight[x] :
        LADAL = False
        break
    x -= 1
    y += 1

#    if x == y or y-x == 1 :
#        break
print(LADAL)
