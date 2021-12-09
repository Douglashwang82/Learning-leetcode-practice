class Solution:
    def maxSubArray(self, nums: int) -> int:
        local_maximum = 0
        global_maximum = nums[0]
        
        for i in nums:                                  
            local_maximum = max(i, i + local_maximum)   # Kadane's Algorithm O(n) 
            if local_maximum > global_maximum:          # vars (local_maximum, global_maximum, nums)  
                global_maximum = local_maximum
        
        return global_maximum




s = Solution()
example = [-2,1,-3,4,-1,2,1,-5,4]

print(s.maxSubArray(example))