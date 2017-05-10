class Solution(object):
    def solveNQueens(self, n):
        def placeQueens(idx, all_sols):
            if idx >= n:
                all_sols.append(list('.' * x + 'Q' + '.' * (n-1-x) for x in column))
                # all_sols.append(column[:])
                return
            for j in xrange(n):
                if checkValid(idx, j, column):
                    column[idx] = j
                    placeQueens(idx+1, all_sols)

        def checkValid(r, c, column):
            for i in xrange(r):
                dig_left, dig_right = c - (r - i), c + (r - i)

                #check column
                if column[i] == c:
                    return False
                #check diagonal
                if dig_left >= 0 and column[i] == dig_left or dig_right < n and column[i] == dig_right:
                    return False
            return True

        column = [None] * n
        res = []
        placeQueens(0, res)
        return res

if __name__ == "__main__":
    sol = Solution()
    print sol.solveNQueens(4)
