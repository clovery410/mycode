class Solution(object):
    def containsDuplicate(self, nums):
        dup = set()
        for num in nums:
            if num in dup:
                return False
            dup.add(num)
        return True
