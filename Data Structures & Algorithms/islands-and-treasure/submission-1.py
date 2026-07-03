class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        def inbounds(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def bfs(row, col):
            visited = set()
            queue = deque()
            queue.append((row,col,0))
            while queue:
                node = queue.popleft()
                row = node[0]
                col = node[1]
                visited.add((row,col))
                dist = node[2]
                if grid[row][col] == 0:
                    return dist
                
                if inbounds(row - 1, col) and grid[row - 1][col] != -1 and not (row - 1, col)in visited:
                    queue.append((row - 1, col, dist + 1))
                if inbounds(row + 1, col) and grid[row + 1][col] != -1 and not (row + 1, col) in visited:
                    queue.append((row + 1, col, dist + 1))
                if inbounds(row, col - 1) and grid[row][col - 1] != -1 and not (row, col - 1) in visited:
                    queue.append((row, col - 1, dist + 1))
                if inbounds(row, col + 1) and grid[row][col + 1] != -1 and not (row, col + 1) in visited:
                    queue.append((row, col + 1, dist + 1))
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 0 or grid[row][col] == -1:
                    continue                
                grid[row][col] = bfs(row, col)
    






        
        