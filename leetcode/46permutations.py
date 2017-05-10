class Solution(object):
    def permute(self, nums):
        n = len(nums)
        def get_next(current_solution, available_nums, all_solutions):
            if len(available_nums) == 0:
                all_solutions.append(current_solution[:])
                return
            for i in xrange(len(available_nums)):
                current_solution.append(available_nums[i])
                get_next(current_solution, available_nums[:i] + available_nums[i+1:], all_solutions)
                current_solution.pop()

        ans = []
        get_next([], nums, ans)
        return ans

sol = Solution()
s = [1, 2, 3]
print sol.permute(s)
