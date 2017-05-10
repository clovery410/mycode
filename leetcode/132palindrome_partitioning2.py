class Solution(object):
    def minCut(self, s):
        n = len(s)
        p = [[False for _ in xrange(n)] for _ in xrange(n)]
        cut = [n] * n

        for i in xrange(n):
            min_cut = i
            for j in xrange(i+1):
               if s[j] == s[i] and (j + 1 > i - 1 or p[j+1][i-1]):
                   p[j][i] = True
                   min_cut = min(min_cut, cut[j-1] + 1) if j > 0 else 0
            cut[i] = min_cut
        return cut[-1]

if __name__ == "__main__":
    sol = Solution()
    print sol.minCut("aabc")
                   
