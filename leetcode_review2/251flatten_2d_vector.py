class Vector2D(object):
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.row = 0
        self.col = 0
        self.nextNum = None

    def next(self):
        """
        :rtype: int
        """
        return self.nextNum

    def hasNext(self):
        """
        :rtype: bool
        """
        vec2d = self.vec2d
        if self.row >= len(vec2d):
            return False
        if self.col >= len(vec2d[self.row]):
            self.row += 1
            self.col = 0
            return self.hasNext()
        self.nextNum = vec2d[self.row][self.col]
        self.col += 1
        return True

#solution2
class Vector2D2(object):
    def __init__(self, vec2d):
        self.vec2d = vec2d
        self.row = 0
        self.col = -1

    def next(self):
        return self.vec2d[self.row][self.col]

    def hasNext(self):
        self.col += 1
        while self.row < len(self.vec2d):
            if self.col >= len(self.vec2d[self.row]):
                self.row += 1
                self.col = 0
            else:
                return True
        return False
    
if __name__ == "__main__":
    vec2d = [[1,2],[3],[4,5,6]]
    i = Vector2D2(vec2d)
    while i.hasNext():
        print i.next()
