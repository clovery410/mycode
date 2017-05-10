from collections import deque
class Stack(object):
    def __init__(self):
        self.queue = deque([])
        
    def push(self, x):
        self.queue.append(x)
        
    def pop(self):
        length = len(self.queue)
        for i in range(length-1):
            self.queue.append(self.queue.popleft())
        self.queue.popleft()

    def top(self):
        length = len(self.queue)
        for i in range(length-1):
            self.queue.append(self.queue.popleft())
        res = self.queue[0]
        self.queue.append(self.queue.popleft())
        return res

    def empty(self):
        return False if self.queue else True

# solution2, each time when push a value, rotate it to the end
class Stack2(object):
    def __init__(self):
        self.queue = collections.deque()

    def push(self, x):
        q = self.queue
        q.append(x)
        for i in range(len(q)-1):
            q.append(q.popleft())

    def pop(self):
        self.queue.popleft()

    def top(self):
        return self.queue[0]

    def empty(self):
        return not len(self.queue)
        
