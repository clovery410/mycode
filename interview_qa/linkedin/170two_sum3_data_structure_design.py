# solution1, not good, please refer to solution2
class TwoSum(object):
    def __init__(self):
        self.nums = []
        self.sums = set()

    def add(self, number):
        for num in self.nums:
            self.sums.add(num + number)
        self.nums.append(number)

    def find(self, value):
        return value in self.sums

# solution2, use a hashmap to store count
class TwoSum2(object):
    def __init__(self):
        self.nums = collectinos.defaultdict(int)

    def add(self, number):
        self.nums[number] += 1

    def find(self, value):
        for v1, cnt in self.nums.iteritems():
            if value - v1 in self.nums:
                if v1 != value - v1 or cnt > 1:
                    return True
        return False
        
