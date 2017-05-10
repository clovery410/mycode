class Solution(object):
    def permuteUnique(self, nums):
        #this solution will TLE
        def generate(candidates, cur_sol, all_sols):
            if len(candidates) == 0:
                all_sols.add(tuple(cur_sol))
                return
            for i, num in enumerate(candidates):
                cur_sol.append(num)
                generate(candidates[:i] + candidates[i+1:], cur_sol, all_sols)
                cur_sol.pop()
                
        res = set()
        generate(nums, [], res)
        return [list(elem) for elem in res]

    #solution2, use pre to prune early
    def permuteUnique2(self, nums):
        def generate(candidates, cur_sol, all_sols):
            if len(candidates) == 0:
                all_sols.append(list(cur_sol))
                return

            pre = None
            for i, num in enumerate(candidates):
                if num != pre:
                    cur_sol.append(num)
                    generate(candidates[:i] + candidates[i+1:], cur_sol, all_sols)
                    cur_sol.pop()
                pre = num

        nums.sort()
        res = []
        generate(nums, [], res)
        return res

    #solution3, backtracing with list comprehension
    def permuteUnique3(self, nums):
        def generate(nums):
            if len(nums) == 1:
                return [[nums[0]]]
            
            res = []
            for num in set(nums):
                i = nums.index(num)
                res += [[num] + x for x in generate(nums[:i] + nums[i+1:])]
            return res
                
        nums.sort()
        return generate(nums)
    
if __name__ == "__main__":
    sol = Solution()
    nums = [3,3,0,3]
    print sol.permuteUnique(nums)
    print sol.permuteUnique2(nums)
    print sol.permuteUnique3(nums)
    
