from heapq import *
class Solution(object):
    def __init__(self):
        self.count = 0
        self.total = 0
        self.min_heap = []
        self.max_heap = []

    def addNumber(self, x):
        min_heap, max_heap = self.min_heap, self.max_heap
        self.count += 1
        self.total += x
        heappush(min_heap, -heappushpop(max_heap, x))
        if len(min_heap) > len(max_heap):
            heappush(max_heap, -heappop(min_heap))

    def getMean(self):
        return self.total / float(self.count)

    def getMedian(self):
        min_heap, max_heap = self.min_heap, self.max_heap
        if len(max_heap) > len(min_heap):
            return float(max_heap[0])
        else:
            return (max_heap[0] - min_heap[0]) / 2.0

# Follow-up, what if we only most recently k integers, if k is small, we only need to use a queue of size k
# this algorithm is O(n) bound
import bisect, collections
class Solution2(object):
    def __init__(self, k):
        self.cur_nums = []
        self.size = k
        self.queue = collections.deque([])

    def addNumber(self, x):
        cur_nums = self.cur_nums
        queue = self.queue
        bisect.insort_left(cur_nums, x)
        queue.append(x)
        if len(cur_nums) > self.size:
            cur_nums.remove(queue.popleft())

    def getMean(self):
        queue = self.queue
        return sum(queue) / len(queue)

    def getMedian(self):
        cur_nums = self.cur_nums
        l = len(cur_nums)
        if l % 2 == 1:
            return cur_nums[l/2]
        else:
            return (cur_nums[l/2-1] + cur_nums[l/2]) / 2.0
        
if __name__ == "__main__":
    sol = Solution2(3)
    sol.addNumber(-5)
    print sol.getMedian()
    sol.addNumber(-2)
    print sol.getMedian()
    sol.addNumber(-1)
    print sol.getMedian()
    sol.addNumber(-4)
    print sol.getMedian()
    sol.addNumber(-3)
    print sol.getMedian()
        
