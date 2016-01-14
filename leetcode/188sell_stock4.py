class Solution(object):

    #get profit_1[i][j]: max profit when do exactly one transactions at interval [i, j]
    def maxProfit_base(self, prices):
        n = len(prices)
        if n <= 1:
            return None
        profit = [[0 for x in xrange(n)] for x in xrange(n)]
        
        for i in xrange(n):
            minimum = prices[i]
            for j in xrange(i+1, n):
                if minimum > prices[j]:
                    minimum = prices[j]
                profit[i][j] = max(profit[i][j-1], prices[j] - minimum)

        return profit

    #This with at most k transactions algorithm needs O(k*n^3), not good, following maxProfit has better time complexity
    def maxProfit_k(self, prices, k):
        n = len(prices)
        if (n <= 1 or k <= 0):
            return 0
        profit_k = [[[0 for x in xrange(n)] for x in xrange(n)] for x in xrange(k+1)]
        profit_k[1] = self.maxProfit_base(prices)

        for times in xrange(2, k+1):
#            profit_k[i] =   # based on profit_k[0], profit_k[i - 1]
            for i in xrange(n):
                for j in range(i+1, n):
                    value = 0
                    for t in xrange(i, j):
                        value = max(value, profit_k[times-1][i][t] + profit_k[times-1][t+1][j])
                    profit_k[times][i][j] = max(value, profit_k[times-1][i][j])

        print profit_k
#        print profit_k[k][0][n-1]
        return profit_k[k][0][n-1]
        

    #get profit_2[i][j]: max profit when do at most two transactions at interval [i, j]
    def maxProfit_two(self, prices):
        n = len(prices)
        profit_1 = self.maxProfit_base(prices)
        profit_2 = [[0 for x in xrange(n)] for x in xrange(n)]
        for i in xrange(n):
            for j in xrange(i+1, n):
                value = 0
                for k in xrange(i, j):
                    value = max(value, profit_1[i][k] + profit_1[k+1][j])
                profit_2[i][j] = max(value, profit_1[i][j])

        return profit_2

    #get profit_3[i][j]: max profit when do at most three transactions at interval [i, j]
    def maxProfit_three(self, prices):
        n = len(prices)
        profit_2 = self.maxProfit_two(prices)
        profit_3 = [[0 for x in xrange(n)] for x in xrange(n)]
        for i in xrange(n):
            for j in xrange(i+1, n):
                value = 0
                for k in xrange(i, j):
                    value = max(value, profit_2[i][k]+ profit_2[k+1][j])
                profit_3[i][j] = max(value, profit_2[i][j])

        return profit_3

    #if calculate only at most two transactions, can make use of the result of maxProfit_base, go through the array once is enough.
    def maxProfit_mostTwo(self, prices):
        n = len(prices)
        profit = self.maxProfit_base(0, prices)
        max_profit = 0
        for i in xrange(n-1):
            max_profit = max(max_profit, profit[0][i] + profit[i+1][n-1])
        return max_profit

    #only calculate one transaction, with interval [0, n-1]
    def maxProfit_dp(self, prices):
        profit = [0 for x in xrange(len(prices))]
        if (len(prices) == 0):
            return 0
        minimum = prices[0]
        for i in xrange(1, len(prices)):
            if (prices[i] < minimum):
                minimum = prices[i]
            profit[i] = max(profit[i-1], prices[i] - minimum)
        return profit

    #use greedy calculate non-limit transactions, just sum up all the positive profit
    def maxProfit_multiple(self, prices):
        profit = []
        total_profit = 0
        if (len(prices) <= 1):
            return 0
        for i in xrange(len(prices) - 1):
            profit.append(prices[i+1] - prices[i])
        for i in xrange(len(profit)):
            if profit[i] > 0:
                total_profit += profit[i]
        return total_profit

    #This algorithm is awesome, get rid of repeated calculations, need some variations, running time is O(n*k)
    def maxProfit(self, k, prices):
        n = len(prices)
        if n <= 1 or k <= 0:
            return 0
        if k >= n/2:
            return self.maxProfit_multiple(prices)
        
        profit = [[0 for x in xrange(n)] for x in xrange(k+1)]
        profit[1] = self.maxProfit_dp(prices)
        print profit

        for i in xrange(2, k+1):
            _max = profit[i-1][0] - prices[0]
            for j in xrange(1, n):
#                _max = profit[i-1][0] - prices[0]
                if profit[i-1][j] - prices[j] > _max:
                    _max = profit[i-1][j] - prices[j]
                # for l in xrange(1, j):
                #     if max_interval < profit[i-1][l] - prices[l]:
                #         max_interval = profit[i-1][l] - prices[l]
                #     print (j, max_interval+prices[j])
                # print (j, _max + prices[j])
                profit[i][j] = max(profit[i][j-1], _max + prices[j])

        print profit[k][n-1]
        print profit
        return profit
        
if __name__ == '__main__':
#    prices = [2, 7, 8, 3, 10, 4]
    prices = [1, 100, 2, 102, 3, 104]
    prices1 = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
    solution = Solution()
    # result = solution.maxProfit_base(prices)
    # result1 = solution.maxProfit_two(prices)
    # result2 = solution.maxProfit_three(prices)
#    result_k = solution.maxProfit_k(prices1, 2)
    result3 = solution.maxProfit(4, prices1)
    # print result
    # print result1
    # print result2
#    print result_k
    print result3
