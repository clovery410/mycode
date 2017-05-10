from heapq import *
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
        
class Solution(object):
    def minMeetingRooms(self, intervals):
        checkPoint = []
        for elem in intervals:
            checkPoint.append((elem.start, 1))
            checkPoint.append((elem.end, 0))
        checkPoint.sort(key = lambda x: (x[0], x[1]))
        count, res = 0, 0
        for point in checkPoint:
            if point[1] == 1:
                count += 1
                res = max(res, count)
            else:
                count -= 1
        return res

    #solution2, try to use heap instead of sort, but seems the same, it's because the for loop also O(n longn)
    def minMeetingRooms2(self, intervals):
        checkPoint = []
        for elem in intervals:
            heappush(checkPoint, (elem.start, 1))
            heappush(checkPoint, (elem.end, 0))
        count, res = 0, 0
        while len(checkPoint) > 0:
            top = heappop(checkPoint)
            if top[1] == 1:
                count += 1
                res = max(res, count)
            else:
                count -= 1
        return res

    
            

if __name__ == "__main__":
    i1 = Interval(0, 30)
    i2 = Interval(5, 10)
    i3 = Interval(15, 20)

    sol = Solution()
    print sol.minMeetingRooms([i1, i2, i3])
