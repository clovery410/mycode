class MaxStack(object):
    def __init__(self):
        self.stack = []
        self.maximum = []
        
    def push(self, x):
        cur_max = max(x, self.maximum[-1]) if self.maximum else x
        self.stack.append(x)
        self.maximum.append(cur_max)
        
    def pop(self):
        self.stack.pop()
        self.maximum.pop()
        
    def top(self):
        return self.stack[-1] if self.stack else None
    
    def getMax(self):
        return self.maximum[-1] if self.maximum else None

if __name__ == "__main__":
    maxStack = MaxStack()
    maxStack.push(2)
    maxStack.push(1)
    maxStack.push(5)
    maxStack.push(0)

    maxStack.pop()
    maxStack.pop()
    print maxStack.top()
    print maxStack.getMax()
        
