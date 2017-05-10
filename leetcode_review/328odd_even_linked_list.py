class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        if head is None or head.next is None or head.next.next is None:
            return head

        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        prev1, prev2 = dummy1, dummy2
        index, curr = 1, head
        while curr:
            if index % 2 == 1:
                prev1.next = curr
                prev1 = prev1.next
            else:
                prev2.next = curr
                prev2 = prev2.next
            curr = curr.next
            index += 1

        prev1.next = dummy2.next
        return dummy1.next

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    sol = Solution()
    new_head = sol.oddEvenList(node1)
    print new_head.val, new_head.next.val, new_head.next.next.val, new_head.next.next.next.val
