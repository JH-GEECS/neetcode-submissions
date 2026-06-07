class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp_table = [[0] * n for _ in range(m)]
        dp_table[0][0] = 1

        for y in range(m):
            for x in range(n):
                summation = 0
                if x-1 >= 0:
                    summation += dp_table[y][x-1]
                if y-1 >= 0:
                    summation += dp_table[y-1][x]
                dp_table[y][x] += summation
        

        return dp_table[m-1][n-1]