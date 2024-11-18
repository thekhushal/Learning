s = input("Which Statement do you wanna Evaluate : ")

while True:
    p = 0
    o = input("What do you wanna count : ")

    if o.lower() == "alphabet" or o.lower() == "alphabets" :
        for x in s :
            if x.isalpha() :
                p += 1
        print(p)

    elif o.lower() == "number" or o.lower() == "numbers" :
        for x in s :
            if x.isnumeric() :
                p += 1
        print(p)
    
    elif o.lower() == "spaces" or o.lower() == "space" :
        for x in s :
            if x == " " :
                p += 1
        print(p)

    elif o.lower() == "vovles" :
        for x in s :
            if x == "a" or x == "e" or x == "i" or x == "o" or x == "u" :
                p += 1
        print(p)
    
    a = input("Do you wanna Continue : (yes/no) ")
    if a == "yes" :

        b = input("Do you wanna Continue with same String : (yes/no) ")
        if "yes" :
            continue
        else :
            s = input("Give me a new String : ")

    else :
        break