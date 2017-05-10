def binarySearch(nums, key):
    n = len(nums)
    start, end = 0, n - 1
    while start <= end:
        mid = start + (end - start) / 2
        if nums[mid] == key:
            return mid
        if nums[mid] < key:
            start = mid + 1
        else:
            end = mid - 1

    return -1

def binarySearch_with_repeat(nums, key):
    nums = [nums[0] - 1,] + nums + [nums[-1] + 1,]
    n = len(nums)
    start, end = 1, n - 2
    while start <= end:
        mid = (start + end) / 2
        if nums[mid] == key and nums[mid - 1] < key:
            return mid - 1
        if nums[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def binarySearch_variation(nums, key):
    n = len(nums)
    start, end = 0, n - 1
    mid = -1
    while start <= end:
        mid = (start + end) / 2
        if nums[mid] == key:
            return mid
        if nums[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
    return start

def binarySearch_variation_repeat(nums, key):
    nums = [nums[0] - 1,] + nums + [nums[-1] + 1,]
    n = len(nums)
    start, end = 1, n - 2
    while start <= end:
        mid = (start + end) / 2
        if nums[mid] == key and nums[mid - 1] < key:
            return mid - 1
        if nums[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return start - 1

nums = [1, 3, 4, 6, 8, 9]
nums2 = [1, 3, 5, 5, 7, 8]
#print binarySearch(nums, 10)
#print binarySearch_variation(nums2, 2)
print binarySearch_with_repeat([1,3,5,5,5,7,8], 5)
#print binarySearch_variation_repeat(nums2, 6)
