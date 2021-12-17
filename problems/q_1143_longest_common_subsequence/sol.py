class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        length1 = len(text1) + 1
        length2 = len(text2) + 1
        dp = [[0 for _ in range(length2)] for _ in range(length1)]
        
        for i in range(1, length1):
            for j in range(1, length2):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = max(dp[i][j - 1], dp[i-1][j-1] + 1, dp[i-1][j])
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i-1][j-1], dp[i-1][j])
                
        return dp[length1 - 1][length2 - 1]