# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.count = 0
#         self.dup = 0
from heapq import *
class Solution(object):
    # wrong solution, can not deal with negative numbers
    def findKthLargest(self, nums, k):
        max_num = max(nums)
        counts = [0] * (max_num + 1)
        for num in nums:
            counts[num] += 1

        accu_count = 0
        for i in reversed(xrange(len(counts))):
            count = counts[i]
            accu_count += count
            if accu_count >= k:
                return i
        return max_num

    # matintain a size k heap
    def findKthLargest2(self, nums, k):
        heap = []
        for num in nums:
            heappush(heap, num)
            if len(heap) > k:
                heappop(heap)

        return heap[0]

    # solution3, try to practice writing partition, but seems this solution will TLE
    def findKthLargest3(self, nums, k):
        def threeWayPartition(start, end):
            i = k = start
            pivot = nums[start]
            for j in xrange(start, end):
                if nums[j] == pivot:
                    nums[j], nums[k] = nums[k], nums[j]
                    k += 1
                elif nums[j] < pivot:
                    nums[j], nums[i] = nums[i], nums[j]
                    nums[j], nums[k] = nums[k], nums[j]
                    i += 1
                    k += 1
            
            return i, k-1

        n = len(nums)
        pos = n - k
        start, end = threeWayPartition(0, n)
        while True:
            if start <= pos <= end:
                return nums[pos]
            if start > pos:
                start, end = threeWayPartiton(0, start)
            else:
                start, end = threeWayPartition(end+1, n)
                
                    
                




        
