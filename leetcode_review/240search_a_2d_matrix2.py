class Solution(object):
    #Solution1, idea is start from right upper corner, if curr < target, scan downward, if curr > target, scan leftward. Use Binary search to implement going down and going left
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            #lookup downside
            elif matrix[i][j] < target:
                s, e = i, m - 1
                while s <= e and s < m:
                    mid = (e - s) / 2 + s
                    if matrix[mid][j] == target:
                        return True
                    elif matrix[mid][j] < target:
                        s = mid + 1
                    else:
                        e = mid - 1
                i = s
            #lookup leftward
            else:
                s, e = 0, j
                while s <= e and e >= 0:
                    mid = (e - s) / 2 + s
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] > target:
                        e = mid - 1
                    else:
                        s = mid + 1
                j = e
        return False

    #Solution2, same idea, however, we can directly implement scanning downward and leftward by moving just one step further, since we only need to move (m+n) steps in total, so this solution is O(m+n), better than above O(mlogn + nlogm)
    def searchMatrix2(self, matrix, target):
        row, col = len(matrix), len(matrix[0])
        i, j = 0, col - 1
        while i < row and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False

if __name__ == "__main__":
    matrix = [[1,4,7,11,15], [2,5,8,12,19], [3,6,9,16,22], [10,13,14,17,24], [18,21,23,36,30]]
    sol = Solution()
    print sol.searchMatrix(matrix, 20)
    print sol.searchMatrix2(matrix, 20)
