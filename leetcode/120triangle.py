import sys
class Solution(object):
    #Solution1, bottom up DP solution
    def minimumTotal(self, triangle):
        if len(triangle) == 0 or len(triangle[0]) == 0:
            return 0
        
        row = len(triangle)
        dp = triangle[0] + [sys.maxint] * (row - 1)
        for i in range(1, row):
            for j in reversed(range(len(triangle[i]))):
                # if j > 0:
                #     dp[j] = min(dp[j], dp[j-1]) + triangle[i][j]
                # else:
                #     dp[j] += triangle[i][j]
                dp[j] = min(dp[j], dp[j-1]) + triangle[i][j] if j > 0 else dp[j] + triangle[i][j]
        return min(dp)

    #Solution2, top down DP solution
    def minimumTotal2(self, triangle):
        row = len(triangle)
        dp = triangle[-1][:]
        for i in range(row-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0]
    
if __name__ == "__main__":
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    sol = Solution()
    print sol.minimumTotal(triangle)
    print sol.minimumTotal2(triangle)
        
