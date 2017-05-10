class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        def getRange(start, end):
            if start == end:
                return str(start)
            else:
                return str(start) + "->" + str(end)
            
        res = []
        pre = lower
        
        for num in nums:
            if num > pre:
                res.append(getRange(pre, num-1))
            pre = num + 1

        if pre <= upper:
            res.append(getRange(pre, upper))
        return res

if __name__ == "__main__":
    sol = Solution()
    nums = [0, 1, 3, 50, 75]
    print sol.findMissingRanges(nums, 0, 99)
            
            
