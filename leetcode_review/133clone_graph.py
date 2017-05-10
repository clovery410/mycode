class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # solution1, BFS
    def cloneGraph(self, node):
        if node is None: return None
        new_node = UndirectedGraphNode(node.label)
        graph_map = {node: new_node}
        to_do_list = [node]

        while to_do_list:
            cur_node = to_do_list.pop()
            clone_node = graph_map[cur_node]
            for neighbor in cur_node.neighbors:
                if neighbor not in graph_map:
                    graph_map[neighbor] = UndirectedGraphNode(neighbor.label)
                    to_do_list.append(neighbor)
                clone_neighbor = graph_map[neighbor]
                clone_node.neighbors.append(clone_neighbor)

        return new_node

    # solution2, after reading the code in last round, try to rewrite the recursive DFS
    def cloneGraph2(self, node):
        def dfs(node):
            if node is None: return None
            if node not in graph_map:
                graph_map[node] = UndirectedGraphNode(node.label)
                
            clone_node = graph_map[node]
            for neighbor in node.neighbors:
                clone_node.neighbors.append(dfs(neighbor))
            return clone_node

        graph_map = {}
        return dfs(node)
                    
