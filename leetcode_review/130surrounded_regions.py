from collections import deque
import time
class Solution(object):
    def solve(self, board):
        if len(board) == 0 or len(board[0]) == 0:
            return board

        m, n = len(board), len(board[0])
        queue = deque([])
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == "O":
                    if i in (0, m-1) or j in (0, n-1):
                        queue.append((i-1, j))
                        queue.append((i+1, j))
                        queue.append((i, j-1))
                        queue.append((i, j+1))
                    else:
                        board[i][j] = "#"
        # mark = [[0 for x in range(n)] for x in xrange(m)]
        # for i in xrange(m):
        #     for j in xrange(n):
        #         if mark[i][j] == 0 and board[i][j] == "O":
        #             queue = deque([(i-1, j), (i+1, j), (i, j-1), (i, j+1)])
        #             mark[i][j] = 1
        #             while queue:
        #                 cur_i, cur_j = queue.popleft()
        #                 if 0 < cur_i < m-1 and 0 < cur_j < n-1 and board[cur_i][cur_j] == "#":
        #                     board[cur_i][cur_j] = "O"
        #                     mark[cur_i][cur_j] = 1
        #                     queue.append((cur_i-1, cur_j))
        #                     queue.append((cur_i+1, cur_j))
        #                     queue.append((cur_i, cur_j-1))
        #                     queue.append((cur_i, cur_j+1))
        while queue:
            cur_i, cur_j = queue.popleft()
            if 0 <= cur_i < m and 0 <= cur_j < n and board[cur_i][cur_j] == "#":
                board[cur_i][cur_j] = "O"
                queue.append((cur_i-1, cur_j))
                queue.append((cur_i+1, cur_j))
                queue.append((cur_i, cur_j-1))
                queue.append((cur_i, cur_j+1))
            
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == "#":
                    board[i][j] = "X"
        return board

    #Solution2, more effecient way
    def solve2(self, board):
        if board is None or len(board[0]) == 0:
            return board
        m, n = len(board), len(board[0])
        queue = deque([])
        for i in xrange(m):
            for j in xrange(n):
                if (i in (0, m-1) or j in (0, n-1)) and board[i][j] == "O":
                    queue.append((i, j))
        while queue:
            cur_i, cur_j = queue.popleft()
            if 0 <= cur_i < m and 0 <= cur_j < n and board[cur_i][cur_j] == "O":
                board[cur_i][cur_j] = "V"
                queue.append((cur_i-1, cur_j))
                queue.append((cur_i+1, cur_j))
                queue.append((cur_i, cur_j-1))
                queue.append((cur_i, cur_j+1))
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "V":
                    board[i][j] = "O"
        return board

if __name__ == "__main__":
    board = [["X","X","X","O","X"], ["X","O","O","X","X"], ["X","X","X","O","X"], ["X","O","X","O","X"]]
    sol = Solution()
    time1 = time.time()
    print sol.solve(board)
    print "solution1 --- %s second ---" % (time.time() - time1)
    time2 = time.time()
    print sol.solve2(board)
    print "solution2 --- %s second ---" % (time.time() - time2)
                            
