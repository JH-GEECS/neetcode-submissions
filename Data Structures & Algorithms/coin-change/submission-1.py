class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        전형적인 fib 계열 문제이다.
        amount의 index를 구성하기 위해서 필요한 화페를 산출하면 된다.
        amount가 너무 firm하게 정해져서 풀리는 문제이다.

        """
        from math import inf
        dp_table = [inf] * (amount+1)  # index의 화폐가치를 구하는 최적의 방법
        dp_table[0] = 0

        for i in range(1, amount+1):
            dp_hyp = []
            for val in coins:
                if i-val >= 0:
                    dp_hyp.append(dp_table[i-val]+1)

            if len(dp_hyp) != 0:
                dp_table[i] = min(dp_hyp)

        val = dp_table[amount]

        if not math.isinf(val):
            return val
        else:
            return -1

        