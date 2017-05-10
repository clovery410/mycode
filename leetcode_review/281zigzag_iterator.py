class ZigzagIterator(object):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.pos1 = 0
        self.pos2 = 0
        self.turn = 0

    def next(self):
        if not self.turn:
            res = self.v1[self.pos1]
            self.pos1 += 1
        else:
            res = self.v2[self.pos2]
            self.pos2 += 1
        self.turn ^= 1
        return res

    def hasNext(self):
        if self.pos1 >= len(self.v1) and self.pos2 >= len(self.v2):
            return False
        elif self.pos1 >= len(self.v1):
            self.turn = 1
        elif self.pos2 >= len(self.v2):
            self.turn = 0
        return True

# Follow-up, extend to k vectors
import collections
class ZigzagIterator2(object):
    def __init__(self, v1, v2):
        self.queue = collections.deque([])
        if v1: self.queue.append(iter(v1))
        if v2: self.queue.append(iter(v2))
        self.total = sum(map(len, [v1, v2]))
        
    def next(self):
        it = self.queue.popleft()
        try:
            value = it.next()
        except StopIteration:
            return self.next()
        self.total -= 1
        self.queue.append(it)
        return value

    def hasNext(self):
        return self.total > 0

class ZigzagIterator3(object):
    def __init__(self, v1, v2):
        self.data = deque([(len(v), iter(v)) for v in (v1, v2) if v])

    def next(self):
        _len, _iter = self.data.popleft()
        if _len > 1:
            self.data.append((_len - 1, _iter))
        return _iter.next()

    def hasNext(self):
        return bool(self.data)
