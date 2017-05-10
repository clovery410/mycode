class Solution(object):
    #Solution1 Union Find
    def countComponents(self, n, edges):
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            xRoot = find(x)
            yRoot = find(y)
            if xRoot == yRoot:
                return 0
            else:
                parent[xRoot] = yRoot
                return 1

        parent = range(n)
        count = 0

        for edge in edges:
            count += union(edge[0], edge[1])
        return n - count

    #Solution2 DFS
    def countComponents2(self, n, edges):
        #dfs search
        def dfs(curr_node, graph, visited):
            if visited[curr_node]:
                return
            else:
                visited[curr_node] = 1
                for neighbor in graph[curr_node]:
                    dfs(neighbor, graph, visited)
                    
        #construct the graph
        visited = [0 for x in xrange(n)]
        graph = {x: [] for x in xrange(n)}
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        for node in xrange(n):
            visited[node] = 0
            
        cc = 0
        for node in xrange(n):
            if visited[node] == 0:
                cc += 1
                dfs(node, graph, visited)
        return cc

    #Solution3, BFS
    def countComponents3(self, n, edges):
        #bfs search
        stack = []
        visited = [0 for x in xrange(n)]
        graph = {x: [] for x in xrange(n)}
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        for node in xrange(n):
            visited[node] = 0

        count = 0
        for node in xrange(n):
            if visited[node] == 0:
                stack.append(node)
                while stack:
                    top = stack.pop()
                    visited[top] = 1
                    for neighbor in graph[top]:
                        if visited[neighbor] == 0:
                            stack.append(neighbor)
                count += 1
        return count
        
if __name__ == "__main__":
    sol = Solution()
    n = 5
    edges = [[0, 1], [1, 2], [0, 2], [3, 4]]
    print sol.countComponents3(n, edges)
