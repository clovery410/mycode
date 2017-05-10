def merge_sort(nums):
    if len(nums) <= 1:
        return
    mid = len(nums) / 2
    left = nums[0:mid]
    right = nums[mid:]

    merge_sort(left)
    merge_sort(right)

    l, r = 0, 0
    for i in xrange(len(nums)):
        l_val = left[l] if l < len(left) else None
        r_val = right[r] if r < len(right) else None

        if (l_val is not None and r_val is not None and l_val < r_val) or r_val is None:
            nums[i] = left[l]
            l += 1
        elif (l_val is not None and r_val is not None and l_val > r_val) or l_val is None:
            nums[i] = right[r]
            r += 1
        else:
            raise Exception('Count not merge, sub arrays size does not match')

    return nums

print merge_sort([1, 3, 5, 2, 4, 6, 10, 20, 30, 11, 12, 13])
    
