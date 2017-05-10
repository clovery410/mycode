class Solution(object):
    def nextPermutation(self, nums):
        for i in reversed(range(1, len(nums))):
            if nums[i-1] < nums[i]:  #find a reverse here
                idx = self.findSecond(nums, i-1)
                nums[i-1], nums[idx] = nums[idx], nums[i-1]
                self.reverseList(nums, i)
                return nums
        self.reverseList(nums, 0)
        return nums

    def findSecond(self, nums, idx):
        target = nums[idx]
        for i in reversed(range(idx+1, len(nums))):
            if nums[i] > target:
                return i

    def reverseList(self, nums, idx):
        s, e = idx, len(nums) - 1
        while s < e:
            nums[s], nums[e] = nums[e], nums[s]
            s += 1
            e -= 1

if __name__ == "__main__":
    sol = Solution()
    print sol.nextPermutation([1, 4, 5, 8, 3])
    
