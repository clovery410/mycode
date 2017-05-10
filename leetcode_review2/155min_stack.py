class MinStack(object):
    def __init__(self):
        self.val_stack = []
        self.min_stack = []

    def push(self, x):
        self.val_stack.append(x)
        if self.min_stack:
            self.min_stack.append(min(self.min_stack[-1], x))
        else:
            self.min_stack.append(x)

    def pop(self):
        self.val_stack.pop()
        self.min_stack.pop()
        
    def top(self):
        return self.val_stack[-1]

    def getMin(self):
        return self.min_stack[-1]
