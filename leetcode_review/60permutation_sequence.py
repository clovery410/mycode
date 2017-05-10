import math
class Solution(object):
    def getPermutation(self, n, k):
        #initialize numbers
        k -= 1
        nums = range(1, n+1)
        res = []
        
        while len(res) < n:
            fact = math.factorial(len(nums) - 1)
            idx = k / fact
            res.append(str(nums[idx]))
            del nums[idx]
            k -= fact * idx
        return ''.join(res)

if __name__ == "__main__":
    sol = Solution()
    print sol.getPermutation(4, 14)
