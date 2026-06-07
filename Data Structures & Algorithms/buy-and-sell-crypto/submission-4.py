class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        min_value = prices[0]

        for idx, price in enumerate(prices):
            dp[idx] = max([dp[idx-1] if idx-1 >= 0 else 0, price - min_value])
            min_value = price if price < min_value else min_value
        
        return dp[-1]  
                 

            