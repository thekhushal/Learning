check = "no"
while True :
    if check.lower() == "no" :
        sense = input()

    ask = input("Calculate \(Alphabet, Number, Spaces, Vovels\) \n")

    x = 0 
    count = 0

    if ask.lower() == "Alphabet" or ask.lower() == "a" :

        while x < len(sense) :

            if sense[x].isalpha() :
                count += 1
            x += 1
        print(count)

    if ask.lower() == "numbers" or ask.lower() == "n"  :

        while x < len(sense) :

            if sense[x].isnumeric() :
                count += 1
            x += 1
        print(count)

    if ask.lower() == "spaces" or ask.lower() == "s" :
        while x < len(sense) :

            if sense[x] == " " :
                count += 1
            x += 1
        print(count)

    if ask.lower() == "vovle" or ask.lower() == "v" : 
        while x < len(sense) :

            if sense[x] == "a" or sense[x] == "e" or sense[x] == "i" or sense[x] == "o" or sense[x] == "u" : 
                count += 1
            x += 1
        print(count)

    Continue = input("would you like to continue : ")
    if Continue == "yes" :
        check = input("Would you like to continue with same string : ")
    else :
        break