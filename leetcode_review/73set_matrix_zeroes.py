class Solution(object):
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0]) if len(matrix) > 0 else 0
        if m == 0 or n == 0: return

        last_row = last_col = False
        if matrix[-1][-1] == 0:
            last_row = last_col = True
        if any(x == 0 for x in matrix[-1]):
            last_row = True
        if any(x[-1] == 0 for x in matrix):
            last_col = True

        for i in xrange(m-1):
            for j in xrange(n-1):
                if matrix[i][j] == 0:
                    matrix[-1][j] = 0
                    matrix[i][-1] = 0

        for i in xrange(m-1):
            if matrix[i][-1] == 0:
                for j in xrange(n-1):
                    matrix[i][j] = 0
        for j in xrange(n-1):
            if matrix[-1][j] == 0:
                for i in xrange(m-1):
                    matrix[i][j] = 0

        if last_row:
            for j in xrange(n):
                matrix[-1][j] = 0
        if last_col:
            for i in xrange(m):
                matrix[i][-1] = 0
