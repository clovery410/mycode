class Solution(object):
    def productExceptSelf(self, nums):
        # output[i] = (nums[0] * nums[1] * ... * nums[i-1]) * (nums[i+1] * ... * nums[n-1])
        # so we can seprate the product into two parts, left product and right product
        output = [1] * len(nums)

        # first calculate the left accumulate product, store them in the result array
        for i in xrange(1, len(nums)):
            output[i] = output[i-1] * nums[i-1]

        # then calculate the right accumulate product, if O(n) space is allowed, just allocate a right result array just as left, but actually O(1) is enough, since the accumulate product only depends on the previous accumulated product and nums[i+1]
        pre = 1
        for i in reversed(xrange(len(nums) - 1)):
            pre *= nums[i+1]
            output[i] *= pre
        return output

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4]
    print sol.productExceptSelf(nums)
