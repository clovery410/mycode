class Solution(object):
    def exist(self, board, word):
        def check(idx, r, c):
            if idx >= len(word):
                return True
            if 0 <= r < m and 0 <= c < n and board[r][c] == word[idx]:
                temp = board[r][c]
                board[r][c] = '#'
                if check(idx+1, r+1, c) or check(idx+1, r-1, c) or check(idx+1, r, c+1) or check(idx+1, r, c-1):
                    return True
                board[r][c] = temp
            return False

        m, n = len(board), len(board[0]) if len(board) > 0 else 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and check(0, i, j):
                    return True
        return False

if __name__ == "__main__":
    sol = Solution()
    board = [['A','B','C','E'],
             ['S','F','C','S'],
             ['A','D','E','E']]
    word = "SEE"
    print sol.exist(board, word)
