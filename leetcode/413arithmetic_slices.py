class Solution(object):
    # solution1
    def numberOfArithmeticSlices(self, A):
        def getCount(n):
            total = 0
            i = 1
            while n - i > 0:
                total += n - i
                i += 1
            return total
            
        diff = [A[i] - A[i-1] for i in xrange(1, len(A))]
        start_idx = 0
        cur_idx = 1
        res = 0
        while cur_idx < len(diff):
            if diff[cur_idx] == diff[start_idx]:
                cur_idx += 1
                continue
            if cur_idx - start_idx > 1:
                res += getCount(cur_idx - start_idx)
            start_idx = cur_idx
            cur_idx += 1
            
        if cur_idx - start_idx > 1:
            res += getCount(cur_idx - start_idx)
        return res

    # solution2, simplifise solution1
    def numberOfArithmeticSlices2(self, A):
        res = 0
        cur = 0
        for i in xrange(2, len(A)):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                cur += 1
            else:
                cur = 0
            res += cur
        return res

if __name__ == "__main__":
    sol = Solution()
    A = [2,1,3,4,5,6]
    print sol.numberOfArithmeticSlices(A)
    print sol.numberOfArithmeticSlices2(A)
