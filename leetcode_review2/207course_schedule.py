class Solution(object):
    #solution1, use topological sort to detect cycle
    def canFinish(self, numCourses, prerequisites):
        in_degree = collections.defaultdict(set)
        out_degree = collections.defaultdict(set)
        for start_node, end_node in prerequisites:
            out_degree[start_node].add(end_node)
            in_degree[end_node].add(start_node)

        sink_nodes = []
        for node in xrange(numCourses):
            if node not in out_degree:
                sink_nodes.append(node)

        while sink_nodes:
            cur_node = sink_nodes.pop()
            for neighbor in in_degree[cur_node]:
                out_degree[neighbor].remove(cur_node)
                if len(out_degree[neighbor]) == 0:
                    del out_degree[neighbor]
                    sink_nodes.append(neighbor)
                    
        if len(out_degree) > 0:
            return False
        return True

    #solution2, use dfs to detect cycle, use three states, 0 denote not started yet, -1 means currently visiting, 1 means finished. So, during on the dfs process, if we meet a node whose state is -1 means we have a cycle.
    def canFinish2(self, numCourses, prerequisites):
        def dfs(node):
            if visited[node] == -1:
                return False
            if visited[node] == 1:
                return True

            visited[node] = -1
            res = True
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    res = False
                    break
            visited[node] = 1
            return res
        
        graph = collections.defaultdict(list)
        visited = [0] * numCourses
        for start_node, end_node in prerequisites:
            graph[start_node].append(end_node)
            
        for node in xrange(numCourses):
            if not dfs(node):
                return False
        return True
