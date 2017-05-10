class Solution(object):
    def findCelebrity(self, n):
        # find potential celebrity, whom does not know anybody after him
        celebrity = 0
        for i in xrange(1, n):
            if knows(celebrity, i):
                celebrity = i

        # check whether the celebrity knows anybody before him, and whether all people knows him
        for i in xrange(n):
            if i == celebrity:
                continue
            if (i < celebrity and knows(celebrity, i)) or not knows(i, celebrity):
                return -1

        return celebrity
