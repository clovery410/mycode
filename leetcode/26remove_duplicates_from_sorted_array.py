class Solution(object):
    # this solution is for non-sorted array
    def removeDuplicates(self, nums):
        if len(nums) <= 1:
            return len(nums)
        
        visited = set()
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] not in visited:
                visited.add(nums[start])
                start += 1
            else:
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1
        return start

    # correct solution for this question
    def removeDuplicates2(self, nums):
        pre, cur = 0, 1
        while cur < len(nums):
            if nums[pre] != nums[cur]:
                pre += 1
                if cur > pre:
                    nums[pre], nums[cur] = nums[cur], nums[pre]
            cur += 1
        return pre + 1 if len(nums) > 0 else 0

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2]
    print sol.removeDuplicates2(nums)
