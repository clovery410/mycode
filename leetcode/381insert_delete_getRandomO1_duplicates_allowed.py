class RandomizedCollection(object):
    def __init__(self):
        self.nums = []
        self.maps = dict()

    def insert(self, val):
        self.nums.append(val)
        idx = len(self.nums) - 1
        if val not in self.maps:
            self.maps[val] = {idx}
            return True
        else:
            self.maps[val].add(idx)
            return False

    def remove(self, val):
        maps = self.maps
        nums = self.nums
        
        if val not in maps: return False

        indices = maps[val]
        idx1 = indices.pop()
        idx2 = len(nums) - 1
        last_val = nums.pop()

        if idx1 != idx2:
            nums[idx1] = last_val
            maps[last_val].discard(idx2)
            maps[last_val].add(idx1)

        if len(indices) == 0:
            del maps[val]
            
        return True

    def getRandom(self):
        idx = random.randint(0, len(self.nums)-1)
        return self.nums[idx]
