s = input("Which Statement do you wanna Evaluate : ")

def count_alpha(s):
    p = 0
    for x in s :
        if x.isalpha() :
            p += 1
    print(p)

def count_numbers(s1):
    p = 0
    for x in s1:
        if x.isnumeric() :
            p += 1
    print(p)

def count_spaces(s3):
    p = 0
    for x in s3 :
        if x == " " :
            p += 1
    print(p)

def count_vowels(s4):
    p = 0
    for x in s4 :
        if x == "a" or x == "e" or x == "i" or x == "o" or x == "u" :
            p += 1
    print(p)

def next_string(str):
    newstr = ""
    b = input("Do you wanna Continue with same String : (yes/no) ")
    if b == "yes" :
        newstr = str
    else :
        newstr = input("Give me a new String : ")
    return newstr

while True:
    o = input("What do you wanna count : ")

    if o.lower() == "alphabet" or o.lower() == "alphabets" :
        count_alpha(s)
    elif o.lower() == "number" or o.lower() == "numbers" :
        count_numbers(s)
    elif o.lower() == "spaces" or o.lower() == "space" :
        count_spaces(s)
    elif o.lower() == "voweles" :
        count_vowels(s)
    a = input("Do you wanna Continue : (yes/no) ")
    if a == "yes" :
        s = next_string(s)
    else :
        break