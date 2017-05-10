import random

def shuffle(nums):
    n = len(nums)
    for i in xrange(n):
        j = random.randint(i, n-1)
        nums[i], nums[j] = nums[j], nums[i]

    print nums

nums = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5]
shuffle(nums)
