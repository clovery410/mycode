class Solution(object):
    # Slow version -- Time Limit Exceeded
    def threeSumClosest(self, nums, target):
        n = len(nums)
        if n < 3:
            return None
        optiaml = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i in xrange(n):
            for j in xrange(i+1, n):
                two_sum = nums[i] + nums[j]
                k = (j+n) / 2
                while k > j and k < n:
                    if target - two_sum == nums[k]:
                        return target
                    
                    curr = two_sum + nums[k]
                    if abs(target - curr) < abs(target - optiaml):
                        optimal = curr
                    if target - two_sum > nums[k]:
                        k = (k+n+1) / 2
                    else:
                        k = (j+k) / 2
        return optiaml

    def revised_threeSum(self, nums, target):
        n = len(nums)
        nums.sort()
        optimal = nums[0] + nums[1] + nums[2]
        for k in xrange(n):
            i = k + 1
            j = n - 1
            first_sum = nums[k]
            remainder = target - nums[k]
            while i < j:
                last_two_sum = nums[i] + nums[j]
                curr = first_sum + last_two_sum
                if curr == target:
                    return curr
                if abs(target - curr) < abs(target - optimal):
                    optimal = curr
                if last_two_sum < remainder:
                    i += 1
                else:
                    j -= 1

        return optimal

if __name__ == '__main__':
    sol = Solution()
    nums = [0, -1, 7, -5, 4, 2, -4]
#    print sol.threeSumClosest(nums, 2)
    print sol.revised_threeSum(nums, 15)
