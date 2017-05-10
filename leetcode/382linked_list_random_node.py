import random
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# this solution is not what the OJ want
class Solution(object):
    def __init__(self, head):
        self.head = head
        self.length = self.getLength(head)

    def getRandom(self):
        pos = random.randrange(self.length)
        cur = self.head
        while pos > 0:
            cur = cur.next
            pos -= 1
        return cur.val

    def getLength(self, head):
        node, length = head, 0
        while node:
            node = node.next
            length += 1
        return length

# solution2, this is correct solution for reservoir sampling, but just slow
class Solution2(object):
    def __init__(self, head):
        self.head = head
        
    def genRandom(self):
        res, n = None, 1
        cur = self.head
        while cur:
            if random.randrange(n) == 0:
                res = cur
            cur = cur.next
            n += 1
        return res.val

# solution3, use stefan's solution which use buffer to reduce the time of random generation funciton
class Solution3(object):
    def __init__(self, head):
        self.head = head

    def genRandom(self):
        _buffer = [None] * 100
        before = 0
        cur = self.head
        while cur:
            now = 0
            while cur and now < 100:
                _buffer[now] = cur
                cur = cur.next
                now += 1
            r = random.randrange(before + now)
            if r < now:
                pick = _buffer[now]
            before += now
        return pick.val
