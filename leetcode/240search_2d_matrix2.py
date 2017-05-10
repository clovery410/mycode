class Solution(object):
    def searchMatrix(self, matrix, target):
        def binarySearch(nums, key):
            nums = [nums[0] - 1,] + nums + [nums[-1] + 1,]
            n = len(nums)
            start, end = 1, n - 2
            while start <= end:
                mid = start + (end - start) / 2
                if nums[mid] == key:
                    return mid
                if nums[mid] < key:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1
        
        row = len(matrix)
        for i in xrange(row):
            if matrix[i][0] > target:
                return False
            if binarySearch(matrix[i], target) != -1:
                return True
        return False

    # O(n) running time
    def searchMatrix_quick(self, matrix, target):
        row = len(matrix)
        col = len(matrix[0])
        i, j = 0, col - 1
        while i < row and j >= 0:
            curr = matrix[i][j]
            if curr == target:
                return True
            if curr < target:
                i += 1
            else:
                j -= 1
        return False
