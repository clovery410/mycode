from heapq import *
import sys
class Solution(object):
    # solution1, use heap, although the push and pop from heap is O(n logn), but since I will keep heap at most of length of 3, since it can be considered as O(1)
    def thirdMax(self, nums):
        heap = []
        for num in nums:
            if num in heap:
                continue
            heappush(heap, num)
            if len(heap) > 3:
                heappop(heap)
                
        if len(heap) == 3:
            return heap[0]
        else:
            return max(heap)

    # solution2, does not use heap, which is purely O(n) solution
    def thirdMax2(self, nums):
        cand1 = cand2 = cand3 = -sys.maxint - 1
        for num in nums:
            if num > cand1:
                cand3 = cand2
                cand2 = cand1
                cand1 = num
            elif num < cand1 and num > cand2:
                cand3 = cand2
                cand2 = num
            elif num < cand2 and num > cand3:
                cand3 = num
                
        return cand3 if cand3 > -sys.maxint-1 else cand1

if __name__ == "__main__":
    sol = Solution()
    nums = [2, 2, 1, 3]
    print sol.thirdMax(nums)
    print sol.thirdMax2(nums)
                
