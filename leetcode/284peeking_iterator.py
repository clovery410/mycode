"""
Assume the iterface for Iterator is already implemented for you
The functions for Iterator are as follow: hasNext(), next()
"""
class PeekingIterator(object):
    def __init__(self, iterator):
        self.iterator = iterator
        self.first = None

    def peek(self):
        if not self.first:
            self.first = self.iterator.next()
        return self.first

    def next():
        if self.first:
            res = self.first
            self.first = None
            return res
        return self.iterator.next()

    def hasNext():
        return True if self.iterator.hasNext() or self.first else False
