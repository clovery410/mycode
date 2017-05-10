import collections
class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.window = collections.deque([])
        self.total = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.window.append(val)
        self.total += val
        if len(self.window) > self.size:
            self.total -= self.window.popleft()
        return self.total / float(len(self.window))

if __name__ == "__main__":
    m = MovingAverage(3)
    print m.next(1)
    print m.next(10)
    print m.next(3)
    print m.next(5)
