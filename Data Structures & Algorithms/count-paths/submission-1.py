class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m <= 1 or n <= 1:
            return 1
        dp = [[0] * n for _ in range(m)] 
        dp[0][0] = 1
        for row in range(0,m):
            for col in range(0,n):
                if row == 0 and col == 0:
                    continue
                left = 0
                up = 0
                if row - 1 >= 0:
                    up = dp[row - 1][col]
                if col - 1 >= 0:
                    left = dp[row][col - 1]    
                dp[row][col] = left + up
        return dp[m-1][n-1]

        