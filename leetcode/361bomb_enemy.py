class Solution(object):
    def maxKilledEnemies(self, grid):
        m, n = len(grid), len(grid[0]) if len(grid) > 0 else 0
        score = [[0] * n for x in xrange(m)]
        res = 0

        # from up to down
        for j in xrange(n):
            accu_enemy = 0
            for i in xrange(1, m):
                pre = grid[i-1][j]
                if pre == 'E': accu_enemy += 1
                if pre == 'W': accu_enemy = 0
                if grid[i][j] =='0':
                    score[i][j] += accu_enemy
                    res = max(res, score[i][j])

        # from down to up
        for j in xrange(n):
            accu_enemy = 0
            for i in reversed(xrange(m-1)):
                pre = grid[i+1][j]
                if pre == 'E': accu_enemy += 1
                if pre == 'W': accu_enemy = 0
                if grid[i][j] == '0':
                    score[i][j] += accu_enemy
                    res = max(res, score[i][j])

        # from left to right
        for i in xrange(m):
            accu_enemy = 0
            for j in xrange(1, n):
                pre = grid[i][j-1]
                if pre == 'E': accu_enemy += 1
                if pre == 'W': accu_enemy = 0
                if grid[i][j] == '0':
                    score[i][j] += accu_enemy
                    res = max(res, score[i][j])

        # from right to left
        for i in xrange(m):
            accu_enemy = 0
            for j in reversed(xrange(n-1)):
                pre = grid[i][j+1]
                if pre == 'E': accu_enemy += 1
                if pre == 'W': accu_enemy = 0
                if grid[i][j] == '0':
                    score[i][j] += accu_enemy
                    res = max(res, score[i][j])
        return res

    #solution2
    def maxKilledEnemies2(self, grid):
        m, n = len(grid), len(grid[0]) if len(grid) > 0 else 0
        row_enemy, col_enemy = 0, [0] * n
        res = 0
        for i in xrange(m):
            for j in xrange(n):

                # no need to re-calculate enemy if there is no wall behind unless its a j == 0
                if j == 0 or grid[i][j-1] == 'W':
                    row_enemy = 0
                    for k in xrange(j, n):
                        if grid[i][k] == 'W':
                            break
                        row_enemy += grid[i][k] == 'E'

                # no need to re-calculate enemy if there is no wall behind unless its a i == 0
                if i == 0 or grid[i-1][j] == 'W':
                    col_enemy[j] = 0
                    for k in xrange(i, m):
                        if grid[k][j] == 'W':
                            break
                        col_enemy[j] += grid[k][j] == 'E'

                # empty spot, check res
                if grid[i][j] == '0':
                    res = max(res, row_enemy + col_enemy[j])
        return res
        
if __name__ == "__main__":
    sol = Solution()
    grid = [['0','E','0','0'],['E','0','W','E'],['0','E','0','0']]
    print sol.maxKilledEnemies(grid)
    print sol.maxKilledEnemies2(grid)
