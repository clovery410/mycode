class Solution(object):
    def canJump(self, nums):
        if len(nums) == 0: return True
        l = len(nums)
        farest = nums[0]
        for i in xrange(1, l):
            if farest < i:
                return False
            if farest >= l - 1:
                return True
            farest = max(farest, i + nums[i])
        return True if farest >= l - 1 else False

if __name__ == "__main__":
    sol = Solution()
    nums = [3, 2, 1, 1, 4]
    print sol.canJump(nums)
