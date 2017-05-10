class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        y = 0
        temp = x
        while temp:
            y = y * 10 + temp % 10
            temp /= 10
        return y == x

if __name__ == "__main__":
    sol = Solution()
    print sol.isPalindrome(-2147483648)
