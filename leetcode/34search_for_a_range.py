class Solution(object):
    #Solution 1, most original version, first find any number equals to target, than do two binary search
    def searchRange(self, nums, target):
        start, end = 0, len(target)
        # Find the index of any number in nums equals to target
        while start <= end:
            mid = (end - start) / 2 + start
            if nums[mid] == target:
                break
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        if start > end:
            return [-1, -1]
        
        # Extend nums, initialize
        new_nums = [nums[0] - 1, ] + nums + [nums[-1] + 1, ]
        left_tail = right_head = mid + 1
        left_head, right_tail = 1, len(new_nums) - 1
        range_head = range_tail = mid + 1

        # evaluate left sub
        while left_head <= left_tail:
            mid = (left_tail - left_head) + left_head
            if new_nums[mid] == target and new_nums[mid-1] < target:
                range_head = mid
                break
            elif new_nums[mid] == target:
                left_tail = mid - 1
            else:
                left_head = mid + 1

        # evaluate right sub
        while right_head <= right_tail:
            mid = (right_tail - right_head) / 2 + right_head
            if new_nums[mid] == target and new_nums[mid+1] > target:
                range_tail = mid
                break
            elif new_nums[mid] == target:
                right_head = mid + 1
            else:
                right_tail = mid - 1
        return [range_head, range_tail]

    # Solution 2, more concise version from the forum
    def searchRange2(self, nums, target):
        def searchStart(nums, x):
            s, e = 0, len(nums) - 1
            while s <= e:
                mid = (e - s) / 2 + s
                if nums[mid] >= x:
                    e = mid - 1
                else:
                    s = mid + 1
            return s

        def searchEnd(nums, x):
            s, e = 0, len(nums) - 1
            while s <= e:
                mid = (e - s) / 2 + s
                if nums[mid] > x:
                    e = mid - 1
                else:
                    s = mid + 1
            return e
        
        start, end = searchStart(nums, target), searchEnd(nums, target)
        return [start, end] if start <= end else [-1, -1]

    # Solution 3, just one round of binary search
    def searchRange3(self, nums, target):
        s, e = 0, len(nums) - 1
        while nums[s] < nums[e]:
            mid = (e - s) / 2 + s
            if nums[mid] < target:
                s = mid + 1
            elif nums[mid] > target:
                e = mid - 1
            else:
                if nums[mid] == nums[s]:
                    e -= 1
                else:
                    s += 1
        return [s, e] if nums[s] == nums[e] == target else [-1, -1]
