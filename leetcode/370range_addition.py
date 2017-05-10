class Solution(object):
    # brute force solution, will TLE
    def getModifiedArray(self, length, updates):
        res = [0] * length
        for s, e, inc in updates:
            for i in xrange(s, e+1):
                res[i] += inc
        return res

    # solution2
    def getModifiedArray2(self, length, updates):
        res = [0] * (length+1)

        for s, e, inc in updates:
            res[s] += inc
            res[e+1] -= inc

        for i in xrange(1, len(res)):
            res[i] += res[i-1]
        return res[:-1]

if __name__ == "__main__":
    sol = Solution()
    updates = [[1, 3, 2], [2, 4, 3], [0, 2, -2]]
    print sol.getModifiedArray2(5, updates)
            
