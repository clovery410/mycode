import heapq
class Solution(object):
    def getSkyline(self, buildings):
        heap = []
        rank, res = [], []
        for building in buildings:
            rank.append((building[0], building[2], 1))
            rank.append((building[1], building[2], 0))
        rank.sort(key = operator.itemgetter(0, 2))
        res.append(rank[0][:2])
        pre = rank[0]
        heapq.heappush(heap, rank[0][1])
        for i in xrange(1, len(rank)):
            cur = rank[i]
            height = cur[1]
            if_left = cur[2]
            if is_left:
                if -height < heap[0]:
                    res.append([cur[0], height])
                heapq.heappush(heap, -height)
            else:
                heap.remove(-height)
                heapq.heapify(heap)
                #since remove element from heap and heapify are slow, you can use following instead
                # j = heap.index(height)
                # heap[j] = heap[-1]
                # heap.pop()
                # if j < len(heap):
                #     heapq._siftup(heap, j)
                #     heapq._siftdown(heap, 0, j)
            if pre[2] == 0 and is_left and cur[0] > pre[0]:
                res.append([pre[0], 0])
            pre = cur
        return res

    #Solution2, not separate intervals as in and out points
    

if __name__ == "__main__":
    buildings = [[2,9,10], [3,7,15], [5,12,12], [15,20,10], [19,24,8]]
    sol = Solution()
    print sol.getSkyline(buildings)
