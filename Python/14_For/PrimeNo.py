n = int(input("Prime no.'s till : ")) + 1

# for x in range(3, n) :
#     p = 0
#     for y in range(2, x) :
#         if x%y == 0 :
#             p += 1
#             break
#     if p == 0 :
#         print(x)

#performance improved
for x in range(2, n) :
    p = True
    for y in range(2, int(x+1/2)) : #TODO : Add Coment
        if x%y == 0 :
            p = False
            break
    if p == True :
        print(x)
'''
3
5
'''