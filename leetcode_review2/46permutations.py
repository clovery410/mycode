class Solution(object):
    #solution1, classic backtracing solution
    def permute(self, nums):
        def generate(candidates, cur_sol, all_sols):
            if len(candidates) == 0:
                all_sols.append(list(cur_sol))
                return
            for i, num in enumerate(candidates):
                cur_sol.append(num)
                generate(candidates[:i] + candidates[i+1:], cur_sol, all_sols)
                cur_sol.pop()

        res = []
        generate(nums, [], res)
        return res

    #solution2
    def permute2(self, nums):
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [[nums[0]]]
        res = []
        for i, num in enumerate(nums):
            res += [[num] + x for x in self.permute2(nums[:i] + nums[i+1:])]
        return res

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3]
    print sol.permute2(nums)
