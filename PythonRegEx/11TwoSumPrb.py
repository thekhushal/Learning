nums = [2, 7, 11, 15]
nums.sort()

target = 9

start = 0
end = len(nums) - 1

while start < end :
    if nums[start] + nums [end] == target:
        print(start, end)
        start += 1
    elif nums[start] + nums[end] <= target:
        start += 1
    elif nums[start] + nums[end] >= target:
        end -= 1
    else:
        print(f"There is combination that sums-up to {target}")
