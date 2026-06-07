from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        target_length = len(cost)+1
        # cost.append(0)  # 마지막 stair는 cost = 0

        dp_table = [0] * target_length
        
        # 하단이 0이 되어야 하네, 시작할 때의 cost가 0이 되어야 하므로
        # dp_table[0] = cost[0]
        # dp_table[1] = cost[1]

        # transition으로 이동 비용을 옮기기
        for idx in range(2, target_length):
            dp_table[idx] = min(
                dp_table[idx-1] + cost[idx-1],
                dp_table[idx-2] + cost[idx-2],
            )

        # for idx in range(2, target_length):
        #     # 해당 floor까지 도달하는데 있어서 최소 비용 이 드는 것으로
        #     dp_table[idx] = min(
        #         dp_table[idx-1],
        #         dp_table[idx-2]
        #     ) + cost[idx]
        #     pass

        return dp_table[-1]
        