class Solution(object):
    def __init__(self, iterator):
        self.top = None
        self.iterator = iterator
        
    def peek(self):
        if not self.top:
            self.top = self.iterator.next()
        return self.top
    
    def next(self):
        if self.top:
            res = self.top
            self.top = None
            return res
        return self.iterator.next()

    def hasNext(self):
        return True if self.top or self.iterator.hasNext() else False

    
