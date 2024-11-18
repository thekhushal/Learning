# Find the number of spaces in a string
    # e.g. "Hello how are you?" => 3
    # "Adding 5 and 10 results in 15" => 6

s = input()
a = 0
l = len(s)
p = 0
while a < l :
    if s[a] == " " :
        p += 1
    a += 1
print(p)