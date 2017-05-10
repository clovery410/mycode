class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head

        prev, curr = head, head.next

        while curr:
            if curr.val == prev.val:
                curr = curr.next
            else:
                prev.next = curr
                prev, curr = curr, curr.next
        prev.next = None
        return head

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(2)
    node4 = ListNode(3)
    node5 = ListNode(3)
    node6 = ListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    sol = Solution()
    new_head = sol.deleteDuplicates(node1)
    print new_head.val, new_head.next.val, new_head.next.next.val, new_head.next.next.next.val, new_head.next.next.next.next
