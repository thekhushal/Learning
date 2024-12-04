# Second Highest

# a = [20, 4, 10, 50, 30, 25]

# Method one

# for x in range(len(a)):
#     min = a[x]
#     for y in range(x+1, len(a)):
#         if min > a[y]:
#             min = a[y]
#             why = y
    
#     swap = a [x]
#     a [x] = min
#     a[why] = swap

# print(a[len(a)-2])

# Method two
# h = 0
# sh = 0
# for x in range(len(a)):
#     if a[x] > h:
#         sh = h
#         h = a[x]
#     elif a[x] > sh:
#         sh = a[x]
# print(sh)

