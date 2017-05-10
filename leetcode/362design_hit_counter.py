class HitCounter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = collections.deque([])

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        queue = self.hits
        if len(queue) == 0:
            queue.append([timestamp, 1])
            return
        while len(queue) > 0 and timestamp - queue[0][0] >= 300:
            queue.popleft()
        if len(queue) > 0 and timestamp == queue[-1][0]:
            queue[-1][1] += 1
        else:
            queue.append([timestamp, 1])

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        queue = self.hits
        while len(queue) > 0 and timestamp - queue[0][0] >= 300:
            queue.popleft()
        return sum(x[1] for x in queue)
