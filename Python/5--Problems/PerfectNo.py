num = int(input("Enter the number : "))
a = [] # List of all the proper divisor  of  input

for x in range(1, int(num+1/2)) :
    if num%x == 0 :
        a.append(x)

IsPer = 0
for x in range(len(a)) :
    IsPer += a[x]


if num == IsPer :
    print(num, " is a perfect no. ")
else :
    print(num, " is not a perfect no. ")