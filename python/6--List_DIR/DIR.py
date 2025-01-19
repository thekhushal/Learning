import os
d = '.' 
for o in os.listdir(d) :
    print(o, os.path.isdir(o))
    if os.path.isdir(o) :
        for p in os.listdir(o) :
            print("\t", p, os.path.isdir(os.path.join(o, p)))

