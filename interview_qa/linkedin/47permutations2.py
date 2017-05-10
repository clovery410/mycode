class Solution(object):
    def permuteUnique(self, nums):
        def generate(cur_sol, all_sols, nums):
            if len(nums) == 0:
                all_sols.append(list(cur_sol))
                return

            pre = nums[0] - 1
            for i, num in enumerate(nums):
                if num == pre:
                    continue
                cur_sol.append(num)
                generate(cur_sol, all_sols, nums[:i] + nums[i+1:])
                cur_sol.pop()
                pre = num
                
        res = []
        nums.sort()
        generate([], res, nums)
        return res
