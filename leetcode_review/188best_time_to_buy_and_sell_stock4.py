class Solution(object):
    def maxProfit_multiple(self, prices):
        profits = [prices[i] - prices[i-1] for i in xrange(1, len(prices))]
        return sum(profit for profit in profits if profit > 0)
    
    def maxProfit(self, k, prices):
        n = len(prices)

        if n <= 1:
            return 0
        if k > n / 2:
            return self.maxProfit_multiple(prices)

        # transition equation:
        # diff = prices[i] - prices[i-1]
        # local[i][j] = max(local[i-1][j] + diff, global[i-1][j-1] + diff)
        # global[i][j] = max(local[i][j], global[i-1][j])
        local_max = [[0 for x in xrange(k+1)] for x in xrange(n)]
        global_max = [[0 for x in xrange(k+1)] for x in xrange(n)]

        for i in xrange(1, n):
            diff = prices[i] - prices[i-1]
            for j in xrange(1, k+1):
                local_max[i][j] = max(local_max[i-1][j] + diff, global_max[i-1][j-1] + diff)
                global_max[i][j] = max(global_max[i-1][j], local_max[i][j])
        return global_max[-1][-1]
        
