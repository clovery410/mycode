class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0]) if len(matrix) > 0 else 0
        self.total = [[0 for x in xrange(n + 1)] for x in xrange(m + 1)]
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                self.total[i][j] = matrix[i-1][j-1] + self.total[i-1][j] + self.total[i][j-1] - self.total[i-1][j-1]
        
    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.total[row2+1][col2+1] - self.total[row1][col2+1] - self.total[row2+1][col1] + self.total[row1][col1]

if __name__ == "__main__":
    matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
    sol = NumMatrix(matrix)
    print sol.sumRegion(2, 1, 4, 3)
