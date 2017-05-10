class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ret = []
        n = len(nums)
        if n <= 0:
            return []
        
        head = tail = nums[0]
        for i in xrange(1, n):
            curr = nums[i]
            if curr - tail == 1:
                tail = curr
            else:
                if head == tail:
                    ret.append(str(head))
                else:
                    ret.append(str(head) + '->' + str(tail))
                head = tail = curr
        if head == tail:
            ret.append(str(head))
        else:
            ret.append(str(head) + '->' + str(tail))
        return ret

    #Recursive solution, slower than the iterative version
    def summaryRanges2(self, nums):
        n = len(nums)
        if n <= 0:
            return []
        def getNext(nums, start, end, curr_i, ret):
            if curr_i >= n:
                if end == start:
                    ret.append(str(nums[start]))
                else:
                    ret.append(str(nums[start]) + '->' + str(nums[end]))
                return ret
            if nums[curr_i] - nums[end] > 1:
                if end == start:
                    ret.append(str(nums[start]))
                else:
                    ret.append(str(nums[start]) + '->' + str(nums[end]))
                getNext(nums, curr_i, curr_i, curr_i + 1, ret)
            else:
                getNext(nums, start, curr_i, curr_i + 1, ret)
        ret = []
        getNext(nums, 0, 0, 0, ret)
        return ret

sol = Solution()
print sol.summaryRanges2([0])
                
                
