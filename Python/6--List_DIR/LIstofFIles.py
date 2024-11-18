import os

d = input("Enter : ") #D:\CODE\Learning\Python\Files101
t = 0

def Files(d, t) :

    for o in os.listdir(d) :

        for x in range(t) :
            print("\t", end = "") 
        
        print(o) 
        
        if os.path.isdir(os.path.join(d, o)) : 
           
            Files(os.path.join(d, o), (t+1))
                                                               


Files(d, t)