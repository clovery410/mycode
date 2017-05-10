# Warmup, no assumption that majority exist, just find the most frequenyly number in the array
def select_most(nums):
    helper = {】
    max_count = 0
    ret = None
    
    for item in nums:
        if item not in helper:
            helper[item] = 1
        else:
            helper[item] += 1
        if helper[item] > max_count:
            max_count = helper[item]
            ret = item

    return ret

# Assumption: if majority exist in the array, find it! Can implement with only O(1) space
def select_majority(nums):
    count = 1
    candidate = nums[0]
    for i in xrange(1, len(nums)):
        if count == 0:
            candidate = nums[i]
            count = 1
        elif nums[i] == candidate:
            count += 1
        else:
            count -= 1

    return candidate
        
