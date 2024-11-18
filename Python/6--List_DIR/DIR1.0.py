import os

i = input("Enter : ")

cf = '\  '
def Files(d,cf) :


    for o in os.listdir(d) :

        cf = d + cf[0] + o
        
        if d != i :
            print("\t", end = "")
            print(d, end = "\t")

        
        print(o, "\t", os.path.isdir(o))
        #print(o)
    
        if os.path.isdir(o) :

            cfl = cf
            Files(cfl, cf)

    print(d)

Files(i,cf)