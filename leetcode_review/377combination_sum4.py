class Solution(object):
    def combinationSum4(self, nums, target):
        def generate(remain):
            if remain in cache:
                return cache[remain]
            if remain < 0:
                return 0
            if remain == 0:
                return 1
                
            res = 0
            for num in nums:
                res += generate(remain - num)
            cache[remain] = res
            return res
        
        cache = {}
        return generate(target)

if __name__ == "__main__":
    sol = Solution()
    print sol.combinationSum4([1,2,3], 4)
