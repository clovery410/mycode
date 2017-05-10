import collections
class Solution(object):
    def solve(self, board):
        if board is None or len(board) == 0:
            return
        row, col = len(board), len(board[0])
        queue = collections.deque([])

        for i in xrange(row):
            board[i] = list(board[i])
        for i in xrange(row):
            for j in xrange(col):
                if (i in [0, row-1] or j in [0, col-1]) and board[i][j] == 'O':
                    queue.append((i, j))
        while queue:
            i, j = queue.popleft()
            if board[i][j] == "O":
                board[i][j] = "V"
                if i > 0:
                    queue.append((i-1, j))
                if i < row - 1:
                    queue.append((i+1, j))
                if j > 0:
                    queue.append((i, j-1))
                if j < col - 1:
                    queue.append((i, j+1))

        for i in xrange(row):
            for j in xrange(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "V":
                    board[i][j] = "O"
        for i in xrange(row):
            board[i] = ''.join(board[i])

if __name__ == "__main__":
    sol = Solution()
    board = ["OXXOX","XOOXO","XOXOX","OXOOO","XXOXO"]
    sol.solve(board)
    print board
                        
                    
