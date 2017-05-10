from heapq import *
class Solution(object):
    def topKFrequent(self, nums, k):
        count = collections.defaultdict(int)
        for num in nums:
            count[num] += 1

        heap = []
        for num, cnt in count.items():
            heappush(heap, (-cnt, num))
        res = []
        for i in xrange(k):
            res.append(heappop(heap)[1])
        return res
