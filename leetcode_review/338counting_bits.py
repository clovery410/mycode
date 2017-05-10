class Solution(object):
    def countBits(self, n):
        res = [0] * (n+1)
        if n < 1:
            return res
        
        res[1] = 1
        for i in range(2,n+1):
            quotation = i / 2
            remainder = i % 2
            res[i] = res[quotation] + res[remainder]
        return res

if __name__ == "__main__":
    sol = Solution()
    print sol.countBits(0)
            
