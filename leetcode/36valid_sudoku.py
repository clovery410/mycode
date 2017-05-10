class Solution(object):
    def isValidSudoku(self, board):
        n = len(board)

        #check row
        for i in xrange(n):
            curr_row = set()
            for j in xrange(n):
                if board[i][j] in curr_row:
                    return False
                if board[i][j] != '.':
                    curr_row.add(board[i][j])

        #check column
        for j in xrange(n):
            curr_col = set()
            for i in xrange(n):
                if board[i][j] in curr_col:
                    return False
                if board[i][j] != '.':
                    curr_col.add(board[i][j])

        #check sub-box
        row = col = 0
        while row <= n:
            curr_box = set()
            for i in xrange(3):
                for j in xrange(3):
                    if board[row+i][col+j] in curr_box:
                        return False
                    if board[row+i][col+j] != '.':
                        curr_box.add(board[row+i][col+j])
            col += 3
            if col >= n:
                row += 3
                col = 0

        return True
