class Solution(object):
    def numTrees(self, n):
        if n <= 2:
            return n
        count = [0] * (n + 1)
        count[0], count[1] = 1, 1
        for i in xrange(2, n + 1):
            for j in xrange(1, i+1):
                count[i] += count[j-1] * count[i-j]
        return count[-1]

if __name__ == "__main__":
    sol = Solution()
    print sol.numTrees(4)
