# Thisone will print each posiblity by itself
list = [2,0,1,2,3,0,0,2,3,1,1,1,1,1,1,2,2,1,2,2,3,3,1,2,3]

def check(a,b) :
    for b in range(-1, b+1) :
        if a == b :
            if a == -1 :
                c = 2
            else :
                c = a

        elif a == -1 or b == -1 :
            if a == -1 :
                c = b
            else :
                c = a
                
        elif a == 0 or b == 0 :
            if a == 0 :
                c = b
            else :
                c = a

        else : 
            if a<b :
                c = a
            else :
                c = b
    return c

x = 4
y = 3
for a in range(-1,x) :
    print("for", a, ":")
    
    c = check(x, y)
        
    for o in list :
        if o == c :
            TorF = True
        else :
            TorF = False
    
    if TorF == False :
        print("Wrong Output \n When input is {} & {} output should not be {}".format(a,b,c))
    else :
        print("All good, ready for job :)")
        #print("{} \t {} \t {}".format(a,b,c))

"""

"""