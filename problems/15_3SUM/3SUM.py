class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Solving Process:
            1. The first thinking is two pointer approach with hash table it is a O(n^2).
        """
        output = []
        a_dict = {}
        for i in range(len(nums)):
            a_dict[nums[i]] = i

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                temp = nums[i] + nums[j]
                if a_dict.get(temp):
                                        