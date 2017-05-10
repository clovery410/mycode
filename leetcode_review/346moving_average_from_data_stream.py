import collections
class MovingAverage(object):
    def __init__(self, size):
        self.window = collections.deque([])
        self.total = 0
        self.size = size

    def next(self, val):
        if len(self.window) == self.size:
            self.total -= self.window.popleft()
        self.window.append(val)
        self.total += val
        return self.total / float(len(self.window))

if __name__ == "__main__":
    ma = MovingAverage(3)
    print ma.next(1)
    print ma.next(10)
    print ma.next(3)
    print ma.next(5)
