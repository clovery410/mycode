 this NestedInteger holds a nested list
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
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        def getMaxDepth(cur_list, depth):
            self.max_depth = max(depth, self.max_depth)
            for elem in cur_list:
                if not elem.isInteger():
                    getMaxDepth(elem.getList(), depth + 1)

        def getNestedSum(cur_list, depth):
            for elem in cur_list:
                if elem.isInteger():
                    self.total += elem.getInteger() * (self.max_depth - depth)
                else:
                    getNestedSum(elem.getList(), depth + 1)

        self.max_depth = 0
        self.total = 0
        getMaxDepth(nestedList, 1)
        getNestedSum(nestedList, 0)
        return self.total
        
