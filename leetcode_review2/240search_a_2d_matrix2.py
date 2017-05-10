class Solution(object):
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0]) if len(matrix) > 0 else 0
        if m == 0 or n == 0:
            return False
        
        cur_i, cur_j = 0, n - 1
        while cur_i < m and cur_j >= 0:
            cur_num = matrix[cur_i][cur_j]
            if cur_num == target:
                return True
            if cur_num < target:
                cur_i += 1
            else:
                cur_j -= 1
        return False
