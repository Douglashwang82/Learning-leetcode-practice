class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        acc = 1
        output1 = []
        output2 = []
        for number in nums:
            output1.append(acc)
            acc *= number
        acc = 1
        for number in reversed(nums):
            output2.append(acc)
            acc *= number
        result = map(lambda x, y: x * y, output1,  reversed(output2))
        return list(result)