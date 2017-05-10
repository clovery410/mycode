class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        if len(intervals) == 0:
            return []
        
        check_point = []
        for interval in intervals:
            check_point.append((interval.start, 0))
            check_point.append((interval.end, 1))

        check_point.sort(key = lambda x: (x[0], x[1]))

        count = 0
        res = []
        for point in check_point:
            if point[1] == 0:
                if count == 0:
                    enter = point[0]
                count += 1
            else:
                count -= 1
                if count == 0:
                    new_interval = Interval(enter, point[0])
                    res.append(new_interval)
        return res
                    
