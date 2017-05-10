import heapq
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        new_head = None
        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, node))
        if heap:
            new_head = heapq.heappop(heap)[1]
            if new_head.next:
                heapq.heappush(heap, (new_head.next.val, new_head.next))
            pre_node = new_head
        while heap:
            curr_node = heapq.heappop(heap)[1]
            if curr_node.next:
                heapq.heappush(heap, (curr_node.next.val, curr_node.next))
            pre_node.next = curr_node
            pre_node = curr_node
        return new_head

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)

    node1.next = node3
    node3.next = node5
    node2.next = node4
    node4.next = node6

    sol = Solution()
    new_head = sol.mergeKLists([node1, node2])
    print new_head.val
    print new_head.next.val
    print new_head.next.next.val
    print new_head.next.next.next.val
    print new_head.next.next.next.next.val
    print new_head.next.next.next.next.next.val
    print sol.mergeKLists([[]])
        
