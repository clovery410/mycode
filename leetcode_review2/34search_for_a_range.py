class Solution(object):
    def searchRange(self, nums, target):
        start = end = -1
        
        # first check corner case
        if nums[0] == target:
            start = 0
        if nums[-1] == target:
            end = len(nums) - 1
            
        # first search range start
        if start == -1:
            s, e = 0, len(nums) - 1
            while s <= e:
                mid = (e - s) / 2 + s
                if nums[mid] == target and nums[mid-1] < target:
                    start = mid
                    break
                if nums[mid] < target:
                    s = mid + 1
                else:
                    e = mid - 1
        # then search range end
        if end == -1:
            s, e = 0, len(nums) - 1
            while s <= e:
                mid = (e - s) / 2 + s
                if nums[mid] == target and nums[mid+1] > target:
                    end = mid
                    break
                if nums[mid] <= target:
                    s = mid + 1
                else:
                    e = mid - 1
                    
        return [start, end]

    #second solution, just one round of binary search
    def searchRange2(self, nums, target):
        if len(nums) == 0:
            return [-1, -1]
        s, e = 0, len(nums) - 1
        while nums[s] < nums[e]:
            mid = (e - s) / 2 + s
            if nums[mid] < target:
                s = mid + 1
            elif nums[mid] > target:
                e = mid - 1
            elif nums[s] == nums[mid]:
                e -= 1
            elif nums[e] == nums[mid]:
                s += 1
            else:
                s += 1
                e -= 1
        return [s, e] if nums[s] == target else [-1, -1]

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,2,2,2,3]
    print sol.searchRange2(nums, 2)
                
