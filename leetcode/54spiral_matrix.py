class Solution(object):
    def spiralOrder(self, matrix):
        if len(matrix) == 0:
            return []
        if len(matrix) == 1:
            return matrix[0]
        
        start_i, start_j = 0, 0
        end_i, end_j = len(matrix) - 1, len(matrix[0]) - 1
        res = []

        while start_i <= end_i and start_j <= end_j:
            for j in xrange(start_j, end_j + 1):
                res.append(matrix[start_i][j])
            start_i += 1
            for i in xrange(start_i, end_i + 1):
                res.append(matrix[i][end_j])
            end_j -= 1
            for j in reversed(xrange(start_j, end_j + 1)):
                if start_i <= end_i:
                    res.append(matrix[end_i][j])
            end_i -= 1
            for i in reversed(xrange(start_i, end_i + 1)):
                if start_j <= end_j:
                    res.append(matrix[i][start_j])
            start_j += 1

        return res

if __name__ == "__main__":
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    sol = Solution()
    print sol.spiralOrder(matrix)
