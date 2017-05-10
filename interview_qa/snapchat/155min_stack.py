class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mins = []
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        
        min_val = x
        if len(self.mins) > 0:
            min_val = min(min_val, self.mins[-1])
        self.mins.append(min_val)

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()
        self.mins.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.mins[-1]
