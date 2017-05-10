class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
def addTwoNumbers(head1, head2):
    dummy = ListNode(0)
    pre = dummy
    carry = 0
    
    cur1, cur2 = head1, head2
    while cur1 and cur2:
        total = cur1.val + cur2.val + carry
        pre.next = ListNode(total % 10)
        pre = pre.next
        carry = total / 10
        cur1 = cur1.next
        cur2 = cur2.next

    cur = cur1 if cur1 else cur2
    while cur:
        total = cur.val + carry
        pre.next = ListNode(total % 10)
        pre = pre.next
        carry = total / 10
        cur = cur.next

    if carry:
        pre.next = ListNode(carry)

    return dummy.next

n0 = ListNode(2)
n1 = ListNode(4)
n2 = ListNode(3)
n0.next = n1
n1.next = n2

m0 = ListNode(5)
m1 = ListNode(6)
m2 = ListNode(4)
m0.next = m1
m1.next = m2

result = addTwoNumbers(n0, m0)
import pdb
pdb.set_trace()
