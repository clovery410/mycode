from heapq import *
#solution1, use heap, but TLE
class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.heap = []
        self.timestamp = 0
        self.cache = {}
        
    def get(self, key):
        if key not in self.cache:
            return -1
        value, ts = self.cache[key]
        self.heap.remove((ts, key))
        heapify(self.heap)
        heappush(self.heap, (self.timestamp, key))
        self.cache[key] = (value, self.timestamp)
        self.timestamp += 1
        return value
    
    def set(self, key, value):
        if key not in self.cache:
            if len(self.heap) == self.capacity:
                mv_key = heappop(self.heap)[1]
                del self.cache[mv_key]
        else:
            ts = self.cache[key][1]
            self.heap.remove((ts, key))
            heapify(self.heap)
        heappush(self.heap, (self.timestamp, key))
        self.cache[key] = (value, self.timestamp)
        self.timestamp += 1

#solution2, try to come up another idea
class DoubleLinkedNode(object):
    def __init__(self, key, val):
        self.key = key  #with this attribute, can delete key from hashmap by value in O(1) time
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache2(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = DoubleLinkedNode(0,0)
        self.tail = DoubleLinkedNode(0,0)
        self.head.next, self.tail.prev = self.tail, self.head
        
    def get(self, key):
        if key not in self.cache:
            return -1

        #delete the node from original position
        cur_node = self.cache[key]
        pre_node, pos_node = cur_node.prev, cur_node.next
        pre_node.next = pos_node
        pos_node.prev = pre_node

        #append this node to the end of linked list
        self.tail.prev.next, cur_node.prev = cur_node, self.tail.prev
        cur_node.next, self.tail.prev = self.tail, cur_node

        return self.cache[key].val
            
    def set(self, key, value):
        if key not in self.cache:
            #reach the capacity limit, need to kick off the first node from our double liked list, remember to remove the corresponding key from dictionary either
            if len(self.cache) == self.capacity:
                rm_node = self.head.next
                self.head.next = rm_node.next
                rm_node.next.prev = self.head
                del self.cache[rm_node.key]
        else:
            #remove the old node
            cur_node = self.cache[key]
            cur_node.prev.next, cur_node.next.prev = cur_node.next, cur_node.prev

        #create a new node and append to the end of linked list
        new_node = DoubleLinkedNode(key, value)
        self.tail.prev.next, new_node.prev = new_node, self.tail.prev
        new_node.next, self.tail.prev = self.tail, new_node

        self.cache[key] = new_node

if __name__ == "__main__":
    lru = LRUCache2(3)
    lru.set(1, 1)
    lru.set(2, 2)
    lru.set(3, 3)
    lru.set(4, 4)
    print lru.get(4)
    print lru.get(3)
    print lru.get(2)
    print lru.get(1)
    lru.set(5, 5)
    print lru.get(1)
    print lru.get(2)
    print lru.get(3)
    print lru.get(4)
    print lru.get(5)


            
                
