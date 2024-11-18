## Read whole file at once
# Open file
f = open(".\Myfile.txt")
# Read whole file
print(f.read())
# Close file
f.close()

print("\n Done \n")

## Read file one line at a time
# Open file
f = open(".\Myfile.txt")
# Read one line at a time
print(f.readline()) # 1st Line only
print(f.readline()) # 2nd line
f.close()

print("\n Done \n")

# Enumerate through lines
f = open(".\Myfile.txt")
for l in f:
    print(l)
f.close()

print("\n Done \n")