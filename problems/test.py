def twoSum(nums, target: int):
    output = []
    the_dict = {}
    for i in range(len(nums)):
        the_dict[nums[i]] = i
    for j in range(len(nums)):
        remain = target - nums[j]
        found = the_dict.get(remain)
        if found and found != j:
            output.append([nums[j], nums[found]])
    return output

def threeSum(nums):
    triplets = []
    for i in range(0,len(nums) - 2, 1):
        found = twoSum(nums[i+1:], -nums[i])
        for j in range(len(found)):
            triplets.append([nums[i]] + found[j])
    return triplets



print(threeSum([-1,0,1,2,-1,-4]))