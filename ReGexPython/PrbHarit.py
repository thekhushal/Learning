i = int(input("Num de bkl: "))

for m in range(1, i+1):
    for n in range(1, i+i):
        if (m == 1 and n >= i) or (m == i and n <= i) or (n + m == i + 1) or (n + m == i + i):
            print("*", end = "")
        else:
            print(" ", end = "") 
    print()