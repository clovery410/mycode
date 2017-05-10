def generateMatrix(n):
    if n == 0:
        return []
    matrix = [[0 for x in xrange(n)] for x in xrange(n)]
    start_row, end_row = 0, n-1
    start_col, end_col = 0, n-1
    num = 1

    while start_row <= end_row and start_col <= end_col:
        for j in xrange(start_col, end_col+1):
            matrix[start_row][j] = num
            num += 1
        start_row += 1

        for i in xrange(start_row, end_row+1):
            matrix[i][end_col] = num
            num += 1
        end_col -= 1

        for j in reversed(xrange(start_col, end_col+1)):
            matrix[end_row][j] = num
            num += 1
        end_row -= 1

        for i in reversed(xrange(start_row, end_row+1)):
            matrix[i][start_col] = num
            num += 1
        start_col += 1
    return matrix

if __name__ == "__main__":
    print generateMatrix(4)
