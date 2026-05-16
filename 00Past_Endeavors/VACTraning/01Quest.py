#Given an integer array nums, find the subarray with the largest sum, and return its sum

n = int(input("Enter a number: "))
l = list(map(int, input().split()))

currsum = 0; maximum = 0

for i in l :
    currssum += i
    if currsum > maxsum:
        maxsum  = currsum
    if currsum <= 0:
        currsum = 0
print(maxsum)