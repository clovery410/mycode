from collections import deque
class Solution(object):
    #solution1, TLE
    def numSquares(self, n):
        dp = [0] * (n+1)
        i = 1
        while i * i <= n:
            dp[i*i] = 1
            i += 1

        squares = []
        for i in xrange(1, n+1):
            if dp[i] == 1:
                squares.append(i)
                continue
            cur = i
            for num in squares:
                cur = min(cur, 1 + dp[i - num])
            dp[i] = cur

        return dp[-1]

    #solution2, try to use BFS, but Memory Limit Exceed
    def numSquares2(self, n):
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i*i)
            i += 1

        queue = deque([n])
        count = 1
        while queue:
            length = len(queue)
            for _ in xrange(length):
                cur_num = queue.popleft()
                for square_num in squares:
                    if cur_num - square_num == 0:
                        return count
                    queue.append(cur_num - square_num)
            count += 1

    #solution3, modified version of BFS, use set to eliminate duplicate cases
    def numSquares3(self, n):
        i = 1
        squares = set()
        while i * i <= n:
            squares.add(i*i)
            i += 1

        cur_level = {n}
        count = 1
        while cur_level:
            next_level = set()
            for cur in cur_level:
                if cur in squares:
                    return count
                for num in squares:
                    if num < cur:
                        next_level.add(cur - num)
            count += 1
            cur_level = next_level
        return count
            
if __name__ == "__main__":
    sol = Solution()
#    print sol.numSquares(12)
#    print sol.numSquares2(12)
    print sol.numSquares3(9975)
            
            
