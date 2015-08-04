f = open('clustering1.txt')

content = f.read()
lines = content.splitlines()

num_node = int(lines[0])

class Node(object):
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class linkedList(object):
    def __init__(self, head=None):
        self.head = head

    def print_list(self):
        current = self.head
        import pdb
        pdb.set_trace()
        while current is not None:
            print("%s -> " % current.data)
            current = current.nextNode

    def insert(self, node):
        if not self.head:
            self.head = node
        else:
            node.nextNode = self.head
            self.head = node

    def search(self, lList, node):
        if self.head == node:
            return self.head
        else:
            if lList.head.nextNode:
                self.search(linkedList(lList.head.nextNode), node)
            else:
                raise ValueError("Node not in Linked List")

    def size(self):
        current = self.head
        size = 0
        while current is not None:
            size += 1
            current = current.nextNode
        return size

    def delete(self, node):
        if self.size() == 0:
            raise ValueError("List is empty")
        else:
            current = self.head
            previous = None
            found = False
            while not found:
                if current == node:
                    found = True
                elif current is None:
                    raise ValueError("Node not in Linked List")
                else:
                    previous = current
                    current = current.nextNode
            if previous is None:
                self.head = current.nextNode
            else:
                previous.nextNode = current.nextNode

    def reverse_iterate(self):
        if self.size() <= 1:
            return self
        else:
            previous = self.head
            current = previous.nextNode
            while current is not None:
                self.head = current
                current = current.nextNode
                self.head.nextNode = previous
                previous = self.head
        return self

    def reverse_recursive(self, lList):
        if self.head is None:
            return None

        first = self.head
        lList.head.nextNode = first.nextNode
        tail = reverse_recursive(lList)
        
        


if __name__ == '__main__':
    list1 = linkedList()
    node1 = Node("1")
    node2 = Node("2")
    node3 = Node("3")
    node4 = Node("4")

    list1.insert(node1)
    list1.insert(node2)
    list1.insert(node3)
    list1.insert(node4)

    list1.print_list()

import pdb
pdb.set_trace()
