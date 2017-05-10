class Solution(object):
    def permuteUnique(self, nums):
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in xrange(len(l) + 1):
                   new_ans.append(l[:i] + [n] + l[i:])
                   if i < len(l) and l[i] == n:
                       break
            ans = new_ans
        return ans


sol = Solution()
nums = [1,1,2]
print sol.permuteUnique(nums)
