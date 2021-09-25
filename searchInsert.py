def searchInsert(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        for i, n in enumerate(nums):
            if target < n:
                return i
                
nums = [1, 5, 7, 9]
targets = [7, 4, 15, 0]
for target in targets:
    print(searchInsert(nums, target))