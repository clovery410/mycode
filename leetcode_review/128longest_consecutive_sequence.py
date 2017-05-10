class Solution(object):
    #solution1, first come up idea, since forget how to implement union-find, use a hashmap instead. But this code is really ugly...
    def longestConsecutive(self, nums):
        num_range = {}
        res = 1
        for num in nums:
            if num in num_range:
                continue
            start, end = num, num
            length = 1
            if num - 1 in num_range and num + 1 in num_range:
                pre_start, pre_end = num_range[num-1]
                next_start, next_end = num_range[num+1]
                length += pre_end - pre_start + 1
                length += next_end - next_start + 1
                num_range[pre_start] = [pre_start, next_end]
                num_range[next_end] = [pre_start, next_end]
                num_range[num] = [pre_start, next_end]
            elif num - 1 in num_range:
                pre_start, pre_end = num_range[num-1]
                num_range[pre_start] = [pre_start, num]
                num_range[num] = [pre_start, num]
                length += pre_end - pre_start + 1
            elif num + 1 in num_range:
                next_start, next_end = num_range[num+1]
                num_range[next_end] = [num, next_end]
                num_range[num] = [num, next_end]
                length += next_end - next_start + 1
            else:
                num_range[num] = [num, num]
            res = max(res, length)
        return res

    #solution2, rewrite solution1 in a more concise way, idea is the same
    def longestConsecutive2(self, nums):
        num_range = {}
        res = 1
        for num in nums:
            if num in num_range:
                continue

            length = 1
            pre_start, pre_end = num_range[num-1] if num-1 in num_range else (num, None)
            next_start, next_end = num_range[num+1] if num+1 in num_range else (None, num)

            if pre_end is not None:
                length += pre_end - pre_start + 1
                num_range[pre_start] = (pre_start, next_end)

            if next_start is not None:
                length += next_end - next_start + 1
                num_range[next_end] = (pre_start, next_end)

            num_range[num] = (pre_start, next_end)
            res = max(res, length)
        return res

    # solution3, learned from discuss
    def longestConsecutive3(self, nums):
        available = set(nums)
        res = 1
        while available:
            first = last = available.pop()
            while first - 1 in available:
                first -= 1
                available.remove(first)
            while last + 1 in available:
                last += 1
                available.remove(last)
            res = max(res, last - first + 1)
        return res

# Following try the union find solution

if __name__ == "__main__":
    sol = Solution()
    print sol.longestConsecutive([100,4,200,1,3,2])
    print sol.longestConsecutive3([100,4,200,1,3,2])
