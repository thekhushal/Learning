# list
# s1="Harit"
# s2="Khush"
# s3="Mann"

# print("Welcome {}".format(s1))
# print("Welcome {}".format(s2))
# print("Welcome {}".format(s3))

# Array and elements
print("\n****Static****")
s= ["Harit", "Khush", "Mann", "Someone"]
l = len(s)
i = 0
while i < l:
    print("Welcome {}".format(s[i]))
    i += 1

# Add item to list
print("\n****Append****")
s.append("Tony")
l = len(s)
i = 0
while i < l:
    print("Welcome {}".format(s[i]))
    i += 1

# Insert item into list
print("\n****Insert****")
s.insert(2, "Ojas")
l = len(s)
i = 0
while i < l:
    print("Welcome {}".format(s[i]))
    i += 1

# Add another list into list
print("\n****Extend****")
s1 = ["Mony", "Guddu"]
s.extend(s1)
l = len(s)
i = 0
while i < l:
    print("Welcome {}".format(s[i]))
    i += 1

# Extract item from list
print("\n****Pop****")
s.pop(4)
l = len(s)
i = 0
while i < l:
    print("Welcome {}".format(s[i]))
    i += 1

print("\n****Pop****")
s.pop() # removes last item
l = len(s)
i = 0
while i < l:
    print("Welcome {}".format(s[i]))
    i += 1

# Remove item from list by item
print("\n****Remove****")
s.remove("Mony")
l = len(s)
i = 0
while i < l:
    print("Welcome {}".format(s[i]))
    i += 1

# Remove item from list by index
print("\n****Del****")
del s[4]
l = len(s)
i = 0
while i < l:
    print("Welcome {}".format(s[i]))
    i += 1

# Remove all items from list
print("\n****Clear****")
s.clear()
l = len(s)
i = 0
while i < l:
    print("Welcome {}".format(s[i]))
    i += 1

# Delete the list
print("\n****Del****")
del s
l = len(s) # will error

