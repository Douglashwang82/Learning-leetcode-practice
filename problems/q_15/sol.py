"""
    Working pieces:
        1. subset
        2. sum of three number equal to zero
        3. duplicate elements
    Direction: 
        1. using hashing (dictory in python) for best seaching element 
        2. Solve it base on twoSUM
        3. Sort the list and using pointer to help to avoid duplicate element
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()                 # helpful for removing duplicates
        pointer = 0                 #  
        while pointer < len(nums) - 2:
            found = self.twoSum(nums[pointer+1:],-nums[pointer])
            triplets += found
            pointer += 1
            while nums[pointer - 1] == nums[pointer] and pointer < len(nums) -1:
                pointer += 1
        return triplets

    def twoSum(self, nums: List[int],target: int) -> List[List[int]]:
        output = [[]]
        the_dict = {}
        for i in range(len(nums)):
            the_dict[nums[i]] = i
            
        for j in range(len(nums)):
            found = the_dict.get(target - nums[j])    
            if found and found > j:
                temp = [-target, nums[j], nums[found]]
                if output[-1] != temp:
                    output.append(temp)
        return output[1:]