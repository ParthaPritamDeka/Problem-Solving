def twoSum(nums, target):
    if len(nums) <= 1:
        return False
    buff_dict = {}
    for i in range(len(nums)):
        if nums[i] in buff_dict:
            return [buff_dict[nums[i]], nums[i]]
        else:
            buff_dict[target - nums[i]] = i
            
print twoSum([9,8,2,3], 5)
buff_dict = {-4 : 0, -3 : 1, 3 : 2}
