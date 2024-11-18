'''
*
**
***
****
*****
******
*******
********
*********
**********
*********
********
*******
******
*****
****
***
**
*
'''

i = 1
k = int(input("how long should diamond be : "))

if k%2 == 0 :
    k = (k/2) + 1
elif k%2 != 0 :
    k = (k+1)/2

while i <= k:
    j = 1
    while j <= i:
        print("*", end = '')
        j += 1
    print()
    i += 1

i = k-1
while 1 <= i :
    j = 1
    while j <= i :
        print("*", end = '')
        j += 1
    print()
    i -= 1   
