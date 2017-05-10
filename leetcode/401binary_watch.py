class Solution(object):
    def readBinaryWatch(self, num):
        def hour(lo, value, num):
            if num == 0:
                return [str(value) + ":"] if value <= 11 else []
            hour_res = []
            for i in xrange(lo, 4):
                hour_res += hour(i+1, value + 2 ** i, num-1)
            return hour_res

        def minute(lo, value, num):
            if num == 0:
                if value > 59: return []
                if value < 10: return ["0" + str(value)]
                else: return [str(value)]
            minute_res = []
            for i in xrange(lo, 6):
                minute_res += minute(i+1, value + 2 ** i, num-1)
            return minute_res
                
        res = []
        for i in xrange(min(4, num+1)):
            for res1 in hour(0, 0, i):
                for res2 in minute(0, 0, num-i):
                    res.append(res1 + res2)
        return res
        
