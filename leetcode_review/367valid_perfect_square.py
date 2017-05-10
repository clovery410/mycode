class Solution(object):
    def isPerfectSquare(self, num):
        start, end = 1, num
        while start <= end:
            mid = (end - start) / 2 + start
            if mid * mid == num:
                return True
            elif mid * mid < num:
                start = mid + 1
            else:
                end = mid - 1
        return False

if __name__ == "__main__":
    sol = Solution()
    print sol.isPerfectSquare(14)
