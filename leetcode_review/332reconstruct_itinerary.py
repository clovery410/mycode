from heapq import *
class Solution(object):
    def findItinerary(self, tickets):
        def dfs(node):
            if len(res) == len(tickets) + 1:
                return res
            edges = sorted(graph[node])
            for neighbor in edges:
                res.append(neighbor)
                graph[node].remove(neighbor)
                if dfs(neighbor):
                    return res
                graph[node].append(neighbor)
                res.pop()
                
        # construct the graph
        graph = collections.defaultdict(list)
        for depart, dest in tickets:
            graph[depart].append(dest)
            
        res = ["JFK"]
        return dfs("JFK")

    # solution2, use Hierholzer's algorithm to find a Eulerian path in the graph which is a valid reconstruction
    def findItinerary2(self, tickets):
        def dfs(node):
            while graph[node]:
                dfs(heappop(graph[node]))
            res.append(node)

        # build the graph, use heap to store the neighbors.
        graph = collections.defaultdict(list)
        for depart, destination in tickets:
            heappush(graph[depart], destination)
            
        res = []
        dfs("JFK")
        return res[::-1]



        
                
                
            
            
            
