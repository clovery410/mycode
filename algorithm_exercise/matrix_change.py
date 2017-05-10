# There is an M*N matrix, if matrix[i][j] == 0, convert all the elements on row i and column j to 0, pay attention to use as littl extra memory as possible

# Fisrt try, easy version with extra (M+N) space
def matrix_change(matrix):
    row = len(matrix)
    col = len(matrix)
    row_count = [0 for x in xrange(row)]
    col_count = [0 for x in xrange(col)]

    for i in xrange(row):
        for j in xrange(col):
            if matrix[i][j] == 0:
                row_count[i] = 1
                col_count[j] = 1
    for i in xrange(row):
        for j in xrange(col):
            if row_count[i] == 1 or col_count[j] == 1:
                matrix[i][j] = 0

    return matrix

# Second try, with two extra flag variable
def matrix_change2(matrix):
    row = len(matrix)
    col = len(matrix)
    last_row = last_col = False
    if matrix[-1][-1] == 0:
        last_row = last_col = True
    else:
        for j in xrange(col-1):
            if matrix[-1][j] == 0:
                last_row = True
                break
        for i in xrange(row-1):
            if matrix[i][-1] == 0:
                last_col = True
                break

    for i in xrange(row-1):
        for j in xrange(col-1):
            if matrix[i][j] == 0:
                matrix[i][-1] = 0
                matrix[-1][j] = 0
    for i in xrange(row-1):
        for j in xrange(col-1):
            if matrix[i][-1] == 0 or matrix[-1][j] == 0:
                matrix[i][j] = 0

    if last_col:
        for i in xrange(row):
            matrix[i][-1] = 0
    if last_row:
        for j in xrange(col):
            matrix[-1][j] = 0

matrix = [[1,2,3,4],[5,6,0,7],[8,10,12,13],[9,0,4,5]]
matrix_change2(matrix)
print matrix
