class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1: return x
        left = 0
        right = x - 1
        
        while left <= right:
            mid = (left + right) // 2
            sqrt = mid * mid
            if sqrt == x: return mid
            if sqrt < x: left = mid + 1
            if sqrt > x: right = mid - 1

        return mid if sqrt < x else mid - 1