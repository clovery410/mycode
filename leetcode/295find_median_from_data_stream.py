#solution1, first implementation using sort, find method running time is O(nlogn), TLE
class MedianFinder(object):
    def __init__(self):
        self.isSort = True
        self.nums = []

    def addNum(self, num):
        if self.nums and num < self.nums[-1]:
            self.isSort = False
        self.nums.append(num)

    def findMedian(self):
        if not self.isSort:
            self.nums.sort()
            self.isSort = True
        l = len(self.nums)
        return (self.nums[(l-1)/2] + self.nums[l/2]) / 2.0

#solution2, try to use heap
import heapq
class MedianFinder2(object):
    def __init__(self):
        self.small_heap = []
        self.large_heap = []
        self.mid = None

    def addNum(self, num):
        small_max = -self.small_heap[0] if len(self.small_heap) > 0 else None
        large_min = self.large_heap[0] if len(self.large_heap) > 0 else None
        if self.mid == None:
            if small_max == None and large_min == None or small_max <= num <= large_min:
                self.mid = num
            elif num < small_max:
                self.mid = small_max
                heapq.heappop(self.small_heap)
                heapq.heappush(self.small_heap, -num)
            else:
                self.mid = large_min
                heapq.heappop(self.large_heap)
                heapq.heappush(self.large_heap, num)
        else:
            if small_max == None and large_min == None:
                heapq.heappush(self.small_heap, -(min(self.mid, num)))
                heapq.heappush(self.large_heap, max(self.mid, num))
            else:
                heapq.heappop(self.small_heap)
                heapq.heappop(self.large_heap)
                candidates = sorted([small_max, large_min, self.mid, num])
                heapq.heappush(self.small_heap, -candidates[0])
                heapq.heappush(self.small_heap, -candidates[1])
                heapq.heappush(self.large_heap, candidates[2])
                heapq.heappush(self.large_heap, candidates[3])
            self.mid = None

    def findMedian(self):
        return self.mid if self.mid else (-self.small_heap[0] + self.large_heap[0]) / 2.0

#solution3, simplify solution2 with more concise code, learned from discuss.
#actually, we do need use self.mid to hold the odd length's middle number, just make two heaps size different
from heapq import *
class MedianFinder3(object):
    def __init__(self):
        self.small_heap = []
        self.large_heap = []

    #when adding a number, first push into large heap, then pop back a smallest number from large heap, then push this number into small heap. In order to make the length difference is at most 1, each time also need to check the length, if len(small) > len(large), then move one number to large heap. In this way, the number count in large heap is alaways equal or one more than small heap.
    def addNum(self, num):
        small, large = self.small_heap, self.large_heap
        heappush(small, -heappushpop(large, num))
        if len(small) > len(large):
            heappush(large, -heappop(small))

    def findMedian(self):
        small, large = self.small_heap, self.large_heap
        if len(small) < len(large):
            return float(large[0])
        else:
            return (-small[0] + large[0]) / 2.0
    
if __name__ == "__main__":
    median = MedianFinder3()
    median.addNum(1)
    median.addNum(2)
    print median.findMedian()
    median.addNum(3)
    median.addNum(0)
    print median.findMedian()
        
