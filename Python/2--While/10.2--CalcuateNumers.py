# Find the number of numbers in a string
    # e.g. "Hello how are you?" => 0
    # "Adding 5 and 10 results in 15" => 5

s = input()
a = 0
l = len(s)
p = 0
while a < l :
    if s[a].isnumeric() :
        p += 1
    a += 1
print(p)