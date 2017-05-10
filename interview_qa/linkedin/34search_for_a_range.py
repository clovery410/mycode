class Solution(object):
    def searchRange(self, nums, target):
        def searchStart(s, e):
            while s <= e:
                mid = (e - s) / 2 + s
                if nums[mid] >= target:
                    e = mid - 1
                else:
                    s = mid + 1
            return s if s < len(nums) and nums[s] == target else -1

        def searchEnd(s, e):
            while s <= e:
                mid = (e - s) / 2 + s
                if nums[mid] <= target:
                    s = mid + 1
                else:
                    e = mid - 1
            return e if e >= 0 and nums[e] == target else -1

        if len(nums) == 0:
            return [-1,-1]
        
        start_idx = searchStart(0, len(nums) - 1)
        end_idx = searchEnd(0, len(nums) - 1)
        return [start_idx, end_idx]

if __name__ == "__main__":
    sol = Solution()
    nums = [5,7,7,8,8,10]
    target = 11
    print sol.searchRange(nums, target)
