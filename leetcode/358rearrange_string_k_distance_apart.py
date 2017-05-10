import collections
from heapq import *
class Solution(object):
    def rearrangeString(self, _str, k):
        if k <= 0:
            return _str
        
        count = collections.defaultdict(int)
        for c in _str:
            count[c] += 1

        heap, res = [], []
        for key, val in count.items():
            heappush(heap, (-val, key))

        while len(res) < len(_str):
            temp = []
            for i in xrange(k):
                if len(heap) == 0:
                    return '' if len(res) < len(_str) else ''.join(res)
                cnt, c = heappop(heap)
                res.append(c)
                if cnt < -1:
                    temp.append((cnt + 1, c))
            for item in temp:
                heappush(heap, item)
        return ''.join(res)

if __name__ == "__main__":
    sol = Solution()
    print sol.rearrangeString("aaadbbcc", 3)
