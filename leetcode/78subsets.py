class Solution(object):
    def subsets(self, nums):
        def generate(idx, cur_sol, all_sols):
            if idx >= len(nums):
                all_sols.append(list(cur_sol))
                return
            
            generate(idx+1, cur_sol, all_sols)
            cur_sol.append(nums[idx])
            generate(idx+1, cur_sol, all_sols)
            cur_sol.pop()

        res = []
        generate(0, [], res)
        return res

    #solution2, use for loop
    def subsets2(self, nums):
        def generate(idx, cur_sol, all_sols):
            if idx <= len(nums):
                all_sols.append(list(cur_sol))

            for i in xrange(idx, len(nums)):
                cur_sol.append(nums[i])
                generate(i+1, cur_sol, all_sols)
                cur_sol.pop()
                
        res = []
        generate(0, [], res)
        return res

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3]
    print sol.subsets(nums)
    print sol.subsets2(nums)
