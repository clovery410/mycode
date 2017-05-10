class Solution(object):
    def inorderPrint(self, s):
        def peekNextToken():
            while self.idx < len(s) and s[self.idx] != '(':
                self.idx += 1
            return True if s[self.idx] == '(' else False

        def getNextToken():
            while self.idx < len(s) and s[self.idx] == ' ':
                self.idx += 1
                
            x = ''
            while self.idx < len(s) and s[self.idx] not in ' ,':
                x += s[self.idx]
                self.idx += 1
            while self.idx < len(s) and s[self.idx] in ' ,':
                self.idx += 1
                
            y = ''
            while self.idx < len(s) and s[self.idx] not in ' ,':
                y += s[self.idx]
                self.idx += 1
            while self.idx < len(s) and s[self.idx] != ')':
                self.idx += 1

            if s[self.idx] == ')':
                return (x, y)
            else:
                return ('', '')

        def inorder(node):
            if len(out_degree[node]) >= 1:
                inorder(out_degree[node][0])
                
            print node
            
            if len(out_degree[node]) == 2:
                inorder(out_degree[node][1])
                
        in_degree = collections.defaultdict(int)
        out_degree = collections.defaultdict(list)

        while peekNextToken():
            x, y = getNextToken()
            if x == '' or y == '':
                print "Invalid, input, string format error!"
                return
            
            in_degree[y] += 1
            if in_degree[y] > 1:
                print "Invalid input, have more than 1 parent"
                return

            if y in out_degree[x]:
                print "Invalid input, have duplicate edges"
                return
            
            out_degree[x].append(y)
            if len(out_degree[x]) > 2:
                print "Invalid input, have more than two children"
                return

        # find root
        roots = []
        for key, val in in_degree.items():
            if val == 0:
                roots.append(key)
        if len(roots) == 0 or len(roots) > 1:
            print "Invalid input, not a valid tree"
            return
        
        # print tree
        inorder(root[0])
        
            
