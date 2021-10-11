"""
    Working Pieces:
        1. No * / % ...
        2. Special case: divide((-2**31),(-1)) return (2**31 - 1)
    Directions:
        1. "<<", ">>" shift bit operation. it is list *2 and /2
        2. dividing is equal to multiple subtractions.
        3. Reduce subtractions as many as you can.
        4. my way: doubling the divisor.
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend <= -2**31 and divisor == -1: return 2**31 - 1
        isNegative = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)
        output = 0
        dividend = abs(dividend)
        divisor  = abs(divisor)
        while dividend >= divisor:
            quotient = 1
            temp_div = divisor
            while temp_div << 1 < dividend:
                quotient = quotient << 1
                temp_div = temp_div << 1
            dividend -= temp_div
            output += quotient
        return -output if isNegative else output