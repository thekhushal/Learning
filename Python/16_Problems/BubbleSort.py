list = []

ask = ""
while True :

    if ask == "" or ask == "y" or ask == "yes" :
        num = int(input("Enter a no. : "))
        list.append(num)
    else :
        break

    ask = input("Do you wanna continue")

print(list) # All good till here

i = 1
j = 2

while True :
    
    CurrentNo = list[ len(list)-i]
    PreviousNo = list[len(list)-j]

    if CurrentNo < PreviousNo :

        list.insert( len(list) - j, CurrentNo )
        del list[list[ len(list)-i]]
    
    i += 1
    j += 1

    if i == len(list) :
        break

print(list)
