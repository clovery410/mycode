class Solution(object):
    def searchMatrix(self, matrix, target):
        row = len(matrix)
        r_start, r_end = 0, row - 1
        while r_start <= r_end:
            r_mid = r_start + (r_end - r_start) / 2
            if matrix[r_mid][0] == target:
                return True
            if matrix[r_mid][0] < target:
                r_start = r_mid + 1
            else:
                r_end = r_mid - 1

        col = len(matrix[r_end])
        col_start, col_end = 0, col - 1
        while col_start <= col_end:
            col_mid = col_start + (col_end - col_start) / 2
            if matrix[r_end][col_mid] == target:
                return True
            if matrix[r_end][col_mid] < target:
                col_start = col_mid + 1
            else:
                col_end = col_mid - 1
        return False
