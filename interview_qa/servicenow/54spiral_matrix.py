# solution1
def spiralOrder(matrix):
    m, n = len(matrix), len(matrix[0]) if len(matrix) else 0
    if m == 0 or n == 0:
        return []
    start_row, end_row = 0, m-1
    start_col, end_col = 0, n-1
    res = []

    while start_row <= end_row and start_col <= end_col:
        for j in xrange(start_col, end_col+1):
            res.append(matrix[start_row][j])
        start_row += 1
        
        for i in xrange(start_row, end_row+1):
            res.append(matrix[i][end_col])
        end_col -= 1

        for j in reversed(xrange(start_col, end_col+1)):
            if start_row <= end_row:
                res.append(matrix[end_row][j])
        end_row -= 1

        for i in reversed(xrange(start_row, end_row+1)):
            if start_col <= end_col:
                res.append(matrix[i][start_col])
        start_col += 1

    return res

# solution2, another coding style
def spiralOrder2(matrix):
    m, n = len(matrix), len(matrix[0]) if len(matrix) else 0
    if m == 0 or n == 0:
        return []
    res = []
    direction = 0
    row_loop_count, col_loop_count = m-1, n
    row, col = 0, -1
    total_count = m * n

    while len(res) < total_count:
        if direction == 0:
            for k in xrange(col_loop_count):
                col += 1
                res.append(matrix[row][col])
            direction += 1
            col_loop_count -= 1
            
        elif direction == 1:
            for k in xrange(row_loop_count):
                row += 1
                res.append(matrix[row][col])
            direction += 1
            row_loop_count -= 1

        elif direction == 2:
            for k in xrange(col_loop_count):
                col -= 1
                res.append(matrix[row][col])
            direction += 1
            col_loop_count -= 1

        else:
            for k in xrange(row_loop_count):
                row -= 1
                res.append(matrix[row][col])
            direction = 0
            row_loop_count -= 1
    return res
                
if __name__ == "__main__":
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print spiralOrder(matrix)
    print spiralOrder2(matrix)
        
