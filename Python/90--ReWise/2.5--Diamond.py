length = int(input("What should be the length : "))

if length % 2 == 0 :
    length = (length) / 2
else :
    length = ((length + 1) / 2) - 1

x = 0
fixed = "yes"
while 0 <= x <= length :

    z = 0
    while z < length - x :
        print(" ", end = "")
        z += 1

    starno = (x * 2) + 1
    z = 0
    while z < starno :
        print("*", end = "") 
        z += 1

    print()

    if fixed == "yes" :
        x += 1
        if x == length :
            fixed = "Hell No"
    else :
        x -= 1

# input -- 7 lines
#   *       # 1    # 3
#  ***      # 3    # 2
# *****     # 5    # 1
#*******    # 7    # 0
# *****     # 5    # 1
#  ***      # 3    # 2
#   *       # 1    # 3

# 1st observation = (7 = 7)
# 2nd observation = repete after it hits limit
# 3rd observation = eveery time 2 star increases, after limit hits everytime 2 star dec
# 4th observation = spaces
# 5th observation = 1+-, repetitive
# 6th observation

# input -- 3
# input -- 5 
# input -- 9
# input -- 25
"""
***
**
*

*
**
***
"""
