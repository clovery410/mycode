class Solution(object):
    def findTheDifference(self, s, t):
        count = collections.defaultdict(int)
        for c in s:
            count[c] += 1

        for c in t:
            count[c] -= 1
            if count[c] < 0:
                return c
        
