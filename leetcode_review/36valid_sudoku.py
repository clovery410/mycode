class Solution(object):
    def isValidSudoku(self, board):
        # check row
        for i in range(9):
            cur_row = set()
            for j in range(9):
                if board[i][j] in cur_row: return False
                if board[i][j] != '.': cur_row.add(board[i][j])

        # check column
        for j in range(9):
            cur_column = set()
            for i in range(9):
                if board[i][j] in cur_column: return False
                if board[i][j] != '.': cur_column.add(board[i][j])

        # check sub-box
        for k in range(9):
            cur_subbox = set()
            r, c = k / 3 * 3, k % 3 * 3
            for i in range(3):
                for j in range(3):
                    if board[r+i][c+j] in cur_subbox: return False
                    if board[r+i][c+j] != '.': cur_subbox.add(board[r+i][c+j])

        return True
