class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)] 
        dp[0][0] = 1
        print(dp)
        for row in range(m):
            for col in range(n):
                if 0 <= row - 1 and row - 1 < m:
                    dp[row][col] += dp[row - 1][col]
                if 0 <= col - 1 and col - 1 < n:
                    dp[row][col] += dp[row][col - 1]

        return dp[m-1][n-1] 
        