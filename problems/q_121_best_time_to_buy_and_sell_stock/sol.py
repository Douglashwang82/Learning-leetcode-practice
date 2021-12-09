class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        minValue = prices[0]
        maxProfit = 0
        for price in prices:
            profit = price - minValue
            if profit > maxProfit:
                maxProfit =  profit
            if price < minValue:
                minValue = price
        return maxProfit