from collections import deque, defaultdict
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        indegree = defaultdict(list)
        outdegree = [0] * numCourses
        topo_order = []
        for edge in prerequisites:
            outdegree[edge[0]] += 1
            indegree[edge[1]].append(edge[0])

        # Here can use either queue or stack
        queue = deque([])
        count = 0
        for node in xrange(numCourses):
            if outdegree[node] == 0:
                queue.append(node)

        while queue:
            cur_node = queue.popleft()
            count += 1
            topo_order.append(cur_node)
            for pre in indegree[cur_node]:
                outdegree[pre] -= 1
                if outdegree[pre] == 0:
                    queue.append(pre)

        return topo_order if count == numCourses else []
