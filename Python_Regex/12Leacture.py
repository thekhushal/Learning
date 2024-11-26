# string tupple are immutable data type, if we do any changes these changes are made in new memory address
# im-mutable datatype means, when value of variable of this tyoe is changed a new memory address is created

# dictionary

# keys in dictionary should be onf immutable datatype
mydictionary = {"amount":0}
for x in range(10):
    mydictionary["amount"] = mydictionary["amount"] +1
print(mydictionary)
