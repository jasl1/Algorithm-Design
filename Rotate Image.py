class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        for step in range(n):
            if step == n-1-step:
                break
            
            for j in range(step, n-step-1):
                t1 = matrix[step][j] 
                t2 = matrix[j][n-step-1]
                t3 = matrix[n-step-1][n - 1 -j]
                t4 = matrix[n - 1 -j][step]

                matrix[j][n-step-1] = t1
                matrix[n-step-1][n - 1 -j] = t2
                matrix[n - 1 -j][step] = t3
                matrix[step][j] = t4
