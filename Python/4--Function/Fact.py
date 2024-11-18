# num = int(input("Gave a nuo. : ")) # 5
# fact = num

# for x in range(2, num) : # 1,T; 2,T; 3,T; 
#     fact = fact*x #5*1=5 ; 5*2=10 ; 10*3= 30
# print(fact)


"""
take a no.
mult it with 
5*4*3*2*1
"""


def myfunc(num) : #4,3,2,1
    if num == 1: #F,F,F,T
        return num; # 1
    fact = num * myfunc(num-1) # 4*6=24; 3*2=6;2*1=2, 
    return fact # 2,6,24

num = int(input("Give a nuo. : ")) # 5
print(myfunc(num))
