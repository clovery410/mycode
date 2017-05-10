class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        if head is None:
            return None
        new_head = RandomListNode(head.label)
        curr1, curr2 = head, new_head
        cache = {head: new_head}
        
        while curr1.next:
            new_node = RandomListNode(curr1.next.label)
            cache[curr1.next] = new_node
            curr2.next = new_node
            curr1 = curr1.next
            curr2 = curr2.next
            
        curr1, curr2 = head, new_head
        while curr1:
            if curr1.random:
                cache[curr1].random = cache[curr1.random]
            curr1 = curr1.next
        return new_head
