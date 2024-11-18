s = input("Enter a String : ")
# ladal     laddal   ladbl    ladlal
# 01234     012345   01234    012345
l = len(s)
i = 0
a = l-1
p = True
while i < a :
    if s[i] != s[a] :
        p = False
        break
    i += 1
    a -= 1
print(p)