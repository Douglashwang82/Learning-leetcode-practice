    class Solution:
        def containsDuplicate(self, nums: List[int]) -> bool:
            return True if len(nums) == set(nums) else False