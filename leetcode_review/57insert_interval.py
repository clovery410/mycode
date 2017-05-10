class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    #solution1, iterate through the list
    def insert(self, intervals, newInterval):
        if len(intervals) == 0: return [newInterval]
        
        res = []
        newStart, newEnd = newInterval.start, newInterval.end
        idx = 0
        while idx < len(intervals) and intervals[idx].end < newStart:
            res.append(intervals[idx])
            idx += 1
        
        if idx < len(intervals) and intervals[idx].start < newStart:
            mergeStart = intervals[idx].start
        else:
            mergeStart = newStart
            
        while idx < len(intervals) and intervals[idx].start <= newEnd:
            idx += 1

        if idx > 0 and intervals[idx-1].end > newEnd:
            mergeEnd = intervals[idx-1].end
        else:
            mergeEnd = newEnd

        res.append(Interval(mergeStart, mergeEnd))
        for i in xrange(idx, len(intervals)):
            res.append(intervals[i])

        return res

    #solution2, rewrite solution1 in a more concise way
    def insert2(self, intervals, newInterval):
        idx1, l = 0, len(intervals)
        newStart, newEnd = newInterval.start, newInterval.end

        while idx1 < l and intervals[idx1].end < newStart:
            idx1 += 1
            
        idx2 = idx1
        while idx2 < l and intervals[idx2].start <= newEnd:
            newInterval = Interval(min(newInterval.start, intervals[idx2].start), max(newInterval.end, intervals[idx2].end))
            idx2 += 1
            
        return intervals[:idx1] + [newInterval] + intervals[idx2:]
            
