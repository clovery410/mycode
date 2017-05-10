import time
class Solution(object):
    #Solution1
    def maxSubArray(self, nums):
        if nums == []:
            return None
        record = nums[:]
        for i in xrange(1, len(nums)):
            record[i] = max(record[i], record[i] + record[i-1])
        return max(record)
    
    #Solution2
    def maxSubArray2(self, nums):
        res = cur_total = nums[0]
        for num in nums[1:]:
            cur_total = cur_total + num if cur_total >= 0 else num
            res = max(res, cur_total)
        return res

if __name__ == "__main__":
    nums = [-2, 0, -1, 3, 6, -4, 1, -5, 4]
    sol = Solution()
    start_time1 = time.time()
    print sol.maxSubArray(nums)
    print ("solution1 --- %s seconds ---" % (time.time() - start_time1))
    start_time2 = time.time()
    print sol.maxSubArray2(nums)
    print ("solution2 --- %s seconds ---" % (time.time() - start_time2))
    
