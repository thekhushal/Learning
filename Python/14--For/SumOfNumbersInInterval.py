from datetime import datetime

a = int(input(""))
b = int(input(""))
p = 0

for x in range(a, b+1):
    if x < b:
        print(x, end = " + ")
    else :
        print(x, end = " = ")
    p += x
print(p)


# for i in range (5):
#     print (i)
# else:
#     print("Done")

# print(datetime.now())
# for i in range(100000):
#     pass
# print(datetime.now())