class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp = [0] * len(prices)
        best_value = 0
        min_value = prices[0]

        for idx, price in enumerate(prices):
            best_value = price - min_value if (price - min_value) > best_value else best_value
            min_value = price if price < min_value else min_value

        return best_value
                 

            