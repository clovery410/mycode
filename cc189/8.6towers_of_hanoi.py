class Solution(object):
    def towersOfHanoi(self, n):
        def helper(n, moveFrom, moveTo):
            if n == 1:
                print str(n) + ": Move from " + str(moveFrom) + " to " + str(moveTo)
            else:
                intermediate = 3 - moveFrom - moveTo
                helper(n-1, moveFrom, intermediate)
                print str(n) + ": Move from " + str(moveFrom) + " to " + str(moveTo)
                helper(n-1, intermediate, moveTo)
        helper(n, 0, 2)

#Following implementation is more object oriented way
class Tower(object):
    def __init__(self, i):
        self.index = i
        self.disks = []

    def add(self, d):
        if len(self.disks) > 0 and self.disks[-1] <= d:
            print "Error placing disk: " + str(d)
        else:
            self.disks.append(d)

    def moveTopTo(self, t):
        top = self.disks.pop()
        t.add(top)
        print "move " + str(top) + " from " + str(self.index) + " to " + str(t.index)

    def moveDisks(self, n, destination, temp):
        if n > 0:
            self.moveDisks(n-1, temp, destination)
            self.moveTopTo(destination)
            temp.moveDisks(n-1, destination, self)
        
class Hanoi(object):
    def hanoi(self, n):
        towers = [Tower(i) for i in xrange(n)]
        for i in reversed(xrange(1, n+1)):
            towers[0].add(i)
        towers[0].moveDisks(n, towers[2], towers[1])
            

if __name__ == "__main__":
    # sol = Solution()
    # sol.towersOfHanoi(4)
    han = Hanoi()
    han.hanoi(3)
