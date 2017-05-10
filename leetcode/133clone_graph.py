from collections import deque
class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution(object):
    #Solution1, use bfs and queue
    def cloneGraph(self, node):
        if node is None:
            return None
        new_root = UndirectedGraphNode(node.label)
        queue = deque([node])
        visited = {node: new_root}
        while queue:
            old = queue.popleft()
            for neighbor in old.neighbors:
                if neighbor not in visited:
                    new_node = UndirectedGraphNode(neighbor.label)
                    visited[neighbor] = new_node
                    visited[old].neighbors.extend([new_node])
                    queue.append(neighbor)
                else:
                    visited[old].neighbors.extend([visited[neighbor]])
        return new_root

    #Solution2, use dfs, better to use return version recursion
    def cloneGraph2(self, node):
        def dfs(cur_old_node):
            if cur_old_node is None:
                return None
            if cur_old_node in visited:
                return visited[cur_old_node]
            cur_new_node = UndirectedGraphNode(cur_old_node.label)
            visited[cur_old_node] = cur_new_node
            for neighbor in cur_old_node.neighbors:
                cur_new_node.neighbors.extend([dfs(neighbor)])

        visited = {}
        return dfs(node)
                
                
