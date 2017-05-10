#solution1, O(n) average move solution, but use O(n^2) space and also O(n^2) preprocess, need to be optimize further
class TicTacToe(object):
    def __init__(self, n):
        self.board = [[None] * n for x in range(n)]
        self.length = n
        
    def move(self, row, col, player):
        """
        @param row The row of the board
        @param col The col of the board
        @param player The player, can be either 1, or 2
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins
                2: Player 2 wins
        """
        if player == 1:
            self.board[row][col] = 'X'
        else:
            self.board[row][col] = 'O'
        return self.checkResult(row, col, player)

    def checkResult(self, row, col, player):
        symbol = 'X' if player == 1 else 'O'
        #check row
        if all(elem == symbol for elem in self.board[row]): return player

        #check col
        if all(row[col] == symbol for row in self.board): return player

        #check diagonal
        if all(self.board[x][x] == symbol for x in range(self.length)): return player
        if all(self.board[x][self.length-1-x] == symbol for x in range(self.length)): return player

        #otherwise, return 0
        return 0

#solution2, use extra space rows, cols, and two variable diagonal, anti_diagonal to denote each row, col and two diagonals accumulative values, if player is 1, always add 1, if player is 2, always minus 1. In this way, if any rows, cols diagonals val equals to n means player1 wins, if equals to -n, means player2 win.
class TicTacToe2(object):
    def __init__(self, n):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0

    def move(self, row, col, player):
        if player == 1:
            self.rows[row] += 1
            self.cols[col] += 1
            if row == col: self.diagonal += 1
            if row + col == self.n - 1: self.anti_diagonal += 1
        else:
            self.rows[row] -= 1
            self.cols[col] -= 1
            if row == col: self.diagonal -= 1
            if row + col == self.n - 1: self.anti_diagonal -= 1

        val = self.n if player == 1 else -self.n
        if self.rows[row] == val or self.cols[col] == val or self.diagonal == val or self.anti_diagonal == val:
            return player
        return 0

if __name__ == "__main__":
    toe = TicTacToe2(3)
    print toe.move(0, 0, 1)
    print toe.move(0, 2, 2)
    print toe.move(2, 2, 1)
    print toe.move(1, 1, 2)
    print toe.move(2, 0, 1)
    print toe.move(1, 0, 2)
    print toe.move(2, 1, 1)
    
        
