from collections import deque, defaultdict
class Solution(object):
    #Solution1, topological sort solution
    def canFinish(self, numCourses, prerequisites):
        indegree = defaultdict(list)
        outdegree = [0] * numCourses

        for edge in prerequisites:
            indegree[edge[1]].append(edge[0])
            outdegree[edge[0]] += 1
        
        queue = deque([])
        # push sink node into queue
        for node in xrange(numCourses):
            if outdegree[node] == 0:
                queue.append(node)

        count = 0
        while queue:
            cur_node = queue.popleft()
            count += 1
            for pre in indegree[cur_node]:
                outdegree[pre] -= 1
                if outdegree[pre] == 0:
                    queue.append(pre)
        return count == numCourses
                
    #Solution2, use dfs to detect whether there is a cycle
    def canFinish(self, numCourses, prerequisites):
        def dfs(node):
            if visited[node] == -1:
                return False
            elif visited[node] == 1:
                return True
            visited[node] = -1

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            visited[node] = 1
            return True
                    
        graph = defaultdict(list)
        visited = [0] * numCourses

        for edge in prerequisites:
            graph[edge[0]].append(edge[1])

        for node in graph:
            if visited[node] == 0:
                if not dfs(node):
                    return False
        return True
