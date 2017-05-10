import heapq
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if len(nums) <= k:
            return [max(nums)] if len(nums) > 0 else []
        heap, res = [], []
        n = len(nums)
        for i in xrange(k):
            heapq.heappush(heap, -nums[i])
        for i in xrange(n - k):
            res.append(-heap[0])
            heap.remove(-nums[i])
            heapq.heapify(heap)
            heapq.heappush(heap, -num[i+k])
        res.append(-heap[0])
        return res

if __name__ == "__main__":
    sol = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    print sol.maxSlidingWindow(nums, 3)
        
