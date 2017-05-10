class Solution(object):
    def combinationSum(self, candidates, target):
        def helper(idx, value, cur_solution, all_solutions):
            if value == 0:
                all_solutions.add(tuple(cur_solution))
                return
            if idx >= len(candidates):
                return
            cur_val = candidates[idx]
            if cur_val <= value:
                cur_solution.append(cur_val)
                helper(idx+1, value - cur_val, cur_solution, all_solutions)
                cur_solution.pop()
                helper(idx+1, value, cur_solution, all_solutions)

        res = set()
        candidates.sort()
        helper(0, target, [], res)
        return [[elem for elem in row] for row in res]

if __name__ == "__main__":
    candidates = [10,1,2,7,6,1,5]
    sol = Solution()
    print sol.combinationSum(candidates, 8)
