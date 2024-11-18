integer = []

stop, a =0, 1
while True :
    num = int(input("Enter no. : "))
    integer.append(num)
    if a != num and stop == 0:
        ans = a
        stop = 1
    a += 1
    ask = input("do you wish to continue:(y/n)")
    if ask == "n" :
        break
print(ans)
