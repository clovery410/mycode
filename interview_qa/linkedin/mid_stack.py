from heapq import *
class MidStack(object):
    def __init__(self):
        self.small_heap = []
        self.large_heap = []

    def addNumber(self, x):
        heappush(self.small_heap, heappushpop(self.large_heap, x))
        if len(self.small_heap) > len(self.large_heap):
            heappush(self.large_heap, -heappop(self.small_heap))
        
    def getMedian(self):
        if len(self.small_heap) == len(self.large_heap):
            return (-self.small_heap[0] + self.large_heap[0]) / 2.0
        else:
            return float(self.large_heap[0])
