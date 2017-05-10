class Solution(object):
    def generateMatrix(self, n):
        start_i = start_j = 0
        end_i = end_j = n - 1
        num = 1
        matrix = [[0 for x in xrange(n)] for x in xrange(n)]
        while start_i <= end_i and start_j <= end_j:
            for j in xrange(start_j, end_j + 1):
                matrix[start_i][j] = num
                num += 1
            start_i += 1

            for i in xrange(start_i, end_i + 1):
                matrix[i][end_j] = num
                num += 1
            end_j -= 1

            for j in reversed(xrange(start_j, end_j + 1)):
                matrix[end_i][j] = num
                num += 1
            end_i -= 1

            for i in reversed(xrange(start_i, end_i + 1)):
                matrix[i][start_j] = num
                num += 1
            start_j += 1
            
        return matrix
            
