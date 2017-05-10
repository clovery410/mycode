class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def helper(word, idx, row, col, visited):
            if idx >= len(word):
                return True
            if (row, col) in visited:
                return False
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return False
            elif word[idx] == board[row][col]:
                print row, col, idx, word[idx]
                visited[(row, col)] = 1
                if helper(word, idx + 1, row - 1, col, visited):
                    return True
                elif helper(word, idx + 1, row + 1, col, visited):
                    return True
                elif helper(word, idx + 1, row, col - 1, visited):
                    return True
                elif helper(word, idx + 1, row, col + 1, visited):
                    return True
                else:
                    del visited[(row, col)]
                    return False
            else:
                return False
            
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == word[0]:
                    visited = {}
                    if helper(word, 0, i, j, visited):
                        return True
        return False


if __name__ == '__main__':
    sol = Solution()
    board = ["ABCE", "SFES", "ADEE"]
    word = "ABCESEEEFS"
    print sol.exist(board, word)
