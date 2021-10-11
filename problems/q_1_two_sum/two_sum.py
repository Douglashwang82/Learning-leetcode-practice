# Hashtable Approach
# Time O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        the_dic = {}
        length = len(nums)
        for i in range(length):
            the_dic[nums[i]] = i
            
        for i in range(length):
            remain = target - nums[i]
            find = the_dic.get(remain)
            if find and i != find:
                return [i, find]
