class Solution(object):
    # solution1, do two round BFS (or DFS), to find the longest path.
    def findMinHeightTrees(self, n, edges):
        def bfs(root):
            queue = deque([[root]])
            visited = {root}
            while queue:
                cur_path = queue.popleft()
                last_node = cur_path[-1]
                for neighbor in graph[last_node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(path + [neighbor])
            return cur_path
            
        graph = collections.defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        path1 = bfs(0)
        path2 = bfs(path1[-1])

        l = len(path2)
        if l % 2 == 1:
            return [path2[l/2]]
        else:
            return [path2[l/2-1], path2[l/2]]

    # use two round dfs to find the longest path
    def findMinHeightTrees2(self, n, edges):
        def dfs(root, visited):
            if root in visited:
                return []
            visited.add(root)
            path = []
            for neighbor in graph[root]:
                next_path = dfs(neighbor, visited)
                if len(next_path) > len(path):
                    path = next_path
            return [root] + path

        graph = collections.defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        path1 = dfs(0, set())
        path2 = dfs(path1[-1], set())

        l = len(path2)
        if l % 2 == 1:
            return [path2[l/2]]
        else:
            return [path2[l/2-1], path2[l/2]]
        
    # solution3, the trick last time learned from discuss
    # today, rewrite it by self understanding, which is actually a topological sort idea, each time tackle with sink nodes
    def findMinHeightTrees3(self, n, edges):
        graph = collections.defaultdict(set)
        for node1, node2 in edges:
            graph[node1].add(node2)
            graph[node2].add(node1)

        leaves = collections.deque([])
        for node, neighbors in graph.items():
            if len(neighbors) == 1:
                leaves.append(node)

        while n > 2:
            length = len(leaves)
            n -= length
            for i in xrange(length):
                cur_node = leaves.popleft()
                for neighbor in graph[cur_node]:
                    graph[neighbor].remove(cur_node)
                    if len(graph[neighbor]) == 1:
                        leaves.append(neighbor)
                        
        return list(leaves)
        
        
