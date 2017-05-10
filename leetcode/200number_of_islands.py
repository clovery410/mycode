from collections import deque
class Solution(object):
    def numIslands(self, grid):
        if len(grid) == 0:
            return 0
        
        m, n = len(grid), len(grid[0])
        res = 0
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == '1':
                    res += 1
                    grid[i][j] = '0'
                    queue = deque([(i-1, j), (i+1, j), (i, j-1), (i, j+1)])
                    while queue:
                        cur_i, cur_j = queue.popleft()
                        if 0 <= cur_i < m and 0 <= cur_j < n and grid[cur_i][cur_j] == '1':
                            grid[cur_i][cur_j] = '0'
                            queue.append((cur_i-1, cur_j))
                            queue.append((cur_i+1, cur_j))
                            queue.append((cur_i, cur_j-1))
                            queue.append((cur_i, cur_j+1))
        return res
                        
        
