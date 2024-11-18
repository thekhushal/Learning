a=2
b=3
print("age of my first son is", b , "age of second is",a)
print("age of my first son is {} age of second is {}".format(b, a))
print("age of my first son is {0} age of second is {1}".format(b, a))
print("age of my first son is {1} age of second is {0}".format(b, a))
print('the sum of {0} and {1} is : {2} & the product of {0} & {1} is : {3}'.format(a, b, a+b, a*b))
print()

# Format String

alpha=2
beta=3
gama=4
a= "Age of my Younger Son is {} & Age of my Middle son is {} "
b= "Age of my First Son is {0} & Age of my TShird son is {2}"
print(a.format(alpha,beta,gama))
print(b.format(alpha,beta,gama))