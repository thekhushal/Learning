#Given an array of numbers, find GCD of the array elements

def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a%b)

n = int(input(""))
l = list(map(int, input().split()))

gcd = l[0]
for i in range(1, n):
    gcd = GCD(gcd, l[i])
print(gcd)