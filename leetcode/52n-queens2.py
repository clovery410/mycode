class Solution(object):
    def totalNQueens(self, n):
        def generate(idx):
            if idx >= n:
                self.count += 1
                return
            for j in xrange(n):
                if checkValid(idx, j):
                    column[idx] = j
                    generate(idx+1)
        def checkValid(r, c):
            for i in xrange(r):
                dia_left, dia_right = c - (r - i), c + (r - i)

                #check same column
                if column[i] == c:
                    return False
                #check diagonal
                if dia_left >= 0 and column[i] == dia_left or dia_right < n and column[i] == dia_right:
                    return False
            return True
        
        self.count = 0
        column = [None] * n
        generate(0)
        return self.count

if __name__ == "__main__":
    sol = Solution()
    print sol.totalNQueens(8)

            
                    
        
