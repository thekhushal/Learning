# Find the number of vowels in a string
    # e.g. "Hello how are you?" => 7
    # "Adding 5 and 10 results in 15" => 6

s = input()
a = 0
l = len(s)
p = 0
while a < l :
    if s[a] == "a" or s[a] == "e" or s[a] == "i" or s[a] == "o" or s[a] == "u" :
        p += 1
    a += 1
print(p)
