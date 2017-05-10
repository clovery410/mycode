class Solution(object):
    #solution1, wrote by myself after studying the case in N-Queens
    def solveSudoku(self, board):
        def solve(r, c):
            if r == 9:
                return True
            if c == 9:
                return solve(r+1, 0)
            if board[r][c] == '.':
                k = r / 3 * 3+ c / 3
                for num in candidates[k]:
                    board[r][c] = num
                    candidates[k].remove(num)   # remove current subbox available candidates for next recursion
                    if checkValid(r, c) and solve(r, c+1):
                        return True
                    candidates[k].add(num)     # add back that candidate in to current subbox available candidates
                    board[r][c] = '.'
                return False
            else:
                return solve(r, c+1)

        def checkValid(row, col):
            # check row:
            cur_row = set()
            for j in range(9):
                if board[row][j] in cur_row: return False
                if board[row][j] != '.': cur_row.add(board[row][j])
            # check col:
            cur_col = set()
            for i in range(9):
                if board[i][col] in cur_col: return False
                if board[i][col] != '.': cur_col.add(board[i][col])
            return True

        candidates = self.getCandidates(board)
        print solve(0, 0)
        return board
        
    def getCandidates(self, board):
        candidates = []
        all_num = {'1','2','3','4','5','6','7','8','9'}
        for k in range(9):
            cur_subbox = set()
            r, c = k / 3 * 3, k % 3 * 3
            for i in range(3):
                for j in range(3):
                    if board[r+i][c+j] != '.': cur_subbox.add(board[r+i][c+j])
            candidates.append(all_num.difference(cur_subbox))
        return candidates

    # #solution2, re-study the solution wrote last time
    # def solveSudoku2(self, board):
        

if __name__ == "__main__":
    sol = Solution()
    board = [['5','3','.','.','7','.','.','.','.'],
             ['6','.','.','1','9','5','.','.','.'],
             ['.','9','8','.','.','.','.','6','.'],
             ['8','.','.','.','6','.','.','.','3'],
             ['4','.','.','8','.','3','.','.','1'],
             ['7','.','.','.','2','.','.','.','6'],
             ['.','6','.','.','.','.','2','8','.'],
             ['.','.','.','4','1','9','.','.','5'],
             ['.','.','.','.','8','.','.','7','9']]
    print sol.solveSudoku(board)
