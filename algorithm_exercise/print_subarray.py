def print_subarray(nums):
    n = len(nums)
    for i in xrange(n):
        for j in xrange(i+1, n+1):
            print nums[i:j]

nums = [1, 2, 3, 4]
print_subarray(nums)
