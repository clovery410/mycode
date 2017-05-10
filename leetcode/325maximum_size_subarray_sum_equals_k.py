class Solution(object):
    # brute-force solution, TLE
    def maxSubArrayLen(self, nums, k):
        max_len = 0
        l = len(nums)
        for start in xrange(l):
            cur_total = 0
            for end in xrange(start, l):
                cur_total += nums[end]
                if cur_total == k:
                    max_len = max(max_len, end - start + 1)
        return max_len

    # soltion2
    def maxSubArrayLen2(self, nums, k):
        nums = [0] + nums
        sum_record = {}
        cur_total = 0
        max_len = 0
        for j in xrange(len(nums)):
            cur_total += nums[j]
            pre_sum = cur_total - k
            if pre_sum in sum_record:
                max_len = max(max_len, j - sum_record[pre_sum])
            if cur_total not in sum_record:
                sum_record[cur_total] = j
        return max_len

if __name__ == "__main__":
    sol = Solution()
    nums = [1,-1,5,-2,3]
    print sol.maxSubArrayLen(nums, 3)
    print sol.maxSubArrayLen2(nums, 3)
            
