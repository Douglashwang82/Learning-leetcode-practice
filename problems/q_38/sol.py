"""
    Working Pieces:
        1. Recursive
        2. grouping elements
        3. regular expression? (from discussion)
    Directions:
        1. resursive
"""
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"
        fromNextLayer = self.countAndSay(n - 1)
        operatedString = self.operateString(fromNextLayer)
        return operatedString
    
    def countLength(self, s:str):
        return str(len(s)) + s[0]
    
    def operateString(self, s:str):
        left = mid = 0
        right = len(s) - 1
        preparation = ""
        while mid <= right:
            if s[mid] != s[left]:
                preparation += self.countLength(s[left:mid]) # 333 -> 23
                left = mid
            if mid == right:
                preparation += self.countLength(s[left:])
            mid += 1
        return preparation