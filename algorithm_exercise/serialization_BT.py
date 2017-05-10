class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#solution1, use pre-order traversal pattern to serialize the binary tree
class Serialization(object):
    # use pre-order traversal to serialize binary tree, need to append '#' to each leaf node
    def serializeBinaryTree(self, root):
        def preorder(node):
            if node is None:
                strList.append('#')
            else:
                strList.append(str(node.val))
                preorder(node.left)
                preorder(node.right)

        strList = []
        preorder(root)
        return ''.join(strList)

    def deserializeBinaryTree(self, s):
        if s == '': return None
        root = TreeNode(s[0])
        stack = [[root, 'empty']]
        for i in range(1, len(s)):
            cur_s = s[i]
            top = stack[-1]
            if cur_s != '#':
                new_node = TreeNode(cur_s)
                if top[1] == 'empty':
                    top[0].left = new_node
                    top[1] = 'left'
                else:
                    stack.pop()[0].right = new_node
                stack.append([new_node, 'empty'])
            else:
                if top[1] == 'empty':
                    top[1] = 'left'
                else:
                    stack.pop()
        return root

    #we can also use recursive solution to deserialize the preorder traversal string
    def deserializeBinaryTree2(self, s):
        def preorder(idx):
            if idx >= len(s): return None, idx+1
            if s[idx] == '#': return None, idx+1
            cur_node = TreeNode(s[idx])

            left_res = preorder(idx+1)
            cur_node.left, l_idx = left_res[0], left_res[1]

            right_res = preorder(l_idx)
            cur_node.right, r_idx= right_res[0], right_res[1]
            return cur_node, r_idx
        return preorder(0)[0]

from collections import deque
#solution2, use level order traversal pattern to serialize the binary tree
class Serialization2(object):
    def serializeBinaryTree(self, root):
        strList = []
        queue = deque([root])
        while len(queue) > 0:
            length = len(queue)
            for i in range(length):
                cur = queue.popleft()
                if cur == '#':
                    strList.append('#')
                else:
                    strList.append(str(cur.val))
                    if cur.left: queue.append(cur.left)
                    else: queue.append('#')
                    if cur.right: queue.append(cur.right)
                    else: queue.append('#')
            if all(elem == '#' for elem in queue):
                break
        return ''.join(strList)

    def deserializeBinaryTree(self, s):
        if s == '': return None
        root = TreeNode(s[0])
        queue = deque([root])
        idx = 1
        while len(queue) > 0:
            if idx >= len(s): break
            length = len(queue)
            for i in range(length):
                cur_node = queue.popleft()
                if s[idx] != '#':
                    cur_node.left = TreeNode(s[idx])
                    queue.append(cur_node.left)
                idx += 1
                if s[idx] != '#':
                    cur_node.right = TreeNode(s[idx])
                    queue.append(cur_node.right)
                idx += 1
        return root

if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)

    node1.left = node2
    node1.right = node3
    node3.left = node4
    node4.right = node5
    
    ser = Serialization()
    print ser.serializeBinaryTree(node1)
    print ser.deserializeBinaryTree2('12##34#5###').right.val
    ser = Serialization2()
    print ser.serializeBinaryTree(node1)
    print ser.deserializeBinaryTree('123##4##5').right.val
    
