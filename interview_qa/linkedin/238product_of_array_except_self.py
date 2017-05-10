class Solution(object):
    # solution1, use extra space, record left accumutive product and right accumutive product
    def productExceptSelf(self, nums):
        n = len(nums)
        left_product = [1] * (n+1)
        right_product = [1] * (n+1)

        for i in xrange(n):
            left_product[i+1] = left_product[i] * nums[i]
        for i in reversed(xrange(n)):
            right_product[i] = right_product[i+1] * nums[i]

        res = [0 for x in xrange(n)]
        for i in xrange(n):
            res[i] = left_product[i] * right_product[i+1]
        return res

    # solution2, try to optimize the space comlexity to O(1), make use of output array
    def productExceptSelf2(self, nums):
        n = len(nums)
        output = [1] * n
        for i in xrange(1, n):
            output[i] = output[i-1] * nums[i-1]

        accumu_prod = 1
        for i in reversed(xrange(n-1)):
            accumu_prod *= nums[i+1]
            output[i] *= accumu_prod

        return output

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,4]
    print sol.productExceptSelf(nums)
    print sol.productExceptSelf2(nums)
