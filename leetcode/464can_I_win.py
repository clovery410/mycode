class Solution(object):
    # original solution, but will TLE
    def canIWin(self, maxChoosableInteger, desiredTotal):
        def check(target):
            if max(remain) >= target:
                return True
            choices = list(remain)
            for elem in choices:
                remain.remove(elem)
                if not check(target - elem):
                    remain.add(elem)
                    return True
                remain.add(elem)
            return False
        
        remain = set(range(1, maxChoosableInteger + 1))
        return check(desiredTotal)

    # solution2, use memoization to speedup, but still TLE on Leetcode OJ
    def canIWin2(self, maxChoosableInteger, desiredTotal):
        def check(target):
            s = str(state)
            if s in visited:
                return visited[s]

            done = False
            for i in xrange(1, len(state)):
                if done:
                    break
                if state[i] == 0:
                    state[i] = 1
                    if i >= target or not check(target - i):
                        visited[s] = True
                        done = True
                    state[i] = 0
                    
            if not done: visited[s] = False
            return visited[s]

        # pre calculate whether the total sum is less than desiredTotal so that can directly return False
        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False
        state = [0 for x in xrange(maxChoosableInteger + 1)]
        visited = {}
        return check(desiredTotal)

    # solution3, use other guys's python solution, this solution can pass OJ
    def canIWin3(self, maxChoosableInteger, desiredTotal):
        def check(remain, target):
            s = str(remain)
            if s in visited:
                return visited[s]

            if remain[-1] >= target:
                return True
            
            for i, num in enumerate(remain):
                if not check(remain[:i] + remain[i+1:], target - num):
                    visited[s] = True
                    return True

            visited[s] = False
            return False

        # pre calculate whether the total sum is less than desiredTotal so that can directly return False
        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False
        visited = {}
        return check(range(1, maxChoosableInteger + 1), desiredTotal)

if __name__ == "__main__":
    sol = Solution()
    print sol.canIWin3(20, 209)
