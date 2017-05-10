class Solution(object):
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m-1
        while low < high:
            mid = (high - low) / 2 + low
            if matrix[mid][-1] < target:
                low = mid + 1
            else:
                high = mid
        left, right = 0, n - 1
        while left <= right:
            mid = (right - left) / 2 + left
            if matrix[low][mid] == target:
                return True
            elif matrix[low][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    sol = Solution()
    print sol.searchMatrix(matrix, 12)
