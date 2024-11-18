a = int(input(""))
b = int(input(""))
p = a

print(a, end = "")
while a < b :
    a += 1
    p += a
    print(" +", a, end = "")
print(" =", p)
