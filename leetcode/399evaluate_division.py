import collections
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        def dfs(start, end, visited):
            if end in graph[start]:
                return pairs[(start, end)]
            
            visited.add(start)
            res = -1.0
            for neighbor in graph[start]:
                if neighbor not in visited:
                    following = dfs(neighbor, end, visited)
                    if following != -1.0:
                        res = pairs[(start, neighbor)] * following
            visited.remove(start)
            return res
            
        pairs = {}
        graph = collections.defaultdict(set)
        for i in xrange(len(equations)):
            a, b = equations[i]
            pairs[(a, b)] = values[i]
            pairs[(b, a)] = 1 / values[i]
            graph[a].add(b)
            graph[b].add(a)

        res = []
        print pairs, graph
        for start_node, end_node in queries:
            if start_node not in graph or end_node not in graph:
                res.append(-1.0)
            elif start_node == end_node:
                res.append(1.0)
            else:
                visited = set()
                res.append(dfs(start_node, end_node, visited))
        return res

if __name__ == "__main__":
    sol = Solution()
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    print sol.calcEquation(equations, values, queries)

        
