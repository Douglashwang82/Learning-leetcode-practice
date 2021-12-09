class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        count = 0
        for i in range(len(digits)):
            count *= 10
            count += digits[i]
        count += 1
        return [i for i in str(count)]