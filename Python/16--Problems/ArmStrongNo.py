num = input("Enter a no. : ")
a = []
for x in range(len(num)) :
    a.append(num[x])

ArmStr = 0
for x in range(len(a)) :
    ArmStr += int(a[x])**len(num)
print(ArmStr)
if ArmStr == int(num) :
    print(num, " is an Arm Strong no. ")
else :
    print(num, " is not an Arm strong no. ")

# 153
# 1^3 + 5^3 +  3^3 = 1 + 125 + 27 = 153
# 154
# 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190
