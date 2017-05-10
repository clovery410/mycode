class Solution(object):
    def combinationSum(self, candidates, target):
        def generate(idx, cur_sol, all_sols, remain):
            if remain == 0:
                all_sols.append(cur_sol[:])
                return
            for i in xrange(idx, len(candidates)):
                cur_num = candidates[i]
                if remain - cur_num >= 0:
                    cur_sol.append(cur_num)
                    generate(i, cur_sol, all_sols, remain - cur_num)
                    cur_sol.pop()
        res = []
        candidates.sort()
        generate(0, [], res, target)
        return res

if __name__ == "__main__":
    sol = Solution()
    candidates = [2,3,6,7]
    target = 7
    print sol.combinationSum(candidates, target)
