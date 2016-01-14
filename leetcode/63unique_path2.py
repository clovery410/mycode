class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        if obstacleGrid[row-1][col-1] == 1:
            return 0
        
        path = [[1 for x in xrange(col)] for x in xrange(row)]
        _i, _j = row, col
        
        for i in reversed(xrange(row)):
            if obstacleGrid[i][0] == 1:
                _i = i
        while _i < row:
            path[_i][0] = 0
            _i += 1
            
        for j in reversed(xrange(col)):
            if obstacleGrid[0][j] == 1:
                _j = j
        while _j < col:
            path[0][_j] = 0
            _j += 1
            
        for i in xrange(1, row):
            for j in xrange(1, col):
                if obstacleGrid[i-1][j] == 1 and obstacleGrid[i][j-1] == 1:
                    path[i][j] = 0
                elif obstacleGrid[i-1][j] == 1:
                    path[i][j] = path[i][j-1]
                elif obstacleGrid[i][j-1] == 1:
                    path[i][j] = path[i-1][j]
                else:
                    path[i][j] = path[i-1][j] + path[i][j-1]
                    
        return path[row-1][col-1]

if __name__ == '__main__':
    sol = Solution()
    grid = [[0,0,0],[0,1,0],[0,0,0]]
    print sol.uniquePathsWithObstacles(grid)
