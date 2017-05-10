class MinStack(object):
    def __init__(self):
        self.stack = []
        self.minVal = []

    def push(self, num):
        self.stack.append(num)
        if len(self.minVal) == 0:
            self.minVal.append(num)
        else:
            self.minVal.append(min(self.minVal[-1], num))

    def pop(self):
        self.minVal.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minVal[-1]

if __name__ == "__main__":
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    print ms.getMin()
    ms.pop()
    print ms.top()
    print ms.getMin()
