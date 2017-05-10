class Solution(object):
    #Solution1, running time O(m^2 * n^2)
    def maxSumSubmatrix(self, matrix, k):
        m, n = len(matrix), len(matrix[0])
        res = sys.maxint
        areas = [[0 for x in xrange(n)] for x in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                area = matrix[i][j]
                if i >= 1:
                    area += areas[i-1][j]
                if j >= 1:
                    area += areas[i][j-1]
                if i >=1 and j >= 1:
                    area -= areas[i-1][j-1]
                areas[i][j] = area

        for i in xrange(m):
            for j in xrange(n):
                for ii in xrange(i, m):
                    for jj in xrange(j, n):
                        area = areas[ii][jj]
                        if i >= 1:
                            area -= areas[i-1][jj]
                        if j >= 1:
                            area -= areas[ii][j-1]
                        if i >= 1 and j >= 1:
                            area += areas[i-1][j-1]
                        if area <= k:
                            res = max(res, area)
        return res

    #Solution2
    def maxSumSubmatrix(self, matrix, k):
        m, n = len(matrix), len(matrix[0])
        areas = [[0 for x in xrange(n)] for x in xrange(m)]
        res = -sys.maxint - 1
        for i in xrange(m):
            areas[i][0] = matrix[i][0]
            for j in xrange(1, n):
                areas[i][j] = areas[i][j-1] + matrix[i][j]
        for j in xrange(n):
            for s in xrange(j, n):
                slst = [0]
                total = 0
                for i in xrange(m):
                    total += areas[i][s]
                    if j >= 1:
                        total -= areas[i][j-1]
                    #using sorted fact
                    u = bisect.bisect_left(slst, total - k)
                    if u <= i:
                        res = max(res, total - slst[u])
                        if res == k:
                            return res
                    bisect.insort(slst, total)
        return res
                
