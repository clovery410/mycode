class Solution(object):
    def isValidSudoku(self, board):
        # check row
        for i in xrange(9):
            row_set = set()
            for j in xrange(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] not in row_set:
                    row_set.add(board[i][j])
                else:
                    return False

        # check column
        for j in xrange(9):
            col_set = set()
            for i in xrange(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] not in col_set:
                    col_set.add(board[i][j])
                else:
                    return False

        # check sub-board
        for k in xrange(9):
            s_i = k /3 * 3
            s_j = k % 3 * 3
            sub_set = set()
            for i in xrange(s_i, s_i+3):
                for j in xrange(s_j, s_j+3):
                    if board[i][j] == '.':
                        continue
                    if board[i][j] not in sub_set:
                        sub_set.add(board[i][j])
                    else:
                        return False
        return True

    # more concise version
    def isValidSudoku(self, board):
        # check row
        for i in xrange(9):
            row_set = set()
            for j in xrange(9):
                if board[i][j] in row_set: return False
                if board[i][j] != '.': row_set.add(board[i][j])

        # check column
        for j in xrange(9):
            col_set = set()
            for i in xrange(9):
                if board[i][j] in col_set: return False
                if board[i][j] != '.': col_set.add(board[i][j])

        # check sub-board
        for k in xrange(9):
            s_i = k /3 * 3
            s_j = k % 3 * 3
            sub_set = set()
            for i in xrange(s_i, s_i+3):
                for j in xrange(s_j, s_j+3):
                    if board[i][j] in sub_set: return False
                    if board[i][j] != '.': sub_set.add(board[i][j])

        return True


