class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    #solution1, do the reverse, then add one, then reverse again
    def plusOne(self, head):
        def reverseLinkedList(head):
            pre, cur = None, head
            while cur:
                _next = cur.next
                cur.next = pre
                pre, cur = cur, _next
            return pre

        def addOne(head):
            carry = 1
            dummy = ListNode(-1)
            pre = dummy
            cur = head
            while cur:
                num, carry = (cur.val + carry) % 10, (cur.val + carry) / 10
                pre.next = ListNode(num)
                pre, cur = pre.next, cur.next
            if carry:
                pre.next = ListNode(carry)
            return dummy.next

        tail = reverseLinkedList(head)
        new_tail = addOne(tail)
        new_head = reverseLinkedList(new_tail)
        return new_head

    #solution2, do not reverse the linked list because we only plus one, only nend to mark the lowest digit whose value is not 9 as pre, then if last node is not 9, it's simply, directly plus one to last node, otherwise, need to plus pre's value by one first, then change all the nodes' value to 0 after pre.
    def plusOne2(self, head):
        dummy = ListNode(0)
        dummy.next = head
        pre = cur = dummy
        while cur.next:
            cur = cur.next
            if cur.val != 9:
                pre = cur

        if cur.val != 9:
            cur.val += 1
        else:
            pre.val += 1
            pre = pre.next
            while pre:
                pre.val = 0
                pre = pre.next
        return dummy if dummy.val == 1 else dummy.next

if __name__ == "__main__":
    sol = Solution()
    node1 = ListNode(9)
    node2 = ListNode(0)
    node3 = ListNode(9)
    node1.next = node2
    node2.next = node3
    
    new_head = sol.plusOne2(node1)
    print new_head.val, new_head.next.val, new_head.next.next.val
        
