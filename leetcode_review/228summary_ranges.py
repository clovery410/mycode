class Solution(object):
    def summaryRanges(self, nums):
        if len(nums) == 0:
            return []

        # small trick to get rid of considering last elment seperately
        nums.append(nums[-1] + 2)
        res = []
        start = pre = nums[0]
        for i in xrange(1, len(nums)):
            cur = nums[i]
            if cur - pre == 1:
                pre = cur
            else:
                if start == pre:
                    res.append(str(start))
                else:
                    res.append(str(start) + "->" + str(pre))
                start = pre = cur
        return res

if __name__ == "__main__":
    sol = Solution()
    nums = [0,1,2,4,5,7]
    print sol.summaryRanges(nums)
            
