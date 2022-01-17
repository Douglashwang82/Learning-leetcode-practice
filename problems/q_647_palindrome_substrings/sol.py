class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))] 
        counter = 0
        
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                length = j - i
                if length == 0:
                    dp[i][j] = True
                elif length == 1 and s[i] == s[j]:
                    dp[i][j] = True
                elif s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    
                counter += dp[i][j]
        return counter