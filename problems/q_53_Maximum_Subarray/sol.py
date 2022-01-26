class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_maximum = local_maximum = nums[0]
        
        for i in range(1, len(nums)):
            local_maximum = max(local_maximum + nums[i], nums[i])
            global_maximum = max(local_maximum, global_maximum)
        
        return global_maximum




s = Solution()
example = [-2,1,-3,4,-1,2,1,-5,4]

print(s.maxSubArray(example))