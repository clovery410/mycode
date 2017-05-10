import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        
        heap = [(num+nums2[0], i, 0) for i, num in enumerate(nums1)]
        heapq.heapify(heap)
        res = []
        while k > 0 and heap:
            _sum, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i]+nums2[j+1], i, j+1))
            k -= 1
        return res

if __name__ == "__main__":
    nums1 = [1,7,11]
    nums2 = [2,4,6]
    sol = Solution()
    print sol.kSmallestPairs(nums1, nums2, 6)
