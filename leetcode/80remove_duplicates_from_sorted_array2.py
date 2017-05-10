class Solution(object):
    def removeDuplicates(self, nums):
        pre = 0
        for cur in xrange(len(nums)):
            
            if cur > pre and nums[cur] != nums[pre]:
                nums[cur], nums[pre] = nums[pre], nums[cur]

            if pre < 2 or nums[pre-2] != nums[pre]:
                pre += 1
                
        return pre
                
