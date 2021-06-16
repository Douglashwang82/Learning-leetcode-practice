class Solution:
    def reverse(self, x: int) -> int:
        """
        Sovling Process:
            1. Using python, we can get benefit from is slice operation. s[:::]
            2. and its power of handling big integer.    
        """
        negative = 1 if x < 0 else 0 
        abs_x = abs(x)
        x_string = str(abs_x)
        reversed_x_string = x_string[::-1]
        reversed_x = int(reversed_x_string)
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0
        else:
            if negative:
                return -reversed_x
            else:
                return reversed_x
        
