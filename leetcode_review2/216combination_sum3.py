class Solution(object):
    def combinationSum3(self, k, n):
        def getCombination(num, cur_sum, cur_sol, all_sols):
            if len(cur_sol) == k and cur_sum == n:
                all_sols.append(list(cur_sol))
                return
            if len(cur_sol) > k:
                return
            for i in xrange(num, 10):
                if i + cur_sum <= n:
                    cur_sol.append(i)
                    getCombination(i + 1, cur_sum + i, cur_sol, all_sols)
                    cur_sol.pop()
        res = []
        getCombination(1, 0, [], res)
        return res

if __name__ == "__main__":
    sol = Solution()
    print sol.combinationSum3(3, 9)
