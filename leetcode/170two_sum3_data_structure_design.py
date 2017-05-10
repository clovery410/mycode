#solution1, TLE
class TwoSum(object):
    def __init__(self):
        import collections
        self.nums = collections.defaultdict(int)
        
    def add(self, number):
        self.nums[number] += 1
        
    def find(self, value):
        for num in self.nums.keys():
            if num == value - num and self.nums[num] > 1:
                return True
            if num != value - num and value - num in self.nums:
                return True
        return False

#solution2, same idea, but use interator to avoid TLE
class TwoSum(object):
    def __init__(self):
        import collections
        self.nums = collections.defaultdict(int)

    def add(self, number):
        self.nums[number] += 1

    def find(self, value):
        for num, count in self.nums.iteritems():
            if value - num in self.nums:
                if value - num != num or count > 1:
                    return True
        return False

if __name__ == "__main__":
    ts = TwoSum()
    ts.add(0)
    ts.add(1)
    print ts.find(0)
    print ts.find(7)
        
