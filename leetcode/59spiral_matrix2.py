class Solution(object):
    def generateMatrix(self, n):
        res = [[0 for x in xrange(n)] for x in xrange(n)]
        start_i = start_j = 0
        end_i = end_j = n - 1
        curr_num = 1

        while start_i <= end_i and start_j <= end_j:
            for j in xrange(start_j, end_j + 1):
                res[start_i][j] = curr_num
                curr_num += 1
            start_i += 1

            for i in xrange(start_i, end_i + 1):
                res[i][end_j] = curr_num
                curr_num += 1
            end_j -= 1

            for j in reversed(xrange(start_j, end_j + 1)):
                res[end_i][j] = curr_num
                curr_num += 1
            end_i -= 1

            for i in reversed(xrange(start_i, end_i + 1)):
                res[i][start_j] = curr_num
                curr_num += 1
            start_j += 1
        return res

if __name__ == "__main__":
    sol = Solution()
    print sol.generateMatrix(3)
