from heapq import *
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        heap = []
        for a in nums1:
            for b in nums2:
                if len(heap) < k or heap[0][0] < -a - b:
                    heappush(heap, (-a - b, a, b))
                if len(heap) > k:
                    heappop(heap)

        res = []
        while heap:
            _sum, a, b = heappop(heap)
            res.append([a, b])
        return res[::-1]

if __name__ == "__main__":
    sol = Solution()
    nums1 = [1,1,2]
    nums2 = [1,2,3]
    k = 2
    print sol.kSmallestPairs(nums1, nums2, k)
                    
