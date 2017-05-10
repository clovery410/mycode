class Solution(object):
    def exist(self, board, word):
        def dfs(cur_i, cur_j, idx):
            if idx == len(word):
                return True
            if 0 <= cur_i < m and 0 <= cur_j < n and board[cur_i][cur_j] == word[idx]:
                temp = board[cur_i][cur_j]
                board[cur_i][cur_j] = '#'
                for offset_i, offset_j in directions:
                    if dfs(cur_i + offset_i, cur_j + offset_j, idx+1):
                        return True
                board[cur_i][cur_j] = temp
                
            return False
        
        m, n = len(board), len(board[0]) if len(board) > 0 else 0
        if m == 0 or n == 0:
            return False
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True

        return False
                    
                        
