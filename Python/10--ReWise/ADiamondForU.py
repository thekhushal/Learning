""" 
   *    # 3 _ 1
  ***   # 2 _ 3
 *****  # 1 _ 5
******* # 0 _ 7
 *****  # 1 _ 5
  ***   # 2 _ 3
   *    # 3 _ 1


"""

Length = int(input("Length of diamond should be : "))

if Length % 2 == 0: # Even
    Length = int(Length / 2) # Setting Val of Length for first half of Diamond
else : #Odd
    Length = int((Length + 1) / 2) # Val of Length for first half of Diamond

x = 0
reverse = "no" # change in val of this Variable will initiate dec in val of x
while 0 <= x < Length : #Val of x will go up for first half, then down for second half

    longdistance = (Length - 1) - x # This var will store no. of spaces to printed
    for spaces in range(longdistance) :
        print(" ", end="")

    starno = (x * 2) + 1 # This var store no. of stars to be printed
    for stars in range(starno) :
        print("*", end="")
    
    print()

    if x == Length-1  or reverse == "yes" :
    # At (Length-1) we've already printed first Half so here we start decreasing val of x ttill it prints second half
        x -= 1
        reverse = "yes"
    else :
        x += 1
    
    
        
