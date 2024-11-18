# Syntactical errors
# Runtime errors
    # Expected
    # Unexpected

# Expected, so handle the scenario
num = int(input("Enter a number"))
divisor = int(input("Enter divisor"))
if divisor == 0:
    print("Invalid divisor")
    exit()
print(num/divisor)

# Unexpected, so use error handling
print("Hello World!!")
print("Hi there")
try:
    f = open("somefile.txt", "r")
    str = f.read()
    f.close()
except FileNotFoundError as fnf:
    print("The given file was not found, please create the file")
except BaseException as err:
    print(err)
    exit()
print("Length of the file is", len(str))


# Unexpected, so use error handling
print("Hello World!!")
f = open("somefile.txt", "w")
try:
    f.write("something")
except:
    print("Warning: Some error occured")
finally:
    f.close()
print("Done")
