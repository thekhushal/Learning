lastNo = int(input("Show Prime No. till : ")) #100

check = 5  #2,

print("2 \n3")
while check <= lastNo :

    NotPrime = False
    x = 3
    while x <= check / 2 : # insted of 2 divide it by primeno[x] this way itll be really efficient
            
        if check % x == 0 :
            check += 2
            NotPrime = True
        x += 2
    
    if NotPrime == False :
        print(check)
        check += 2

"""    if check == 2 or check == 3 :
        PrimeNo.append(check)
        print(check)
        check += 1
    else :
        x = 0
        while PrimeNo[x] <= check / 2 : # insted of 2 divide it by primeno[x] this way itll be really efficient
            if check % PrimeNo[x] :
                check += 2
                NotPrime = True
                x += 1
    
        if NotPrime == False :
            PrimeNo.append(check)
            print(check)
            check += 1"""