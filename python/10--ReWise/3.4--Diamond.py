length = int(input("Length of diamond should be : "))
if length < 0 :
    print("Aagaye Aukat Pe")
    exit
elif length % 2 == 0 : #Even
    length = int(length / 2) # Eg: (8 --> 4)
else :#Odd
    length = int((length - 1) / 2) # Eg: (7 --> 4)


for x in range(length + 1) : # increasing order of stars

    for space in range( length - x ) :
        print(" ", end = "")

    for star in range( 1 + (x * 2) ) : # Eg : (3 --> 7)
        print("*", end = "")

    print()

for x in range(length-1, -1, -1) : #Decreasing Order of stars

    for space in range( length - x ) :
        print(" ", end = "")

    for star in range( 1 + (x * 2) ) : # Eg : (3 --> 7)
        print("*", end = "")

    print()