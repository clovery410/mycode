class ListNode(object):
    def __init__(self, key, x):
        self.key = key
        self.val = x
        self.prev = None
        self.next = None
        
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode(-1, 0)
        self.tail = ListNode(-2, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.cache:
            return -1
        node = self.cache[key]
        
        # extract this node from original position, and relink predecessor and successor
        pre_node, pos_node = node.prev, node.next
        pre_node.next = pos_node
        pos_node.prev = pre_node

        # append this node to last
        node.prev = self.tail.prev
        self.tail.prev.next = node
        node.next = self.tail
        self.tail.prev = node

        return node.val

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.cache:
            node = self.cache[key]
            pre_node, pos_node = node.prev, node.next
            pre_node.next, pos_node.prev = pos_node, pre_node

        elif len(self.cache) == self.capacity:
            rm_node = self.head.next
            self.head.next = rm_node.next
            rm_node.next.prev = self.head
            del self.cache[rm_node.key]
            
        new_node = ListNode(key, value)
        new_node.prev = self.tail.prev
        self.tail.prev.next = new_node
        new_node.next = self.tail
        self.tail.prev = new_node
        self.cache[key] = new_node
