a = "Sillent"
b = "Liseten"

isAnagram = True
if len(a) != len(b):
    print(f"{a} & {b} are not anagrams")
else:
    for x in range(len(a)):
        if (a[x] in b) & (b[x] in a):
            continue
        else:
            isAnagram = False
    
    if isAnagram == True:
        print(f"{a} & {b} are anagrams")
    else:
        print(f"{a} & {b} are not anagrams")
