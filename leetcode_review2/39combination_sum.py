class Solution(object):
    def combinationSum(self, candidates, target):
        def getCombination(idx, cur_sum, cur_sol, all_sols):
            if cur_sum == target:
                all_sols.append(list(cur_sol))
                return
            if idx >= len(nums):
                return

            cur_num = nums[idx]
            if cur_sum + cur_num <= target:
                cur_sol.append(cur_num)
                getCombination(idx, cur_sum + cur_num, cur_sol, all_sols)
                cur_sol.pop()
                getCombination(idx+1, cur_sum, cur_sol, all_sols)
                
        nums = sorted(list(set(candidates)))
        res = []
        getCombination(0, 0, [], res)
        return res

if __name__ == "__main__":
    sol = Solution()
    candidates = [2, 3, 6, 7]
    print sol.combinationSum(candidates, 7)
