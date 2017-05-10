class Solution(object):
    def fourSum(self, nums, target):
        if len(nums) < 4: return []
        nums.sort()
        res = []
        pre_a = -sys.maxint-1
        for i, a in enumerate(nums):
            if a == pre_a: continue
            
            pre_b = nums[i]-1
            for j in xrange(i+1, len(nums)):
                b = nums[j]
                if b == pre_b: continue
                
                s, e = j + 1, len(nums) - 1
                while s < e:
                    c, d = nums[s], nums[e]
                    if a + b + c + d == target:
                        res.append([a, b, c, d])
                        while s < e and nums[s] == c: s += 1
                        while s < e and nums[e] == d: e -= 1
                    elif a + b + c + d < target:
                        s += 1
                    else:
                        e -= 1
                pre_b = b
            pre_a = a
        return res
