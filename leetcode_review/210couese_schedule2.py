class Solution(object):
    # solution1, use topological sort
    def findOrder(self, numCourses, prerequisites):
        in_degree = collections.defaultdict(list)
        out_degree = [0] * numCourses
        for start_node, end_node in prerequisites:
            in_degree[end_node].append(start_node)
            out_degree[start_node] += 1

        sink_nodes = []
        for node in xrange(numCourses):
            if out_degree[node] == 0:
                sink_nodes.append(node)

        course_order = []
        while sink_nodes:
            cur_node = sink_nodes.pop()
            course_order.append(cur_node)
            for neighbor in in_degree[cur_node]:
                out_degree[neighbor] -= 1
                if out_degree[neighbor] == 0:
                    sink_nodes.append(neighbor)
                    
        return course_order if len(course_order) == numCourses else []

    # solution2, practice with dfs search
    def findOrder2(self, numCourses, prerequisites):
        def dfs(node):
            if state[node] == -1:
                return False
            if state[node] == 1:
                return True

            res = True
            state[node] = -1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    res = False
                    break

            course_order.append(node)
            state[node] = 1
            return res

        graph = collections.defaultdict(list)
        for start_node, end_node in prerequisites:
            graph[start_node].append(end_node)

        course_order = []
        state = [0] * numCourses
        for node in xrange(numCourses):
            if state[node] == 0:
                if not dfs(node):
                    return []
                
        return course_order
