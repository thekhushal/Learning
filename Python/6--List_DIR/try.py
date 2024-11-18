import os

i = input("Enter : ")

t = int(0)

prev = ""

def tab(t) :

    for x in range(t) :
        tab = "\t"
        return tab


def Files(d,t,prev) :

    for o in os.listdir(d) :

        if d == prev :
            t -= 1

        if True :
            print(tab(t), end = "")

        #print(o, "\t", os.path.isdir(o))
        print(o)
    
        if os.path.isdir(o) :

            prev = d
            t += 1
            Files(o,t,prev)

Files(i,t,prev)