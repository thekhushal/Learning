# data = ""
# mylist = []
# x = 0

# for char in data:
#     if char in  "[({":
#         mylist.append(char)
#     elif(mylist):
#         if (char == "}" and mylist.pop() != "{"):
#             x = 1
#             break
#         elif ( char == "]" and mylist.pop() != "[" ):
#             x = 1
#             break
#     else:
#         x = 1
#         break

# if ( x == 0 and len(mylist) == 0):
#     print("valid")
# else:
#     print("invalid")


# sorting
# a = [400, 32, 12, 40, 50, 23, 54, 256, 23, 67]

# for x in range(len(a)):
#     min = a[x]
#     for y in range(x+1, len(a)):
#         if min > a[y]:
#             min = a[y]
#             why = y
#     swap = a [x]
#     a [x] = min
#     a[why] = swap
# print(a)

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

# Print Duplicate elements from list
a = [10, 20, 30, 20, 10, 20]

for x in range(len(a)):
    for y in range(x+1, len(a)):
        if a[x] == a[y]:
            print(a[x])
