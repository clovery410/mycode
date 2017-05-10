class Solution(object):
    def combinationSum2(self, candidates, target):
        def getCombination(idx, cur_sum, cur_sol, all_sols):
            if cur_sum == target:
                all_sols.add(tuple(cur_sol))
                return
            if idx >= len(candidates):
                return
            for i in xrange(idx, len(candidates)):
                cur_num = candidates[i]
                if cur_num + cur_sum <= target:
                    cur_sol.append(cur_num)
                    getCombination(i+1, cur_sum + cur_num, cur_sol, all_sols)
                    cur_sol.pop()

        candidates.sort()
        res = set()
        getCombination(0, 0, [], res)
        return list(list(elem) for elem in res) 

if __name__ == "__main__":
    sol = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    print sol.combinationSum2(candidates, 7)
