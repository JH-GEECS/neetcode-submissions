class Solution:
    def climbStairs(self, n: int) -> int:
        """
        You are given an integer n representing the number of steps to reach the top of a staircase.
        You can climb with either 1 or 2 steps at a time.

        Return the number of distinct ways to climb to the top of the staircase.

        :param n:
        :return:
        """
        
        m = max(2, n)
        
        dp_table = [0] * (m+1)

        dp_table[0] = 1
        dp_table[1] = 1
        dp_table[2] = 2

        for i in range(2, m+1):
            dp_table[i] = dp_table[i-1] + dp_table[i-2]

        return dp_table[n]