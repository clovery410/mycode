class Solution(object):
    def majorityElement(self, nums):
        count1, count2 = 0, 0
        res = []
        for num in nums:
            if count1 > 0 and num == candidate1:
                count1 +=1
            elif count2 > 0 and num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 += 1
            elif count2 == 0:
                candidate2 = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        if count1 > 0 and self.verifyMajority(nums, candidate1):
            res.append(candidate1)
        if count2 > 0 and self.verifyMajority(nums, candidate2):
            res.append(candidate2)
        return res

    def verifyMajority(self, nums, target):
        count = 0
        for num in nums:
            if num == target:
                count += 1
        return True if count > len(nums) / 3 else False
