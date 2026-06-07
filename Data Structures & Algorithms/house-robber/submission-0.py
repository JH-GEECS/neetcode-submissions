class Solution:
    def rob(self, nums: List[int]) -> int:
        # 2개의 집을 턴다고 가정을 하자.
        # 그런데 3개까지가 있을 때
        # [0, 1, 2, 3, 4, 5] 있을 떄 어짜피 인접한 집은 털지 않으면서 최대한 많은 집을 털어야 하는데
        # [0, 10, 10, 80, 10]
        # [0, 100, 110]
        #  the ith house is the neighbor of the (i-1)th and (i+1)th house.
        # i번째 집까지 털면서 최대 값을 얻으면 되는 문제이다.
        # dp[i] = max(dp[i-1] + arr[i], arr[i]) ⚠️ 이거 틀림
        # dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        # 이 경우에는 kadein algorithm이 맞을 것으로 보인다.
        # i번째 집을 터는데 있어서
        # 그러니까 수열과 똑같은 꼴인 것이지 여기까지 터는데 있어서 최적의 값을 골라야 한다.
        # 마지막으로는 max(dp[n], dp[n-1])을 하는게 맞을 것 같다.

        if len(nums) <= 2:
            return max(nums)

        dp_table = [0] * len(nums)  # 어짜피 n개의 list로 구현이 되어 있으니까
        dp_table[0] = nums[0]
        dp_table[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp_table[i] = max(dp_table[i-1], dp_table[i-2]+nums[i])
        
        return dp_table[-1]

        