import math
class Solution(object):
    #solution1, kind of math solution
    def getPermutation(self, n, k):
        res = []
        k -= 1
        
        #initialize fact = [1, 1, 2, 6, 24 ... n!]
        fact = [1] * (n+1)
        for i in xrange(1, n+1):
            fact[i] = fact[i-1] * i

        #initialize nums = [1, 2, 3 ... n]
        nums = [num for num in range(1, n+1)]

        for i in range(1, n+1):
            idx = k / fact[n-i]
            res.append(str(nums[idx]))
            del nums[idx]
            k -= idx * fact[n-i]
        return ''.join(res)


if __name__ == "__main__":
    sol = Solution()
    print sol.getPermutation(9, 24)
                
