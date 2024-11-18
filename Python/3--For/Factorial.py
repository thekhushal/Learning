n = int(input("Find Factorial of : "))
p = n
for x in range(1, n) :
    p = p*(n-x)
print(p)

# for x in range(2, n) :
#     p = p*x
# print(p)