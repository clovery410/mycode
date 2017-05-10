#!/opt/python-3.4/linux/bin/python3
import numpy as np
import sys
import collections

class HierarchicalClustering(object):
    def __init__(self):
        # use adjacent list to store graph
        self.graph = collections.defaultdict(set)
        # store the edges by the key of weight after compute betweeness
        self.reversed_edge_weight = collections.defaultdict(list)
        self.node_cnt = 0
        
    def preprocessInput(self):
        graph = self.graph

        # read data from stdin
        for line in sys.stdin:
            cur_line_s = line.partition('#')[0].strip()
            if cur_line_s == '':
                continue

            cur_array = cur_line_s.split(",")
            if len(cur_array) != 2:
                print ("Invalid Input: not correct parameter numbers")
                return
            
            node1, node2 = cur_array
            node1, node2 = node1.strip(), node2.strip()

            graph[node1].add(node2)
            graph[node2].add(node1)

        self.node_cnt = len(graph)
        
        # pre-check if this is empty cluster
        if self.node_cnt == 0:
            print ("It's an empty social network! Directly return.")
            return

        # do bfs and computte the betweeness
        edge_weight = self.buildEdgeWeight()
        self.getReversedEdgeWeight(edge_weight)

        # cut edge with highest betweeness each time to divide clusters
        cluster_nums = 0
        while True:
            clusters = self.getClusters()
            if len(clusters) != cluster_nums:
                cluster_nums = len(clusters)
                print ('{0} clusters: {1}'.format(cluster_nums, clusters[0:]))
            if cluster_nums == self.node_cnt:
                break
            self.cutClusters()

    def buildEdgeWeight(self):
        """
        This function is used to do bfs with root of each node, then compute betweeness
        Hashtable label is used to store the shortest path count which go through this node
        Hashtable parents and children are used to store parent and child info of each node
        When computing betweeness, each leave node has credit 1, intermediate node has 1 + the credit carried from its children
        Label is used to split the credit to all its parents based on the label weight.
        """
        
        def bfs(root):
            queue = collections.deque([root])
            visited = {root}
            parents = collections.defaultdict(set)
            children = collections.defaultdict(int)
            label = collections.defaultdict(int)
            label[root] = 1
            
            while queue:
                next_level_node = []
                while queue:
                    cur_node = queue.popleft()
                    for neighbor in graph[cur_node]:
                        if neighbor not in visited:
                            label[neighbor] += 1  # compute how many shortest path go through this node
                            next_level_node.append(neighbor)
                            if cur_node not in parents[neighbor]:
                                children[cur_node] += 1
                            parents[neighbor].add(cur_node)

                # put the node into queue layer by layer when doing bfs
                while next_level_node:
                    next_node = next_level_node.pop()
                    visited.add(next_node)
                    queue.append(next_node)

            # use topological sort to perform credit calculation in last step of betweeness
            sink_nodes = [node for node in graph.keys() if children[node] == 0]
            node_weight = collections.defaultdict(int)
            
            while sink_nodes:
                cur_node = sink_nodes.pop()
                node_weight[cur_node] += 1
                for parent_node in parents[cur_node]:
                    temp_val = node_weight[cur_node] * label[parent_node] / sum(label[node] for node in parents[cur_node])
                    edge_weight[(parent_node, cur_node)] += temp_val
                    node_weight[parent_node] += temp_val
                    children[parent_node] -= 1
                    if children[parent_node] == 0:
                        sink_nodes.append(parent_node)

        graph, edge_weight = self.graph, collections.defaultdict(int)
        for root in graph.keys():
            bfs(root)
        return edge_weight

    def getReversedEdgeWeight(self, edge_weight):
        """
        This function is used to reversed the edge-weight relationship stored in our hashtable
        So that makes it easy to do the cutting according to the descending order of edge_weights
        """
        reversed_edge_weight = self.reversed_edge_weight
        visited = set()
        for (start_node, end_node), weight in edge_weight.items():
            if (start_node, end_node) in visited or (end_node, start_node) in visited:
                continue
            average_weight = (weight + edge_weight[(end_node, start_node)]) / 2
            reversed_edge_weight[average_weight].append((start_node, end_node))
            visited.add((start_node, end_node))
        
    def getClusters(self):
        """
        This function is used to get the current clusters based on our graph information
        """
        graph = self.graph
        visited, clusters = set(), []
        for cur_node in graph.keys():
            if cur_node in visited:
                continue
            visited.add(cur_node)
            queue = collections.deque([cur_node])
            cur_level_cluster = []
            while queue:
                top_node = queue.popleft()
                cur_level_cluster.append(top_node)
                for neighbor_node in graph[top_node]:
                    if neighbor_node not in visited:
                        visited.add(neighbor_node)
                        queue.append(neighbor_node)
            clusters.append(cur_level_cluster)
        return clusters
                
    def cutClusters(self):
        """
        This function is used to perform the cutting, just pick the highest weight among all edges
        If there are several edges with same highest weight, just cut them all
        """
        graph = self.graph
        cut_weight = max(self.reversed_edge_weight)

        for (start_node, end_node) in self.reversed_edge_weight[cut_weight]:
            graph[start_node].remove(end_node)
            graph[end_node].remove(start_node)
            
        del self.reversed_edge_weight[cut_weight]
        
if __name__ == "__main__":
    hc = HierarchicalClustering()
    hc.preprocessInput()
    
