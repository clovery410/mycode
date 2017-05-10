class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
import gc
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        cur1, cur2 = headA, headB

        while cur1 != cur2:
            cur1 = cur1.next if cur1 else headB
            cur2 = cur2.next if cur2 else headA
            
        gc.collect()
        return cur1
