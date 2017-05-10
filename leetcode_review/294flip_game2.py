class Solution(object):
    # naive DFS
    def canWin(self, s):
        for i in range(len(s) - 1):
            if s[i] == '+' and s[i+1] == '+':
                if not self.canWin(s[:i] + '--' + s[i+2:]): return True
        return False

    #solution2, add some memoization
    def canWin2(self, s, visited = {}):
        if s in visited: return visited[s]
        for i in range(len(s) - 1):
            if s[i] == '+' and s[i+1] == '+':
                if not self.canWin2(s[:i] + '--' + s[i+2:]):
                    visited[s] = True
                    return True
        visited[s] = False
        return False

if __name__ == "__main__":
    sol = Solution()
    print sol.canWin("+-+-")
    print sol.canWin2("+-+-")
