import copy
class Solution(object):
    def eightQueens(self):
        def placeQueens(idx, all_sols):
            if idx >= len(grid):
                all_sols.append(copy.deepcopy(grid))
                return
            for j in xrange(8):
                grid[idx][j] = 1
                if checkValid(idx, j, grid):
                    placeQueens(idx+1, all_sols)
                grid[idx][j] = 0

        def checkValid(r, c, grid):
            for i in xrange(r):
                dig_left, dig_right = c - (r - i), c + (r - i)
                if grid[i][c] == 1:
                    return False
                if dig_left >= 0 and grid[i][dig_left] == 1 or dig_right < 8 and grid[i][dig_right] == 1:
                    return False
            return True
        
        grid = [[0 for x in xrange(8)] for x in xrange(8)]
        res = []
        placeQueens(0, res)
        return len(res)

    #solution2, optimize space complexcity to 1 dimension since each row we only have one queen, single array column[r] = c indicates row r has a queen at column c.
    def eightQueens2(self):
        def placeQueens(idx, all_sols):
            if idx >= 8:
                all_sols.append(column[:])
                return
            for j in xrange(8):
                if checkValid(idx, j, column):
                    column[idx] = j
                    placeQueens(idx+1, all_sols)

        def checkValid(r, c, column):
            for i in xrange(r):
                dig_left, dig_right = c - (r - i), c + (r - i)
                if column[i] == c:
                    return False
                if dig_left >= 0 and column[i] == dig_left or dig_right < 8 and column[i] == dig_right:
                    return False
            return True
        
        column = [None] * 8
        res = []
        placeQueens(0, res)
        return res


if __name__ == "__main__":
    sol = Solution()
    print sol.eightQueens2()
            

