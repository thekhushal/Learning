#You have been given a integer array/list(ARR) of size N. In the array you are only having 0, 1 and 2 elements. Write a function to sort the array using this algorithm.


n = int(input(""))
l = list(map(int,input().split()))
low = 0 ; mid = 0 ; high = n-1

while mid <= high :
    if l[mid] == 0:
        l[mid], l[low] = l[low], l[mid]
        low += 1
        mid += 1
    elif l[mid] == 1:
        mid += 1
    elif l[mid] == 2:
        l[mid], l[high] = l[high], l[mid]
        high -= 1
for i in l:
    print(i,end=" ")

