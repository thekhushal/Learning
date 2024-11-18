name =  input("")
le = len(name)

# to print first 5 characters of name
print("to print first 5 characters of name")
print(name[0:5]) # 0:4 gives first 5 element, from index 0 to 4 first 5 element
print(name[:5]) # :4 automaticly prints elements from 1st index (which is 0) to 4th index

#to print last 5 characters of name
print("\nto print last 5 characters of name")
print(name[le-5:le])
print(name[le-5:])
print(name[-5:])

# to 
