class Solution(object):
    def numIslands(self, grid):
        m, n = len(grid), len(grid[0]) if len(grid) > 0 else 0
        if m == 0 or n == 0:
            return 0
        count = 0

        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == '1':
                    count += 1
                    queue = collections.deque([(i, j)])
                    while queue:
                        cur_i, cur_j = queue.popleft()
                        if 0 <= cur_i < m and 0 <= cur_j < n and grid[cur_i][cur_j] == '1':
                            grid[cur_i][cur_j] = '0'
                            for offset_i, offset_j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                                queue.append((cur_i + offset_i, cur_j + offset_j))
        return count
                                
        
