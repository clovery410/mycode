class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(-1)
        pre = dummy
        cur1, cur2 = l1, l2
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                pre.next = cur1
                cur1 = cur1.next
            else:
                pre.next = cur2
                cur2 = cur2.next
            pre = pre.next
        if cur1:
            pre.next = cur1
        if cur2:
            pre.next = cur2
        return dummy.next
