import operator
class Solution(object):
    #Solution1, use two pointers, one pass, O(n) running time
    def minSubArrayLen(self, s, nums):
        n = len(nums)
        left = right = 0
        curr_sum, min_length = 0, n + 1
        while right < n:
            curr_sum += nums[right]
            if min_length == 1:
                return 1
            while curr_sum >= s and left <= right:
                min_length = min(min_length, right - left + 1)
                curr_sum -= nums[left]
                left += 1
            right += 1

        return 0 if min_length > n else min_length
            
    #Solution2, use binary search, O(nlogn) running time
    def minSubArrayLen2(self, s, nums):
        sums = list(self.accumulate([0] + nums, operator.add))
        min_length = len(nums) + 1
        for i, curr_sum in enumerate(sums):
            if curr_sum == s:
                min_length = min(min_length, i)
            elif curr_sum > s:
                start, end = 0, i
                while start < end:
                    mid = (end - start) / 2 + start
                    if sums[mid] <= curr_sum - s:
                        start = mid + 1
                    else:
                        end = mid
                min_length = min(min_length, i - end + 1)
        return 0 if min_length > len(nums) else min_length

    def accumulate(self, iterable, func = operator.add):
        it = iter(iterable)
        total = next(it)
        yield total
        for element in it:
            total = func(total, element)
            yield total

if __name__ == "__main__":
    sol = Solution()
    nums = [2, 3, 1, 2, 4, 3]
    print sol.minSubArrayLen(7, nums)
    print sol.minSubArrayLen2(7, nums)
