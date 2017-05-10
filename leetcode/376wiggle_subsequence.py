class Solution(object):
    #Solution1, O(n) solution, most efficient
    def wiggleMaxLength(self, nums):
        if len(nums) < 2:
            return len(nums)
        count = 0
        pre = nums[0]
        j = 1
        # if increase = -1 means initial, increase = 0 means decrease, increase = 1 means increase
        increase = -1
        while j < len(nums):
            if nums[j] > pre:
                if increase == 0 or increase == -1:
                    count += 1
                    increase = 1
            elif nums[j] < pre:
                if increase == 1 or increase == -1:
                    count += 1
                    increase = 0
            j += 1
            pre = nums[j]
        return count

    #Solution2, use extra space to record difference
    def wiggleMaxLength2(self, nums):
        if len(nums) < 2:
            return len(nums)
        diff = [nums[i+1] - nums[i] for i in xrange(len(nums)-1)]
        count = 1
        for i in xrange(1, len(diff)):
            if diff[i] < 0 and diff[i-1] > 0 or diff[i] > 0 and diff[i-1] < 0:
                count += 1
        return count + 1

    #Solution3, greedy
    def wiggleMaxLength3(self, nums):
        f = d = 1
        for i in xrange(1, len(nums)):
            if nums[i] > nums[i-1]:
                f = d + 1
            elif nums[i] < nums[i-1]:
                d = f + 1
        return min(len(nums), max(f, d))

    #Solution4, dp
    def wiggleMaxLength4(self, nums):
        if len(nums) < 2:
            return len(nums)
        up = 1
        down = 1
        for i in xrange(1, len(nums)):
            if nums[i] > nums[i-1]:
                up = max(down + 1, up)
            if nums[i] < nums[i-1]:
                down = max(up + 1, down)
        return max(up, down)

if __name__ == "__main__":
    wiggle = [1,17,5,10,13,15,10,5,16,8]
    sol = Solution()
    print sol.wiggleMaxLength2(wiggle)
    print sol.wiggleMaxLength3(wiggle)
    print sol.wiggleMaxLength4(wiggle)
                    
                
