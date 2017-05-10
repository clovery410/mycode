class Solution(object):
    def trailingZeroes(self, n):
        """
        The key idea here is: 
        trailing zero is composed by 2 * 5, so just count all the products of 5 is enough, 
        since there are more numbers that are multiple of 2 than are multiple of 5.
        However, 25 = 5 * 5, 50 = 2 * 5 * 5, need to recurse from 5 to pow(5, x) until pow(5, x) > n
        """
        res = 0
        largest_multiple_five = 5

        while largest_multiple_five <= n:
            res += n / largest_multiple_five
            largest_multiple_five *= 5

        return res
