class Solution(object):
    def canAttendMeetings(self, intervals):
        intervals.sort(key = lambda x: x.start)
        
        for i in xrange(1, len(intervals)):
            pre_end, cur_start = intervals[i-1].end, intervals[i].start
            if cur_start < pre_end:
                return False
        return True
