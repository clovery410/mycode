class Solution(object):
    def spiralOrder(self, matrix):
        m, n = len(matrix), len(matrix[0]) if len(matrix) > 0 else 0
        total_count = m * n
        direction = 0  # direction has four values, 0 is go right, 1 is go down, 2 is go left, 3 is go up
        row_loop_count, col_loop_count = m - 1, n
        i, j = 0, -1
        res = []
        while len(res) < total_count:
            if direction == 0:
                for k in xrange(col_loop_count):
                    j += 1
                    res.append(matrix[i][j])
                direction += 1
                col_loop_count -= 1
                
            elif direction == 1:
                for k in xrange(row_loop_count):
                    i += 1
                    res.append(matrix[i][j])
                direction += 1
                row_loop_count -= 1
                
            elif direction == 2:
                for k in xrange(col_loop_count):
                    j -= 1
                    res.append(matrix[i][j])
                direction += 1
                col_loop_count -= 1
                
            else:
                for k in xrange(row_loop_count):
                    i -= 1
                    res.append(matrix[i][j])
                direction = 0
                row_loop_count -= 1

        return res

if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,2,3],[4,5,6]]
    print sol.spiralOrder(matrix)
                    
                    
