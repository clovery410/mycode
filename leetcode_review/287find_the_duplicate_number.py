class Solution(object):
    def findDuplicate(self, nums):
        start, end = 1, len(nums) - 1
        while start < end:
            mid = (end - start) / 2 + start
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count <= mid:
                start = mid + 1
            else:
                end = mid
        return start

if __name__ == "__main__":
    sol = Solution()
    nums = [1,3,4,2,2]
    print sol.findDuplicate(nums)
