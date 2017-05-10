class Solution(object):
    def firstUniqChar(self, s):
        count = collections.defaultdict(int)
        for c in s:
            count[c] += 1

        i = 0
        while i < len(s):
            if count[s[i]] == 1:
                return i
            i += 1
        return -1

    # solution2, learned from discuss
    def firstUniqChar2(self, s):
        chars = collections.defaultdict(lambda: s.count(c))
        return ([i for i, c in enumerate(s) if chars[c] < 2] or [-1])[0]
