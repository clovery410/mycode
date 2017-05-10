from collections import deque
class Solution(object):
    def numIslands(self, grid):
        def bfs(x, y):
            if x >= 1 and grid[x-1][y] == '1' and (x-1, y) not in visited:
                visited[(x-1, y)] = True
                bfs(x - 1, y)
            if x+1 < m and grid[x+1][y] == '1' and (x+1, y) not in visited:
                visited[(x+1, y)] = True
                bfs(x + 1, y)
            if y >= 1 and grid[x][y-1] == '1' and (x, y-1) not in visited:
                visited[(x, y-1)] = True
                bfs(x, y - 1)
            if y+1 < n and grid[x][y+1] == '1' and (x, y+1) not in visited:
                visited[(x, y+1)] = True
                bfs(x, y + 1)
                
        m, n = len(grid), len(grid[0]) if len(grid) > 0 else 0
        count = 0
        visited = {}
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == '1' and (i, j) not in visited:
                    count += 1
                    bfs(i, j)
        return count

    #solution2, use queue to do it iteratively, faster than recursive solution
    def numIslands2(self, grid):
        m, n = len(grid), len(grid[0]) if len(grid) > 0 else 0
        if m == 0 or n == 0: return 0

        count = 0
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == '1':
                    count += 1
                    queue = deque([(i, j)])
                    while queue:
                        cur_i, cur_j = queue.popleft()
                        if grid[cur_i][cur_j] == '1':
                            grid[cur_i][cur_j] = '0'
                            if cur_i > 0: queue.append((cur_i-1, cur_j))
                            if cur_i < m - 1: queue.append((cur_i+1, cur_j))
                            if cur_j > 0: queue.append((cur_i, cur_j-1))
                            if cur_j < n - 1: queue.append((cur_i, cur_j+1))
        return count
        
if __name__ == "__main__":
    sol = Solution()
    grid = [['1','1','0','0','0'], ['1','1','0','0','0'], ['0','0','1','0','0'], ['0','0','0','1','1']]
    grid2 = [['1','1','1'], ['0','1','0'], ['1','1','1']]
    print sol.numIslands(grid2)
    print sol.numIslands2(grid2)
