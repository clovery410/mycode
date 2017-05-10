class Vector2D(object):
    
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.x = 0
        self.y = -1
        
    def next(self):
        """
        :rtype: int
        """
        return self.vec2d[self.x][self.y]
    
    
    def hasNext(self):
        """
        :rtype: bool
        """
        self.y += 1
        while self.x < len(self.vec2d):
            if self.y >= len(self.vec2d[self.x]):
                self.x += 1
                self.y = 0
            else:
                return True
        return False
