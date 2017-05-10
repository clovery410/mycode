def shift_array(nums, sh):
    count = i = 0
    n = len(nums)
    temp = nums[0]
    while count <= n:
        nums[(i + sh) % n], temp = temp, nums[(i + sh) % n]
        i += sh
        count += 1

nums = [1, 2, 3, 4, 5, 6, 7]
shift_array(nums, 4)
print nums
