class Solution(object):
    # solution1, need O(n) extra space and O(nlog n) running time
    def wiggleSort(self, nums):
        temp = sorted(nums)
        mid = (len(temp) + 1) / 2
        
        k = 0
        for i in reversed(xrange(mid)):
            nums[k] = temp[i]
            k += 2
        
        j = 1
        for i in reversed(xrange(mid, len(temp))):
            nums[j] = temp[i]
            j += 2

    # solution2, can optimize the space compexcity to O(1)
    
        
        
