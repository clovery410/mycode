class Stack(object):
    def __init__(self):
        self.queue = collections.deque([])
        
    def push(self, x):
        queue = self.queue
        queue.append(x)
        for i in xrange(len(queue) - 1):
            queue.append(queue.popleft())

    def pop(self):
        self.queue.popleft()
        
    def top(self):
        return self.queue[0]

    def empty(self):
        return len(self.queue) == 0
