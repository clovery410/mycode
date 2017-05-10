class Solution(object):
    def maximalSquare(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        
        dp = [[int(x) for x in row] for row in matrix]
        max_count = 0
        for i in range(len(matrix)):
            if dp[i][0] == 1:
                max_count = 1
        for j in range(len(matrix[0])):
            if dp[0][j] == 1:
                max_count = 1
                
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if dp[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                    max_count = max(max_count, dp[i][j])
        return max_count * max_count
                

if __name__ == "__main__":
    matrix = ["10100", "10111", "11111", "10010"]
    sol = Solution()
    print sol.maximalSquare(matrix)
