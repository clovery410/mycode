import sys
class Solution(object):
    #Solution1, use idea of longest increasing subsequence(LIS) to maintain an increasing list. Running time is O(n*log n)
    def increasingTriplet(self, nums):
        def binarySearch(s, e, target):
            while s < e:
                mid = (e - s) / 2 + s
                if lis[mid] == target:
                    return mid
                if lis[mid] < target:
                    s = mid + 1
                else:
                    e = mid - 1
            return s

        lis = []
        for num in nums:
            if len(lis) == 0 or num > lis[-1]:
                lis.append(num)
            else:
                idx = binarySearch(0, len(lis)-1, num)
                lis[idx] = num
            if len(lis) >= 3:
                return True
        return False

    #Solution2, since we only need to check whether there is more than 3, maintain 3 variables is enough, it's a O(n) solution
    def increasingTriplet2(self, nums):
        if len(nums) < 3:
            return False
        first, second= nums[0], None
        for i in xrange(1, len(nums)):
            cur = nums[i]
            if second is not None:
                if cur > second:
                    return True
                if first < cur <= second:
                    second = cur
                else:
                    first = cur
            else:
                if cur > first:
                    second = cur
                elif cur < first:
                    first = cur
        return False

    #Solution3, rewrite solution2 into more elegant version
    def increasingTriplet3(self, nums):
        first = second = sys.maxint
        for num in nums:
            if num <= first: first = num
            elif num < second: second = num
            elif num > second: return True
        return False
        
                    
                    
            
            
