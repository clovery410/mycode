class MinStack(object):
    def __init__(self):
        self.stack = []
        self.mn = []
            
    def push(self, x):
        self.stack.append(x)
        if not self.mn or x < self.mn[-1]:
            self.mn.append(x)
        else:
            self.mn.append(self.mn[-1])
            
    def pop(self):
        del self.stack[-1]
        del self.mn[-1]

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.mn[-1]

if __name__ == '__main__':
    sol = MinStack()
    sol.push(3)
    sol.push(2)
    print sol.getMin()
    sol.pop()
    print sol.top()
