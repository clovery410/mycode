class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def duplicate_ll(head):
    new_head = ListNode(head.val)
    curr = head.next
