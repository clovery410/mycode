class Solution(object):
    def threeSumZero(self, nums):
        dic = {}
        res = []
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        nums.sort()    
        for i in xrange(len(nums)):
            first = nums[i]
            j = i + 1
            while j < len(nums):
                target = -first - dic[nums[j]]
                if -first - dic[nums[j]] in dic:
                    if target != nums[j]:
                        res.append((nums[i], nums[j], target))
                    elif dic[target] > 2 or (dic[target] > 1 and nums[j] != nums[i]):
                        res.append(nums[i], nums[j], target)
                pre = nums[j]
                j += 1
                while nums[j] == pre:
                    j += 1
        return res
