class Solution(object):
    def combinationSum2(self, candidates, target):
        def generate(idx, cur_sol, all_sols, remain):
            if remain == 0:
                all_sols.add(tuple(cur_sol))
                return
            for i in xrange(idx, len(candidates)):
                cur_num = candidates[i]
                if remain - cur_num >= 0:
                    cur_sol.append(cur_num)
                    generate(i+1, cur_sol, all_sols, remain - cur_num)
                    cur_sol.pop()
        res = set()
        candidates.sort()
        generate(0, [], res, target)
        return [list(x) for x in res]

if __name__ == "__main__":
    sol = Solution()
    candidates = [10,1,2,7,6,1,5]
    target = 8
    print sol.combinationSum2(candidates, target)
