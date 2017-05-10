import heapq
class Solution(object):
    #Solution1, use heap
    def kthSmallest(self, matrix, k):
        heap = []
        n = len(matrix)
        for i in xrange(n):
            for j in xrange(n):
                if len(heap) == k + 1:
                    heapq.heappop(heap)
                heapq.heappush(heap, -matrix[i][j])
        if len(heap) == k + 1:
            heapq.heappop(heap)
        return -heapq.heappop(heap)

    #Solution2, Optimized heap solution
    def kthSmallest2(self, matrix, k):
        n = len(matrix)
        heap = [(row[0], i, 0) for i, row in enumerate(matrix)]
        heapq.heapify(heap)
        res = 0
        for i in xrange(k):
            res, i, j = heapq.heappop(heap)
            if j + 1 < n:
                heapq.heappush(heap, (matrix[i][j+1], i, j+1))
        return res

    #Solution3, binary search solution
    def kthSmallest3(self, matrix, k):
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo < hi:
            mid = (hi - lo) / 2 + lo
            if sum(bisect.bisect_right(row, mid) for row in matrix) < k:
                lo = mid + 1
            else:
                hi = mid
        return lo

if __name__ == "__main__":
    matrix = [[1,5,9],[10,11,13],[12,13,15]]
    sol = Solution()
            
