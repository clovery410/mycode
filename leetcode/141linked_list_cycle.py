class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        first = second = head

        while first and first.next:
            first = first.next.next
            second = second.next
            
            if first == second:
                return True

        return False

    def conciseSolution(self, head):
        try:
            first = head.next
            second = head

            while first is not second:
                first = first.next.next
                second = second.next
            return True
        except:
            return False

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node2

    sol = Solution()
    print sol.hasCycle(node1)
    print sol.conciseSolution(node1)
