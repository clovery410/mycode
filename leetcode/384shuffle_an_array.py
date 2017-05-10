class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type size: int
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        shuffle = self.nums[:]
        n = len(self.nums)
        for i in xrange(n):
            rand_idx = random.randrange(i, n)
            shuffle[i], shuffle[rand_idx] = shuffle[rand_idx], shuffle[i]
        return shuffle
