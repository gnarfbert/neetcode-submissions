class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l,r = 0, len(matrix) - 1

        while l < r:

            # for an n * n matrix you only need n - 1 rotations
            for i in range(r - l):
                top, bottom = l, r

                #stores the temp
                temp = matrix[top][l + i]

                #bottom left to top left
                matrix[top][l + i] = matrix[bottom - i][l]

                #bottom right to bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                #top right to bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                #top left to top right
                matrix[top + i][r] = temp

            l += 1
            r -= 1



        