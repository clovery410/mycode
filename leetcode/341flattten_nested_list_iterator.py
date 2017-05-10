class NestedIterator(object):
    def __init__(self, nestedList):
        self.nestedList = nestedList
        self.stack = []
        self.index = 0
        self.nextInt = None

    def next(self):
        return self.nextInt

    def hasNext(self):
        if len(self.stack) == 0 and self.index >= len(self.nestedList):
            return False
        if len(self.stack) == 0:
            self.stack.append(self.nestedList[self.index])
            self.index += 1
            
        while len(self.stack) > 0 and not self.stack[-1].isInteger():
            topList = self.stack.pop().getList()
            for elem in reversed(topList):
                self.stack.append(elem)
                
        if len(self.stack) > 0:
            self.nextInt = self.stack.pop().getInteger()
            return True
        else:
            return self.hasNext()
