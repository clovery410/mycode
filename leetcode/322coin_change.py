class Solution(object):
    def coinChange(self, coins, amount):
        coins.sort(reverse = True)
        dp = [0,] + [amount+1 for x in xrange(amount)]
        change = {}
        for i in xrange(1, amount+1):
            for coin in coins:
                if i >= coin:
                    change[i] = min(dp[i-coin] + 1, dp[i])
                    dp[i] = min(dp[i-coin] + 1, dp[i])
        return -1 if dp[-1] > amount else dp[-1]

if __name__ == "__main__":
    sol = Solution()
    coins = [2, 5]
    print sol.coinChange(coins, 11)
        
