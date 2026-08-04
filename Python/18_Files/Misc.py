# open modes: x w a r 
# x = creates a file if not exists, else errors
# w = creates or overwrites a file
# a = creates a file or opens it for appends
# r = opens a file to read
import os

def readfile(file) :
    print("Reading file")
    f = open(file)
    print(f.read())
    f.close()

os.remove("testfile.txt")

print("Creating file with x")
f = open("testfile.txt", "x")
f.write("This should not have errored")
f.close()

readfile("testfile.txt")

print("Overwriting file with w")
f = open("testfile.txt", "w")
f.write("This should overwrite the file")
f.close()

readfile("testfile.txt")

print("Create file with w")
f = open("testfile.txt", "w")
f.write("This is by w option")
f.close()

readfile("testfile.txt")

print("Appending file with a")
f = open("testfile.txt", "a")
f.write("\nThis will be appended")
f.close()

readfile("testfile.txt")
