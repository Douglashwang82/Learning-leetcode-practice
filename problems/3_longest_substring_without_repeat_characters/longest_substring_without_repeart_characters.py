# Hash table to reduce the element searching.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used_char = {}
        start = maximum = 0
        for i in range(len(s)):
            # if not used_char.get(s[i]):   # this will cause error 
                                            # because value 0 makes not statement True
            if s[i] in used_char and start <= used_char[s[i]]: # need to check the start with 
                start = used_char[s[i]] + 1                    # found index
            else:
                maximum = max(maximum, i - start + 1)
            used_char[s[i]] = i
        return maximum



s = Solution()

print(s.lengthOfLongestSubstring("tmmzuxt"))