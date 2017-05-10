class Solution(object):
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        dp = [[(0, 0) for x in xrange(n)] for x in xrange(m)]
        initial_hp = 1 - dungeon[0][0] if dungeon[0][0] < 0 else 1
        dp[0][0] = (dungeon[0][0], initial_hp)
        for i in xrange(1, m):
            energy = dp[i-1][0][0] + dungeon[i][0]
            hp = max(dp[i-1][0][1], 1 - energy)
            dp[i][0] = (energy, hp)
        for j in xrange(1, n):
            energy = dp[0][j-1][0] + dungeon[0][j]
            hp = max(dp[0][j-1][1], 1 - energy)
            dp[0][j] = (energy, hp)

        for i in xrange(1, m):
            for j in xrange(1, n):
                hp_upper, hp_left = dp[i-1][j][1], dp[i][j-1][1]
                if hp_upper < hp_left:
                    energy = dp[i-1][j][0] + dungeon[i][j]
                    new_hp = max(hp_upper, 1 - energy)
                elif hp_upper > hp_left:
                    energy = dp[i][j-1][0] + dungeon[i][j]
                    new_hp = max(hp_left, 1 - energy)
                else:
                    energy = max(dp[i-1][j][0], dp[i][j-1][0]) + dungeon[i][j]
                    new_hp = max(hp_left, 1 - energy)
                dp[i][j] = (energy, new_hp)
        return dp[-1][-1][1]

    #Solution2, dp + binary search
    def calculateMinimumHP2(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        upperbound = 1
        for i in xrange(m):
            for j in xrange(n):
                if dungeon[i][j] < 0:
                    upperbound -= dungeon[i][j]
        s, e = 1, upperbound
        while s < e:
            mid = (e - s) / 2 + s
            curr_try = self.validTry(dungeon, mid)
            prev_try = self.validTry(dungeon, mid-1)
            if curr_try and not prev_try:
                return mid
            elif curr_try:
                e = mid - 1
            else:
                s = mid + 1
        return s

    def validTry(self, dungeon, hp):
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0 for x in xrange(n)] for x in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if i == 0:
                    dp[i][j] = dp[i][j-1] if j > 0 else hp
                elif j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                if dp[i][j] > 0:
                    dp[i][j] += dungeon[i][j]
        return True if dp[-1][-1] > 0 else False
        

if __name__ == "__main__":
    matrix = [[0,-40,100], [-30,-30,1], [30,30,0]]
    sol = Solution()
    print sol.calculateMinimumHP(matrix)
    print sol.calculateMinimumHP2(matrix)
