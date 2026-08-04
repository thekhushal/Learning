num = (input("Enter a number: "))
PalNum = 0
for x in range(len(num)) :

    PalNum += (int(num) % 10)
    num = num // 10
print("reverse of ", num, " is ", PalNum)
if num == PalNum:
    print(num, " is a Palindrome number as ", num, " is equal to ", PalNum)
else:
    print(num, " is not a Palindrome number as ", num, " is not equal to ", PalNum)
