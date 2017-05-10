class Solution(object):
    #solution1, running time is O(n)
    def findPeakElement(self, nums):
        nums.append(nums[-1] - 1)
        l = len(nums)
        pre = nums[0] - 1
        for i in xrange(l-1):
            if nums[i] > pre and nums[i] > nums[i+1]:
                return i
            pre = nums[i]

    #soluton2, running is also O(n)
    def findPeakElement2(self, nums):
        nums.append(nums[-1] - 1)
        l = len(nums)
        pre = nums[0] - 1
        for i in xrange(l-1):
            if nums[i] > pre and nums[i] > nums[i+1]:
                return i
            pre = nums[i]

    #solution3, binary search
    def findPeakElement3(self, nums):
        def helper(nums, start, end):
            mid = (end - start) / 2 + start
            mid_num = nums[mid]
            mid_left = nums[mid-1]
            mid_right = nums[mid+1]
            if end - start < 2:
                if end == len(nums) - 1:
                    return end
                elif start == 0:
                    return 0
            if mid_left < mid_num and mid_right < mid_num:
                return mid
            elif mid_left < mid_num and mid_num < mid_right:
                return helper(nums, mid, end)
            elif mid_left > mid_num and mid_num > mid_right:
                return helper(nums, start, mid)
            else:
                return helper(nums, start, mid)
            
        l = len(nums)
        if l == 1:
            return 0
        elif l == 2:
            if nums[0] < nums[1]:
                return 1
            else:
                return 0
        res = helper(nums, 0, l - 1)
        return res

    #solution more neat binary search
    def findPeakElement4(self, nums):
        l = len(nums)
        low, high = 0, l-1
        while low < high:
            mid = (high - low) / 2 + low
            if nums[mid] < nums[mid+1]:
                low = mid + 1
            else:
                high = mid
        return low
    
if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,1]
    print sol.findPeakElement(nums)
    print sol.findPeakElement3(nums)
    print sol.findPeakElement4(nums)
