class Solution(object):
    def sqrt(self, num):
        start, end = 1, num
        while start <= end:
            mid = (end - start) / 2 + start
            if mid * mid == num:
                return mid
            if mid * mid < num:
                start = mid + 1
            else:
                end = mid - 1
        return end
    
    def sqrtDecimal(self, num):
        start, end = 1.0, float(num)
        mid = (end - start) / 2 + start
        while abs(mid * mid - num) > 0.000001:
            mid = (end - start) / 2 + start
            if mid * mid < num:
                start = mid
            else:
                end = mid
        return mid

    def getTogether(self, num):
        cloest_num = self.sqrt(num)
        if cloest_num * cloest_num == num:
            return cloest_num
        else:
            return self.sqrtDecimal(num)

if __name__ == "__main__":
    sol = Solution()
    print sol.sqrt(25)
    print sol.sqrtDecimal(25)
    print sol.getTogether(25)
