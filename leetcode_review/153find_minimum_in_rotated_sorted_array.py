class Solution(object):
    #Solution1, the first solution come up with
    def findMin(self, nums):
        s, e = 0, len(nums) - 1
        while s < e:
            if nums[s] < nums[e]:
                return nums[s]
            else:
                mid = (e - s) / 2 + s
                if nums[mid] > nums[e]:
                    s = mid + 1
                elif nums[mid] < nums[s]:
                    e = mid
        return nums[s]

    #Solution2, more concise version
    def findMin2(self, nums):
        s, e = 0, len(nums) - 1
        while s < e:
            mid = (e - s) / 2 + s
            if nums[mid] > nums[e]:
                s = mid + 1
            else:
                e = mid
        return nums[s]
                    
                    
