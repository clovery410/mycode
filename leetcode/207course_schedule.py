class Solution(object):
    def __init__(self):
#        self.path = []
        self.flag = True
        
    def dfs(self, graph, node, curr_path, visited):
        print graph
        print node
        print curr_path
        
        if node not in graph:
            return
        curr_path.append(node)
        visited[node] = 1
        for item in graph[node]:
            visited[item] = 1
            if item in curr_path:
                self.flag = False
                break
            else:
                self.dfs(graph, item, curr_path, visited)
            if curr_path:
                curr_path.pop()
#        self.path.append(curr_path)
            
    def canFinish(self, numCourses, prerequisites):
        graph = {}
        visited = [0 for x in xrange(numCourses)]
        
        for edge in prerequisites:
            if edge[0] not in graph:
                graph[edge[0]] = [edge[1]]
            else:
                graph[edge[0]].append(edge[1])

        for node in graph:
            if visited[node] == 0:
                self.dfs(graph, node, [], visited)
                if self.flag is False:
                    return False

        # if self.flag is False:
        #     return False
        return True

    # Stack works like recursion
    def solution_with_stack(self, numCourses, prerequisites):
        graph = {}
        visited = [0 for x in xrange(numCourses)]
        
        for edge in prerequisites:
            if edge[0] not in graph:
                graph[edge[0]] = [edge[1]]
            else:
                graph[edge[0]].append(edge[1])

        stack = []
        for node in graph:
            if visited[node] == 0:
                stack.append(node)
                curr_v = {}
                curr_v[node] = 1
                while stack:
                    top = stack.pop()
                    visited[top] = 1
                    if top in graph:
                        curr_v[top] = 1
                        for elem in graph[top]:
                            if elem in curr_v:
                                return False
                            if visited[elem] == 0:
                                stack.append(elem)

        return True


if __name__ == '__main__':
    n = 6
    pre = [[0,1],[0,2],[1,2],[1,4],[3,5]]
    sol = Solution()
    print sol.canFinish(n, pre)
    print sol.solution_with_stack(n, pre)
