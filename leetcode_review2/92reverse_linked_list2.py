class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        if m == n:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        start = head
        for i in xrange(m-1):
            start = start.next
            pre = pre.next

        first, second = start, start.next
        for j in xrange(n-m):
            temp = second.next
            second.next = first
            first, second = second, temp
            
        pre.next = first
        start.next = second
        return dummy.next
            
            
