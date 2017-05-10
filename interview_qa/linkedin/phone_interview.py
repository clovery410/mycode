class TwoSum(object):
    """
    Stores @param input in an internal data structure.
    Returns true if there is any pair of numbers in the internal data structure which
    have sum @param val, and false otherwise.
    For example, if the numbers 1, -2, 3, and 6 had been stored,
    the method should return true for 4, -1, and 9, but false for 10, 5, and 0
    """
    def __init__(self):
        self.num_counts = collections.defaultdict(int)

    def store(self, num):
        self.num_counts[num] += 1
        
    def test(self, val):
        for num, cnt in self.num_counts.iteritems():
            remain_num = val - num
            if remain_num == num and cnt > 1:
                return True
            elif remain_num != num and self.num_counts[remain_num] > 0:
                return True
        return False

class MaximumConsecutiveSequence(object):
    """
    Write a function that, given a list of integers (both positive and negative) returns the sum of the contiguous subsequence with maximum sum. Thus, given the sequence (1, 2, -4, 1, 3, -2, 3, -1) it should return 5.
    """
    def maximum_sum_sequence(self, nums):
         if len(nums) == 0:
             return 0
         cur_max = all_max = nums[0]
         for i in xrange(1, len(nums)):
             cur_num = nums[i]
             cur_max = max(cur_max + cur_num, 0)
             all_max = max(all_max, cur_max)
         return all_max

     def maximum_product_sequence(self, nums):
         if len(nums) == 0:
             return 0
         cur_min = cur_max = nums[0]
         all_max = nums[0]
         
         for i in xrange(1, len(nums)):
             cur_num = nums[i]
             if cur_num <= 0:
                 temp = cur_max
                 cur_max = max(cur_min * cur_num, cur_num)
                 cur_min = min(cur_num, cur_num * temp)
             else:
                 cur_max = max(cur_max * cur_num, cur_num)
                 cur_min = min(cur_min * cur_num, cur_num)
                 
             all_max = max(all_max, cur_max)
             
         return all_max if all_max >= 0 else 0
