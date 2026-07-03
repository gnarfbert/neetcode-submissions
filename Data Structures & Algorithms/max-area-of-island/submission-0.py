class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        n = len(grid)
        m = len(grid[0])
        q = []

        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                if grid[row][col] == 1:
                    currArea = 0
                    q.append((row,col))
                    grid[row][col] = 0
                    while q: 
                        row, col = q.pop(0)
                        currArea += 1
                        if 0 <= row - 1 < n and grid[row-1][col] == 1:
                            q.append((row-1, col))
                            grid[row-1][col] = 0
                        if 0 <= row + 1 < n and grid[row+1][col] == 1:
                            q.append((row+1,col))
                            grid[row+1][col] = 0
                        if 0 <= col - 1 < m and grid[row][col - 1] == 1:
                            q.append((row, col - 1))
                            grid[row][col - 1] = 0
                        if 0 <= col + 1 < m and grid[row][col + 1] == 1:
                            q.append((row, col + 1))
                            grid[row][col + 1] = 0
                    maxArea = max(maxArea, currArea)
        
        return maxArea
                        

        