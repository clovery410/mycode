class Solution(object):
    def permute(self, nums):
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [[nums[0]]]
        
        res = []
        for i, num in enumerate(nums):
            res += [[num] + x for x in self.permute(nums[:i] + nums[i+1:])]
        return res

    #solution2,classic backtracing solution
    def permute2(self, nums):
        def generate(candidates, cur_sol, all_sols):
            if len(candidates) == 0:
                all_sols.append(list(cur_sol))
                return
            for i, num in enumerate(candidates):
                cur_sol.append(num)
                generate(candidates[:i] + candidates[i+1:], cur_sol, all_sols)
                cur_sol.pop()

        if len(nums) == 0: return []
        res = []
        generate(nums, [], res)
        return res

if __name__ == "__main__":
    sol = Solution()
    print sol.permute([1,2,3,4])
    print sol.permute2([1,2,3,4])
