class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = set()
        q = []

        for row in range(0,len(grid)):
            for col in range(0, len(grid[0])):
                #begin BFS search
                if grid[row][col] == "1" and (row,col) not in visited:
                    q.append((row, col))
                    while q:
                        row, col = q.pop(0)
                        if (row, col) not in visited:
                            visited.add((row,col))
                        
                        #BFS search all four neighbors
                        if 0 <= row - 1 < len(grid) and (row - 1, col) not in visited:
                            visited.add((row - 1, col))
                            if grid[row-1][col] == "1":
                                q.append((row - 1, col))
                        if 0 <= row + 1 < len(grid) and (row + 1, col) not in visited:
                            visited.add((row + 1, col))
                            if grid[row+1][col] == "1":
                                q.append((row + 1, col))
                        if 0 <= col - 1 < len(grid[0]) and (row, col - 1) not in visited:
                            visited.add((row, col - 1))
                            if grid[row][col-1] == "1":
                                q.append((row, col - 1))
                        if 0 <= col + 1 < len(grid[0]) and (row, col + 1) not in visited:
                            visited.add((row, col + 1))
                            if grid[row][col + 1] == "1":  
                                q.append((row, col + 1))
                    count += 1
        return count





        