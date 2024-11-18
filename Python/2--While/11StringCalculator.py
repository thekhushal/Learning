s1 = "yes"

while True :
    if s1 == "yes" :
        s = input("Input a string : ")
    o = input("Calculate no. of ")
    l = len(s)
    a = 0
    p = 0
    if o.lower() == "alphabet" or o.lower() == "alphabets" :
        while a < l :
            if s[a].isalpha() :
                p += 1
            a += 1
        print(p)
    elif o.lower() == "number" or o.lower() == "numbers" :
        while a < l :
            if s[a].isnumeric() :
                p += 1
            a += 1
        print(p)
    elif o.lower() == "spaces" or o.lower() == "space" :
        while a < l :
            if s[a] == " " :
                p += 1
            a += 1
        print(p)
    elif o.lower() == "vovles" :
        while a < l :
            if s[a] == "a" or s[a] == "e" or s[a] == "i" or s[a] == "o" or s[a] == "u" :
                p += 1
            a += 1
        print(p)
    
    q = input("Would you like to continue (yes/no): ")
    if q == "yes" :
        s1 = input("would you like to change string (yes or no) : ")

    else :
        break