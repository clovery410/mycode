class Queue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def push(self, x):
        self.stack1.append(x)
        
    def pop(self):
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())
        res = self.stack1.pop() if len(self.stack1) > 0 else None
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())
        return res
            
    def peek(self):
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())
        res = self.stack1[0] if len(self.stack1) > 0 else None
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())
        return res
    
    def empty(self):
        return True if len(self.stack1) == 0 else False

#solution2, more elegent solution
class Queue2(object):
    def __init__(self):
        self.in_stack, self.out_stack = [], []

    def push(self, x):
        self.in_stack.append(x)

    def pop(self):
        self.move()
        self.out_stack.pop()

    def peek(self):
        self.move()
        return self.out_stack[-1]

    def empty(self):
        return (not self.in_stack) and (not self.out_stack)

    def move(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
