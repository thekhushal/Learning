p = 1
q = p
#d = int(input("Where to start from : "))
o = int(input("How long should we continue : "))

print(p)
print(p)
o -= 2

for x in range(o) :
    q = p + q
    print(q)
    p = q - p

"""
5
5
10
15
25
"""

# for x in range(o) :
#     q = p + q
#     for x in range(d, o) :
#         print(q)
#         break
#     p = q - p