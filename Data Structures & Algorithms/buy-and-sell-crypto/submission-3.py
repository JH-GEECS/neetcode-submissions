class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 원하는 target value를 기준으로 computation을 해야 한다.

        if len(prices) == 1:
            return 0

        right_idx = 0
        left_idx = 0
        max_profit = 0

        while right_idx < len(prices):
            max_profit = max(max_profit, prices[right_idx] - prices[left_idx])

            # 여기를 조금 옮기기
            if prices[right_idx] < prices[left_idx]:
                left_idx = right_idx

            right_idx += 1

        return max_profit
                 

            