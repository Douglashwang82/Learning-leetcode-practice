class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Solving Process:
            1. Construct the operation step-by-step.
                1. leading space
                2. -/+ sign
                3. integer range.[2^-31, 2^31 - 1]
        """ 

        
        #leading space clear
        pointer = 0
        while pointer < len(s):
            if s[pointer] == " ":
                pointer+=1
            else:
                break
                
        #  Null handle
        if pointer == len(s):
            return 0
        
        # -/+ sign handling
        negative = 0
        if s[pointer] == "+":
            pointer += 1
        elif s[pointer] == "-":
            pointer += 1
            negative = 1
        # Ascii integer range 48-57
        output = 0
        while pointer < len(s) and 48 <= ord(s[pointer]) <= 57:
            output = 10 * output + ord(s[pointer]) - 48
            pointer += 1
            
        # negative handling
        if negative:
            output = -output
    
        # 32-bit integer handling, clamping
        if output < -2**31:
            return -2**31
        if output > 2**31 - 1:
            return 2**31 - 1
        return output
