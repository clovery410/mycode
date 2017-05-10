class Solution(object):
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0]) if len(matrix) > 0 else 0
        cur_i, cur_j = 0, n-1
        while cur_i < m and cur_j >= 0:
            if target == matrix[cur_i][cur_j]:
                return True
            if target < matrix[cur_i][cur_j]:
                cur_j -= 1
            else:
                cur_i += 1
        return False
