import heapq
class Solution(object):
    def kthLargest(self, nums, k):
        heap = []
        for num in nums:
            if len(heap) == k + 1:
                heapq.heappop(heap)
            heapq.heappush(heap, num)
        heapq.heappop(heap)
        return heap[0]

    def kthLargest2(self, nums, k):
        def threeWayPartition(start, end):
            pivot = nums[start]
            i = j = m = start
            while j <= end:
                if nums[j] == pivot:
                    nums[m], nums[j] = nums[j], nums[m]
                    m += 1
                elif nums[j] < pivot:
                    nums[m], nums[j] = nums[j], nums[m]
                    nums[i], nums[m] = nums[m], nums[i]
                    i += 1
                    m += 1
                j += 1
            return i, m - 1

        n = len(nums)
        pos = n - k
        start, end = threeWayPartition(0, n-1)
        while True:
            if pos >= start and pos <= end:
                return nums[start]
            elif pos < start:
                start, end = threeWayPartition(0, start - 1)
            else:
                start, end = threeWayPartition(end + 1, n - 1)
        
if __name__ == "__main__":
    nums = [3, 2, 1, 5, 5, 4]
    sol = Solution()
    print sol.kthLargest(nums, 2)
    print sol.kthLargest2(nums, 2)
