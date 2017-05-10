import math
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution(object):
    def printLL(self, head):
        new_head = self.reverseLL(head)
        curr = new_head
        while curr:
            print curr.val
            curr = curr.next

    def reverseLL(self, head):
        if head is None or head.next is None:
            return head
        first_head = head
        second_head = head.next
        head.next = None

        while second_head:
            curr = second_head
            second_head = second_head.next
            curr.next = first_head
            first_head = curr
        return first_head

    def printLL2(self, head):
        nodes = []
        curr = head
        while curr:
            nodes.append(curr.val)
            curr = curr.next
        for i in reversed(xrange(len(nodes))):
            print nodes[i]

    def printLL3(self, head):
        l = 0
        curr = head
        while curr:
            curr = curr.next
            l += 1
        for i in reversed(xrange(l)):
            curr = head
            for j in xrange(i):
                curr = curr.next
            print curr.val

    def printLL4(self, head, m):
        n = 0
        curr = head
        heads_set = []
        while curr:
            if n % m == 0:
                heads_set.append(curr)
            curr = curr.next
            n += 1

#        sub_length = math.ceil(n / m)
        sub_length = (n + m - 1) / m
        for tmp_head in reversed(heads_set):
            nodes = []
            count = 0
            curr = tmp_head
            while curr and count < sub_length:
                nodes.append(curr.val)
                curr = curr.next
                count += 1
            for i in reversed(xrange(len(nodes))):
                print nodes[i]

        

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(7)
    node8 = ListNode(8)
    node9 = ListNode(9)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8
#    node8.next = node9

    sol = Solution()
    # sol.printLL2(node1)
    # sol.printLL3(node1)
    sol.printLL4(node1, 3)
