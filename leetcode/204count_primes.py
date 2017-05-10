class Solution(object):
    def countPrimes(self, n):
        i = 2
        mark = [0 for x in xrange(n)]
        while i * i < n:
            if mark[i] == 0:
                j = i * i
                while j < n:
                    mark[j] = 1
                    j += i
            i += 1
        count = 0
        for i in xrange(2, n):
            if mark[i] == 0:
                count += 1

        return count


if __name__ == "__main__":
    sol = Solution()
    print sol.countPrimes(499979)
