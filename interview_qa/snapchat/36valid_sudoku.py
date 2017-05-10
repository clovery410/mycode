class Solution(object):
    def isValidSudoku(self, board):
        # check line
        for i in xrange(9):
            used = set()
            for j in xrange(9):
                cur = board[i][j]
                if cur != '.' and cur in used:
                    return False
                used.add(cur)

        # check column
        for j in xrange(9):
            used = set()
            for i in xrange(9):
                cur = board[i][j]
                if cur != '.' and cur in used:
                    return False
                used.add(cur)

        # check 3 x 3 subboard
        for k in xrange(9):
            start_i, start_j = k / 3 * 3, k % 3 * 3
            used = set()
            for i in xrange(start_i, start_i + 3):
                for j in xrange(start_j, start_j + 3):
                    cur = board[i][j]
                    if cur != '.' and cur in used:
                        return False
                    used.add(cur)
        return True
