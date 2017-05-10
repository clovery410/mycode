class Solution(object):
    def gameOfLife(self, board):
        """
        live cell < 2 or > 3 live -> die
        live cell 2 or 3 live -> live
        die cell 3 live -> live
        """
        m, n = len(board), len(board[0]) if len(board) > 0 else 0
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in xrange(m):
            for j in xrange(n):
                lives = 0
                for diff_i, diff_j in directions:
                    ii, jj = i + diff_i, j + diff_j
                    if 0 <= ii < m and 0 <= jj < n and  board[ii][jj] & 1 != 0:
                        lives += 1
                if lives == 3 or lives + board[i][j] == 3:
                    board[i][j] |= 1 << 1

        for i in xrange(m):
            for j in xrange(n):
                board[i][j] >>= 1
        
