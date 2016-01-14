class Solution(object):
    def productExceptSelf(self, nums):
        output = []
        for i in reversed(nums):
            output.append(i)
        current_1 = nums[0]
        current_2 = output[0]
        nums[0] = output[0] = 1
        for i in xrange(1, len(nums)):
            temp_1 = nums[i]
            temp_2 = output[i]
            nums[i] = current_1 * nums[i-1]
            output[i] = current_2 * output[i-1]
            current_1 = temp_1
            current_2 = temp_2
        output.reverse()

        for i in xrange(len(nums)):
            output[i] = output[i] * nums[i]
        return output


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    sol = Solution()
    print sol.productExceptSelf(nums)
