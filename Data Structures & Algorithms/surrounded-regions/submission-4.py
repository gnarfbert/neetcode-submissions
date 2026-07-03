class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])

        def dfs(row,col):
            stack = []
            stack.append((row,col))
            while stack:
                nr, nc = stack.pop()
                if (nr < 0 or nr == n or nc < 0 or nc == m or board[nr][nc] != "O"):
                    continue
                    
                board[nr][nc] = "T"            
                stack.append((nr - 1, nc))
                stack.append((nr + 1, nc))
                stack.append((nr, nc - 1))
                stack.append((nr, nc + 1))

        for row in range(0,n):
            if board[row][0] == 'O':
                dfs(row,0)
            if board[row][m - 1] == 'O':
                dfs(row, m - 1)
        for col in range(0,m):
            if board[0][col] == 'O':
                dfs(0, col)
            if board[n - 1][col] == 'O':
                dfs(n- 1, col)  

        for row in range(0,n):
            for col in range(0,m):
                if board[row][col] == 'O':
                    board[row][col] = 'X'  

        for row in range(0,n):
            for col in range(0,m):
                if board[row][col] == 'T':
                    board[row][col] = 'O' 