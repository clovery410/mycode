class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        curr1, curr2 = headA, headB
        length1 = length2 = 0
        while curr1:
            length1 += 1
            curr1 = curr1.next
        while curr2:
            length2 += 1
            curr2 = curr2.next

        curr1, curr2 = headA, headB
        if length1 > length2:
            while length1 > length2:
                curr1 = curr1.next
                length1 -= 1
        if length2 > length1:
            while length2 > length1:
                curr2 = curr2.next
                length2 -= 1
        while curr1 and curr2:
            if curr1 == curr2:
                return curr1
            else:
                curr1 = curr1.next
                curr2 = curr2.next
        return None
