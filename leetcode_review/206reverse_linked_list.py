class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        left = head
        right = head.next
        left.next = None

        while right.next:
            temp = right.next
            right.next = left
            left = right
            right = temp
        right.next = left
        return right

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)

    node1.next = node2
    node2.next = node3

    sol = Solution()
    new_head = sol.reverseList(node1)
    print new_head.val, new_head.next.val, new_head.next.next.val, new_head.next.next.next
