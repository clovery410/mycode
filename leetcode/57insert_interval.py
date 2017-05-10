class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        check_point = []
        for time in intervals:
            check_point.append((time.start, 0))
            check_point.append((time.end, 1))
        check_point.append((newInterval.start, 0))
        check_point.append((newInterval.end, 1))

        check_point.sort(key = lambda x: (x[0], x[1]))
        s_count = 0
        res = []
        for point in check_point:
            if s_count == 0:
                s = point[0]
            if point[1] == 0:
                s_count += 1
            else:
                s_count -= 1
            if s_count == 0:
                res.append(Interval(s, point[0]))
        return res
            
