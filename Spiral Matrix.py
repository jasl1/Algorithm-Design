class Solution(object):
    def spiralOrder(self, matrix):
        top = 0
        bottom = len(matrix) -1
        left = 0
        right = len(matrix[0]) -1
        output = []

        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                output.append(matrix[top][i])
            top+=1
            print(output,'\n')

            for j in range(top, bottom + 1):
                output.append(matrix[j][right])
            right -=1
            print(output,left, right,'\n')

            if top <= bottom: 
                for i in range(right, left - 1, -1):
                    output.append(matrix[bottom][i])
                bottom-=1
            print(output,'\n')


            if left <= right:
                for j in range(bottom, top - 1, -1):
                    output.append(matrix[j][left])
                left +=1
            print(output,'\n')

        return output
