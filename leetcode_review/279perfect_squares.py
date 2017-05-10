import math, sys, time, pdb
class Solution(object):
    _dp = [0]
    #Solution1, learned from discuss, bfs, take it as a tree
    def numSquares(self, n):
        squares = [i*i for i in xrange(1, int(math.sqrt(n)) +1)]
        res = 0
        curCheck = set([n])
        while curCheck:
            nextCheck = set([])
            res += 1
            for x in curCheck:
                for square in squares:
                    if x == square:
                        return res
                    elif x < square:
                        break
                    nextCheck.add(x - square)
            curCheck = nextCheck
        return res

    #Solution2, really slow...
    def numSquares2(self, n):
        def helper(n):
            # pdb.set_trace()
            if n in cache:
                return cache[n]
            cache[n] = 1 + min(helper(n - num) for num in squares if num < n)
            return cache[n]
        
        squares = [i*i for i in reversed(xrange(1, int(math.sqrt(n)) +1))]
        cache = {x: 1 for x in squares}
        res = helper(n)
        return res

    #Solution3, dp, slow
    def numSquares3(self, n):
        squares = [i*i for i in xrange(1, int(n**0.5+1))]
        s = set(squares)
        dp = [1 for i in xrange(n+1)]
        for i in xrange(1, n+1):
            if i not in s:
                # dp[i] = min(dp[i-j] for j in squares if j < i) + 1
                dp[i] = min(dp[i-j] for j in squares[:int(i**0.5)]) + 1
        return dp[-1]

    #Solution4, other people's dp solution
    def numSquares4(self, n):
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[-1]
        
if __name__ == "__main__":
    sol = Solution()
    time1 = time.time()
    print sol.numSquares(8935)
    print ("solution1 --- %s second ---" % (time.time() - time1))
    time2 = time.time()
    print sol.numSquares2(8935)
    print ("solution2 --- %s second ---" % (time.time() - time2))
    time3 = time.time()
    print sol.numSquares3(8935)
    print ("solution3 --- %s second ---" % (time.time() - time3))
    time4 = time.time()
    print sol.numSquares4(8935)
    print ("solution4 --- %s second ---" % (time.time() - time4))
            
