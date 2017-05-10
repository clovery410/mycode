class Solution(object):
    # first do a O(n^2) solution
    def lengthOfLIS(self, nums):
        if len(nums) == 0:
            return 0
        
        dp = [1] * len(nums)
        for i in xrange(1, len(nums)):
            cur_count = 0
            for j in xrange(i):
                if nums[i] > nums[j]:
                    cur_count = max(cur_count, dp[j])
            dp[i] = cur_count + 1
        return max(dp)

    # solution2, try to come up a O(nlog n) solution, which is a binary search solution
    def lengthOfLIS2(self, nums):
        if len(nums) == 0:
            return 0

        stack = []
        res = 0
        for num in nums:
            if len(stack) == 0 or num > stack[-1]:
                stack.append(num)
                res = max(res, len(stack))
            else:
                s, e = 0, len(stack) - 1
                while s <= e:
                    mid = (e - s) / 2 + s
                    if stack[mid] == num:
                        res = max(res, mid + 1)
                        break
                    elif stack[mid] < num:
                        s = mid + 1
                    else:
                        e = mid - 1
                if s > e:
                    stack[s] = num
                res = max(res, s + 1)
        return res

    # solution3, modify a little bit to make solution2 more concise, only need to replace the first greater element
    def lengthOfLIS3(self, nums):
        stack = []
        for num in nums:
            if len(stack) == 0 or stack[-1] < num:
                stack.append(num)
            else:
                s, e = 0, len(stack) - 1
                while s <= e:
                    mid = (e - s) / 2 + s
                    if stack[mid] < num:
                        s = mid + 1
                    else:
                        e = mid - 1
                stack[s] = num
        return len(stack)

if __name__ == "__main__":
    sol = Solution()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print sol.lengthOfLIS(nums)
    print sol.lengthOfLIS2(nums)
    print sol.lengthOfLIS3(nums)
        
