class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        # first reverse horizontally
        for i in xrange(n):
            for j in xrange(n/2):
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]

        # then reversed diagonally
        for i in xrange(n):
            for j in xrange(n-i):
                matrix[i][j], matrix[n-1-j][n-1-i] = matrix[n-1-j][n-1-i], matrix[i][j]
                
        return matrix
        
