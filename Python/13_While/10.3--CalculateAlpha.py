## len, IsAlpha, IsNum
# Find the number of alphabets in a string 
    # e.g. "Hello how are you?" => 14
    # "Adding 5 and 10 results in 15" => 18
'''
AIM :
Take an input Eg : Hello how are you?
Check first char. for alpha
    if yes then count
check second char for alpha
    if yes then count
Check third char for alpha
    if yes then count
.
.
.
check 18th char for alpha
    if yes then count

write the no. as ans
'''
s = input()
a = 0
l = len(s)
p = 0
while a < l :
    if s[a].isalpha() :
        p += 1
    a += 1
print(p)

# Hello how are you?