class Solution(object):
    def isToeplitzMatrix(self, matrix):
        m, n = len(matrix), len(matrix[0])

        # Check each element against the element diagonally above and to the left
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False

        return True
