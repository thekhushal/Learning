s = input("what would like to revrse : ")
# How are you
# 01234567890
i = 1
l = len(s)
while i <= l :
    d = l-i
    print(s[d], end = "")
    i += 1
# # uoy era woh

print()

i = len(s)-1
while i >= 0 :
    print(s[i], end = "")
    i -= 1
