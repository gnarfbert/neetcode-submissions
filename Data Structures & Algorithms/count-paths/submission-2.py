class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m <= 1 or n <= 1:
            return 1
        dp = [[0] * n for _ in range(m)]

        dp[0][0] = 1

        for row in range(m):
            for col in range(n):
                if 0 <= col - 1 < n:
                    dp[row][col] += dp[row][col-1]
                if 0 <= row - 1 < m:
                    dp[row][col] += dp[row-1][col]

        return dp[m-1][n-1]        