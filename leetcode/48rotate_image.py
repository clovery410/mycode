class Solution(object):
    # Brute-force, O(n^2) space
    def rotate(self, matrix):
        row = col = len(matrix)
        new_matrix = [[0 for x in xrange(row)] for x in xrange(row)]

        for i in xrange(row):
            for j in xrange(col):
                new_matrix[j][i] = matrix[col-1-i][j]

        print new_matrix

    def rotate_inplace(self, matrix):
        n = len(matrix)
        for i in xrange(n-1):
            for j in xrange(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        mid = n / 2
        for i in xrange(n):
            j = 0
            while j < n / 2:
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]
                j += 1
        print matrix
        
matrix = [[1,2,3], [4,5,6], [7,8,9]]
sol = Solution()
sol.rotate_inplace(matrix)
                
        
