class Solution(object):
    def solveSudoku(self, board):
        def checkValid(cur_i, cur_j):
            # check row
            row_used = set()
            for j in xrange(9):
                cur = board[cur_i][j]
                if cur in row_used: return False
                if cur != '.': row_used.add(cur)

            # check column
            col_used = set()
            for i in xrange(9):
                cur = board[i][cur_j]
                if cur in col_used: return False
                if cur != '.': col_used.add(cur)

            return True

        def solve(s_i, s_j):
            if s_i == 9:
                return True
            if s_j == 9:
                return slove(s_i + 1, 0)
            if board[s_i][s_j] == '.':
                k = s_i / 3 * 3 + s_j / 3
                for num in candidates[k]:
                    board[s_i][s_j] = num
                    candidates[k].remove(num)
                    if checkValid(s_i, s_j) and slove(s_i, s_j + 1):
                        return True
                    candidates[k].add(num)
                    board[s_i][s_j] = '.'
                return False
            else:
                return solve(s_i, s_j + 1)
                        
        # preprocess
        candidates = [{'1','2','3','4','5','6','7','8','9'} for x in xrange(9)]
        for k in xrange(9):
            s_i, s_j = k / 3 * 3, k % 3 * 3
            for i in xrange(s_i, s_i + 3):
                for j in xrange(s_j, s_j + 3):
                    candidates[k].discard(board[i][j])

        solve(0, 0)
                        
            
