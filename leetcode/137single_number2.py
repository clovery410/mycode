import math
class Solution(object):
    def singleNumber(self, nums):
        array = []
        n = len(nums)
        for i in xrange(32):
            bit_sum = 0
            for j in xrange(n):
                bit_n = ((1 << i) & nums[j]) >> i
                bit_sum += bit_n
            data = bit_sum % 3
            array.insert(0, data)

        _sum = 0
        _i = 1
        if array[0] == 0:
            for i in reversed(xrange(1, 32)):
                _sum += array[i] * _i
                _i *= 2
        else:
            for i in reversed(xrange(1, 32)):
                _sum += array[i] * _i
                _i *= 2
            print _sum
            _sum = -pow(2, 31) + _sum
        return _sum

    def singleNumber_2(self, nums):
        n = len(nums)
        sign_bit = 0
        for i in xrange(n):
            if nums[i] < 0:
                sign_bit += 1
                nums[i] = -nums[i]
                print nums[i]
        if sign_bit % 3 != 0:
            sign = -1
        else:
            sign = 1

        array = []
        for i in xrange(32):
            bit_sum = 0
            for j in xrange(n):
                bit_n = ((1 << i) & nums[j]) >> i
                bit_sum += bit_n
            data = bit_sum % 3
            print data
            array.insert(0, data)
        _sum = 0
        _i = 1
        for i in reversed(xrange(0, 32)):
            _sum += array[i] * _i
            _i *= 2
        return _sum * sign
    
if __name__ == '__main__':
    nums = [-2147483646,-2147483646,-2147483646,2147483645,-2147483648,2147483645,2147483645]
    sol = Solution()
    print sol.singleNumber_2(nums)
            
