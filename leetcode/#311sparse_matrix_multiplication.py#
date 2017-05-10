class Solution(object):
    def multiply(self, A, B):
        row = len(A)
        col = len(B[0])
        count = len(A[0])
        res = [[0 for x in xrange(col)] for x in xrange(row)]
    
        for i in xrange(row):
            for k in xrange(count):
                if A[i][k] != 0:
                    for j in xrange(col):
                        res[i][j] += A[i][k] * B[k][j]
                
        return res
