class Solution:
    def romanToInt(self, s: str) -> int:
        """
            Solving Process:
                1. First, I think I thought of build a dictionary to store special patterns like "IV, IX,..."
                2. And, use one pointer approach to see if current substring s[pointer: pointer + 2] makes a pattern that in the dictionary.
                3. If yes, let total amount subtract the first pointer's value.
                4. if not, let total amount add the it.
                5. Untail the pointer reach the end.
                6. Return the total amount.
        """
        symbols = {"I":1, "V":5, "X":10,"L":50,"C":100, "D":500,"M":1000}
        special_combinations = {"IV", "IX", "XL", "XC", "CD", "CM"}
        total_amount = 0
        if len(s) == 1: return symbols[s] # For string with legnth 1. ex: "I", "V", ....
        for pointer in range(len(s)):
            if s[pointer:pointer + 2] in special_combinations: # "Check the substring with length 2 if it is in the special_combinations.
                total_amount -= symbols[s[pointer]]            # Finding synbols in a dictionary is O(1) -> hash table.
            else:                                              # If not in the special_combinations, just add it in the amount.
                total_amount += symbols[s[pointer]]
        return total_amount