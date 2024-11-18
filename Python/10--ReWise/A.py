"""
 ***
*   *    
*   *
*****
*   *
*   *
*   *
"""

length = int(input("How long should 'A' be : "))
width = int(input("How wide should 'B' be : "))

if length % 2 == 0 :
    mid = int(length / 2)
else :
    mid = int((length - 1) / 2)

for row in range(length) :
    for column in range(width) :
        if (row == 0 and column == 0) or (row == 0 and column == width-1) or (1 <= column < width-1 and row != mid and row != 0) :
            print(" ", end = "")
        else :
            print("*", end = "")
    print()