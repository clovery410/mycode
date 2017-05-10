class Solution(object):
    def permute(self, nums):
        def generate(cur_sol, all_sols, remain_num):
            if len(remain_num) == 0:
                all_sols.append(cur_sol[:])
                return
            for num in list(remain_num):
                cur_sol.append(num)
                remain_num.remove(num)
                generate(cur_sol, all_sols, remain_num)
                cur_sol.pop()
                remain_num.add(num)
                
        res = []
        remain_num = set(nums)
        generate([], res, remain_num)
        return res

    # solution2
    def permute2(self, nums):
        def generate(cur_sol, all_sols, remain_nums):
            if len(remain_nums) == 0:
                all_sols.append(cur_sol[:])
                return
            for i, num in enumerate(remain_nums):
                cur_sol.append(num)
                generate(cur_sol, all_sols, remain_nums[:i] + remain_nums[i+1:])
                cur_sol.pop()
                
        res = []
        generate([], res, nums)
        return res

    # solution3
    def permute3(self, nums):
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]

        res = []
        for i, num in enumerate(nums):
            res.extend([num] + x for x in self.permute3(nums[:i] + nums[i+1:]))
        return res
