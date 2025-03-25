mylist = [-4, -1, 1, 2]
target = 1
diff = float('inf')

for i in range(len(mylist) - 2):
    start = i+1
    end = len(mylist) - 1

    while start < end:
        total_sum = mylist[i] + mylist[start] + mylist [end]
        if abs(total_sum - target) < abs(target - diff):
            diff = total_sum
        elif(total_sum < target):
            start += 1
        elif(total_sum > target):
            end -= 1
print(diff)

# high order function
# First class functionw