# IF O < 40 DONT BUY FROM HERE
# if 40 >= O > 30 RS BRING 1 KG 
# IF 30 >= O > 20 RS BRING 2 KG
# IF 20 >= O > 10 RS BRING 3 KG
# IF 10 > O DONT BUY FROM HERE

O = int(input("Cost of 1 kg ONION is : "))

#if 10 >= O <= 40 :
if O <= 40 and O >= 10 :
    if O > 30 :
        print("BRING 1 KG ")
    elif O > 20 : 
        print("BRING 2 KG ")
    elif O > 10 :
        print("BRING 3 KG ")
    # else :
    #     print("Dont buy from here")
else :
    print("Dont buy from here")