class Solution(object):
    def maximalSquare(self, matrix):
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0
        if m == 0 or n == 0:
            return 0

        res = 0
        dp = [[0 for x in xrange(n)] for x in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 or j == 0:
                    dp[i][j] =int( matrix[i][j])
                elif matrix[i][j] == '0':
                    dp[i][j] = 0
                elif matrix[i-1][j] == '1' and matrix[i][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                else:
                    dp[i][j] = int(matrix[i][j])
                res = max(res, dp[i][j])
        return res * res

    # solution2, more concise
    def maximalSquare2(self, matrix):
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0
        if m == 0 or n == 0:
            return 0

        res = 0
        dp = [[int(x) for x in row]for row in matrix]
        for i in xrange(m):
            for j in xrange(n):
                if i > 0 and j > 0 and matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                res = max(res, dp[i][j])

        return res * res
                    
