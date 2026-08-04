f = open(".\myfile.txt")
print(f.read())
f.close()

f = open(".\myfile.txt", "w")
f.write("I'm overwriting the code")
print(f.read())
f.close()

# f = open(".\myfile.txt","r")
# f.close()

# open modes: x w a r 
# x = creates a file if not exists, else errors
# w = creates or overwrites a file
# a = creates a file or opens it for appends
# r = opens a file to read
    