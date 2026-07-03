class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])


        def search(row, col, direction):
            if (row, col) in visited:
                return
            if (row < 0 or row >= m) or (col < 0 or col >= n):
                return
            matrix[row][col] = 0
            visited.add((row,col))
            if direction == 1:
                search(row - 1, col,1)
                search(row + 1, col,1)
            if direction == 0:
                search(row, col - 1,0)
                search(row, col + 1,0)
            return

        zeroPos = set()
        visited = set()
        for row in range(0, len(matrix)):
            for col in range(0, len(matrix[row])):
                if matrix[row][col] == 0:
                    zeroPos.add((row, col))

        print(zeroPos)
        for nr, nc in zeroPos:
            print(nr)
            print(nc)
            visited.clear()
            search(nr,nc, 1)
            visited.clear()
            search(nr,nc, 0)
        

        

        