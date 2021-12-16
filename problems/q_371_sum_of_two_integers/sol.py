# import math
# class Solution:
#     def getSum(self, a: int, b: int) -> int:
#         a_2 = 2**a
#         b_2 = 2**b
#         ab_2 = a_2 * b_2
#         return int(math.log(ab_2, 2))

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
                
        while b & mask > 0:
            diff = a ^ b
            carry = (a & b) << 1
            a = diff
            b = carry
        return (a & mask) if b > 0 else a