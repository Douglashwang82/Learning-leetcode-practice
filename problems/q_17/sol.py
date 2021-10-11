"""
    Working pieces:
        1. N nested loop
        
    Directions:
        1. Reculsive (x)
        2. While (v)
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        output = [""] if len(digits) >0 else []
        while len(digits) > 0:
            output = self.insertElements(digits[0], output)
            digits = digits[1:]
        return output
    
    def insertElements(self, one_digit, element_pool):
        output = []
        my_dict = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        for character in my_dict[one_digit]:
            for element in element_pool:
                output.append(element+character)
        return output
            
        
        