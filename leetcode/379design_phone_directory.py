import heapq
# actually, we don't need to use heap here, using queue is just fine, please see solution2
class PhoneDirectory(object):
    def __init__(self, maxNumbers):
        self.used = set()
        self.numbers = range(maxNumbers)
        heapq.heapify(self.numbers)
        
    def get(self):
        if len(self.numbers) == 0: return -1
        cur = heapq.heappop(self.numbers)
        self.used.add(cur)
        return cur
        
    def check(self, number):
        return number not in self.used
        
    def release(self, number):
        if number in self.used:
            self.used.remove(number)
            heapq.heappush(self.numbers, number)

import collections
#solution2, use queue instead of heap
#actually, use stack is also fine, it that way, the assigned number would be the newest released number
class PhoneDirectory2(object):    
    def __init__(self, maxNumbers):
        self._max = maxNumbers
        self.used = set()
        self.available = collections.deque(range(maxNumbers))

    def get(self):
        if len(self.available) == 0: return -1
        num = self.available.popleft()
        self.used.add(num)
        return num

    def check(self, number):
        if number < 0 or number >= self._max: return False
        return number not in self.used

    def release(self, number):
        if number in self.used:
            self.used.remove(number)
            self.available.append(number)


            
