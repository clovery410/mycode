import math
class Solution(object):
    #Very very slow, since I construct all the possible solutions which are not required in this problem
    def combinationSum4(self, nums, target):
        def helper(candidates, remain, cur_solution, all_solutions):
            if remain == 0:
                all_solutions.add(tuple(cur_solution))
                return
            if len(candidates) == 0:
                return
            for i, cur_val in enumerate(candidates):
                if cur_val <= remain:
                    cur_solution.append(cur_val)
                    helper(candidates, remain - cur_val, cur_solution, all_solutions)
                    cur_solution.pop()
                    helper(candidates[:i] + candidates[i+1:], remain, cur_solution, all_solutions)
        res = set()
        helper(nums, target, [], res)
        return len(res)

    #normal recursive solution
    def combinationSum5(self, nums, target):
        def helper(idx, remain, cur_solution):
            if remain == 0:
                self.res += self.permutationCount(cur_solution)
                return
            if idx >= len(nums):
                return
            cur_val = nums[idx]
            if cur_val <= remain:
                cur_solution.append(cur_val)
                helper(idx, remain - cur_val, cur_solution)
                cur_solution.pop()
                helper(idx+1, remain, cur_solution)
        nums.sort()
        self.res = 0
        helper(0, target, [])
        return self.res

    def permutationCount(self, array):
        dup = dict((elem, array.count(elem)) for elem in set(array))
        count = math.factorial(len(array))
        for num in dup:
            count /= math.factorial(dup[num])
        return count
        # return math.factorial(l) / reduce(lambda x, y: x * y, dup)

    def combinationSum6(self, nums, target):
        def helper(remain):
            if remain in cache:
                return cache[remain]
            if remain == 0:
                cache[remain] = 1
            elif remain < 0:
                cache[remain] = 0
            else:
                count = 0
                for num in nums:
                    count += helper(remain - num)
                cache[remain] = count
            return cache[remain]
        cache = {}
        return helper(target)
    
    #Non recursion solution
    def combinationSum7(self, nums, target):
        n = len(nums)
        res = 0
        stack = [(0, target, [])]
        while len(stack) > 0:
            idx, remain, cur_solution = stack.pop()
            if remain == 0:
                res += self.permutationCount(cur_solution)
            # if idx < len(nums):
            #     if nums[idx] <= remain:
            #         stack.append((idx, remain - nums[idx], cur_solution + [nums[idx],]))
            #         stack.append((idx+1, remain, cur_solution))
            for i in xrange(idx, len(nums)):
                if nums[i] <= remain:
                    # new_solution = list(cur_solution)
                    # new_solution.append(nums[i])
                    stack.append((i, remain - nums[i], cur_solution + [nums[i],]))
        return res

    #dp solution, bottom up
    def combinationSum8(self, nums, target):
        dp = [0] * (target + 1)
        #initialize dp
        dp[0] = 1
        #calculate each dp[i] based on the sum of all solution from dp[i-num] for num in nums
        for i in xrange(1, target+1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i-num]
        return dp[-1]

    #dp solution, top down with hashmap, but this solution may make the stack crash.
    def combinationSum9(self, nums, target):
        def helper(target):
            if target < 0 or len(nums) == 0:
                return 0
            if target == 0:
                return 1
            if target in cache:
                return cache[target]

            count = 0
            for num in nums:
                count += helper(target - num)
            cache[target] = count
            return count
        cache = {}
        return helper(target)
                
if __name__ == "__main__":
    nums = [1,50]
    nums2 = [3,33,333]
    sol = Solution()
    # print sol.combinationSum7(nums, 200)
    # print sol.combinationSum7(nums2, 10000)
    print sol.combinationSum8(nums, 200)
    print sol.combinationSum8(nums2, 10000)
    print sol.combinationSum9(nums, 200)
    # print sol.combinationSum9(nums2, 10000)
