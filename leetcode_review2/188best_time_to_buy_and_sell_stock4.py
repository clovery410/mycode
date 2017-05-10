class Solution(object):
    def maxProfit(self, k, prices):
        if k <= 0: return 0
        
        l = len(prices)
        if k > l / 2:
            return sum(prices[i+1] - prices[i] for i in xrange(l-1) if prices[i+1] > prices[i])
        
        hold = [[-prices[0] for x in xrange(l)] for x in xrange(k+1)]
        unhold = [[0 for x in xrange(l)] for x in xrange(k+1)]

        for i in xrange(1, k+1):
            for j in xrange(1, l):
                hold[i][j] = max(hold[i][j-1], unhold[i-1][j-1] - prices[j])
                unhold[i][j] = max(unhold[i][j-1], hold[i][j-1] + prices[j])

        return unhold[-1][-1]

if __name__ == "__main__":
    sol = Solution()
    print sol.maxProfit(2, [2,5,7,1,9,4,8])
