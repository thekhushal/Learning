"""
Take a number(n)
Write its tables 
    (i) -> Starting from 1 to n
    (ii) -> Starting from m to n
"""
# from re import M


p = int(input("Find tables of : "))

m = int(input("Starting from : "))
n = int(input("Till : ")) + 1

for x in range(m, n) :
    print(p*x)