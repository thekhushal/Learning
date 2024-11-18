"""
Take 2 int input
Check for the biggest
    BUT 
    if a = -1 and b = -1 
        print(2)
    ' 0 ' is considered biggest of all numbers 
        so if ' 0 ' is one of the no. then print ' 0 '
"""

"""
    -1  -1      2
    -1  0       0
    -1  1       1
    -1  2       2    
    -1  3       3

    0   -1      0
    0   0       0
    0   1       1
    0   2       2
    0   3       3

    1   -1      1
    1   0       1
    1   1       1
    1   2       1
    1   3       1

    2   -1      2
    2   0       2
    2   1       1
    2   2       2
    2   3       2

    3   -1      3
    3   0       3
    3   1       1
    3   2       2
    3   3       3

if both are >= 1, pick min
else pick max 
    if this is -1, pick 2
"""

a = int(input("Enter : "))
b = int(input("Enter : "))

if a >= 1 and b >= 1 :
    c = min(a,b)
else :
    c = max(a,b)
    if c == -1 :
        c = 2

print(c)

if a == b :
    if a == -1 :
        c = 2
    else :
        c = a

elif a <= 0 or b <= 0 :
    if a <= 0 :
        if a == 0 and b == -1 :
            c = a
        else :
            c = b
    else :
        c = a

# else :
#     c = min(a,b)