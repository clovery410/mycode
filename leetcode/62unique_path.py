class Solution(object):
    def uniquePaths(self, m, n):
        path = [[1 for x in xrange(n)] for x in xrange(m)]

        for i in xrange(1, m):
            for j in xrange(1, n):
                path[i][j] = path[i-1][j] + path[i][j-1]

        return path[m-1][n-1]

if __name__ == '__main__':
    sol = Solution()
    print sol.uniquePaths(3, 7)
