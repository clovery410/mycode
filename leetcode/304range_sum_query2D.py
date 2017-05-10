class NumMatrix(object):
    def __init__(self, matrix):
        self.matrix = matrix
        self.mem = [[0 for x in xrange(len(matrix[0]))] for x in xrange(len(matrix))]
        for i in xrange(len(self.mem)):
            total = 0
            for j in xrange(len(self.mem[0])):
                total += self.matrix[i][j]
                self.mem[i][j] = total
                
                
    def sumRegion(self, row1, col1, row2, col2):
        total = 0
        for i in xrange(row1, row2+1):
            total += (self.mem[i][col2] - self.mem[i][col1] + self.matrix[i][col1])
        return total

# Solution 2, dp
class NumMatrix2(object):
    def __init__(self, matrix):
        self.matrix = matrix
        if not self.matrix:
            return
        self.mem = [[None for x in xrange(len(matrix[0]))] for x in xrange(len(matrix))]
        self.mem[0][0] = self.matrix[0][0]
        for i in xrange(1, len(self.mem)):
            self.mem[i][0] = self.mem[i-1][0] + self.matrix[i][0]
        for j in xrange(1, len(self.mem[0])):
            self.mem[0][j] = self.mem[0][j-1] + self.matrix[0][j]
        for i in xrange(1, len(self.mem)):
            for j in xrange(1, len(self.mem[0])):
                self.mem[i][j] = self.matrix[i][j] + self.mem[i-1][j] + self.mem[i][j-1] - self.mem[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        if not self.matrix:
            return 0
        if row1 == col1 == 0:
            return self.mem[row2][col2]
        elif row1 == 0:
            return self.mem[row2][col2] - self.mem[row2][col1-1]
        elif col1 == 0:
            return self.mem[row2][col2] - self.mem[row1-1][col2]
        else:
            return self.mem[row2][col2] - self.mem[row1-1][col2] - self.mem[row2][col1-1] + self.mem[row1-1][col1-1]

# Solution3, add one more row and one more column to remove corner case
class NumMatrix3(object):
    def __init__(self, matrix):
        self.matrix = matrix
        row = len(matrix)
        col = len(matrix[0]) if row > 0 else 0
        self.mem = [[0 for x in xrange(col + 1)] for x in xrange(row + 1)]
        for i in xrange(1, row+1):
            for j in xrange(1, col+1):
                self.mem[i][j] = self.matrix[i-1][j-1] + self.mem[i-1][j] + self.mem[i][j-1] - self.mem[i-1][j-1]
        print self.mem

    def sumRegion(self, row1, col1, row2, col2):
        if not self.matrix:
            return 0
        return self.mem[row2+1][col2+1] - self.mem[row1][col2+1] - self.mem[row2+1][col1] + self.mem[row1][col1]
    
# Your NumMatrix object will be instantiated and called as such:
matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
matrix2 = []
numMatrix = NumMatrix(matrix)
numMatrix2 = NumMatrix2(matrix2)
numMatrix3 = NumMatrix3(matrix2)
#print numMatrix.mem
#print numMatrix2.mem
print numMatrix.sumRegion(2, 1, 4, 3)
print numMatrix.sumRegion(1, 1, 2, 2)
print numMatrix2.sumRegion(2, 1, 4, 3)
print numMatrix2.sumRegion(1, 1, 2, 2)
print numMatrix3.sumRegion(2, 1, 4, 3)
print numMatrix3.sumRegion(1, 1, 2, 2)
