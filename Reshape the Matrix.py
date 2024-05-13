class Solution(object):
    def matrixReshape(self, mat, r, c):
        width = len(mat[0])
        height = len(mat)

        if width * height != r*c:
            return mat 

        mat1 = []
        for i in range(r):
            mat1.append([])
        
        counter= 0
        row_c = 0
        for i in range(height):
            for j in range(width):
                mat1[row_c].append(mat[i][j])
                counter += 1
                if counter >= c:
                    counter = 0
                    row_c += 1
        return mat1
