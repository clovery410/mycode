class Solution(object):
    def singleNumber(self, nums):
        # get the xor result of all numbers
        all_xor = 0
        for num in nums:
            all_xor ^= num

        # find the particular bit
        mask = 1
        while all_xor & mask == 0:
            mask <<= 1

        # divide the numbers into two part
        nums1, nums2 = [], []
        for num in nums:
            if num & mask == 0:
                nums1.append(num)
            else:
                nums2.append(num)

        # do xor again separately in two arrays
        num1 = num2 = 0
        for num in nums1:
            num1 ^= num
        for num in nums2:
            num2 ^= num
        return [num1, num2]
