class Solution(object):
    #wrong solution...
    def maximalRectangle(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        dp = [[(0, 0, 0) for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        res = 0
        for i in range(len(matrix)):
            if matrix[i][0] == "1":
                dp[i][0] = (dp[i-1][0][0] + 1, 1, 1) if i >= 1 else (1, 1, 1)
                res = max(res, dp[i][0][0])
        for j in range(len(matrix[0])):
            if matrix[0][j] == "1":
                dp[0][j] = (1, dp[0][j-1][1] + 1, 1) if j >= 1 else (1, 1, 1)
                res = max(res, dp[0][j][1])
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == "1":
                    up_count = dp[i-1][j][0] + 1
                    left_count = dp[i][j-1][1] + 1
                    left_up_count = dp[i-1][j-1][2] + 1
                    dp[i][j] = (up_count, left_count, left_up_count)
                
                    res = max(res, up_count, left_count, min(up_count, left_count) * left_up_count)
        print dp
        return res

    # correct dp solution
    def maximalRectangle2(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        n = len(matrix[0])
        height = [0] * (n+1)
        res = 0
        for row in matrix:
            for j in xrange(n):
                height[j] = height[j] + 1 if row[j] == "1" else 0
            stack = [-1]
            for s in xrange(n + 1):
                while height[s] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = s - stack[-1] - 1
                    res = max(res, h * w)
                stack.append(s)
        return res
                
        
        

if __name__ == "__main__":
    matrix = ["10100", "10111", "11111", "10010"]
    matrix2 = ["1111", "1111", "1111"]
    sol = Solution()
    print sol.maximalRectangle2(matrix2)
