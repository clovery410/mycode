import collections
class Solution(object):
    #solution1, use hashmap
    def findTheDifference(self, s, t):
        counts = collections.defaultdict(int)
        for c in s:
            counts[c] += 1
        for c in t:
            if c not in counts or counts[c] == 0:
                return c
            counts[c] -= 1

    #solution2, use bit manipulation
    def findTheDifference2(self, s, t):
        res = 0
        for c in t + s:
            res ^= ord(c)
        return chr(res)

if __name__ == "__main__":
    sol = Solution()
    s = "abcd"
    t = "dbagc"
    print sol.findTheDifference2(s, t)
