"""
Problems:
    1. Reverse
        -> accumulate
Directions:
    1. Bitwise operation "^"
    2. mask = 0xffffffff # limit the number in 32bits range
    3. mask = 0x1 # Number ^ mask = result,  result = 1 iff Number is odd or first digit is 1 instead of 0.
    4. shift operator >>, <<

"""
class Solution:
    def reverseBits(self, n: int) -> int:
        mask = 0x1
        output = 0
        counter = 0
        while counter < 32:
            output <<= 1
            temp = n & mask
            output += temp
            n >>= 1
            counter += 1
        return output