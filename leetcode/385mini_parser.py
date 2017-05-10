#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        def splitString(s):
            res = []
            idx = 0
            while idx < len(s):
                if s[idx] in '[]':
                    res.append(s[idx])
                    idx += 1
                elif s[idx] not in '[],':
                    j = idx + 1
                    while j < len(s) and s[j].isdigit():
                        j += 1
                    res.append(s[idx:j])
                    idx = j
                else:
                    idx += 1
            return res

        string = splitString(s)
        if len(string) == 1:
            return NestedInteger(int(string[0]))
        root = NestedInteger()
        stack = [root]
        i = 1
        while i < len(string):
            if string[i] == '[':
                stack.append(NestedInteger())
            elif string[i] == ']':
                top = stack.pop()
                if stack:
                    stack[-1].add(top)
            else:
                stack[-1].add(int(string[i]))
            i += 1
        return root
                        
