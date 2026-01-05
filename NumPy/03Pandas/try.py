arr = [[1, 2, 3], [4, 5, 6], [7, 8, 19]]

target = 4
lo = arr[0][len(arr[0])-1 ]
hi = arr[len(arr)-1][len(arr[0])-1 ]
mid = arr[(len(arr)-1)//2][(len(arr[0])-1)]

if mid == target:
    print("Found")
elif mid < target:
    lo = mid + 1
elif mid > target:
    hi = mid - 1
else:
    print("Not Found")