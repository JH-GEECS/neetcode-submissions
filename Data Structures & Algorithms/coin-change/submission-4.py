class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        import math
        MAX_VAL = 10000
        
        dp = [math.inf] * (MAX_VAL+1)

        dp[0] = 0
        for coin in coins:
            if coin > MAX_VAL: 
                continue
            else:
                dp[coin] = 1

        for val in range(len(dp)):
            try:
                dp[val] = min([dp[val-coin] for coin in coins if val-coin >= 0]) + 1
            except:
                continue

        ans = dp[amount]

        if math.isinf(ans):
            return -1
        else:
            return dp[amount]

        