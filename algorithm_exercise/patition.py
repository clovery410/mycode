def patition(nums, value):
    n = len(nums)
    i = j = 0
    while j < n:
        if nums[j] > value:
            j += 1
        else:
            if i != j:
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1

    return i - 1


nums = [5, 2, 8, 9, 1, 3, 7]
patition(nums, 7)
print nums
