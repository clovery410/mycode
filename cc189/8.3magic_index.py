class Solution(object):
    # if numbers are distinct, we can use binary search
    def magicIndex(self, nums):
        s, e = 0, len(nums) - 1
        while s < e:
            mid = (e - s) / 2 + s
            if nums[mid] == mid:
                return mid
            if nums[mid] < mid:
                s = mid + 1
            else:
                e = mid - 1
        return -1

    # if numbers are not distinct, we need a little more trick here
    def magicIndex2(self, nums):
        def helper(s, e):
            if s > e:
                return -1
            mid = (e - s) / 2 + s
            if nums[mid] == mid:
                return mid

            #first search left
            left = helper(s, min(mid-1, nums[mid]))
            if left >= 0: return left

            #if left fail, then search right
            right = helper(max(mid + 1, nums[mid]), e)
            return right
        return helper(0, len(nums) - 1)
            

if __name__ == "__main__":
    sol = Solution()
    nums = [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]
    print sol.magicIndex2(nums)
         
