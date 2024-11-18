x = int(input("first value : "))
a = 100
b = 1000
c = 10000

if x <= a :
    print("{0} is less than or equal to {1}".format(x, a))
elif x <= b : 
    print('{0} is less than or equal to {1} BUT more than {2}'.format(x, b, a))   
elif x <= c :
    print('{0} is less than or equal to {1} BUT more than {2}'.format(x, c, b))
else :
    print('{0} is more than {1}'.format(x, c))
