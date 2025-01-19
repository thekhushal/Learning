'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''

# i = 1
# while i <= 5 :
#     j = 4
#     k = 1
#     while j >= i :
#         print("a", end="")
#         j -= 1
#     print()
#     i += 1

p = int(input("How long should Diamond be : "))

# Sorting Even & Odd ; DOing necessary operation
if p%2 == 0 :
    i = p/2 + 1
elif p%2 != 0 : 
    i = (p+1)/2
k = 1

#First half of Diamond ; 
while i >= 1 :
    j = 1
    while j < i :
        print(" ", end="")
        j += 1

    l = 1
    while l <= k : 
        print("*", end="")
        l += 1

    k += 2
    i -= 1
    print()

i = 1

if p%2 == 0 :
    q = p/2
    k = p-1
else :
    q = p - (p+1)/2
    k = p-2

while i <= q :
    j = 1
    while j <= i :
        print(" ", end="")
        j += 1
    l = 1 
    while l <= k :
        print("*", end="")
        l += 1
    print()
    k -= 2
    i += 1