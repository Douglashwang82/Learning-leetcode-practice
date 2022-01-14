class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(s, length):
            left = 0
            right = length - 1
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        if not s: return None
            
        length = len(s)
        odd_maximum = 1
        even_maximum = 0
        odd_start = even_start = length - 1
        
        for i in range(len(s) - 1, -1, -1):
            if (i + odd_maximum <= length) and isPalindrome(s[i:i + odd_maximum + 1], odd_maximum):
                odd_maximum += 2
                odd_start = i
            if (i + even_maximum <= length) and isPalindrome(s[i:i + even_maximum + 1], even_maximum):
                even_maximum += 2
                even_start = i
        
        if odd_maximum > even_maximum:
            return s[odd_start: odd_start + odd_maximum - 2]
        else:
            return s[even_start: even_start + even_maximum - 2]