import os
d = '..\..\..\Files101' #this will dicide which which file we are talking about if d = '.' current file d = '..' parent folder d = '.\ while' while folder pr this can contain direct path as well

print(os.listdir(d)) # This will print a list contaning all files and folders in "d"

for o in os.listdir(d) : # this will do nothing but "ENUMERATE" within list

    #print(o)
    print(o, "\t", os.path.isdir(o)) # this will print 'true' also if "o" is a 'directory' ; the syntax mean
    
    if os.path.isdir(o) : #if o is true ture then you will go in 
    
        for p in os.listdir(o) :
    
            print("\t", p, os.path.isdir( os.path.join(o, p) ))#this os.path.join(o, p) will join the path of o & p