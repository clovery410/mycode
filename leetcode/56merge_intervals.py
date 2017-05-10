class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        check_point = []
        for time in intervals:
            check_point.append((time.start, 0))
            check_point.append((time.end, 1))
        check_point.sort()
        res = []

        count = 0
        for cur_point in check_point:
            if count == 0:
                start_time = cur_point[0]
            if cur_point[1] == 0:
                count += 1
            if cur_point[1] == 1:
                count -= 1
            if count == 0:
                res.append([start_time, cur_point[0]])
        return res
