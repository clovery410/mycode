class NumMatrix(object):
    # this solution is a little bit slow since it still cost O(n) time to calculate sumRegion
    # def __init__(self, matrix):
    #     self.sums = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix))]
    #     for i in range(len(matrix)):
    #         for j in range(1, len(matrix[0]) + 1):
    #             self.sums[i][j] = self.sums[i][j-1] + matrix[i][j-1]
        
    # def sumRegion(self, row1, col1, row2, col2):
    #     return sum(self.sums[i][col2+1] - self.sums[i][col1] for i in range(row1, row2+1))

    def __init__(self, matrix):
        self.matrix = matrix
        row, col = len(matrix), len(matrix[0]) if matrix else 0
        self.sums = [[0 for _ in range(col + 1)] for _ in range(row + 1)]
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                self.sums[i][j] = self.sums[i-1][j] + self.sums[i][j-1] - self.sums[i-1][j-1] + matrix[i-1][j-1]
    def sumRegion(self, row1, col1, row2, col2):
        if not self.matrix or not self.matrix[0]:
            return 0
        return self.sums[row2+1][col2+1] - self.sums[row1][col2+1] - self.sums[row2+1][col1] + self.sums[row1][col1]
    
if __name__ == "__main__":
    matrix = NumMatrix([[3,0,1,4,2], [5,6,3,2,1], [1,2,0,1,5], [4,1,0,1,7], [1,0,3,0,5]])
    matrix2 = NumMatrix([])
    print matrix2.sumRegion(1,1,2,2)
