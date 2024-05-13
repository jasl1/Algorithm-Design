class Solution(object):
    def findDiagonalOrder(self, mat):
        m, n = len(mat), len(mat[0])
        result = []

        # Variables to track the direction of diagonal traversal
        direction = 1  # 1 for upward, -1 for downward
        row, col = 0, 0

        while len(result) < m * n:
            # Add current element to result
            result.append(mat[row][col])

            # Move to next element in diagonal direction
            if direction == 1:
                # Upward diagonal traversal
                if col == n - 1:
                    row += 1
                    direction = -1
                elif row == 0:
                    col += 1
                    direction = -1
                else:
                    row -= 1
                    col += 1
            else:
                # Downward diagonal traversal
                if row == m - 1:
                    col += 1
                    direction = 1
                elif col == 0:
                    row += 1
                    direction = 1
                else:
                    row += 1
                    col -= 1

        return result
