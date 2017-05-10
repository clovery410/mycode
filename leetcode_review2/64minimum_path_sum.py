class Solution(object):
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0]) if len(grid) > 0 else 0
        if m == 0 or n == 0:
            return 0
        sums = grid[0]
        for j in xrange(1, n):
            sums[j] += sums[j-1]

        for i in xrange(1, m):
            for j in xrange(n):
                if j == 0:
                    sums[j] += grid[i][0]
                else:
                    sums[j] = min(sums[j], sums[j-1]) + grid[i][j]
                    
        return sums[-1]
