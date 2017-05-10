class Solution(object):
    def summaryRanges(self, nums):
        if len(nums) == 0:
            return []

        nums.append(nums[-1] + 2)
        res = []
        start_num = nums[0]
        for i in xrange(1, len(nums)):
            cur_num, pre_num = nums[i], nums[i-1]
            if cur_num > pre_num + 1:
                if pre_num == start_num:
                    res.append(str(pre_num))
                else:
                    res.append(str(start_num) + '->' + str(pre_num))
                start_num = cur_num

        return res
                
