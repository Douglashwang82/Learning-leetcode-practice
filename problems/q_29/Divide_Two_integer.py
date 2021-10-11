"""
Reference: Leetcode Question 29 Divide two numbers: https://leetcode.com/problems/divide-two-integers/

"""


class Solution:
        def divide(self, dividend: int, divisor: int) -> int:
            sum = 0
            temp_dividend = abs(dividend)
            temp_divisor = abs(divisor)
            
            if divisor == 0:
                return 0
            if dividend > 2**31 -1 or dividend < - 2**31:
                return 2**31 -1
            if dividend == -2**31 and divisor == -1:
                return 2**31 -1
            if divisor == 1:
                return dividend
            elif divisor == -1:
                return -dividend
                
            while temp_dividend >= temp_divisor:        
                temp_dividend -= temp_divisor
                sum += 1

            if dividend > 0 and divisor > 0 or dividend < 0 and divisor < 0:
                return sum
            else:
                return -sum



if __name__ == "__main__":
    dividend = -2**31
    divisor = -1
    solution = Solution()
    print(solution.divide(dividend,divisor))


 