def PivotIndex(nums):
    index = 0
    left_sum = 0
    right_sum = sum(nums) - nums[0]

    while index < len(nums):
        if left_sum == right_sum:
            return index
        else:
            left_sum += nums[index]
            index += 1
            if index < len(nums):
                right_sum -= nums[index]

    return -1

nums = [1,7,3,6,5,6]
# nums = [2,1,-1]
# nums = [1,2,3,4,5]
print(PivotIndex(nums))
        