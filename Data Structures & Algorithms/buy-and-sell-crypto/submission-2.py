class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 원하는 target value를 기준으로 computation을 해야 한다.

        min_price = 100
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            
            current_profit = max(price-min_price, 0)
            if current_profit > max_profit:
                max_profit = current_profit
        
        return max_profit
                 

            