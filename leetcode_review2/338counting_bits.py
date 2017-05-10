class Solution(object):
    def countBits(self, num):
        if num <= 1:
            return [0] if num == 0 else [0, 1]
        
        res = [0] * (num + 1)
        res[1] = 1
        idx, weight = 2, 2
        while idx < (num + 1):
            for i in xrange(weight):
                if idx >= num + 1:
                    break
                res[idx] = res[i] + 1
                idx += 1
            weight *= 2
        return res

if __name__ == "__main__":
    sol = Solution()
    print sol.countBits(5)
        
