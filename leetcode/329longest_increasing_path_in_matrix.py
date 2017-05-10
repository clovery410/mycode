from collections import defaultdict
class Solution(object):
    max_total = 0
    #Solution1, first try, backtracing, but reach TLE
    def longestIncreasingPath(self, matrix):
        def helper(cur_i, cur_j, mark, count):
            if (cur_i, cur_j) in mark:
                return
            if count > self.max_total:
                self.max_total = count
            mark[(cur_i, cur_j)] = 1
            cur_val = matrix[cur_i][cur_j]
            if cur_i >= 1 and matrix[cur_i-1][cur_j] > cur_val:
                helper(cur_i-1, cur_j, mark, count+1)
            if cur_i < row-1 and matrix[cur_i+1][cur_j] > cur_val:
                helper(cur_i+1, cur_j, mark, count+1)
            if cur_j >= 1 and matrix[cur_i][cur_j-1] > cur_val:
                helper(cur_i, cur_j-1, mark, count+1)
            if cur_j < col-1 and matrix[cur_i][cur_j+1] > cur_val:
                helper(cur_i, cur_j+1, mark, count+1)
            del mark[(cur_i, cur_j)]

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        row, col = len(matrix), len(matrix[0])
        for i in xrange(row):
            for j in xrange(col):
                helper(i, j, {}, 1)
        return self.max_total

    #Solution2,
    def longestIncreasingPath(self, matrix):
        def dfs(cur_i, cur_j):
            if (cur_i, cur_j) in memo:
                return memo[(cur_i, cur_j)]
            if len(graph[(cur_i, cur_j)]) == 0:
                memo[(cur_i, cur_j)] = 1
            else:
                memo[(cur_i, cur_j)] = max(dfs(i, j) for i, j in graph[(cur_i, cur_j)]) + 1
            return memo[(cur_i, cur_j)]
            
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        row, col = len(matrix), len(matrix[0])

        #Construct graph
        memo = {}
        graph = defaultdict(list)
        indegree = [[0 for x in xrange(col)] for x in xrange(row)]
        for i in xrange(row):
            for j in xrange(col):
                cur_val = matrix[i][j]
                if i >= 1 and matrix[i-1][j] > cur_val:
                    graph[(i, j)].append((i-1, j))
                    indegree[(i-1, j)] += 1
                if i < row - 1 and matrix[i+1][j] > cur_val:
                    graph[(i, j)].append((i+1, j))
                    indegree[(i+1, j)] += 1
                if j >= 1 and matrix[i][j-1] > cur_val:
                    graph[(i, j)].append((i, j-1))
                    indegree[(i, j-1)] += 1
                if j < col - 1 and matrix[i][j+1] > cur_val:
                    graph[(i, j)].append((i, j+1))
                    indegree[(i, j+1)] += 1
        max_len = 1
        for i in xrange(row):
            for j in xrange(col):
                if indegree[i][j] == 0:
                   max_len = max(max_len, dfs(i, j))
        return max_len

    #Solution3, dp solution, much faster
    def longestIncreasingPath3(self, matrix):
        def helper(cur_i, cur_j):
            if memo[cur_i][cur_j]:
                return memo[cur_i][cur_j]
            cur_val = matrix[cur_i][cur_j]
            up = helper(cur_i-1, cur_j) if cur_i >= 1 and cur_val < matrix[cur_i-1][cur_j] else 0
            down = helper(cur_i+1, cur_j) if cur_i < row-1 and cur_val < matrix[cur_i+1][cur_j] else 0
            left = helper(cur_i, cur_j-1) if cur_j >= 1 and cur_val < matrix[cur_i][cur_j-1] else 0
            right = helper(cur_i, cur_j+1) if cur_j < col-1 and cur_val < matrix[cur_i][cur_j+1] else 0
            memo[cur_i][cur_j] = max(up, down, left, right) + 1
            return memo[cur_i][cur_j]

        if not matrix or not matrix[0]:
            return 0
        row, col = len(matrix), len(matrix[0])
        memo = [[0 for x in xrange(col)] for x in xrange(row)]

        return max(helper(i, j) for j in xrange(col) for i in xrange(row))
