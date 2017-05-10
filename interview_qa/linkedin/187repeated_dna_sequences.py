class Solution(object):
    def findRepeatedDnaSequences(self, s):
        counter = collections.defaultdict(int)
        i = 0
        while i + 9 < len(s):
            counter[s[i:i+10]] += 1
            i += 1

        res = []
        for c, cnt in counter.iteritems():
            if cnt > 1:
                res.append(c)
        return res
