class Solution(object):
    def gameOfLife(self, board):
        neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        m, n = len(board), len(board[0]) if len(board) > 0 else 0
        for i in xrange(m):
            for j in xrange(n):
                live_count = 0
                for diff_x, diff_y in neighbors:
                    x, y = i + diff_x, j + diff_y
                    if 0 <= x < m and 0 <= y < n and board[x][y] & 1 == 1:
                        live_count += 1
                if live_count == 3 or board[i][j] + live_count == 3:
                    board[i][j] += 2

        for i in xrange(m):
            for j in xrange(n):
                board[i][j] >>= 1
        return board
