# open parameters, default mode
f = open(".\Myfile.txt")
print(f.read())
f.close()


# With read mode
f = open(".\Myfile.txt", "r")
print(f.read())
f.close()

# With write mode
f = open(".\Myfile.txt", "w")
f.write("I am writing from python")
f.close()

# With read mode
f = open(".\Myfile.txt", "r")
print(f.read())
f.close()

# With append mode
f = open(".\Myfile.txt", "a")
f.write("I am writing another line from python")
f.close()

# With read mode
f = open(".\Myfile.txt", "r")
print(f.read())
f.close()