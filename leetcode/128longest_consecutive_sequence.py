class Solution(object):
    def longestConsecutive(self, nums):
        unions = {}
        res = 0
        for num in nums:
            if unions.has_key(num):
                continue
            head = tail = num
            if unions.has_key(num-1):
                head = unions[num-1][0]
            if unions.has_key(num+1):
                tail = unions[num+1][1]
            unions[head] = unions[tail] = unions[num] = (head, tail)
            res = max(res, tail - head + 1)
        return res

if __name__ == "__main__":
    sol = Solution()
    nums = [5, 100, 4, 200, 1, 3, 2]
    print sol.longestConsecutive(nums)
    
