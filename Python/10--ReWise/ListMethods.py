


# Elements
print("\n****Static****")
s= ["Harit", "Khush", "Mann", "Someone"]

for i in range(len(s)) : # print all element of list
    print("2Welcome {}".format(s[i]))

# Add item to list

print("\n****Append****")
s.append("Tony")

for i in range(len(s)) : # print all element of list

    print("Welcome {}".format(s[i]))


# Insert item into list

print("\n****Insert****")
s.insert(2, "Ojas")

for i in range(len(s)) : # print all element of list

    print("Welcome {}".format(s[i]))


# Add another list into list
print("\n****Extend****")

s1 = ["Mony", "Guddu"]
s.extend(s1)

for i in range(len(s)) : # print all element of list

    print("Welcome {}".format(s[i]))

# Extract item from list

print("\n****Pop****")
s.pop(4)

for i in range(len(s)) : # print all element of list

    print("Welcome {}".format(s[i]))


# Remove last item of list

print("\n****Pop****")
s.pop() # removes last item

for i in range(len(s)) : # print all element of list

    print("Welcome {}".format(s[i]))


# Remove item from list by item

print("\n****Remove****")
s.remove("Mony")

for i in range(len(s)) : # print all element of list

    print("Welcome {}".format(s[i]))


# Remove item from list by index

print("\n****Del****")
del s[4]

for i in range(len(s)) : # print all element of list

    print("Welcome {}".format(s[i]))


# Remove all items from list

print("\n****Clear****")
s.clear()

for i in range(len(s)) : # print all element of list

    print("Welcome {}".format(s[i]))


# Delete the list
print("\n****Del****")
del s
l = len(s) # will error because there's no s left
