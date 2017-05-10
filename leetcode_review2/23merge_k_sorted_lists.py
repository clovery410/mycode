class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        from heapq import *
        dummy = ListNode(0)
        pre = dummy
        heap = []
        for head in lists:
            if head:
                heappush(heap, (head.val, head))

        while heap:
            cur_val, cur_node = heappop(heap)
            pre.next = cur_node
            pre = cur_node
            if cur_node.next:
                heappush(heap, (cur_node.next.val, cur_node.next))

        return dummy.next
