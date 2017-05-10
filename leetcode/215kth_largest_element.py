from random import randint
class Solution(object):
    def partition(self, start, end, p, nums):
        pivot = nums[p]
        nums[p], nums[start] = nums[start], nums[p]
        i = j = k = start
        
        while j <= end:
            if nums[j] == pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            elif nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                nums[k], nums[i] = nums[i], nums[k]
                i += 1
                k += 1
            j += 1
        return k, i-1
    
    def findKthLargest(self, nums, k):
        n = len(nums)
        target = n - k
        mid_h, mid_e = self.partition(0, n - 1, randint(0, n-1), nums)
        s, e = 0, n-1
        while True:
            if target >= mid_h - s and target <= mid_e - s:
                return nums[mid_h]
            elif target > mid_e - s:
                r = randint(mid_e + 1, e)
                mid_h, mid_e = self.partition(mid_e + 1, e, r, nums)
            else:
                r = randint(s, mid_h - 1)
                mid_h, mid_e = self.partition(s, mid_h - 1, r, nums)
