class Solution(object):
    #Solution1, this solution deals with numbers in candidates are not distinct
    def combinationSum(self, candidates, target):
        def helper(idx, _sum, cur_solution, all_solutions):
            if _sum == target:
                all_solutions.append(cur_solution[:])
                return
            if idx >= len(candidates) or _sum > target:
                return
            helper(idx+1, _sum, cur_solution, all_solutions)
            cur_solution.append(candidates[idx])
            helper(idx, _sum+candidates[idx], cur_solution, all_solutions)
            cur_solution.pop()
        res = []
        candidates = list(set(candidates))
        helper(0, 0, [], res)
        return res

    #Solution2, if we could assume numbers in candidates are distinct, then we could sort first, which can stop early when we are doing backtracing
    def combinationSum2(self, candidates, target):
        def helper(idx, value, cur_solution, all_solutions):
            if value == 0:
                all_solutions.append(cur_solution[:])
                return
            if idx >= len(candidates):
                return
            cur_val = candidates[idx]
            if cur_val <= value:
                helper(idx+1, value, cur_solution, all_solutions)
                cur_solution.append(cur_val)
                helper(idx, value - cur_val, cur_solution, all_solutions)
                cur_solution.pop()
        res = []
        candidates.sort()
        helper(0, target, [], res)
        return res

if __name__ == "__main__":
    candidates = [2,3,6,7]
    sol = Solution()
    print sol.combinationSum(candidates, 7)
    print sol.combinationSum2(candidates, 7)
