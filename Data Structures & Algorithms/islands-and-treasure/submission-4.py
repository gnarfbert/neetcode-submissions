class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        for row in range(0,n):
            for col in range(0,m):
                
                if grid[row][col] == 2147483647:
                    q = []
                    visited = set()
                    q.append((row,col,0))
                    visited.add((row,col))
                    tmp = 2147483647
                    while q:
                        c_row, c_col, dist = q.pop(0)
                        if grid[c_row][c_col] == 0:
                            tmp = min(tmp, dist)
                            break
                        dist += 1
                        if 0 <= c_row - 1 < n and grid[c_row-1][c_col] != -1 and (c_row - 1,c_col) not in visited:
                            q.append((c_row - 1, c_col, dist))
                            visited.add((c_row - 1, c_col))
                        if 0 <= c_row + 1 < n and grid[c_row+1][c_col] != -1 and (c_row + 1, c_col) not in visited:
                            q.append((c_row + 1, c_col, dist))
                            visited.add((c_row + 1, c_col))
                        if 0 <= c_col - 1 < m and grid[c_row][c_col - 1] != -1 and (c_row, c_col-1) not in visited:
                            q.append((c_row, c_col - 1, dist))
                            visited.add((c_row, c_col - 1))
                        if 0 <= c_col + 1 < m and grid[c_row][c_col + 1] != -1 and (c_row, c_col+1) not in visited:
                            q.append((c_row, c_col + 1, dist))
                            visited.add((c_row, c_col + 1))                        


                    grid[row][col] = tmp
        