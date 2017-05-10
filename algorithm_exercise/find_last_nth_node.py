class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def find_node(self, head, n):
        ret_node = curr_node = head
        i = 0
        while i < n:
            if curr_node is None:
                return None
            curr_node = curr_node.next
            i += 1
        while curr_node is not None:
            curr_node = curr_node.next
            ret_node = ret_node.next

        return ret_node

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4

sol = Solution()
print sol.find_node(node1, 2).val
        
