def findMaximumTriples(nums):
    indices = [None] * len(nums)
    nums.sort()
    for i in reversed(xrange(len(nums))):
        cur = []
        for j in xrange(i):
            if nums[i] % nums[j] == 0:
                cur.append(j)
        indices[i] = cur

    res = 0
    for idx in indices:
        for i in idx:
            if len(indices[i]) > 0:
                res += 1
    return res
            

if __name__ == "__main__":
    nums = [1,2,3,4,5,6,8]
    print findMaximumTriples(nums)
