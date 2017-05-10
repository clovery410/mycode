class Solution(object):
    def gameOfLife(self, board):
        row, col = len(board), len(board[0]) if len(board) > 0 else 0
        flip = []
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        for i in xrange(row):
            for j in xrange(col):
                neighbor_live = 0
                for diff_x, diff_y in directions:
                    neighbor_i, neighbor_j = i + diff_x, j + diff_y
                    if 0 <= neighbor_i < row and 0 <= neighbor_j < col:
                        if board[neighbor_i][neighbor_j] == 1:
                            neighbor_live += 1
                if board[i][j] == 1 and (neighbor_live < 2 or neighbor_live > 3):
                    flip.append((i, j))
                if board[i][j] == 0 and neighbor_live == 3:
                    flip.append((i, j))
        for i, j in flip:
            board[i][j] ^= 1

    #solution2, use O(1) space, which make use of second bit to store the informatin for next state
    def gameOfLife2(self, board):
        m, n = len(board), len(board[0]) if len(board) > 0 else 0
        for i in xrange(m):
            for j in xrange(n):
                live_count = 0
                for ii in xrange(max(0, i-1), min(i+2, m)):
                    for jj in xrange(max(0, j-1), min(j+2, n)):
                        live_count += board[ii][jj] & 1
                if live_count == 3 or live_count - board[i][j] == 3:
                    board[i][j] |= 2
                    
        for i in xrange(m):
            for j in xrange(n):
                board[i][j] >>= 1
        
        
                    
        
