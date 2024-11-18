length = int(input("Lenght shoud bee : "))

if length % 2 == 0 : # Even
    length = int(length / 2 )
else : # Odd
    length = int((length + 1) / 2)


for x in range(1, length + 1) :
    for y in range(x) :
        print("*", end = "")
    print()

for x in range(length-1, 0, -1) :
    for y in range(x) :
        print("*", end = "")
    print()