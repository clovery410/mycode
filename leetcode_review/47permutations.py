class Solution(object):
    #solution1, classic backtracing, using sort and set to eliminate duplicate situation
    def permute(self, nums):
        def generate(candidates, cur_sol, all_sols):
            if len(candidates) == 0:
                all_sols.append(list(cur_sol))
                return

            for num in set(candidates):
                i = candidates.index(num)
                cur_sol.append(num)
                generate(candidates[:i] + candidates[i+1:], cur_sol, all_sols)
                cur_sol.pop()
                    
        if len(nums) == 0: return []
        res = []
        generate(sorted(nums), [], res)
        return res

    #solution2, another backtracing way using list comprehension, here use sort() and set to eliminate duplicate
    def permute2(self, nums):
        def generate(nums):
            if len(nums) == 1: return [[nums[0]]]
            
            res = []
            for num in set(nums):
                i = nums.index(num)
                res += [[num] + x for x in self.permute(nums[:i] + nums[i+1:])]
            return res
        
        if len(nums) == 0: return []
        return generate(sorted(nums))


if __name__ == "__main__":
    sol = Solution()
    print sol.permute([3,3,0,0,2,3,2])
    print sol.permute2([3,3,0,0,2,3,2])
