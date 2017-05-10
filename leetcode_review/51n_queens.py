class Solution(object):
    def solveNQueens(self, n):
        def placeQueen(row, all_sols):
            if row >= n:
                all_sols.append(list('.' * x + 'Q' + '.' * (n-x-1) for x in column))
                return
            for col in xrange(n):
                column[row] = col
                if checkValid(row, col):
                    placeQueen(row+1, all_sols)

        def checkValid(r, c):
            for i in xrange(r):
                # check column
                if column[i] == c:
                    return False

                # check diagonal
                dia_left, dia_right = c - (r - i), c + (r - i)
                if (dia_left >= 0 and column[i] == dia_left) or (dia_right < n and column[i] == dia_right):
                    return False
            return True

        column = [None] * n
        res = []
        placeQueen(0, res)
        return res

if __name__ == "__main__":
    sol = Solution()
    print sol.solveNQueens(4)
