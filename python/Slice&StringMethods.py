a="Hello How Are You?"
print(len(a))

#      Sliicing String: To print a specific or a 
print("#Slicing String")
print(a[17]) #print one character in the str
print(a[6:9]) #print multi chars (slice) in the string
print(a[6:9],a[14:17]) #print multi slices, how &you
print(a[6:9],a[14:]) #print mu
print(a[:9],a[14:]) #print 
print(a[-4:-1])
print(a[-4:])
print("#String Functions")
print(a)
print(a.upper()) # upper
print(a.lower()) # lower
a=a.upper()
print(a)
print()

print("#Replace Functions")
print(a.replace("E","R")) # replace
print(a.replace("ARE","R"))
print()

print("#Count Functions")
print(a.count("E")) # count
print()

print("index function")
print(a.index("E")) #index
print(a.index("E",2))
#     print(a.index("E", 2, 10)) # errors out
#     print(a.index("E", 2, 12)) # errors out
print(a.index("E", 2, 13))
print(a.index("E",a.index("E")+1))
#     print(a.index("z")) # errors out since "z" don't exist

a="Hello How Are You?"
print("find function", a.find("Are"))

print("startswith", a.startswith("Hello"))
print("endswith", a.endswith("You?")) 
