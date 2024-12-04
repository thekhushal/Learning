# Print Duplicate elements from list
# Input
a = [10, 20, 30, 20, 10]

for x in range(len(a)):
    for y in range(x+1, len(a)):
        if a[x] == a[y]:
            print(a[x])

# Output
# 10 
# 20