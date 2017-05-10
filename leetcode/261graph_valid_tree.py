class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        def dfs(node, graph, visited):
            if node is None:
                return
            visited[node] = 1
            for neighbor in graph[node]:
                if visited[neighbor] == 0:
                    dfs(neighbor, graph, visited)
                    
        if len(edges) != n - 1:
            return False
        if len(edges) == 0 and n == 1:
            return True
        
        visited = [0 for x in xrange(n)]
        graph = {x:[] for x in xrange(n)}
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        for node in xrange(n):
            if len(graph[node]) == 0:
                return False
            
        dfs(0, graph, visited)
        
        for i in xrange(len(visited)):
            if visited[i]== 0:
                return False
        return True
