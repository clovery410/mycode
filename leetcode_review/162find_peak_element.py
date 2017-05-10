class Solution(object):
    def findPeakElement(self, nums):
        s, e = 0, len(nums) - 1
        while s < e:
            mid = (e - s) / 2 + s
            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid
            if nums[mid] < nums[mid+1]:
                s = mid + 1
            else:
                e = mid - 1
        return s

    #Solution2, also elegant solution from previous coding
    def findPeakElement2(self, nums):
        s, e = 0, len(nums) - 1
        while s < e:
            mid = (e - s) / 2 + s
            if nums[mid] < nums[mid+1]:
                s = mid + 1
            else:
                e = mid
        return s

if __name__ == "__main__":
    nums = [6,10,8,11,9,5,4,3,2,1]
    sol = Solution()
    print sol.findPeakElement(nums)
    print sol.findPeakElement2(nums)
