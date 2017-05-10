def insertion_sort(nums):
    n = len(nums)
    for i in xrange(n-1):
        j = i + 1
        pre = j - 1
        while pre >= 0:
            if nums[j] >= nums[pre]:
                break
            nums[j], nums[pre] = nums[pre], nums[j]
            j = pre
            pre -= 1


def partition(nums, start, end):
    pivot = nums[start]
    i = start + 1
    for j in xrange(start + 1, end + 1):
        if nums[j] > pivot:
            continue
        else:
            if i != j:
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[start], nums[i-1] = nums[i-1], nums[start]
    return i-1

def quicksort(nums, start, end):
    if start < end:
        p = partition(nums, start, end)
        quicksort(nums, start, p - 1)
        quicksort(nums, p + 1, end)
            
    

nums = [4, 1, 2, 6, 3, 8, 5]
quicksort(nums, 0, 6)
print nums
