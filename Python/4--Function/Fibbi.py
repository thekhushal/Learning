p = 1
q = p
i = 1
l = int(input("How long to continue"))


#print(p, "\n", q)
print(str(p) + "\n"+ str(q))
#print("{} \n {}".format(p, q))


l -= 2


def fibbi(p,q,i,l) :
    q = p + q
    p = q - p
    print(q)
    if i < l :
        i += 1
        fibbi(p,q,i,l)


fibbi(p,q,i,l)

