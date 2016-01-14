class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        start1 = l1
        start2 = l2
        if l1.val <= l2.val:
            head = curr = l1
            start1 = start1.next
        else:
            head = curr = l2
            start2 = start2.next
            
        while start1 and start2:
            if start1.val <= start2.val:
                curr.next = start1
                curr = curr.next
                start1 = start1.next
            else:
                curr.next = start2
                curr = curr.next
                start2 = start2.next
        if start1:
            curr.next = start1
        if start2:
            curr.next = start2
        return head
