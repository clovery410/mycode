class Solution(object):
    def firstMissingPositive(self, nums):
        l = len(nums)
        i = 0
        while i < l:
            num = nums[i]
            if num <= 0 or num == i + 1 or num > l or num == nums[num-1]:
                i += 1
            else:
                nums[i], nums[num-1] = nums[num-1], nums[i]
        j = 1
        while j <= l:
            if j != nums[j-1]:
                return j
            j += 1
        return j

if __name__ == "__main__":
    sol = Solution()
    nums = [-1, -2, -5, -3, -4]
    print sol.firstMissingPositive(nums)
                
            
            
