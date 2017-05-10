class Solution(object):
    def subsetsWithDup(self, nums):
        def generate(idx, cur_sol, all_sols):
            # subset means it does not need contain all elements, so the condition is <= rather than ==
            # and do not return after this statement
            if idx <= len(nums):
                all_sols.append(list(cur_sol))

            for i in xrange(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                cur_sol.append(nums[i])
                generate(i+1, cur_sol, all_sols)
                cur_sol.pop()
                    
        nums.sort()
        res = []
        generate(0, [], res)
        return res

    #solution2
    def subsetsWithDup2(self, nums):
        def generate(idx, cur_sol, all_sols):
            if idx >= len(nums):
                all_sols.add(tuple(cur_sol))
                return
            generate(idx+1, cur_sol, all_sols)
            cur_sol.append(nums[idx])
            generate(idx+1, cur_sol, all_sols)
            cur_sol.pop()

        nums.sort()
        res = set()
        generate(0, [], res)
        return [list(elem) for elem in res]

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 2]
    print sol.subsetsWithDup(nums)
