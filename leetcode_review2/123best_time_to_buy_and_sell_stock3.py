class Solution(object):
    #use state machine to solve
    def maxProfit(self, prices):
        l = len(prices)
        if l <= 2:
            return max(0, prices[1] - prices[0]) if len(prices) == 2 else 0
        
        hold1 = [-prices[0]] * l
        unhold1 = [0] * l
        hold2 = [-prices[0]] * l
        unhold2 = [0] * l

        for i in xrange(1, l):
            hold1[i] = max(hold1[i-1], -prices[i])
            unhold1[i] = max(unhold1[i-1], hold1[i-1] + prices[i])
            hold2[i] = max(hold2[i-1], unhold1[i-1] - prices[i])
            unhold2[i] = max(unhold2[i-1], hold2[i-1] + prices[i])

        return unhold2[-1]
