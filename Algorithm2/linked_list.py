class LinkedList(object):

    class ListNode(object):

        def __init__(self, data):
            self.data = data
            self.next_node = None

    def __init__(self, objects):
        self.head = self.ListNode(0)

        current_node = self.head
        for obj in objects:
            next_node = self.ListNode(obj)
            current_node.next_node = next_node
            current_node = next_node

    def __str__(self):
        if self.head.next_node is None:
            return 'Empty List'
        else:
            result = str(self.head.next_node.data)
            current_node = self.head.next_node
            while current_node.next_node is not None:
                current_node = current_node.next_node
                result += ' -> %s ' % current_node.data

            return result

    def reverse_recursive(self):
        if self.head.next_node is None:
            return None

        first_node = self.head.next_node
        self.head.next_node = first_node.next_node
        tail = self.reverse_recursive()

        if tail is None:
            self.head.next_node = first_node
        else:
            tail.next_node = first_node

        first_node.next_node = None
        return first_node

    def switch_node(self, val1, val2):
        first_node = second_node = self.head.next_node
        
        while first_node is not None and first_node.data != val1:
            first_node = first_node.next_node
        while second_node is not None and second_node.data != val2:
            second_node = second_node.next_node

        if first_node is None or second_node is None:
            print('At least one node is not exist in the linked list')
        else:
            first_node.data = val2
            second_node.data = val1

    def insert(self, data):
        self.reverse_recursive()
        tail = self.head.next_node
        new_node = self.ListNode(data)
        self.head.next_node = new_node
        new_node.next_node = tail
        self.reverse_recursive()

    def search(self, llist, data):
        current = node
        if current.data == data:
            return current.data
        else:
            if current.next_node:
                node = current.next_node
                self.search(node, data)
            else:
                raise ValueError('Node not in Linked List')
            
                
if __name__ == '__main__':
    list1 = LinkedList([1,2,3,4,5,6])
    list2 = LinkedList([])
    list2.insert(1)
    list2.insert(2)
    print(list1)
    list1.reverse_recursive()
    print(list1)
    result = list1.search(list1.head, 3)
    print(result)
    list1.switch_node(2, 6)
    print(list1)
    print(list2)
                



            
        
        
