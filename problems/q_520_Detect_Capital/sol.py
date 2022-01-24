class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        upperCase = word.upper()
        lowerCase = word.lower()
        if upperCase == word or lowerCase == word:
            return True
        if word[0].upper() == word[0] and word[1:].lower() == word[1:]:
            return True
        return False