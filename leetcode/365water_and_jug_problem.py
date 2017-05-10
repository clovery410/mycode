class Solution(object):
    #Solution1, use the math solution, to see whether a*x + b*y = z has integer solution for a and b
    def canMeasureWater(self, x, y, z):
        if x == 0:
            return z == 0 or y == z
        if y == 0:
            return z == 0 or x == z
        if z < 0 or z > x + y:
            return False
        
        for a in xrange(x+1):
            temp = z - a * x
            if temp % y == 0:
                return True
        return False
