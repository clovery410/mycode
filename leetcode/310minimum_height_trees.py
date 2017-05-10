from collections import defaultdict, deque
class Solution(object):
    #Solution1, brute-force solution
    def findMinHeightTrees(self, n, edges):
        def getHeight(root, visited):
            if root in visited or not graph:
                return 0
            visited[root] = 1
            return 1 + max(getHeight(neighbor, visited) for neighbor in graph[root])

        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        minHeight = n
        res = []
        for node in xrange(n):
            cur_height = getHeight(node, {})
            if cur_height < minHeight:
                res = [node]
                minHeight = cur_height
            elif cur_height == minHeight:
                res.append(node)
        return res

    #Solution2, dfs solution, choose any node, get the longest path, then the root must be in this longest path.
    def findMinHeightTrees2(self, n, edges):
        def dfs(root, visited, path, all_solution):
            if root in visited:
                if len(path) > len(all_solution):
                    all_solution[:] = path[:]
            else:
                visited[root] = 1
                path.append(root)
                for neighbor in graph[root]:
                    dfs(neighbor, visited, path, all_solution)
                path.pop()

        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        start_node = 0
        for node, edge in graph.iteritems():
            if len(edge) == 1:
                start_node = node
                break
            
        longest_path = []
        dfs(start_node, {}, [], longest_path)
        minHeight = n
        res = []
        for node in longest_path:
            cur_height = self.getHeight(graph, node, {})
            if cur_height < minHeight:
                res = [node]
                minHeight = cur_height
            elif cur_height == minHeight:
                res.append(node)
        return res

    def getHeight(self, graph, root, visited):
        if root in visited or not graph:
            return 0
        visited[root] = 1
        return 1 + max(self.getHeight(graph, neighbor, visited) for neighbor in graph[root])

    #Solution3, learned from discuss, let each leaf be a pointer, step one step each iteration, eliminate that leaf, make the neighbor node be the new leaf if that neighbor has no other neighbors, until there are only 1 or 2 nodes left.
    def findMinHeightTrees3(self, n, edges):
        if n == 1: return [0]
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        leaves = [node for node in xrange(n) if len(graph[node]) == 1]
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph.pop(leaf)[0]
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves

    #Solution4, two round bfs, find the longest path of the graph, then return middle one or two
    def findMinHeightTrees4(self, n, edges):
        def bfs(root):
            queue = deque([[root]])
            visited = set([root])
            while queue:
                path = queue.popleft()
                for neighbor in graph[path[-1]]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(path+[neighbor])
            return path
        
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        path1 = bfs(0)
        path2 = bfs(path1[-1])

        if len(path2) % 2 == 0:
            return [path2[len(path2) / 2 - 1], path2[len(path2) / 2]]
        else:
            return [path2[len(path2) / 2]]

        #Solution5, two round dfs, find the longest path of the graph, then return middle one or two
        def findMinHeightTrees5(self, n, edges):
            def dfs(root, visited):
                if root in visited:
                    return []
                visited.add(root)
                cur_path = []
                for neighbor in graph[root]:
                    next_path = dfs(neighbor, visited)
                    if len(next_path) > len(cur_path):
                        cur_path = next_path
                return [root] + cur_path

            graph = defaultdict(list)
            for edge in edges:
                graph[edge[0]].append(edge[1])
                graph[edge[1]].append(edge[0])
            path1 = dfs(0, set([]))
            path2 = dfs(path1[-1], set([]))
            
            if len(path2) % 2 == 0:
                return [path2[len(path2) / 2 - 1], path2[len(path2) / 2]]
            else:
                return [path2[len(path2) / 2]]
            
