class Solution(object):
    # traversal the list once, running time is O(n)
    def searchInsert(self, nums, target):
        length, index = len(nums), 0
        while index < length:
            if nums[index] >= target:
                return index
            else:
                index += 1
        return index

    # Start from two end simultaneously， running time O(n/2)
    def second_solution(self, nums, target):
        length = len(nums)
        i, j = 0, length - 1
        while i <= j:
            num_i, num_j = nums[i], nums[j]
            if num_i < target and num_j >= target:
                i += 1
                j -= 1
            elif num_i < target:
                return j+1
            else:
                return i
        return i

    # This solution uses binary search, running time is O(log n)
    def third_solution(self, nums, target):
        length = len(nums)
        start, end = 0, length - 1
        mid = (start + end) / 2
        
        while (start <= end):
            if nums[start] >= target:
                return start
            if nums[end] < target:
                return end + 1
            if nums[end] == target:
                return end
        
            mid_v = nums[mid]
            if mid_v == target:
                return mid
            elif mid_v < target:
                start = mid + 1
                mid = (start + end) / 2
            else:
                end = mid - 1
                mid = (start + end) / 2
                
