class Solution(object):
    #Solution1, matintain a length 10 window, check whether this was appeared before by putting them into dict
    def findRepeatedDnaSequences(self, s):
        res = []
        d = {}
        for i in xrange(len(s) - 9):
            j = i + 10
            if j > len(s):
                return res
            if s[i:j] in d and d[s[i:j]] == 1:
                res.append(s[i:j])
                d[s[i:j]] += 1
            elif s[i:j] not in d:
                d[s[i:j]] = 1
        return res

    #Solution2, a little bit change from solution1, use set instead of dict here, should be faster than solution1
    def findRepeatedDnaSequences2(self, s):
        res, record = set(), set()
        for i in xrange(len(s) - 9):
            if i + 10 > len(s):
                return list(res)
            substring = s[i:i+10]
            if substring in record:
                res.add(substring)
            else:
                record.add(substring)
        return list(res)

if __name__ == "__main__":
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    sol = Solution()
    print sol.findRepeatedDnaSequences(s)
    print sol.findRepeatedDnaSequences2(s)
