class Solution(object):
    def maxKilledEnemies(self, grid):
        m, n = len(grid), len(grid[0]) if len(grid) > 0 else 0
        row_enemy = 0
        col_enemy = [0] * n
        res = 0
                    
        for i in xrange(m):
            for j in xrange(n):
                # re-calculate row enemy
                if j == 0 or grid[i][j-1] == 'W':
                    row_enemy = 0
                    for k in xrange(j, n):
                        if grid[i][k] == 'W': break
                        if grid[i][k] == 'E': row_enemy += 1

                # re-calculate col enemy
                if i == 0 or grid[i-1][j] == 'W':
                    col_enemy[j] = 0
                    for k in xrange(i, m):
                        if grid[k][j] == 'W': break
                        if grid[k][j] == 'E': col_enemy[j] += 1

                if grid[i][j] == '0':
                    res = max(res, row_enemy + col_enemy[j])
        return res
                    
                            
