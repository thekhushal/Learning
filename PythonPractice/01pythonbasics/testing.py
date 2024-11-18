string = "hello"
strLen = len(string)
for charIndex in range(1, strLen+1):
    print(string[strLen-charIndex], end = "")
print()