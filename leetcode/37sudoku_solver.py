class Solution(object):
    def solveSudoku(self, board):
        self.board = board
        self.val = self.available_val()
        self.solver()

    def available_val(self):
        num = '123456789'
        val, d = {}, {}
        for i in xrange(9):
            for j in xrange(9):
                elem = self.board[i][j]
                if elem != '.':
                    d[('r', i)] = d.get(('r', i), []) + [elem]
                    d[('c', j)] = d.get(('c', j), []) + [elem]
                    d[(i//3, j//3)] = d.get((i//3, j//3), []) + [elem]
                else:
                    val[(i, j)] = []
        for (i, j) in val.keys():
            inval = d.get(('r', i), []) + d.get(('c', j), []) + d.get((i//3, j//3), [])
            val[(i, j)] = [x for x in num if x not in inval]
        return val

    def solver(self):
        if len(self.val) == 0:
            return True
        kee = min(self.val.keys(), key = lambda x: len(self.val[x]))
        nums = self.val[kee]
        for num in nums:
            update = {kee: self.val[kee]}
            if self.validOne(num, kee, update):
                if self.solver():
                    return True
            self.undo(kee, update)
        return False

    def validOne(self, num, kee, update):
        self.board[kee[0]][kee[1]] = num
        del self.val[kee]
        i, j = kee
        for idx in self.val.keys():
            if num in self.val[idx]:
                if idx[0] == i or idx[1] == j or (idx[0]/3, idx[1]/3) == (i/3, j/3):
                    update[idx] = num
                    self.val[idx].remove(num)
                    if len(self.val[idx]) == 0:
                        return False
        return True

    def undo(self, kee, update):
        self.board[kee[0]][kee[1]] = '.'
        for k in update:
            if k not in self.val:
                self.val[k] = update[k]
            else:
                self.val[k].append(update[k])
        return None
        
                    
        

sol = Solution()
board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
sol.solveSudoku(board)
