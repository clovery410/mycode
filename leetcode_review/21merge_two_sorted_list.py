class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeSortedList(self, head1, head2):
        if head1 is None:
            return head2
        if head2 is None:
            return head1

        dummy = ListNode(0)
        prev = dummy
        curr1, curr2 = head1, head2
        if curr1.val <= curr2.val:
            prev.next = curr1
            curr1 = curr1.next
        else:
            prev.next = curr2
            curr2 = curr2.next
        prev = prev.next

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                prev.next = curr1
                curr1 = curr1.next
                prev = prev.next
            else:
                prev.next = curr2
                prev = prev.next
                curr2 = curr2.next
        if curr1:
            prev.next = curr1
        else:
            prev.next = curr2

        return dummy.next
    
