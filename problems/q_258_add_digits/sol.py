class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10: return num
        
        count = 0
        
        while num > 0:
            count += num % 10
            num = num // 10
        return self.addDigits(count)