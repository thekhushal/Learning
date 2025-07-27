x = int(input("Enter the number of rows: ")) +1

for i in range(1, x):
    for j in range(1, x):
        if i % 2 == 0:
            asc = 97
        else:
            asc = 65

        print(ord(int(j+asc)), end=" ")
    print()