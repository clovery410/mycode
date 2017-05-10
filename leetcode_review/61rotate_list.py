class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        dummy = ListNode(0)
        dummy.next = head

        #get length
        l = 0
        tail = dummy
        while tail and tail.next:
            tail = tail.next
            l += 1

        k = k % l
        if k == 0: return dummy.next
        
        pre = dummy
        for i in xrange(l - k):
            pre = pre.next
        tail.next, dummy.next = dummy.next, pre.next
        pre.next = None
        return dummy.next
