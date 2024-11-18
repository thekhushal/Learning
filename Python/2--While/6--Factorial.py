# Input a number and print its factorial 
# For eg. if the no. is 5 the fact will be 5*4*3*2*1= 120
p = int(input("Give me a number : "))
b = p-1
while b > 0 :
    p = p*b
    b -= 1
print(p)
'''
Aim:
5*4
20*3
60*2
120*1
'''