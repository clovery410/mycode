class Solution(object):
    def minPatches(self, nums, n):
        missing = 1
        idx = count = 0
        while missing <= n:
            if idx < len(nums) and nums[idx] <= missing:
                missing += nums[idx]
                idx += 1
            else:
                count += 1
                missing += missing

        return count

if __name__ == "__main__":
    sol = Solution()
    print sol.minPatches([1,2,2], 5)
                
