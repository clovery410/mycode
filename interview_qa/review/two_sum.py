def twoSum(nums, target):
    new_nums = []
    for i, num in enumerate(nums):
        new_nums.append((num, i))
    new_nums.sort()

    s, e = 0, len(new_nums) - 1
    while s < e:
        first, second = new_nums[s], new_nums[e]
        if first[0] + second[0] == target:
            return [first[1], second[1]]
        if first[0] + second[0] < target:
            s += 1
        else:
            e -= 1

def twoSum2(nums, target):
    import collections
    indices = collections.defaultdict(list)
    for i, num in enumerate(nums):
        indices[num].append(i)

    for num in nums:
        remain = target - num
        if num == remain:
            if len(indices[num]) > 1:
                return [indices[num][0], indices[num][1]]
        elif remain in indices:
            return [indices[num][0], indices[remain][0]]

print twoSum2([7, 9, 11, 15, 5], 14)

