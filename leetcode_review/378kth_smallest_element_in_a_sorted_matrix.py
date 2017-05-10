from heapq import *
class Solution(object):
    # solution1, using heap
    def kthSmallest(self, matrix, k):
        m, n = len(matrix), len(matrix[0]) if len(matrix) else 0
        heap = []
        for i in xrange(m):
            heappush(heap, (matrix[i][0], i, 0))

        for x in xrange(k):
            cur_num, cur_i, cur_j = heappop(heap)
            if cur_j + 1 < n:
                heappush(heap, (matrix[cur_i][cur_j+1], cur_i, cur_j + 1))
        return cur_num

    # solution2, using binary search, faster than solution1
    def kthSmallest2(self, matrix, k):
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo < hi:
            mid = (hi - lo) / 2 + lo
            if sum(bisect.bisect(row, mid) for row in matrix) >= k:
                hi = mid 
            else:
                lo = mid + 1
        return lo

if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,5,9],[10,11,13],[12,13,15]]
    k = 9
    print sol.kthSmallest(matrix, k)
