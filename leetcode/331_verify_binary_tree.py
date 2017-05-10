class Solution(object):
    # Solution by Maomao, recursive
    def isValidSerialization(self, preorder):

        nodes = preorder.split(',')

        def _subtreeCount(nodes):
            print nodes
            if nodes[0].find('#') != -1:
                return 1
            else:
                nodeSize = len(nodes)
                if nodeSize <= 1:
                    return None
                leftTreeSize = _subtreeCount(nodes[1:])
                print 'left: ', leftTreeSize

                if leftTreeSize is None:
                    return None

                if leftTreeSize + 1 >= nodeSize:
                    return None

                rightTreeSize = _subtreeCount(nodes[(1 + leftTreeSize):])
                print 'right: ', rightTreeSize
                if rightTreeSize is None:
                    return None

                return leftTreeSize + rightTreeSize + 1

        return _subtreeCount(nodes) == len(nodes)

    # Solution by me, iterative
    def isValidSerialization2(self, preorder):
        nodes = preorder.split(',')
        stack = []
        i = 0
        if nodes[0] == '#' and len(nodes) > 1:
            return False
        
        while True:
            if len(stack) > 2 and stack[-1] == '#' and stack[-2] == '#':
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append('#')
                continue
            if i == len(nodes):
                break
            stack.append(nodes[i])
            i += 1
            
        if len(stack) == 1 and stack[0] == '#':
            return True
        else:
            return False

sol = Solution()
print sol.isValidSerialization("1,#,#,1")
#print sol.isValidSerialization("1, #")
