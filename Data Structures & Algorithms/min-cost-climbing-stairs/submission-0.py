from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        target_length = len(cost)+1
        cost.append(0)  # 마지막 stair는 cost = 0

        dp_table = [0] * target_length

        dp_table[0] = cost[0]
        dp_table[1] = cost[1]

        for idx in range(2, target_length):
            # 해당 floor까지 도달하는데 있어서 최소 비용 이 드는 것으로
            dp_table[idx] = min(
                dp_table[idx-1],
                dp_table[idx-2]
            ) + cost[idx]
            pass

        return dp_table[-1]
        