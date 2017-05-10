import random
class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.indexs = dict()
        self.nums = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.indexs:
            return False
        self.nums.append(val)
        self.indexs[val] = len(self.nums) - 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.indexs:
            idx = self.indexs.pop(val)
            last_item = self.nums.pop()
            if len(self.nums) > 0 and idx < len(self.nums):
                self.nums[idx] = last_item
                self.indexs[last_item] = idx
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        idx = random.randint(0, len(self.nums)-1)
        return self.nums[idx]
