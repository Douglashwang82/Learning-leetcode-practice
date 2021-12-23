class Solution:
    def numDecodings(self, s: str) -> int:
        
        if s[0] == "0":
            return 0
        if len(s) == 1:
            return 1
        
        dp = [0 for _ in range(len(s))]
        dp[0] = 1
        if int(s[0] + s[1]) <= 26 and int(s[0] + s[1]) > 0 and int(s[1]) > 0:
            dp[1] = 2
        elif s[1] == "0" and int(s[0] + s[1]) > 26:
            dp[1] = 0
        else:
            dp[1] = 1
            
        for i in range(2, len(s)):
            temp = int(s[i - 1] + s[i])
            if s[i] == "0":
                if temp<=26 and temp > 0:
                    dp[i] = dp[i - 2]
                else:
                    return 0
            else:
                if temp <= 26 and temp > 10:
                    dp[i] = dp[i - 1] + dp[i - 2]
                else:
                    dp[i] = dp[i - 1]
        return dp[-1]