"""
    Working Pieces:
        1. duplicate
        2. fixed spaces
    Directions:
        1. two pointer approach: one defined, one use for loop
"""
class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums) < 2: return len(nums)
        pointer1 = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[pointer1]:
                pointer1 += 1
                nums[pointer1] = nums[i]
        return pointer1 + 1



test = [1,2,3,3,3,4,4,4,5,5,6,6,6,6,6,6]
my_example = Solution()
print(my_example.removeDuplicates(test))