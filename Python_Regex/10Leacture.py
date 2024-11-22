# Patern 01
# ****
# ****
# ****
# ****

# for i in range(1, 5):
#     for j in range(1, 5):
#         print("*", end=" ")
#     print()

# Pattern 02
# *
# **
# ***

# for i in range(1, 5):
#     for j in range(0, i):
#         print("*", end = " ")
#     print()

# Pattern 03.1
# 1
# 12
# 123

# for i in range(1, 5):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

# Pattern 03.2
# 4
# 45
# 456
# 4567

# for i in range(1, 5):
#     for j in range(4, i+4):
#         print(j, end=" ")
#     print()

# Pattern 03.3
# 1
# 23
# 456
# 78910

# a = 1
# for i in range(1, 5):
#     for j in range(1, i+1):
#         print(a, end=" ")
#         a += 1
#     print()

# Pattern 04.1
# ***
# **
# *

# for i in range(0, 5):
#     for j in range(0, 5-i):
#         print("*", end = " ")
#     print()

# Pattern 04.2
# 1234
# 123
# 12
# 1

# for i in range(5, 1, -1):
#     for j in range(1, i):
#         print(j, end = "")
#     print()

# Pattern 04.3
# 4321
# 432
# 43
# 4

# for i in range (0, 4):
#     for j in range(4, i, -1):
#         print(j, end="")
#     print()

# Pattern 04.4
# 1234
# 567
# 89
# 10

# a = 1
# for i in range(5, 1, -1):
#     for j in range(1, i):
#         print(a, end = "")
#         a += 1
#     print()

# Pattern 04.5

# 8765
# 765
# 65
# 5

# for i in range (0, 4):
#     for j in range(8, i+4, -1):
#         print(j-i, end="")
#     print()

# Pattern 05.1
# ***
#  **
#   *

# for i in range(0, 5):
#     for j in range(0, i):
#         print(" ", end="")
#     for j in range(i, 5):
#         print("*", end="")
#     print()

# ASCII
# A
# AB
# ABC

for i in range(1, 4):
    for j in range(0, i):
        print(chr(ord('A')+j), end="")
    print()