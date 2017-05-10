class Solution(object):
    # solution1, use O(n) running time and O(n) extra space
    def findPeakElement(self, nums):
        temp = [nums[0] - 1] + nums + [nums[-1] - 1]
        for i in xrange(1, len(temp)-1):
            if temp[i] > temp[i-1] and temp[i] > temp[i+1]:
                return i - 1

    #solution2, O(n) running time + O(1) space
    def findPeakElement2(self, nums):
        s, e = 0, len(nums) - 1
        while s < e:
            if nums[s] < nums[e]:
                s += 1
            else:
                e -= 1
        return s
    
    #solution3, after looked at previous coding, know this can be done in binary search, try to write it again
    def findPeakElement3(self, nums):
        s, e = 0, len(nums) - 1
        while s < e:
            mid = (e - s) / 2 + s
            if nums[mid] < nums[mid+1]:
                s = mid + 1
            else:
                e = mid
        return s
