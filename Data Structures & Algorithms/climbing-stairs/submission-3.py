class Solution:
    def climbStairs(self, n: int) -> int:
        """
        You are given an integer n representing the number of steps to reach the top of a staircase.
        You can climb with either 1 or 2 steps at a time.

        Return the number of distinct ways to climb to the top of the staircase.

        :param n:
        :return:
        """

        # m = max(2, n)
        if n <= 2:
            # n = 1인 경우, n = 2인 경우 (2, 1+1)
            return n

        # dp_table = [0] * (m+1)

        dp_table = [0] * (n+1)
        # dp_table[0] = 1  # 그냥 아무 것도 없는 garbage
        dp_table[1] = 1
        dp_table[2] = 2

        for i in range(3, n+1):
            dp_table[i] = dp_table[i-1] + dp_table[i-2]

        return dp_table[n]