#Question: given an array, find how many pairs in array fullfill the require: nums[i] + nums[j] + nums[k] = nums[l], where i < j < k < l

import collections
#following is amortized O(n^2) solution, worst case O(n^3), but needs O(n^2) extra space
def findFourSum(nums):
    res = 0
    two_sums = collections.defaultdict(list)
    for i in xrange(len(nums)-1):
        for j in xrange(i+1, len(nums)):
            two_sums[nums[i] + nums[j]].append((i, j))

    for i in xrange(2, len(nums)-1):
        for j in xrange(i+1, len(nums)):
            _sum = nums[j] - nums[i]
            if _sum in two_sums:
                for pair in two_sums[_sum]:
                    if i > pair[1]:
                        res += 1
    return res

if __name__ == "__main__":
    print findFourSum([1,3,4,5,8,2,10,14,1])
