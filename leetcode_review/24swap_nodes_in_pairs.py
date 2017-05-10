class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head
        while cur and cur.next:
            temp = cur.next.next
            pre.next = cur.next
            cur.next.next = cur
            cur.next = temp
            pre, cur = cur, temp
        return dummy.next
