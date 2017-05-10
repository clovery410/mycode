class Solution(object):
    def searchRange(self, nums, target):
        if len(nums) == 0:
            return [-1, -1]
        if target < nums[0] or target > nums[-1]:
            return [-1, -1]
        nums = [nums[0] - 1,] + nums + [nums[-1] + 1,]

        start = end = 0
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (high - low) / 2 + low
            if nums[mid] == target and nums[mid-1] < target:
                start = mid
                break
            elif nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (high - low) / 2 + low
            if nums[mid] == target and nums[mid+1] > target:
                end = mid
                break
            elif nums[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
        return [start-1, end-1]

    #Solution2
    def searchRange2(self, nums, target):
        if len(nums) <  0:
            return [-1,-1]
        s, e = 0, len(nums) - 1
        while nums[s] < nums[e]:
            mid = (e - s) / 2 + s
            if nums[mid] < target:
                s = mid + 1
            elif nums[mid] > target:
                e = mid - 1
            elif nums[mid] == nums[s]:
                e -= 1
            else:
                s += 1
        return [s, e] if nums[s] == nums[e] else [-1,-1]
                

if __name__ == "__main__":
    nums = [7, 7, 7, 7, 7, 7]
    sol = Solution()
    print sol.searchRange(nums, 7)
    print sol.searchRange2(nums, 7)
        
