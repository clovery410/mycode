class Solution(object):
    def lengthOfLIS(self, nums):
        if len(nums) == 0:
            return 0
        dp = [1] * len(nums)
        for i in xrange(1, len(nums)):
            for j in xrange(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    #Solution2, maintain an increasing sublist, when the new item comes, check whether it is greater than the last num in that sublist, if yes, append the new item to the sublist, it not, replace the first element which is greater than the new item among the sublist use binary search.
    def lengthOfLIS2(self, nums):
        lis = []
        for num in nums:
            if len(lis) == 0 or num > lis[-1]:
                lis.append(num)
            else:
                idx = self.binarySearch(lis, num)
                lis[idx] = num
        return len(lis)

    def binarySearch(self, nums, k):
        s, e = 0, len(nums)
        while s <= e:
            mid = (e - s) / 2 + s
            if nums[mid] == k:
                return mid
            if nums[mid] > k:
                e = mid - 1
            else:
                s = mid + 1
        return s
    
if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    sol = Solution()
    print sol.lengthOfLIS(nums)
    print sol.lengthOfLIS2(nums)
