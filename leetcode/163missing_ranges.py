class Solution(object):
    # First version, really slow
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        l = len(nums)
        if upper < lower:
            return []
        if l == 0:
            if upper == lower:
                return [str(lower),]
            else:
                return [str(lower) + '->' + str(upper)]
            
        ret = []
        if nums[0] == lower + 1:
            ret.append(str(lower))
        elif nums[0] > lower + 1:
            ret.append(str(lower) + '->' + str(nums[0] - 1))
            
        pre = nums[0]
        for i in xrange(1, len(nums)):
            curr_num = nums[i]
            if curr_num > pre + 1:
                if curr_num - 1 == pre + 1:
                    ret.append(str(pre+1))
                else:
                    ret.append(str(pre + 1) + '->' + str(curr_num - 1))
            pre = curr_num
        if pre < upper - 1:
            ret.append(str(pre + 1) + '->' + str(upper))
        elif pre == upper - 1:
            ret.append(str(upper))
        return ret

    #second version, same algorithm, but more clear, do not need to consider corner case separately. Just make the range one larger
    def findMissRanges(self, nums, lower, upper):
        lower -= 1
        upper += 1
        ret = []
        l = len(nums)
        for curr_num in nums:
            if curr_num > lower + 1:
                if curr_num > lower + 2:
                    ret.append(str(lower + 1) + '->' + str(curr_num - 1))
                else:
                    ret.append(str(lower + 1))
            lower = curr_num

        if upper > lower + 1:
            if upper > lower + 2:
                ret.append(str(lower + 1) + '->' + str(upper - 1))
            else:
                ret.append(str(lower + 1))

        return ret

    #Third version, modefied based on version 2, expand the array so that do not neet to consider the last corner separately
    def findMissingRanges3(self, nums, lower, upper):
        nums.append(upper + 1)
        res = []
        pre = lower - 1
        for curr_num in nums:
            if curr_num - pre == 2:
                res.append(str(pre + 1))
            elif curr_num - pre > 2:
                res.append(str(pre + 1) + '->' + str(curr_num - 1))

            pre = curr_num

        return res

    
if __name__ == "__main__":
    sol = Solution()
    nums = [-2, 0, 3]
    print sol.findMissingRanges(nums, -2, 4)
    print sol.findMissingRanges3(nums, -2, 4)
