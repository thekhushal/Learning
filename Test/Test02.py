# Create two variables having value 5
a=b= 5
# Print both
print(a, b)
# Accept a number from user
x = int(input("Enter a number: "))
# Accept another number from user
y = int(input("Enter another number: "))
# Print a sum of these numbers
print("The sum of",x, "and",y, "is :",x+y)

# Create a string variable
str = "  a quick brown fox jumps over a lazy dog "
# Print index of "o" of "over"
print(str.index("o",str.index("o",str.index("o")+1)+1))
print(str.index("over"))
print(str.index("a",str.index("over")))
print(str.index("a lazy"))
# Print the number of times "a" has appeared in str
print(str.count("a"))
# Print the str in upper case
print(str.upper())
# Print the str without any spaces in it
print(str.replace(" ",""))
# Print the number of alphabets in str
b=str.replace(" ","")
print(len(b))
# Print "brown fox jumps" using slice
print(str[10:25])
print(str[str.index("brown"): str.index(" over")])