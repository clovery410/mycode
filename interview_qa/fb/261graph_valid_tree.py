import collections
class Solution(object):
    def validTree(self, n, edges):
        def dfs(parent, node):
            if status[node] == 1:
                return False
            
            status[node] = 1
            for neighbor in graph[node]:
                if neighbor != parent and status[neighbor] != 2:
                    if not dfs(node, neighbor):
                        return False
                    
            status[node] = 2
            return True

        graph = collections.defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)

        status = [0] * n
        if not dfs(None, 0):
            return False
        if any(x == 0 for x in status):
            return False
        return True

if __name__ == "__main__":
    sol = Solution()
    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    edges2 = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    print sol.validTree(n, edges)
    print sol.validTree(n, edges2)
