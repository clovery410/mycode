class Solution(object):
    def canJump(self, nums):
        l = len(nums)
        if l <= 1: return True
        
        i = l - 2
        while i >= 0:
            if nums[i] != 0:
                i -= 1
            else:
                s = i-1
                while s >= 0 and nums[s] <= i - s:
                    s -= 1
                if s < 0: return False
                i = s
        return True

    #solution2, learned from discuss
    def canJump2(self, nums):
        reachable = 0
        for i, num in enumerate(nums):
            if reachable < i:
                return False
            reachable = max(reachable, i + num)

        return True

    
if __name__ == "__main__":
    nums = [2,0,4]
    sol = Solution()
    print sol.canJump2(nums)
