class Solution(object):
    def wiggleMaxLength(self, nums):
        if len(nums) == 0:
            return 0

        # have three status, 0 means initialization, 1 means increasing, 2 means dereasing
        status = 0
        count = 1

        pre = nums[0]
        for num in nums:
            if num == pre:
                continue
            if status == 0:
                count += 1
                status = 1 if num > pre else 2
            elif status == 1 and num < pre:
                count += 1
                status = 2
            elif status == 2 and num > pre:
                count += 1
                status = 1
            pre = num
            
        return count

if __name__ == "__main__":
    sol = Solution()
    nums = [1,17,5,10,13,15,10,5,16,8]
    print sol.wiggleMaxLength(nums)
