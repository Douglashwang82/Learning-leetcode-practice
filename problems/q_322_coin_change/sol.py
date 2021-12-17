class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [-1]  * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        
        for i in range(amount + 1):
            temp = []
            
            for coin in coins:
                front = i - coin
                if front >= 0 and dp[front] != -1:
                    temp.append(dp[front] + 1)
                    
            if temp:
                dp[i] = min(temp)
        
        return dp[amount]